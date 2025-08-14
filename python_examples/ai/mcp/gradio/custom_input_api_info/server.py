import gradio as gr


def dummy_fn(a: int) -> int:
    """Dummy function."""
    return a


def get_some_id(*args, **kwargs) -> gr.Textbox:
    some_id = gr.Textbox(*args, **kwargs)
    some_id.api_info = (  # type: ignore[method-assign]
        lambda: {"type": "string", "minLength": 2, "maxLength": 10}
    )
    return some_id


demo = gr.Interface(
    fn=dummy_fn,
    api_name="dummy_fn",
    inputs=[
        get_some_id(),
    ],
    outputs=[get_some_id()]
)


if __name__ == "__main__":
    demo.launch(mcp_server=True)
