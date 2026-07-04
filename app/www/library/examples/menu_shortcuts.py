import reflex as rx

from components.ui.button import button
from components.ui.menu import menu


def menu_shortcuts() -> rx.Component:
    return menu.root(
        menu.trigger(
            render_=button("Open", variant="outline"),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("My Account"),
                        menu.item("Profile", menu.shortcut("⇧⌘P")),
                        menu.item("Billing", menu.shortcut("⌘B")),
                        menu.item("Settings", menu.shortcut("⌘S")),
                    ),
                    menu.separator(),
                    menu.item("Log out", menu.shortcut("⇧⌘Q")),
                ),
            ),
        ),
    )
