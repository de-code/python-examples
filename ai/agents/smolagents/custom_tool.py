from dotenv import load_dotenv

from smolagents import (
    tool,
    MultiStepAgent,
    ToolCallingAgent,
    Model
)

from ai.agents.smolagents.utils import get_model


@tool
def get_interesting_fact(location: str) -> str:
    '''
    Returns some interesting fact.
    Args:
        location: The location to fetch an interesting fact about.
    Returns:
        str: A string something interesting
    '''
    return f'{location} is a place that is very small indeed.'


def get_agent(model: Model) -> MultiStepAgent:
    return ToolCallingAgent(
        tools=[get_interesting_fact],
        model=model,
    )


def main():
    agent = get_agent(model=get_model())
    agent.run('What are some interesting fact about Smolandsmolr?')


if __name__ == '__main__':
    load_dotenv()
    main()
