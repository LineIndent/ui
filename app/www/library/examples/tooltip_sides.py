import reflex as rx

from components.ui.button import button
from components.ui.tooltip import tooltip

sides = ["left", "top", "bottom", "right"]


def tooltip_sides():

    return rx.el.div(
        *[
            tooltip.provider(
                tooltip.root(
                    tooltip.trigger(
                        render_=button(side.capitalize(), variant="outline", size="sm"),
                    ),
                    tooltip.portal(
                        tooltip.positioner(
                            tooltip.popup(tooltip.arrow(), "Add to library"),
                            side=side,
                        ),
                    ),
                ),
                delay=0,
            )
            for side in sides
        ],
        class_name="flex flex-wrap gap-2",
    )
