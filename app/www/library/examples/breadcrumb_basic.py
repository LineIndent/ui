import reflex as rx

from components.ui.breadcrumb import breadcrumb


def breadcrumb_basic() -> rx.Component:
    return breadcrumb.root(
        breadcrumb.list(
            breadcrumb.item(
                breadcrumb.link("Home", href="#"),
            ),
            breadcrumb.separator(),
            breadcrumb.item(
                breadcrumb.link("Components", href="#"),
            ),
            breadcrumb.separator(),
            breadcrumb.item(
                breadcrumb.page("Breadcrumb"),
            ),
        )
    )
