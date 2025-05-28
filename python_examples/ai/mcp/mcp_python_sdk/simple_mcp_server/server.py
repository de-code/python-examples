from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name='Example MCP Server')


@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
