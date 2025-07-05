# Smolagents MCP Streamable HTTP

In this example we are defining a custom tool via an MCP server using Streamable HTTP.
We are still using [smolagents](https://github.com/huggingface/smolagents) with a chat interfact powered by [Gradio](https://github.com/gradio-app/gradio).

## Environment Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| OPENAI_BASE_URL | The base URL for the OpenAI compatible API | https://api.openai.com/v1 |
| OPENAI_API_KEY | The API key for the above API | |
| OPENAI_MODEL_ID | The model to use | gpt-4o-mini |
| OPENAI_FLATTEN_MESSAGES | Whether the API expects message content to be str rather than object | false |

## Run MCP Server

Because we want to connect to an MCP server, we first need to make one available. You could use run any server or even use one that is already running. But here we'll just run one of the MCP examples:

```console
$ uv run -m python_examples.ai.mcp.mcp_python_sdk.simple_mcp_server.cli
INFO:     Started server process [123456]
INFO:     Waiting for application startup.
[05/28/25 01:02:03] INFO     StreamableHTTP    streamable_http_manager.py:109
                             session manager
                             started
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Run Smolagents Gradio App

This expects the MCP server to be available on `http://127.0.0.1:8000/mcp`

```console
$ uv run -m python_examples.ai.agents.smolagents.smolagents_mcp_streamable_http.agent
* Running on local URL:  http://127.0.0.1:7860
...
```

The chat interface is then available via: `http://127.0.0.1:7860`

## Example prompts

- `Can you add 123 and 234?`
