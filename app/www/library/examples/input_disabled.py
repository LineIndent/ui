import reflex as rx
from components.ui.input import input


def input_disabled():
    return rx.el.div(
        rx.el.p("Disabled Input", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Disabled input",
            disabled=True,
        ),
        class_name="w-full max-w-md p-8",
    )

