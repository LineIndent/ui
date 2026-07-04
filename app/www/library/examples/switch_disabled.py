import reflex as rx

from components.ui.field import field
from components.ui.switch import switch


def switch_disabled() -> rx.Component:

    return field.root(
        switch.root(
            id="switch-disabled-unchecked",
            disabled=True,
        ),
        field.label(
            "Disabled",
            html_for="switch-disabled-unchecked",
        ),
        orientation="horizontal",
        data_disabled="true",
        class_name="w-fit ",
    )
