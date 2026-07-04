import reflex as rx

from components.ui.toggle_group import toggle_group


def toggle_group_vertical() -> rx.Component:
    return toggle_group.root(
        toggle_group.item(
            rx.icon(tag="bold"),
            value="bold",
            aria_label="Toggle bold",
        ),
        toggle_group.item(
            rx.icon(tag="italic"),
            value="italic",
            aria_label="Toggle italic",
        ),
        toggle_group.item(
            rx.icon(tag="underline"),
            value="underline",
            aria_label="Toggle underline",
        ),
        multiple=True,
        orientation="vertical",
        spacing=1,
        default_value=["bold", "italic"],
    )
