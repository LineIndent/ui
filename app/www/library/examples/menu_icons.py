import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.menu import menu


def menu_icons() -> rx.Component:
    return menu.root(
        menu.trigger(
            render_=button("Open", variant="outline"),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.item(hi("UserIcon"), "Profile"),
                    menu.item(hi("CreditCardIcon"), "Billing"),
                    menu.item(hi("Setting07Icon"), "Settings"),
                    menu.separator(),
                    menu.item(
                        hi("LogoutSquare01Icon"), "Log out", variant="destructive"
                    ),
                ),
            ),
        ),
    )
