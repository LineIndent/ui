import reflex as rx

from components.icons.hugeicon import hi
from components.ui.input_group import input_group


def input_group_inline_end() -> rx.Component:
    return input_group.root(
        input_group.input(
            id="inline-end-input",
            type="password",
            placeholder="Enter password",
        ),
        input_group.addon(
            hi("EyeOffIcon", class_name="text-muted-foreground"),
            align="inline-end",
        ),
        class_name="max-w-sm",
    )
