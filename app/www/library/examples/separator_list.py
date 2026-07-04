import reflex as rx

from components.ui.separator import separator


def separator_list() -> rx.Component:
    return rx.el.div(
        rx.el.dl(
            rx.el.dt("Item 1"),
            rx.el.dd("Value 1", class_name="text-muted-foreground"),
            class_name="flex items-center justify-between",
        ),
        separator(),
        rx.el.dl(
            rx.el.dt("Item 2"),
            rx.el.dd("Value 2", class_name="text-muted-foreground"),
            class_name="flex items-center justify-between",
        ),
        separator(),
        rx.el.dl(
            rx.el.dt("Item 3"),
            rx.el.dd("Value 3", class_name="text-muted-foreground"),
            class_name="flex items-center justify-between",
        ),
        class_name="flex w-full max-w-sm flex-col gap-2 text-sm",
    )
