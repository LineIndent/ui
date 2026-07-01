import reflex as rx

from components.icons.hugeicon import hi
from components.ui.badge import badge


def badge_with_icon() -> rx.Component:
    return rx.el.div(
        badge(
            hi("CheckmarkBadge01Icon", custom_attrs={"data-icon": "inline-start"}),
            "Verified",
            variant="secondary",
        ),
        badge(
            "Bookmark",
            hi("Bookmark02Icon", custom_attrs={"data-icon": "inline-end"}),
            variant="outline",
        ),
        class_name="flex flex-wrap gap-2",
    )
