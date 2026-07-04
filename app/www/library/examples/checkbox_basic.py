import reflex as rx

from components.ui.checkbox import checkbox
from components.ui.field import field


def checkbox_basic():
    return rx.el.div(
        field.root(
            checkbox.root(
                checkbox.indicator(),
                id="terms-checkbox-basic",
            ),
            field.label(
                "Accept terms and conditions",
                html_for="terms-checkbox-basic",
            ),
            orientation="horizontal",
        ),
        class_name="mx-auto max-w-sm",
    )
