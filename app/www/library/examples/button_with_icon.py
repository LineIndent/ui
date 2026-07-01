import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button


def button_with_icon() -> rx.Component:
    return rx.el.div(
        button(
            hi("GitBranchIcon", custom_attrs={"data-icon": "inline-start"}),
            "New Branch",
            variant="outline",
        ),
        button(
            "Fork",
            hi("GitForkIcon", custom_attrs={"data-icon": "inline-end"}),
            variant="outline",
        ),
        class_name="flex gap-2",
    )
