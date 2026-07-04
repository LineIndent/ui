import reflex as rx

from components.ui.button import button
from components.ui.kbd import kbd


def kbd_button() -> rx.Component:
    return button(
        "Accept ",
        kbd.root(
            "⏎",
            data_icon="inline-end",
            class_name="translate-x-0.5",
        ),
        variant="outline",
    )
