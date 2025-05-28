import logging
import os

from .server import create_mcp


def main() -> None:
    mcp = create_mcp()
    mcp.run(
        transport=os.getenv(  # type: ignore[arg-type]
            'MCP_TRANSPORT',
            'streamable-http'
        )
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
