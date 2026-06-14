import reflex as rx

from components.ui.input_group import input_with_addons


def input_group_url_input():
    return rx.el.div(
        input_with_addons(
            placeholder="example.com",
            prefix="https://",
            suffix=".com",
        ),
        class_name="w-full max-w-sm mx-auto py-6",
    )
