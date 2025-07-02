import logging
import os

from dotenv import load_dotenv

from pydantic import TypeAdapter

from smolagents import (  # type: ignore[import-untyped]
    GradioUI,
    Model,
    OpenAIServerModel,
    tool,
    ToolCallingAgent
)


LOGGER = logging.getLogger(__name__)


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


def main():
    model = get_model()

    LOGGER.info("Tool name: %r", add_numbers.name)
    LOGGER.info("Tool description: %r", add_numbers.description)
    LOGGER.info("Tool inputs: %r", add_numbers.inputs)
    LOGGER.info("Tool output_type: %r", add_numbers.output_type)

    agent = ToolCallingAgent(
        tools=[add_numbers],
        add_base_tools=False,
        model=model,
        max_steps=3
    )

    LOGGER.info("System prompt:\n%s\n", agent.system_prompt)

    GradioUI(agent).launch(share=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    main()
