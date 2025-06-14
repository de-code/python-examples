from fastapi import FastAPI
from fastapi_mcp import FastApiMCP  # type: ignore[import-untyped]


app = FastAPI(title="MCP Server API", version="0.0.1")


@app.get(
    "/add_numbers",
    operation_id="add_numbers",
    description="Add two numbers"
)
async def add_numbers(a: int, b: int) -> int:
    return a + b


mcp = FastApiMCP(app)
mcp.mount(mount_path="/sse", transport="sse")
