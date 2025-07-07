import logging
import os

from dotenv import load_dotenv

from pydantic import TypeAdapter

from smolagents import (  # type: ignore[import-untyped]
    CodeAgent,
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


PRICE_BY_PRODUCT = {
    "apple": 1.0,
    "banana": 0.5,
    "orange": 0.75,
    "grape": 2.0,
    "watermelon": 3.0
}


@tool
def get_product_names() -> list[str]:
    """
    Get's the product names.

    Returns:
        list[str]: The product names.
    """
    return list(PRICE_BY_PRODUCT.keys())


@tool
def get_product_price(product_name: str) -> float:
    """
    Get's the product price.

    Args:
        product_name (str): The product name.

    Returns:
        float: The product price.
    """
    return PRICE_BY_PRODUCT[product_name]


def main():
    model = get_model()

    writer_agent = ToolCallingAgent(
        tools=[],
        add_base_tools=False,
        model=model,
        name="writer_agent",
        description=(
            """
            Writes text like poems for you.
            """
        ),
        # provide_run_summary=True
    )

    reviewer_agent_1 = ToolCallingAgent(
        tools=[],
        add_base_tools=False,
        model=model,
        name="reviewer_agent_1",
        description=(
            """
            Reviews text for you.
            Prefers a concise and clear style.
            Please provide constructive feedback.
            """
        ),
        # provide_run_summary=True
    )

    reviewer_agent_2 = ToolCallingAgent(
        tools=[],
        add_base_tools=False,
        model=model,
        name="reviewer_agent_2",
        description=(
            """
            Reviews text for you. Prefers a great ending.
            Please provide constructive feedback.
            """
        ),
        # provide_run_summary=True
    )

    manager_agent = CodeAgent(
        tools=[],
        add_base_tools=False,
        model=model,
        managed_agents=[
            writer_agent, reviewer_agent_1, reviewer_agent_2
        ]
    )

    manager_agent.run(
        """
        Please let the `writer` write a poem about bananas.
        Then get it reviewed by both reviewers.
        Then let the writer revise the poem based on the reviews.
        Do that in a loop until the poem is good enough,
        up to 3 revisions.
        Finally, summarize the poem and both reviews.
        Return everything together.
        """
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    main()
