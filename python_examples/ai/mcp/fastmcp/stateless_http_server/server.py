import logging

from fastmcp import FastMCP


mcp: FastMCP = FastMCP(name='Example MCP Server')


@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def main() -> None:
    mcp.run(
        transport='streamable-http',
        stateless_http=True,
        json_response=True
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
