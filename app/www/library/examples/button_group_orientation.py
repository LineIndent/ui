import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.button_group import button_group


def button_group_orientation() -> rx.Component:
    return button_group.root(
        button(
            hi("Add01Icon"),
            variant="outline",
            size="icon",
        ),
        button(
            hi("MinusSignIcon"),
            variant="outline",
            size="icon",
        ),
        orientation="vertical",
        aria_label="Media controls",
        class_name="h-fit",
    )
