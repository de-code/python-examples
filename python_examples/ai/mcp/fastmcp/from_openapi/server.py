import yaml
import httpx

from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, MCPType


client = httpx.AsyncClient(base_url="https://api.apis.guru/v2")

openapi_spec = yaml.safe_load(
    httpx.get("https://api.apis.guru/v2/openapi.yaml").text
)

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="OpenAPI MCP Server",
    route_maps=[
        RouteMap(mcp_type=MCPType.TOOL)
    ]
)
