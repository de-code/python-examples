from fastapi import FastAPI
import gradio as gr
from gradio.mcp import GradioMCPServer


def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


demo = gr.Interface(
    fn=add_numbers,
    api_name="add_numbers",
    inputs=[
        gr.Number(precision=0, value=1),
        gr.Number(precision=0, value=2)
    ],
    outputs=[gr.Number(precision=0)],
)

mcp_server = GradioMCPServer(demo)

app = FastAPI(lifespan=mcp_server.lifespan)

mcp_server.launch_mcp_on_sse(
    app=app,
    subpath="/mcp",
    root_path="/dummy_root_path"
)
