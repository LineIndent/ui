import reflex as rx

from components.icons.hugeicon import hi
from components.ui.breadcrumb import breadcrumb


def breadcrumb_custom_separator() -> rx.Component:
    return breadcrumb.root(
        breadcrumb.list(
            breadcrumb.item(
                breadcrumb.link("Home", href="#"),
            ),
            breadcrumb.separator(hi("LinerIcon")),
            breadcrumb.item(
                breadcrumb.link("Components", href="#"),
            ),
            breadcrumb.separator(hi("LinerIcon")),
            breadcrumb.item(
                breadcrumb.page("Breadcrumb"),
            ),
        )
    )
