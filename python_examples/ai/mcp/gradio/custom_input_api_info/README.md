# Gradio Input Types

In this example we looking into overriding the `api_info`, used to generated MCP tools schema.

## Run

```console
$ uv run -m python_examples.ai.mcp.gradio.custom_input_api_info.server
* Running on local URL:  http://127.0.0.1:7860
* To create a public link, set `share=True` in `launch()`.

🔨 MCP server (using SSE) running at: http://127.0.0.1:7860/gradio_api/mcp/sse
```

The Gradio App will be available under: `http://127.0.0.1:7860`

The MCP server will be available with the two transport modes:

- Streamable HTTP: `http://127.0.0.1:7860/gradio_api/mcp/http` (since [v5.32.0](https://github.com/gradio-app/gradio/releases/tag/gradio%405.32.0))
- SSE (deprecated): `http://127.0.0.1:7860/gradio_api/mcp/sse`
