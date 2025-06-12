# MCP Server Only Example

This example is similar to the simple MCP server. However in this example, we are only enabling the MCP server and not the REST endpoints.

## Run

```console
$ uv run fastapi dev python_examples/ai/mcp/fastapi_mcp/mcp_only/server.py
INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO   Started reloader process [187627] using WatchFiles
INFO   Started server process [187651]
INFO   Waiting for application startup.
INFO   Application startup complete.
```

The MCP server in `SSE` mode is available under: `http://127.0.0.1:8000/sse`
