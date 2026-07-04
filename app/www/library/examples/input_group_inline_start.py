import reflex as rx

from components.icons.hugeicon import hi
from components.ui.input_group import input_group


def input_group_inline_start() -> rx.Component:
    return input_group.root(
        input_group.input(
            id="inline-start-input",
            placeholder="Search...",
        ),
        input_group.addon(
            hi("SearchIcon", class_name="text-muted-foreground"),
            align="inline-start",
        ),
        class_name="max-w-sm",
    )
