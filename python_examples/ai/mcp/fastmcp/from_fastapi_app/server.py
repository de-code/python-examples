from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType


app = FastAPI(title="MCP Server API", version="0.0.1")


@app.get(
    "/add_numbers",
    operation_id="add_numbers",
    description="Add two numbers"
)
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


mcp: FastMCP = FastMCP.from_fastapi(
    app,
    route_maps=[
        RouteMap(mcp_type=MCPType.TOOL)
    ]
)
