import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.button_group import button_group


def button_group_split() -> rx.Component:
    return button_group.root(
        button("Button", variant="secondary"),
        button_group.separator(),
        button(
            hi("Add01Icon"),
            variant="secondary",
            size="icon",
        ),
    )
