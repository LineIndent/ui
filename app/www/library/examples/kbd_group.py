import reflex as rx

from components.ui.kbd import kbd


def kbd_as_group() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            "Use ",
            kbd.group(
                kbd.root("Ctrl + B"),
                kbd.root("Ctrl + K"),
            ),
            " to open the command palette",
            class_name="text-sm text-muted-foreground",
        ),
        class_name="flex flex-col items-center gap-4",
    )
