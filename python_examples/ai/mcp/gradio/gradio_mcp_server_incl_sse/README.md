# Gradio MCP Server Example (Incl SSE)

This example is using `GradioMCPServer` directly.

## Run

```console
$ uv run fastapi dev python_examples/ai/mcp/gradio/gradio_mcp_server_incl_sse/server.py
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      ...
      INFO   Application startup complete.
```

The MCP server will be available with the two transport modes:

- Streamable HTTP: `http://127.0.0.1:8000/mcp/http/`
- SSE (deprecated): `http://127.0.0.1:8000/mcp/sse`
