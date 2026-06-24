import reflex as rx

from components.ui.tooltip import tooltip


def attach_tooltip(func: rx.Component, label: str):
    return tooltip.provider(
        tooltip.root(
            tooltip.trigger(func),
            tooltip.portal(
                tooltip.positioner(
                    tooltip.popup(
                        tooltip.arrow(),
                        label,
                        class_name="rounded-radius",
                    ),
                    side="bottom",
                ),
            ),
        ),
        delay=0,
    )
