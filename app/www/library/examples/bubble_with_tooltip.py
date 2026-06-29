import reflex as rx

from components.icons.hugeicon import hi
from components.ui.bubble import bubble
from components.ui.button import button
from components.ui.tooltip import tooltip


def bubble_tooltip_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("Did you remove the stale route?"),
            variant="secondary",
        ),
        bubble.root(
            bubble.content("Yes, removed it from the registry."),
            bubble.reactions(
                tooltip.provider(
                    tooltip.root(
                        tooltip.trigger(
                            render_=button(
                                hi("Tick02Icon", class_name="size-4"),
                                variant="ghost",
                                class_name="w-6 h-6",
                            )
                        ),
                        tooltip.portal(
                            tooltip.positioner(
                                tooltip.popup(
                                    "Read on Jan 5, 2026 at 4:32 PM",
                                    tooltip.arrow(),
                                ),
                                side="bottom",
                            )
                        ),
                    ),
                    delay=0,
                )
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-4 py-12",
    )
