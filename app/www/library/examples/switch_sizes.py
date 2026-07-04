import reflex as rx

from components.ui.field import field
from components.ui.switch import switch


def switch_sizes() -> rx.Component:
    return field.group(
        field.root(
            switch.root(
                id="switch-size-sm",
                size="sm",
            ),
            field.label(
                "Small",
                html_for="switch-size-sm",
            ),
            orientation="horizontal",
        ),
        field.root(
            switch.root(
                id="switch-size-default",
                size="default",
            ),
            field.label(
                "Default",
                html_for="switch-size-default",
            ),
            orientation="horizontal",
        ),
        class_name="w-full max-w-[10rem]",
    )
