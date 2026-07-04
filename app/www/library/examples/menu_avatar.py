import reflex as rx

from components.icons.hugeicon import hi
from components.ui.avatar import avatar
from components.ui.button import button
from components.ui.menu import menu


def menu_avatar() -> rx.Component:
    return menu.root(
        menu.trigger(
            render_=button(
                avatar.root(
                    avatar.image(src="https://github.com/shadcn.png", alt="shadcn"),
                    avatar.fallback("LR"),
                ),
                variant="ghost",
                size="icon",
                class_name="rounded-full",
            ),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.item(hi("UserIcon"), "Account"),
                        menu.item(hi("CreditCardIcon"), "Billing"),
                        menu.item(hi("Notification01Icon"), "Notifications"),
                    ),
                    menu.separator(),
                    menu.item(
                        hi("LogoutSquare01Icon"),
                        "Sign Out",
                    ),
                ),
                align="end",
            ),
        ),
    )
