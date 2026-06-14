from components.ui.button import button
from components.ui.menu import menu


def menu_high_level():
    return menu.root(
        menu.trigger(render_=button("Open", variant="outline")),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("My Account"),
                        menu.item("Profile"),
                        menu.item("Billing"),
                        menu.item("Settings"),
                    ),
                    menu.separator(),
                    menu.group(
                        menu.item("Team"),
                        menu.submenu_root(
                            menu.submenu_trigger("Invite users"),
                            menu.portal(
                                menu.positioner(
                                    menu.popup(
                                        menu.item("Email"),
                                        menu.item("Message"),
                                        menu.separator(),
                                        menu.item("More..."),
                                    ),
                                    side="right",
                                    align="start",
                                    align_offset=-3,
                                    side_offset=0,
                                ),
                            ),
                        ),
                        menu.item("New Team"),
                    ),
                    menu.separator(),
                    menu.group(
                        menu.item("GitHub"),
                        menu.item("Support"),
                        menu.item("API", disabled=True),
                    ),
                    menu.separator(),
                    menu.group(menu.item("Log out")),
                    class_name="w-40",
                ),
                align="start",
            ),
        ),
    )
