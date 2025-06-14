from typing import Annotated
from fastapi import FastAPI, Query
from fastapi_mcp import FastApiMCP  # type: ignore[import-untyped]


app = FastAPI(title="MCP Server API", version="0.0.1")


@app.get(
    "/add_numbers",
    operation_id="add_numbers",
    description="Add two numbers"
)
async def add_numbers(
    a: Annotated[
        int,
        Query(title="A", description="First number to add")
    ],
    b: Annotated[
        int,
        Query(title="B", description="Second number to add")
    ]
) -> int:
    return a + b


mcp = FastApiMCP(
    app,
    describe_all_responses=True,
    describe_full_response_schema=True
)
mcp.mount(mount_path="/sse", transport="sse")
