import reflex as rx

from components.icons.hugeicon import hi
from components.ui.badge import badge


def badge_as_link() -> rx.Component:
    return badge(
        rx.el.a(
            "Open Link",
            hi("ArrowUpRightIcon", custom_attrs={"data-icon": "inline-end"}),
            href="#link",
            class_name="inline-flex items-center gap-1 text-inherit no-underline",
        ),
    )
