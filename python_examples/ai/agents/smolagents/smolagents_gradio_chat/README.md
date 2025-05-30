# Smolagents Gradio Chat

In this example we are using [smolagents](https://github.com/huggingface/smolagents) with a chat interfact powered by [Gradio](https://github.com/gradio-app/gradio).

## Run

```console
$ python -m python_examples.ai.agents.smolagents.smolagents_gradio_chat.agent
* Running on local URL:  http://127.0.0.1:7860
INFO:httpx:HTTP Request: GET http://127.0.0.1:7860/gradio_api/startup-events "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: HEAD http://127.0.0.1:7860/ "HTTP/1.1 200 OK"
* To create a public link, set `share=True` in `launch()`.
INFO:httpx:HTTP Request: GET https://api.gradio.app/pkg-version "HTTP/1.1 200 OK"
```

The chat interface is then available via: `http://127.0.0.1:7860`
