from components.ui.button import button
from components.ui.menu import menu


def menu_submenu():
    return menu.root(
        menu.trigger(render_=button("Open", variant="outline")),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.item("Team"),
                        menu.submenu_root(
                            menu.submenu_trigger("Invite users"),
                            menu.portal(
                                menu.positioner(
                                    menu.popup(
                                        menu.item("Email"),
                                        menu.item("Message"),
                                        menu.submenu_root(
                                            menu.submenu_trigger("More options"),
                                            menu.portal(
                                                menu.positioner(
                                                    menu.popup(
                                                        menu.item("Calendly"),
                                                        menu.item("Slack"),
                                                        menu.separator(),
                                                        menu.item("Webhook"),
                                                    ),
                                                    side="right",
                                                    align="start",
                                                ),
                                            ),
                                        ),
                                        menu.separator(),
                                        menu.item("Advanced..."),
                                    ),
                                    side="right",
                                    align="start",
                                ),
                            ),
                        ),
                        menu.item("New Team"),
                    ),
                ),
                align="start",
            ),
        ),
    )
