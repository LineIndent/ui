import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.button_group import button_group


def button_group_size() -> rx.Component:
    return rx.el.div(
        button_group.root(
            button("Small", variant="outline", size="sm"),
            button("Button", variant="outline", size="sm"),
            button("Group", variant="outline", size="sm"),
            button(hi("Add01Icon"), variant="outline", size="icon-sm"),
        ),
        button_group.root(
            button("Default", variant="outline"),
            button("Button", variant="outline"),
            button("Group", variant="outline"),
            button(hi("Add01Icon"), variant="outline", size="icon"),
        ),
        button_group.root(
            button("Large", variant="outline", size="lg"),
            button("Button", variant="outline", size="lg"),
            button("Group", variant="outline", size="lg"),
            button(hi("Add01Icon"), variant="outline", size="icon-lg"),
        ),
        class_name="flex flex-col items-start gap-8",
    )
