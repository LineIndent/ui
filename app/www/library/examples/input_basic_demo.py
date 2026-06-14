import reflex as rx
from components.ui.input import input


def input_basic_demo():
    return rx.el.div(
        rx.text("Text Input", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Enter your name",
        ),
        class_name="w-full max-w-md p-8",
    )

