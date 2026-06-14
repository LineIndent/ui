import reflex as rx
from components.ui.link import link


def link_sizes():
    """Link examples with different sizes."""
    return rx.box(
        link("X-Small Link", href="#", size="xs"),
        link("Small Link", href="#", size="sm"),
        link("Medium Link", href="#", size="md"),
        link("Large Link", href="#", size="lg"),
        link("X-Large Link", href="#", size="xl"),
        class_name="flex flex-col items-start gap-4",
    )

