import gradio as gr


def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


add_numbers_interface = gr.Interface(
    fn=add_numbers,
    api_name="add_numbers",
    inputs=[
        gr.Number(precision=0, value=1),
        gr.Number(precision=0, value=2)
    ],
    outputs=[gr.Number(precision=0)],
)

multiply_numbers_interface = gr.Interface(
    fn=multiply_numbers,
    api_name="multiply_numbers",
    inputs=[
        gr.Number(precision=0, value=1),
        gr.Number(precision=0, value=2)
    ],
    outputs=[gr.Number(precision=0)],
)


demo = gr.TabbedInterface(
    interface_list=[
        add_numbers_interface,
        multiply_numbers_interface
    ],
    tab_names=["Add", "Multiply"]
)


if __name__ == "__main__":
    demo.launch(mcp_server=True)
