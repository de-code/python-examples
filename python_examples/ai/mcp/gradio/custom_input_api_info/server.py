import gradio as gr


def dummy_fn(a: int) -> int:
    """Dummy function."""
    return a


def get_integer(*args, precision: int = 0, **kwargs) -> gr.Number:
    assert precision == 0
    number = gr.Number(*args, precision=precision, **kwargs)
    number.api_info = (  # type: ignore[method-assign]
        lambda: {"type": "integer"}
    )
    return number


demo = gr.Interface(
    fn=dummy_fn,
    api_name="dummy_fn",
    inputs=[
        get_integer(),
    ],
    outputs=[get_integer()]
)


if __name__ == "__main__":
    demo.launch(mcp_server=True)
