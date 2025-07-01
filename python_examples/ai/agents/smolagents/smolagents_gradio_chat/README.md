# Smolagents Gradio Chat

In this example we are using [smolagents](https://github.com/huggingface/smolagents) with a chat interfact powered by [Gradio](https://github.com/gradio-app/gradio).

## Environment Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| OPENAI_BASE_URL | The base URL for the OpenAI compatible API | https://api.openai.com/v1 |
| OPENAI_API_KEY | The API key for the above API | |
| OPENAI_MODEL_ID | The model to use | gpt-4o-mini |

## Run

```console
$ uv run -m python_examples.ai.agents.smolagents.smolagents_gradio_chat.agent
* Running on local URL:  http://127.0.0.1:7860
INFO:httpx:HTTP Request: GET http://127.0.0.1:7860/gradio_api/startup-events "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: HEAD http://127.0.0.1:7860/ "HTTP/1.1 200 OK"
* To create a public link, set `share=True` in `launch()`.
INFO:httpx:HTTP Request: GET https://api.gradio.app/pkg-version "HTTP/1.1 200 OK"
```

The chat interface is then available via: `http://127.0.0.1:7860`

## Example prompts

- `Can you add 123 and 234?`
