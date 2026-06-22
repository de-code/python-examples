from argparse import ArgumentParser
import logging
import os
from pathlib import Path
import textwrap
from typing import Dict

from dotenv import load_dotenv

from pydantic import TypeAdapter

from smolagents import (  # type: ignore[import-untyped]
    CodeAgent,
    Model,
    MultiStepAgent,
    OpenAIServerModel,
    tool,
    ToolCallingAgent
)
import yaml

from python_examples.ai.agents.smolagents\
    .smolagents_planning_interval.prompts import (
        PROMPTS_DIR_NAME
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


TASK_TO_TIME_IN_HOURS_MAP = {
    "TaskA": 4,
    "TaskB": 3,
    "TaskC": 2,
    "TaskD": 1
}


AVAILABLE_TASK_NAMES = list(TASK_TO_TIME_IN_HOURS_MAP.keys())


@tool
def get_task_names() -> str:
    """
    Get's the available tasks names.
    Returns a set with the task names.

    Returns:
        set: The task names
    """
    return "Available task: " + ", ".join(AVAILABLE_TASK_NAMES)


@tool
def get_task_to_time_in_hours_map() -> str:
    """
    Get's the available tasks.
    Returns a dict with the task names and the time in hours.

    Returns:
        dict: The task names and the time in hours.
    """
    return "\n".join([
        f"{task}: {hours} hours"
        for task, hours in TASK_TO_TIME_IN_HOURS_MAP.items()
    ])


ASSIGNED_PERSON_BY_TASK_NAME: Dict[str, str] = {}


@tool
def assign_task(task: str, person: str) -> str:
    """
    Assignes task to person. Always use this tool for assignments.
    An assignment might get rejected.
    Returns a dict describing the assignment.

    Args:
        task (str): The task name.
        person (str): The person name.

    Returns:
        dict: The assignment as a dict
    """
    if task not in AVAILABLE_TASK_NAMES:
        raise ValueError(f"Invalid task name: {task}")
    ASSIGNED_PERSON_BY_TASK_NAME[task] = person
    return "\n".join([
        f"{_task}: assigned to {_person}"
        for _task, _person in ASSIGNED_PERSON_BY_TASK_NAME.items()
    ])


def override_agent_prompt_templates(
    agent: MultiStepAgent,
    prompt_filename: str
):
    prompt_templates = yaml.safe_load(
        Path(PROMPTS_DIR_NAME)
        .joinpath(prompt_filename)
        .read_text(encoding="utf-8")
    )
    for key, value in prompt_templates.items():
        agent.prompt_templates[key] = value


def final_answer_check_assign_task_called(*_args):
    if not ASSIGNED_PERSON_BY_TASK_NAME:
        raise AssertionError(
            "You must use the `assign_task` task tool"
        )
    return True


def main():
    parser = ArgumentParser()
    parser.add_argument('--max-steps', type=int, default=30)
    parser.add_argument('--planning-interval', type=int)
    parser.add_argument(
        '--agent-type',
        choices=['tool', 'code'],
        default='tool'
    )
    args = parser.parse_args()

    model = get_model()

    agent_class = (
        CodeAgent
        if args.agent_type == 'code'
        else ToolCallingAgent
    )
    kwargs = {}
    if args.agent_type == 'code':
        kwargs['additional_authorized_imports'] = ['json']
    agent = agent_class(
        tools=[
            get_task_names,
            get_task_to_time_in_hours_map,
            assign_task
        ],
        add_base_tools=False,
        model=model,
        max_steps=args.max_steps,
        planning_interval=args.planning_interval,
        final_answer_checks=[
            final_answer_check_assign_task_called
        ],
        **kwargs
    )
    if args.agent_type == 'tool':
        override_agent_prompt_templates(
            agent=agent,
            prompt_filename="toolcalling_agent.yaml"
        )
    print("System prompt:", agent.system_prompt)
    output = agent.run(textwrap.dedent(
        """
        Assign each of the available tasks so Alice and Bob each
        get exactly same number of tasks,
        with the same total time.
        Make sure you attempt assignment using the `assign_task`
        tool.
        Success is measured based on the correct `assign_task` tool
        usage.
        You MUST only include a single tool call at a time.
        Respond only with valid JSON matching the OpenAI function
        calling schema, with double quotes.
        NEVER use Python syntax, text, or single quotes.
        /no_think
        """
    ))
    assert isinstance(output, str)
    print("Available tasks and time:", TASK_TO_TIME_IN_HOURS_MAP)
    assigned_person_by_task_name = ASSIGNED_PERSON_BY_TASK_NAME
    print("Assignments:", assigned_person_by_task_name)
    total_time: dict[str, int] = {}
    for task, person in assigned_person_by_task_name.items():
        total_time[person] = (
            total_time.get(person, 0)
            + TASK_TO_TIME_IN_HOURS_MAP[task]
        )
    print("Total time:", total_time)
    expected_total_dict = {
        "Alice": 4,
        "Bob": 4
    }
    print("Success:", total_time == expected_total_dict)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    main()
