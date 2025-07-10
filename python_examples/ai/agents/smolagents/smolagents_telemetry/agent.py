import logging
import os

from dotenv import load_dotenv

from pydantic import TypeAdapter

from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

from openinference.semconv.resource import ResourceAttributes
from openinference.instrumentation.smolagents import (
    SmolagentsInstrumentor
)

from smolagents import (  # type: ignore[import-untyped]
    Model,
    OpenAIServerModel,
    tool,
    ToolCallingAgent
)


def get_model() -> Model:
    return OpenAIServerModel(
        model_id=os.getenv(
            'OPENAI_MODEL_ID',
            'gpt-4o-mini'
        ),
        api_base=os.getenv(
            'OPENAI_BASE_URL',
            'https://api.openai.com/v1'
        ),
        api_key=os.environ['OPENAI_API_KEY'],
        flatten_messages_as_text=(
            TypeAdapter(bool).validate_strings(os.getenv(
                'OPENAI_FLATTEN_MESSAGES',
                'false'
            ))
        )
    )


@tool
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers.

    Args:
        a: The first number
        b: The second number
    """
    return a + b


def configure_otlp(otlp_endpoint: str, project_name: str):
    resource = Resource.create({
        ResourceAttributes.PROJECT_NAME: project_name
    })
    trace_provider = TracerProvider(resource=resource)
    trace_provider.add_span_processor(
        SimpleSpanProcessor(OTLPSpanExporter(otlp_endpoint))
    )
    SmolagentsInstrumentor().instrument(
        tracer_provider=trace_provider
    )


def main():
    configure_otlp(
        otlp_endpoint='http://localhost:6006/v1/traces',
        project_name='my-app'
    )

    model = get_model()

    agent = ToolCallingAgent(
        tools=[add_numbers],
        add_base_tools=False,
        model=model,
        max_steps=3
    )
    agent.run('Can you add 123 and 234?')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    main()
