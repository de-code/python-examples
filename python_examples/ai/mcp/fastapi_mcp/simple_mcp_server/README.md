# Simple MCP Server

## Run

```console
$ uv run fastapi dev python_examples/ai/mcp/fastapi_mcp/simple_mcp_server/server.py
INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO   Started reloader process [187627] using WatchFiles
INFO   Started server process [187651]
INFO   Waiting for application startup.
INFO   Application startup complete.
```

The regular FastAPI server will be available on port `8000` with the MCP server mounted in `SSE` mode on `/sse`.

That means you can interact with the tool directly via the REST API on `/add_numbers` (or use `/docs`).

Unfortunately `Streamable HTTP` isn't supported yet ([as of June 2025](https://github.com/tadata-org/fastapi_mcp/issues/61)).
