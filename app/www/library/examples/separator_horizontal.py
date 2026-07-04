import reflex as rx

from components.ui.separator import separator


def separator_horizontal() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div("buridan/ui", class_name="leading-none font-medium"),
            rx.el.div(
                "The UI Library for Reflex Devs.",
                class_name="text-muted-foreground",
            ),
            class_name="flex flex-col gap-1.5",
        ),
        separator(class_name="bg-zinc-200 dark:bg-zinc-800"),
        rx.el.div(
            "A set of beautifully designed components that you can customize, extend, and build on."
        ),
        class_name="flex max-w-sm flex-col gap-4 text-sm",
    )
