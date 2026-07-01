import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button


def button_rounded() -> rx.Component:
    return rx.el.div(
        button(
            "Get Started",
            class_name="rounded-full",
        ),
        button(
            hi("ArrowUp02Icon"),
            variant="outline",
            size="icon",
            class_name="rounded-full",
        ),
        class_name="flex gap-2",
    )
