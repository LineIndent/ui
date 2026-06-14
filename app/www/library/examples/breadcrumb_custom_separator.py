import reflex as rx
from components.ui.breadcrumb import (
    breadcrumb,
    breadcrumb_item,
    breadcrumb_link,
    breadcrumb_list,
    breadcrumb_page,
    breadcrumb_separator,
)


def breadcrumb_custom_separator():
    return rx.el.div(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="#"),
                ),
                breadcrumb_separator(
                    rx.text("/", class_name="text-[var(--muted-foreground)]")
                ),
                breadcrumb_item(
                    breadcrumb_link("Blog", href="#"),
                ),
                breadcrumb_separator(
                    rx.text("/", class_name="text-[var(--muted-foreground)]")
                ),
                breadcrumb_item(
                    breadcrumb_page("Article"),
                ),
            ),
        ),
        class_name="p-8",
    )
