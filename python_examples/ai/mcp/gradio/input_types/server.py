import gradio as gr


def dummy_fn(*_) -> str:
    """Dummy function."""
    return "Dummy output"


demo = gr.Interface(
    fn=dummy_fn,
    api_name="dummy_fn",
    inputs=[
        gr.Number(label="Number (precision=0)", precision=0),
        gr.Number(label="Number (precision=1)", precision=1),
        gr.Slider(minimum=0, maximum=10, value=5),
        gr.Textbox(),
        gr.Checkbox(value=True),
        gr.Radio(choices=["one", "two", "three"]),
        gr.Dropdown(choices=["one", "two", "three"]),
        gr.DateTime(
            label="DateTime (/wo time)", include_time=False
        ),
        gr.DateTime(
            label="DateTime (/w time)", include_time=True
        ),
        # gr.MultimodalTextbox()
    ],
    outputs=[gr.Textbox()]
)


if __name__ == "__main__":
    demo.launch(mcp_server=True)
