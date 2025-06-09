# Integrate FastMCP into FastAPI App

Simple [FastMCP server integrated into FastAPI App](https://gofastmcp.com/deployment/asgi) example.

## Run

```console
$ uv run fastapi dev python_examples/ai/mcp/fastmcp/integrate_into_fastapi_app/server.py
...
INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO   Started reloader process [425543] using WatchFiles
INFO   Started server process [425567]
INFO   Waiting for application startup.
INFO   Application startup complete.
```

Streamable MCP Server available under: `http://127.0.0.1:8000/example/mcp`

## Unit Tests

```bash
uv run pytest python_examples/ai/mcp/fastmcp/integrate_into_fastapi_app/test
```
