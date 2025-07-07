# Smolagents Multi Agent

In this example we are using [smolagents](https://github.com/huggingface/smolagents) with a multi-agent system.

## Environment Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| OPENAI_BASE_URL | The base URL for the OpenAI compatible API | https://api.openai.com/v1 |
| OPENAI_API_KEY | The API key for the above API | |
| OPENAI_MODEL_ID | The model to use | gpt-4o-mini |
| OPENAI_FLATTEN_MESSAGES | Whether the API expects message content to be str rather than object | false |

## Run

```console
$ uv run -m python_examples.ai.agents.smolagents.smolagents_multi_agent.agent
...
Out - Final answer: banana
```
