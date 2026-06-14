import reflex as rx
from components.ui.breadcrumb import (
    breadcrumb,
    breadcrumb_item,
    breadcrumb_link,
    breadcrumb_list,
    breadcrumb_page,
    breadcrumb_separator,
)


def breadcrumb_icon_breadcrumb():
    return rx.el.div(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link(
                        rx.icon(tag="home", size=14),
                        "Home",
                        href="#",
                        class_name="flex flex-row gap-x-1 items-center",
                    ),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link(
                        rx.icon(tag="folder", size=14),
                        "Documents",
                        href="#",
                        class_name="flex flex-row gap-x-1 items-center",
                    ),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_page(
                        rx.icon(tag="file-text", size=14),
                        "README.md",
                        class_name="flex flex-row gap-x-1 items-center",
                    ),
                ),
            ),
        ),
        class_name="p-8",
    )

