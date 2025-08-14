# MCP Server using Gradio API

## Run

```console
$ uv run -m python_examples.ai.mcp.gradio.gradio_api.server
...
```

The Gradio App will be available under: `http://127.0.0.1:7860`

Although in this case the UI won't have any components.

The MCP server will be available with the two transport modes:

- Streamable HTTP: `http://127.0.0.1:7860/gradio_api/mcp/` (since [v5.32.0](https://github.com/gradio-app/gradio/releases/tag/gradio%405.32.0))
- SSE (deprecated): `http://127.0.0.1:7860/gradio_api/mcp/sse`
