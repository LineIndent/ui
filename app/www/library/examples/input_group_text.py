import reflex as rx

from components.ui.input_group import input_group


def input_group_text() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.addon(
                input_group.text("$"),
                align="inline-start",
            ),
            input_group.input(placeholder="0.00"),
            input_group.addon(
                input_group.text("USD"),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.addon(
                input_group.text("https://"),
                align="inline-start",
            ),
            input_group.input(
                placeholder="example.com",
                class_name="!pl-0.5",
            ),
            input_group.addon(
                input_group.text(".com"),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Enter your username"),
            input_group.addon(
                input_group.text("@company.com"),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.textarea(placeholder="Enter your message"),
            input_group.addon(
                input_group.text(
                    "120 characters left",
                    class_name="text-xs text-muted-foreground",
                ),
                align="block-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-6",
    )
