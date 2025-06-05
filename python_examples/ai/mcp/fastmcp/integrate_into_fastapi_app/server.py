from fastapi import FastAPI
from fastmcp import FastMCP


mcp: FastMCP = FastMCP(
    name='Example MCP Server',
    json_response=True,
    stateless_http=True
)


@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


mcp_app = mcp.http_app()

app = FastAPI(lifespan=mcp_app.lifespan)
app.mount("/example", mcp_app)
