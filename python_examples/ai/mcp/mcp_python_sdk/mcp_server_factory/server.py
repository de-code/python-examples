from dataclasses import dataclass
import os

from mcp.server.fastmcp import FastMCP


@dataclass
class AppConfig:
    name: str


def get_app_config() -> AppConfig:
    return AppConfig(name=os.getenv("MCP_NAME", "Demo"))


def create_mcp_for_config(config: AppConfig) -> FastMCP:
    mcp = FastMCP(config.name)

    @mcp.tool()
    def add_numbers(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b

    return mcp


def create_mcp() -> FastMCP:
    return create_mcp_for_config(get_app_config())
