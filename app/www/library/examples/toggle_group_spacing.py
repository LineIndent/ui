import reflex as rx

from components.ui.toggle_group import toggle_group


def toggle_group_spacing() -> rx.Component:
    return toggle_group.root(
        toggle_group.item("Top", value="top", aria_label="Toggle top"),
        toggle_group.item("Bottom", value="bottom", aria_label="Toggle bottom"),
        toggle_group.item("Left", value="left", aria_label="Toggle left"),
        toggle_group.item("Right", value="right", aria_label="Toggle right"),
        size="sm",
        variant="outline",
        spacing=4,
        default_value=["top"],
    )
