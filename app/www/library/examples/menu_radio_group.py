import reflex as rx
from reflex.experimental import ClientStateVar

from components.ui.button import button
from components.ui.menu import menu

panel_position = ClientStateVar.create("panel_position", "bottom")


def menu_radio_group() -> rx.Component:
    return menu.root(
        panel_position,
        menu.trigger(
            render_=button("Open", variant="outline"),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("Panel Position"),
                        menu.radio_group(
                            menu.radio_item(
                                "Top",
                                menu.radio_item_indicator(),
                                value="top",
                            ),
                            menu.radio_item(
                                "Bottom",
                                menu.radio_item_indicator(),
                                value="bottom",
                            ),
                            menu.radio_item(
                                "Right",
                                menu.radio_item_indicator(),
                                value="right",
                            ),
                            value=panel_position.value,
                            on_value_change=panel_position.set_value,
                        ),
                    ),
                    class_name="w-32",
                ),
            ),
        ),
    )
