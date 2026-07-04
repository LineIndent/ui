import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.button_group import button_group
from components.ui.menu import menu


def button_group_dropdown() -> rx.Component:
    return button_group.root(
        button("Follow", variant="outline"),
        menu.root(
            menu.trigger(
                render_=button(
                    hi("ArrowDown01Icon"),
                    variant="outline",
                    class_name="pl-2!",
                ),
            ),
            menu.portal(
                menu.positioner(
                    menu.popup(
                        menu.group(
                            menu.item("Mute Conversation"),
                            menu.item("Mark as Read"),
                            menu.item("Report Conversation"),
                            menu.item("Block User"),
                            menu.item("Share Conversation"),
                            menu.item("Copy Conversation"),
                        ),
                        menu.separator(),
                        menu.group(
                            menu.item("Delete Conversation", variant="destructive"),
                        ),
                        class_name="w-44",
                    ),
                    align="end",
                ),
            ),
        ),
    )
