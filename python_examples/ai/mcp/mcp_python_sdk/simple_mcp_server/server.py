from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name='Example MCP Server')


@mcp.tool()
async def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b
