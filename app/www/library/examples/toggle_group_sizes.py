import reflex as rx

from components.ui.toggle_group import toggle_group


def toggle_group_sizes() -> rx.Component:
    return rx.el.div(
        toggle_group.root(
            toggle_group.item("Top", value="top", aria_label="Toggle top"),
            toggle_group.item("Bottom", value="bottom", aria_label="Toggle bottom"),
            toggle_group.item("Left", value="left", aria_label="Toggle left"),
            toggle_group.item("Right", value="right", aria_label="Toggle right"),
            size="sm",
            variant="outline",
            default_value=["top"],
        ),
        toggle_group.root(
            toggle_group.item("Top", value="top", aria_label="Toggle top"),
            toggle_group.item("Bottom", value="bottom", aria_label="Toggle bottom"),
            toggle_group.item("Left", value="left", aria_label="Toggle left"),
            toggle_group.item("Right", value="right", aria_label="Toggle right"),
            variant="outline",
            default_value=["top"],
        ),
        class_name="flex flex-col gap-4",
    )
