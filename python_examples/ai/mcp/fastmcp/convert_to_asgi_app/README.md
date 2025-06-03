# Convert FastMCP to ASGI App

Simple [FastMCP server converted to an ASGI App](https://gofastmcp.com/deployment/asgi) example.

## Run

```console
$ uv run uvicorn python_examples.ai.mcp.fastmcp.convert_to_asgi_app.server:http_app
INFO:     Started server process [2499000]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Unit Tests

```bash
uv run pytest python_examples/ai/mcp/fastmcp/convert_to_asgi_app/test
```
