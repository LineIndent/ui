import reflex as rx

from components.ui.checkbox import checkbox
from components.ui.field import field


def checkbox_disabled() -> rx.Component:
    return rx.el.div(
        field.root(
            checkbox(
                id="toggle-checkbox-disabled",
                name="toggle-checkbox-disabled",
                disabled=True,
            ),
            field.label(
                "Enable notifications",
                html_for="toggle-checkbox-disabled",
            ),
            orientation="horizontal",
            disabled=True,
        ),
        class_name="mx-auto w-56",
    )
