import reflex as rx

from components.ui.button import button
from components.ui.popover import popover


def popover_aligns():
    sides = [
        "left",
        "top",
        "bottom",
        "right",
        "inline-start",
        "inline-end",
    ]

    return rx.el.div(
        *[
            popover.root(
                popover.trigger(
                    render_=button(
                        side.replace("-", " ").title(), variant="outline", size="sm"
                    )
                ),
                popover.portal(
                    popover.backdrop(),
                    popover.positioner(
                        popover.popup(
                            popover.header(
                                popover.title(f"Align: {side.capitalize()}"),
                                popover.description(
                                    "Set the dimensions for the layer."
                                ),
                            ),
                        ),
                        side=side,
                    ),
                ),
            )
            for side in sides
        ],
        class_name="w-full max-w-xs flex flex-row flex-wrap gap-2.5 items-center justify-center",
    )
