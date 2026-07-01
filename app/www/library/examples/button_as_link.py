import reflex as rx

from components.ui.button import button_variants


def button_render() -> rx.Component:
    return rx.el.a(
        "Login",
        href="#",
        class_name=button_variants(variant="secondary", size="sm"),
    )
