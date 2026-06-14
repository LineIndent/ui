import reflex as rx
from components.ui.kbd import (
    kbd,
    kbd_group,
)


def kbd_with_icons():
    """Kbd with icons"""
    return rx.box(
        kbd_group(
            kbd(
                rx.icon(tag="command", size=12),
            ),
            rx.el.span("+"),
            kbd("K"),
        ),
        kbd_group(
            kbd(
                rx.icon(tag="arrow-left", size=12),
            ),
            kbd(
                rx.icon(tag="arrow-right", size=12),
            ),
        ),
        class_name="flex flex-col items-center gap-4 p-8",
    )
