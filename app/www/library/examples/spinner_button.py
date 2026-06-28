import reflex as rx

from components.ui.button import button
from components.ui.spinner import spinner


def spinner_button():
    return rx.el.div(
        button(spinner(), "Loading...", disabled=True, size="sm"),
        button(spinner(), "Please wait", disabled=True, size="sm", variant="outline"),
        button(spinner(), "Processing", disabled=True, size="sm", variant="secondary"),
        class_name="flex flex-col items-center gap-4",
    )
