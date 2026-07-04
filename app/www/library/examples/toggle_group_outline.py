import reflex as rx

from components.ui.toggle_group import toggle_group


def toggle_group_outline() -> rx.Component:
    return toggle_group.root(
        toggle_group.item(
            "All",
            value="all",
            aria_label="Toggle all",
        ),
        toggle_group.item(
            "Missed",
            value="missed",
            aria_label="Toggle missed",
        ),
        variant="outline",
        default_value=["all"],
    )
