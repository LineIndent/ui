import reflex as rx
from components.ui.link import link


def link_variants():
    """Link examples with different variants."""
    return rx.box(
        link("Primary Link", href="#", variant="primary"),
        link("Secondary Link", href="#", variant="secondary"),
        class_name="flex flex-col items-start gap-4",
    )

