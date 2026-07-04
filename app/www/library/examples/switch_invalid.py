import reflex as rx

from components.ui.field import field
from components.ui.switch import switch


def switch_invalid() -> rx.Component:
    return field.root(
        field.content(
            field.label(
                "Accept terms and conditions",
                html_for="switch-terms",
            ),
            field.description("You must accept the terms and conditions to continue."),
        ),
        switch.root(
            id="switch-terms",
            aria_invalid="true",
        ),
        orientation="horizontal",
        data_invalid="true",
        class_name="max-w-sm",
    )
