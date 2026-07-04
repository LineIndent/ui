import reflex as rx

from components.ui.separator import separator


def separator_menu() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span("Settings", class_name="font-medium"),
            rx.el.span(
                "Manage preferences", class_name="text-xs text-muted-foreground"
            ),
            class_name="flex flex-col gap-1",
        ),
        separator(orientation="vertical"),
        rx.el.div(
            rx.el.span("Account", class_name="font-medium"),
            rx.el.span(
                "Profile & security", class_name="text-xs text-muted-foreground"
            ),
            class_name="flex flex-col gap-1",
        ),
        separator(orientation="vertical", class_name="hidden md:block"),
        rx.el.div(
            rx.el.span("Help", class_name="font-medium"),
            rx.el.span("Support & docs", class_name="text-xs text-muted-foreground"),
            class_name="hidden flex-col gap-1 md:flex",
        ),
        class_name="flex items-center gap-2 text-sm md:gap-4",
    )
