# Gradio Input Types

In this example we are exploring different input types and their effect on the generated MCP tools schema.

## Run

```console
$ uv run -m python_examples.ai.mcp.gradio.input_types.server
* Running on local URL:  http://127.0.0.1:7860
* To create a public link, set `share=True` in `launch()`.

🔨 Launching MCP server:
** Streamable HTTP URL: http://127.0.0.1:7860/gradio_api/mcp/
* [Deprecated] SSE URL: http://127.0.0.1:7860/gradio_api/mcp/sse
```

The Gradio App will be available under: `http://127.0.0.1:7860`

The MCP server will be available with the two transport modes:

- Streamable HTTP: `http://127.0.0.1:7860/gradio_api/mcp/` (since [v5.32.0](https://github.com/gradio-app/gradio/releases/tag/gradio%405.32.0))
- SSE (deprecated): `http://127.0.0.1:7860/gradio_api/mcp/sse`
