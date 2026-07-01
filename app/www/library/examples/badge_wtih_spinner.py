import reflex as rx

from components.ui.badge import badge
from components.ui.spinner import spinner


def badge_with_spinner() -> rx.Component:
    return rx.el.div(
        badge(
            spinner(custom_attrs={"data-icon": "inline-start"}),
            "Deleting",
            variant="destructive",
        ),
        badge(
            "Generating",
            spinner(custom_attrs={"data-icon": "inline-end"}),
            variant="secondary",
        ),
        class_name="flex flex-wrap gap-2",
    )
