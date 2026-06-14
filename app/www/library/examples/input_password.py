import reflex as rx
from components.ui.input import input


def input_password():
    return rx.el.div(
        rx.el.p("Password Input", class_name="text-sm font-medium mb-2"),
        input(
            type="password",
            placeholder="Enter your password",
        ),
        class_name="w-full max-w-md p-8",
    )

