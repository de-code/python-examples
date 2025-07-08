import logging
import os

from dotenv import load_dotenv

from pydantic import TypeAdapter

from smolagents import (  # type: ignore[import-untyped]
    DuckDuckGoSearchTool,
    Model,
    OpenAIServerModel,
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


def main():
    model = get_model()

    agent = ToolCallingAgent(
        tools=[DuckDuckGoSearchTool()],
        add_base_tools=False,
        model=model,
        planning_interval=3
    )
    agent.run(
        'Investigate the health benefits of bananas,'
        ' with web sources. Only use English sources.'
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    main()
