# Smolagents MCP STDIO

In this example we are defining a custom tool via an MCP server using STDIO.
We are still using [smolagents](https://github.com/huggingface/smolagents) with a chat interfact powered by [Gradio](https://github.com/gradio-app/gradio).

## Environment Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| OPENAI_BASE_URL | The base URL for the OpenAI compatible API | https://api.openai.com/v1 |
| OPENAI_API_KEY | The API key for the above API | |
| OPENAI_MODEL_ID | The model to use | gpt-4o-mini |
| OPENAI_FLATTEN_MESSAGES | Whether the API expects message content to be str rather than object | false |

## Run Smolagents Gradio App

```console
$ uv run -m python_examples.ai.agents.smolagents.smolagents_mcp_stdio.agent
* Running on local URL:  http://127.0.0.1:7860
...
```

The chat interface is then available via: `http://127.0.0.1:7860`

## Example prompts

- `Please calculate the square root of 16`
