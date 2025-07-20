import gradio as gr


def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


with gr.Blocks() as demo:
    gr.api(add_numbers, api_name="add_numbers")


if __name__ == "__main__":
    demo.launch(mcp_server=True)
