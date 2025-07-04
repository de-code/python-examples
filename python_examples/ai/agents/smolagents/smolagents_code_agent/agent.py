import logging
import os

from dotenv import load_dotenv

from pydantic import TypeAdapter

from smolagents import (  # type: ignore[import-untyped]
    CodeAgent,
    Model,
    OpenAIServerModel,
    tool
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

    agent = CodeAgent(
        tools=[get_product_names, get_product_price],
        add_base_tools=False,
        model=model,
        max_steps=3
    )

    agent.run("What is the cheapest product?")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    main()
