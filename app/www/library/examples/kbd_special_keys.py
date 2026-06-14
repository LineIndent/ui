import reflex as rx
from components.ui.kbd import (
    kbd,
)


def kbd_special_keys():
    """Special key examples"""
    return rx.box(
        kbd("Enter"),
        kbd("Esc"),
        kbd("Tab"),
        kbd("Space"),
        kbd("←"),
        kbd("→"),
        kbd("↑"),
        kbd("↓"),
        kbd("Delete"),
        kbd("Backspace"),
        class_name="flex flex-wrap gap-2 p-8",
    )

