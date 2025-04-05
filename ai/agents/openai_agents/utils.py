import logging
import os
from typing import Optional

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

from opentelemetry.instrumentation.openai import OpenAIInstrumentor

from openai import AsyncOpenAI

from agents import set_tracing_disabled, Model, OpenAIChatCompletionsModel


LOGGER = logging.getLogger(__name__)


def get_model() -> Model:
    return OpenAIChatCompletionsModel(
        model=os.getenv('OPENAI_MODEL_ID', 'gpt-4o-mini'),
        openai_client=AsyncOpenAI(
            base_url=os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1'),
            api_key=os.environ['OPENAI_API_KEY']
        )
    )


def configure_otlp(otlp_endpoint: str):
    LOGGER.info('Configuring OTLP: %r', otlp_endpoint)
    set_tracing_disabled(True)
    trace_provider = TracerProvider()
    trace_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(otlp_endpoint)))
    OpenAIInstrumentor().instrument(tracer_provider=trace_provider)


def configure_otlp_if_enabled(otlp_endpoint: Optional[str] = None):
    if otlp_endpoint:
        configure_otlp(otlp_endpoint)
