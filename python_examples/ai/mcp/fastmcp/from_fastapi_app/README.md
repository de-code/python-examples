# FastMCP from FastAPI App

Convert [FastAPI App to FastMCP server](https://gofastmcp.com/servers/openapi#fastapi-integration) example.

## Run FastMCP App (from FastAPI App)

```console
$ uv run fastmcp run --transport=streamable-http \
    python_examples/ai/mcp/fastmcp/from_fastapi_app/server.py:mcp
...
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Run FastAPI App (without MCP)

```console
$ uv run uvicorn python_examples.ai.mcp.fastmcp.from_fastapi_app.server:app
...
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Streamable MCP Server available under: `http://127.0.0.1:8000/example/mcp`

## Unit Tests

```bash
uv run pytest python_examples/ai/mcp/fastmcp/from_fastapi_app/test
```
