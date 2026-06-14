import reflex as rx
from components.ui.breadcrumb import (
    breadcrumb,
    breadcrumb_item,
    breadcrumb_link,
    breadcrumb_list,
    breadcrumb_page,
    breadcrumb_separator,
)


def breadcrumb_simple_breadcrumb():
    return rx.box(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="#"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link("Products", href="#"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link("Electronics", href="#"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_page("Laptop"),
                ),
            ),
        ),
        class_name="p-8",
    )

