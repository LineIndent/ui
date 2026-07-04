import reflex as rx

from components.icons.hugeicon import hi
from components.ui.toggle_group import toggle_group


def toggle_group_disabled() -> rx.Component:
    return toggle_group.root(
        toggle_group.item(
            hi("TextBoldIcon"),
            value="bold",
            aria_label="Toggle bold",
        ),
        toggle_group.item(
            hi("TextItalicIcon"),
            value="italic",
            aria_label="Toggle italic",
        ),
        toggle_group.item(
            hi("TextUnderlineIcon"),
            value="strikethrough",
            aria_label="Toggle strikethrough",
        ),
        disabled=True,
    )
