import reflex as rx
from components.ui.textarea import textarea


def textarea_custom_text_area():
    return rx.el.div(
        rx.el.p("Custom Height", class_name="text-sm font-medium mb-2"),
        textarea(
            placeholder="Taller textarea",
            class_name="min-h-32",
        ),
        class_name="w-full max-w-md p-8",
    )
