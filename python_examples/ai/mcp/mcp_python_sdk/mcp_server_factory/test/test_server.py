import pytest
from mcp.types import TextContent

from ..server import AppConfig, create_mcp_for_config


class TestMcp:
    def test_should_set_name(self):
        mcp = create_mcp_for_config(
            config=AppConfig(name="TestApp")
        )
        assert mcp.name == "TestApp"

    @pytest.mark.asyncio
    async def test_should_add_two_numbers(self):
        mcp = create_mcp_for_config(
            config=AppConfig(name="TestApp")
        )
        result = await mcp.call_tool(
            "add_numbers",
            arguments={"a": 1, "b": 2}
        )
        assert result
        assert isinstance(result[0], TextContent)
        assert result[0].text == '3'
