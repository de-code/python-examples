import contextlib
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    name='Example MCP Server',
    stateless_http=True,
    json_response=True
)


@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(mcp.session_manager.run())
        yield


app = FastAPI(lifespan=lifespan)
app.mount("/example", mcp.streamable_http_app())
