from typing import cast

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
        # mcp SDK annotation mismatch: returns tuple[list, dict] at runtime
        # https://github.com/modelcontextprotocol/python-sdk/issues/1251
        content = cast(list[TextContent], result[0])  # type: ignore[index]
        assert content
        assert isinstance(content[0], TextContent)
        assert content[0].text == '3'
