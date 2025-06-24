# Gradio MCP Server Example

This example is using `GradioMCPServer` directly.

## Run

```console
$ uv run fastapi dev python_examples/ai/mcp/gradio/gradio_mcp_server/server.py
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      ...
      INFO   Application startup complete.
```

The MCP server will be available in the `Streamable HTTP` transport mode: `http://127.0.0.1:8000/mcp/`

