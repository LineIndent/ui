import reflex as rx

from components.ui.checkbox import checkbox
from components.ui.field import field


def checkbox_description() -> rx.Component:
    return rx.el.div(
        field.root(
            checkbox(
                id="terms-checkbox-desc",
                name="terms-checkbox-desc",
                default_checked=True,
            ),
            rx.el.div(
                field.label(
                    "Accept terms and conditions",
                    html_for="terms-checkbox-desc",
                ),
                field.description(
                    "By clicking this checkbox, you agree to the terms and conditions."
                ),
                class_name="flex flex-col",
            ),
            orientation="horizontal",
        ),
        class_name="mx-auto w-72",
    )
