import reflex as rx

from components.ui.button import button
from components.ui.button_group import button_group


def button_group_separator() -> rx.Component:
    return button_group.root(
        button("Copy", variant="secondary", size="sm"),
        button_group.separator(),
        button("Paste", variant="secondary", size="sm"),
    )
