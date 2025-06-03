import logging
import os

from fastmcp import FastMCP


mcp: FastMCP = FastMCP(name='Example MCP Server')


@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def main() -> None:
    mcp.run(
        transport=os.getenv(  # type: ignore[arg-type]
            'MCP_TRANSPORT',
            'streamable-http'
        )
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
