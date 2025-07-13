# Smolagents Telemetry using OTLP

In this example we are using [smolagents](https://github.com/huggingface/smolagents) together with [Arize Phoenix](https://github.com/Arize-ai/phoenix) for monitoring. But the agent could be connecting to any OTLP endpoint and `arize-phonix` isn't directly required by your app.

## Environment Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| OPENAI_BASE_URL | The base URL for the OpenAI compatible API | https://api.openai.com/v1 |
| OPENAI_API_KEY | The API key for the above API | |
| OPENAI_MODEL_ID | The model to use | gpt-4o-mini |
| OPENAI_FLATTEN_MESSAGES | Whether the API expects message content to be str rather than object | false |

## Start Arize Phoenix

```console
$ uv run -m phoenix.server.main serve
...
|  🚀 Phoenix Server 🚀
|  Phoenix UI: http://localhost:6006
|
|  Authentication: False
|  Log traces:
|    - gRPC: http://localhost:4317
|    - HTTP: http://localhost:6006/v1/traces
```

## Run

```console
$ uv run -m python_examples.ai.agents.smolagents.smolagents_telemetry_otlp.agent
...
```

You will then see telemetry in the [Phonix UI](http://localhost:6006) under the `my-app` project.
