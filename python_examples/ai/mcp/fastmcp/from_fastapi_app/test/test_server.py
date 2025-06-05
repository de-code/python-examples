from fastapi.testclient import TestClient
from fastmcp import Client
from mcp.types import TextContent

import pytest

from ..server import app, mcp


class TestFastApiApp:
    def test_should_add_two_numbers(self):
        with TestClient(app) as client:
            response = client.get(
                "/add_numbers",
                params={"a": 1, "b": 2}
            )
            response.raise_for_status()
            assert response.json() == 3


class TestMcp:
    @pytest.mark.asyncio
    async def test_should_add_two_numbers(self):
        async with Client(mcp) as client:
            result = await client.call_tool(
                "add_numbers",
                arguments={"a": 1, "b": 2}
            )
            assert isinstance(result[0], TextContent)
            assert result[0].text == '3'
