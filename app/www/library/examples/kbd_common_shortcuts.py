import reflex as rx
from components.ui.kbd import (
    kbd,
    kbd_group,
)


def kbd_common_shortcuts():
    """Common keyboard shortcuts"""
    return rx.box(
        rx.box(
            rx.text("Save:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("S"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Copy:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("C"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Paste:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("V"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Undo:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("Z"),
            ),
            class_name="flex items-center",
        ),
        class_name="flex flex-col gap-3 p-8",
    )

