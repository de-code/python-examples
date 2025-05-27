import pytest
from mcp.types import TextContent

from ..server import mcp


class TestMcp:
    @pytest.mark.asyncio
    async def test_should_add_two_numbers(self):
        result = await mcp.call_tool(
            "add_numbers",
            arguments={"a": 1, "b": 2}
        )
        assert result
        assert isinstance(result[0], TextContent)
        assert result[0].text == '3.0'
