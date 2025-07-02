import logging
import os

from dotenv import load_dotenv

from pydantic import TypeAdapter

from smolagents import (  # type: ignore[import-untyped]
    GradioUI,
    Model,
    OpenAIServerModel,
    Tool,
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


class AddNumbersTool(Tool):
    name = "add_numbers"
    description = "Adds two numbers."
    inputs = {
        "a": {
            "type": "integer",
            "description": "The first number"
        },
        "b": {
            "type": "integer",
            "description": "The second number"
        }
    }
    output_type = "integer"

    def forward(  # pylint: disable=arguments-differ # type: ignore
        self,
        a: int,
        b: int
    ) -> int:
        return a + b


def main():
    model = get_model()

    agent = ToolCallingAgent(
        tools=[AddNumbersTool()],
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
