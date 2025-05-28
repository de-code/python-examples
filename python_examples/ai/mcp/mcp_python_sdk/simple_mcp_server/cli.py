import logging
import os

from .server import mcp


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
