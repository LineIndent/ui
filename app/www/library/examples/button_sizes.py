import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button


def button_size() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            button("Extra Small", size="xs", variant="outline"),
            button(
                hi("ArrowUpRight03Icon"),
                size="icon-xs",
                aria_label="Submit",
                variant="outline",
            ),
            class_name="flex items-start gap-2",
        ),
        rx.el.div(
            button("Small", size="sm", variant="outline"),
            button(
                hi("ArrowUpRight03Icon"),
                size="icon-sm",
                aria_label="Submit",
                variant="outline",
            ),
            class_name="flex items-start gap-2",
        ),
        rx.el.div(
            button("Default", variant="outline"),
            button(
                hi("ArrowUpRight03Icon"),
                size="icon",
                aria_label="Submit",
                variant="outline",
            ),
            class_name="flex items-start gap-2",
        ),
        rx.el.div(
            button("Large", variant="outline", size="lg"),
            button(
                hi("ArrowUpRight03Icon"),
                size="icon-lg",
                aria_label="Submit",
                variant="outline",
            ),
            class_name="flex items-start gap-2",
        ),
        class_name="flex flex-col items-start gap-8 sm:flex-row",
    )
