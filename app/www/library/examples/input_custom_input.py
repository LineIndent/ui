import reflex as rx
from components.ui.input import input


def input_custom_input():
    return rx.el.div(
        rx.el.p("Custom Width", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Max width 300px",
            class_name="max-w-[300px]",
        ),
        class_name="w-full max-w-md p-8",
    )
