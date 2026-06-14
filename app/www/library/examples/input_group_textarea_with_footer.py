import reflex as rx

from components.ui.input_group import textarea_with_footer


def input_group_textarea_with_footer():
    return rx.el.div(
        textarea_with_footer(
            placeholder="Enter your message",
            footer_text="120 characters left",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )
