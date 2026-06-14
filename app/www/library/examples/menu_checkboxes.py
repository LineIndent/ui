from reflex.experimental import ClientStateVar

from components.ui.button import button
from components.ui.menu import menu

show_status_bar = ClientStateVar.create("show_status_bar", True)
show_activity_bar = ClientStateVar.create("show_activity_bar", False)
show_panel = ClientStateVar.create("show_panel", False)


def menu_checkboxes():
    return menu.root(
        menu.trigger(render_=button("Open", variant="outline")),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("Appearance"),
                        menu.checkbox_item(
                            "Status Bar",
                            menu.checkbox_item_indicator(),
                            default_checked=show_status_bar.value,
                            on_checked_change=show_status_bar.set_value(
                                ~show_status_bar.value
                            ),
                        ),
                        menu.checkbox_item(
                            "Activity Bar",
                            disabled=True,
                        ),
                        menu.checkbox_item(
                            "Panel",
                            menu.checkbox_item_indicator(),
                            default_checked=show_panel.value,
                            on_checked_change=show_panel.set_value,
                        ),
                    ),
                    class_name="w-40",
                ),
            ),
        ),
    )
