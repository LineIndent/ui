import reflex as rx
from components.ui.input import input


def input_file_input():
    return rx.el.div(
        rx.el.p("File Input", class_name="text-sm font-medium mb-2"),
        input(
            type="file",
        ),
        class_name="w-full max-w-md p-8",
    )

