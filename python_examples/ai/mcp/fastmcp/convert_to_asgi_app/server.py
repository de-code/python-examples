from fastmcp import FastMCP


mcp: FastMCP = FastMCP(name='Example MCP Server')


@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


http_app = mcp.http_app(json_response=True, stateless_http=True)
