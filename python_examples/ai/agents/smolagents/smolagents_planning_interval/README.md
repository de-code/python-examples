# Smolagents Planning Interval

In this example we are using [smolagents](https://github.com/huggingface/smolagents), demonstrating the use of `planning_interval`.

## Environment Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| OPENAI_BASE_URL | The base URL for the OpenAI compatible API | https://api.openai.com/v1 |
| OPENAI_API_KEY | The API key for the above API | |
| OPENAI_MODEL_ID | The model to use | gpt-4o-mini |
| OPENAI_FLATTEN_MESSAGES | Whether the API expects message content to be str rather than object | false |

## Run Without Planning

```console
$ uv run -m python_examples.ai.agents.smolagents.smolagents_planning_interval.agent
```

## Run With Planning

```console
$ uv run -m python_examples.ai.agents.smolagents.smolagents_planning_interval.agent \
    --planning-interval=2
```
