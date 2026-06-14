import reflex as rx
from components.ui.scroll_area import scroll_area


def scroll_area_general():
    """A basic scroll area example."""
    return rx.el.div(
        scroll_area(
            rx.el.div(
                *[rx.el.p(f"buridan v0.{i}", class_name="p-2") for i in range(30)],
            ),
            class_name="h-72 w-48 rounded-md border border-input",
        ),
        class_name="py-6",
    )
