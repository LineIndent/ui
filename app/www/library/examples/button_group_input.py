import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.button_group import button_group
from components.ui.input import input


def button_group_input() -> rx.Component:
    return button_group.root(
        input(placeholder="Search..."),
        button(
            hi("Search01Icon"),
            variant="outline",
            aria_label="Search",
        ),
    )
