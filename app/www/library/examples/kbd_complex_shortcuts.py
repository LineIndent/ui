import reflex as rx
from components.ui.kbd import (
    kbd,
    kbd_group,
)


def kbd_complex_shortcuts():
    """Complex multi-key shortcuts"""
    return rx.box(
        # Three modifier keys
        rx.box(
            rx.text("Screenshot:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("Shift"),
                rx.el.span("+"),
                kbd("S"),
            ),
            class_name="flex items-center mb-3",
        ),
        # Mac command
        rx.box(
            rx.text("Quit:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("⌘"),
                rx.el.span("+"),
                kbd("Q"),
            ),
            class_name="flex items-center mb-3",
        ),
        # Function key
        rx.box(
            rx.text("Full Screen:", class_name="text-sm font-medium mr-2"),
            kbd("F11"),
            class_name="flex items-center",
        ),
        class_name="p-8",
    )

