import reflex as rx

from components.ui.toggle import toggle


def toggle_sizes() -> rx.Component:
    return rx.el.div(
        toggle(
            "Small",
            variant="outline",
            aria_label="Toggle small",
            size="sm",
        ),
        toggle(
            "Default",
            variant="outline",
            aria_label="Toggle default",
            size="default",
        ),
        toggle(
            "Large",
            variant="outline",
            aria_label="Toggle large",
            size="lg",
        ),
        class_name="flex flex-wrap items-center gap-2",
    )
