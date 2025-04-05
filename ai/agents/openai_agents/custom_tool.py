import json
import logging
import os
import textwrap

from dotenv import load_dotenv

from agents import Agent, Model, ModelSettings, Runner, Tool, function_tool

from ai.agents.openai_agents.utils import configure_otlp_if_enabled, get_model


LOGGER = logging.getLogger(__name__)


@function_tool
def get_weather(location: str) -> str:
    '''
    Returns the current weather for specified location.

    Args:
        location: The location to fetch an weather for.

    Returns:
        str: The current weather
    '''
    return f'The current weather in {location} is sunny at 30C.'


def get_tool_instruction(tool: Tool) -> str:
    LOGGER.info('params_json_schema: %r', tool.params_json_schema)
    example_tool_call = {
        'arguments': json.dumps({
            param_name: param_spec.get('description', param_spec['title'])
            for param_name, param_spec in tool.params_json_schema.get('properties', {}).items()
        }),
        'name': tool.name
    }
    return f'- {tool.name}: {tool.description}\nExample tool call:\n{json.dumps(example_tool_call)}'


def get_agent(model: Model) -> Agent:
    tools = [get_weather]
    tool_instructions = '\n'.join([
        get_tool_instruction(tool)
        for tool in tools
    ])
    instructions = textwrap.dedent(
        f''''
        You are a helpful assistant. Always use a tool and keep your response brief.
        Use previous tool results.
        You only have access to the following tools:
        {tool_instructions}'
        '''
    )
    LOGGER.info('instructions: %r', instructions)
    return Agent(
        name='Assistant',
        instructions=instructions,
        model=model,
        model_settings=ModelSettings(temperature=0),
        tools=tools
    )


def main():
    configure_otlp_if_enabled(otlp_endpoint=os.getenv('OTLP_ENDPOINT'))
    agent = get_agent(model=get_model())
    result = Runner.run_sync(agent, 'What is the weather in Smallville?')
    print(result.final_output)


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    load_dotenv()
    main()
