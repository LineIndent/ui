import reflex as rx

from components.ui.button import button
from components.ui.button_group import button_group
from components.ui.kbd import kbd
from components.ui.tooltip import tooltip


def kbd_tooltip() -> rx.Component:
    return rx.el.div(
        button_group.root(
            tooltip.provider(
                tooltip.root(
                    tooltip.trigger(
                        render_=button("Save", variant="outline"),
                    ),
                    tooltip.portal(
                        tooltip.positioner(
                            tooltip.popup(
                                tooltip.arrow(),
                                "Save Changes ",
                                kbd.root("S"),
                            ),
                        ),
                    ),
                ),
                delay=0,
            ),
            tooltip.provider(
                tooltip.root(
                    tooltip.trigger(
                        render_=button("Print", variant="outline"),
                    ),
                    tooltip.portal(
                        tooltip.positioner(
                            tooltip.popup(
                                tooltip.arrow(),
                                "Print Document ",
                                kbd.group(
                                    kbd.root("Ctrl"),
                                    kbd.root("P"),
                                ),
                            ),
                        ),
                    ),
                ),
                delay=0,
            ),
        ),
        class_name="flex flex-wrap gap-4",
    )
