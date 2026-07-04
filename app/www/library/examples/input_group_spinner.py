import reflex as rx

from components.ui.input_group import input_group
from components.ui.spinner import spinner


def input_group_spinner() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(placeholder="Searching..."),
            input_group.addon(
                spinner(),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Processing..."),
            input_group.addon(
                spinner(),
                align="inline-start",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Saving changes..."),
            input_group.addon(
                input_group.text("Saving..."),
                spinner(),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Refreshing data..."),
            input_group.addon(
                spinner(),
                align="inline-start",
            ),
            input_group.addon(
                input_group.text(
                    "Please wait...",
                    class_name="text-muted-foreground",
                ),
                align="inline-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-4",
    )
