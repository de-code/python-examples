import gradio as gr


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


if __name__ == "__main__":
    demo.launch(mcp_server=True)
