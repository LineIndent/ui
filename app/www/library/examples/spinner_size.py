import reflex as rx

from components.ui.spinner import spinner


def spinner_size():
    return rx.el.div(
        spinner(class_name="size-3"),
        spinner(class_name="size-4"),
        spinner(class_name="size-6"),
        spinner(class_name="size-8"),
        class_name="flex items-center gap-6",
    )
