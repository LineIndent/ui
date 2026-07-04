import reflex as rx

from components.icons.hugeicon import hi
from components.ui.input_group import input_group
from components.ui.kbd import kbd


def kbd_input_group() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(placeholder="Search..."),
            input_group.addon(
                hi("Search01Icon"),
                align="inline-start",
            ),
            input_group.addon(
                kbd.root("⌘"),
                kbd.root("K"),
                align="inline-end",
            ),
        ),
        class_name="flex w-full max-w-xs flex-col gap-6",
    )
