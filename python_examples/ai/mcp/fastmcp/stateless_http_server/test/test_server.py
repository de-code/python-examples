from fastapi.testclient import TestClient

from ..server import mcp


class TestHttpApp:
    def test_should_add_two_numbers_via_jsonrpc_tools_call(
        self
    ):
        http_app = mcp.http_app(
            json_response=True,
            stateless_http=True
        )
        with TestClient(http_app) as client:
            response = client.post(
                "/mcp",
                json={
                    "jsonrpc": "2.0",
                    "method": "tools/call",
                    "params": {
                        "name": "add_numbers",
                        "arguments": {
                            "a": 1,
                            "b": 2
                        }
                    },
                    "id": 1
                },
                headers={
                    "Accept": (
                        "application/json, text/event-stream"
                    )
                }
            )
            response.raise_for_status()
            response_json = response.json()
            assert response_json["result"]["content"] == [{
                "text": "3",
                "type": "text"
            }]
