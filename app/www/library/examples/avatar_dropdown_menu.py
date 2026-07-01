import reflex as rx

from components.ui.avatar import avatar
from components.ui.button import button
from components.ui.menu import menu


def avatar_dropdown_menu() -> rx.Component:
    return menu.root(
        menu.trigger(
            render_=button(
                avatar.root(
                    avatar.image(
                        src="https://github.com/LineIndent.png",
                        custom_attrs={"alt": "lineindent"},
                    ),
                    avatar.fallback("LI"),
                ),
                variant="ghost",
                size="icon",
                class_name="rounded-full",
            )
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.item("Profile"),
                        menu.item("Billing"),
                        menu.item("Settings"),
                    ),
                    class_name="w-32",
                ),
            )
        ),
    )
