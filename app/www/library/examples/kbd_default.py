import reflex as rx
from components.ui.kbd import (
    kbd,
    kbd_group,
)


def kbd_default():
    """
    Example matching the shadcn KbdDemo component.
    Shows keyboard shortcuts with modifier keys.
    """
    return rx.box(
        # Mac modifier keys
        kbd_group(
            kbd("⌘"),
            kbd("⇧"),
            kbd("⌥"),
            kbd("⌃"),
        ),
        # Keyboard shortcut combination
        kbd_group(
            kbd("Ctrl"),
            rx.el.span("+"),
            kbd("B"),
        ),
        class_name="flex flex-col items-center gap-4 p-8",
    )

