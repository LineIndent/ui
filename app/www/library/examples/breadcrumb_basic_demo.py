import reflex as rx
from components.ui.breadcrumb import (
    breadcrumb,
    breadcrumb_ellipsis,
    breadcrumb_item,
    breadcrumb_link,
    breadcrumb_list,
    breadcrumb_page,
    breadcrumb_separator,
)


def breadcrumb_basic_demo():
    return rx.el.div(
        breadcrumb(
            breadcrumb_list(
                breadcrumb_item(
                    breadcrumb_link("Home", href="#"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.box(
                                breadcrumb_ellipsis(class_name="size-4"),
                                rx.el.span("Toggle menu", class_name="sr-only"),
                                class_name="flex items-center gap-1",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("Documentation"),
                            rx.menu.item("Themes"),
                            rx.menu.item("GitHub"),
                            class_name="min-w-[8rem]",
                        ),
                    ),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_link("Components", href="#"),
                ),
                breadcrumb_separator(),
                breadcrumb_item(
                    breadcrumb_page("Breadcrumb"),
                ),
            ),
        ),
        class_name="p-8",
    )

