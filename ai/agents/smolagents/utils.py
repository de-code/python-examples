import os
from smolagents import (
    Model,
    OpenAIServerModel
)

def get_model() -> Model:
    return OpenAIServerModel(
        model_id=os.getenv('OPENAI_MODEL_ID', 'gpt-4o-mini'),
        api_base=os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1'),
        api_key=os.environ['OPENAI_API_KEY']
    )
