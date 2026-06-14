import reflex as rx
from components.ui.input import input


def input_email():
    return rx.el.div(
        rx.el.p("Email Input", class_name="text-sm font-medium mb-2"),
        input(
            type="email",
            placeholder="name@example.com",
        ),
        class_name="w-full max-w-md p-8",
    )

