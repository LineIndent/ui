import reflex as rx

from components.icons.hugeicon import hi
from components.ui.breadcrumb import breadcrumb
from components.ui.button import button
from components.ui.menu import menu


def breadcrumb_dropdown_demo() -> rx.Component:
    return breadcrumb.root(
        breadcrumb.list(
            breadcrumb.item(
                breadcrumb.link("Home", href="#"),
            ),
            breadcrumb.separator(hi("LinerIcon")),
            breadcrumb.item(
                menu.root(
                    menu.trigger(
                        render_=rx.el.button(
                            "Components",
                            hi(
                                "ArrowDown01Icon",
                                custom_attrs={"data-icon": "inline-end"},
                                class_name="size-4",
                            ),
                            class_name="flex flex-row items-center gap-x-2",
                        )
                    ),
                    menu.portal(
                        menu.positioner(
                            menu.popup(
                                menu.group(
                                    menu.item("Documentation"),
                                    menu.item("Themes"),
                                    menu.item("GitHub"),
                                ),
                                align="start",
                            )
                        ),
                    ),
                ),
            ),
            breadcrumb.separator(hi("LinerIcon")),
            breadcrumb.item(
                breadcrumb.page("Breadcrumb"),
            ),
        )
    )
