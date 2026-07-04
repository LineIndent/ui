import reflex as rx

from components.ui.separator import separator


def separator_vertical() -> rx.Component:
    return rx.el.div(
        rx.el.div("Blog"),
        separator(orientation="vertical"),
        rx.el.div("Docs"),
        separator(orientation="vertical"),
        rx.el.div("Source"),
        class_name="flex h-5 items-center gap-4 text-sm",
    )
