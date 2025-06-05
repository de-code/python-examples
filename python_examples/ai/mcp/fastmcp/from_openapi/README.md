# FastMCP from OpenAPI

Create [FastMCP server from OpenAPI spec](https://gofastmcp.com/servers/openapi) example.

## Start FastMCP Server

```console
$ uv run fastmcp run --transport=streamable-http \
    python_examples/ai/mcp/fastmcp/from_openapi/server.py:mcp
...
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Streamable HTTP MCP server endpoint: `http://127.0.0.1:8000/mcp`
