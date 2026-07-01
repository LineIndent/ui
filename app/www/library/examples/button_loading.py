import reflex as rx

from components.ui.button import button
from components.ui.spinner import spinner


def button_loading() -> rx.Component:
    return rx.el.div(
        button(
            spinner(custom_attrs={"data-icon": "inline-start"}),
            "Generating",
            variant="outline",
        ),
        button(
            "Downloading",
            spinner(custom_attrs={"data-icon": "inline-end"}),
            variant="secondary",
            disabled=True,
        ),
        class_name="flex gap-2",
    )
