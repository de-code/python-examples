from fastapi import FastAPI
from fastapi_mcp import FastApiMCP  # type: ignore[import-untyped]


rest_app = FastAPI(title="MCP Server API", version="0.0.1")


@rest_app.get(
    "/add_numbers",
    operation_id="add_numbers",
    description="Add two numbers"
)
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

app = FastAPI(title="MCP Server API", version="0.0.1")
mcp = FastApiMCP(rest_app)
mcp.mount(app, mount_path="/sse", transport="sse")
