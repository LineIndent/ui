import reflex as rx
from components.ui.link import link


def link_with_icon():
    """Link example with an icon."""
    return link("Link with icon", href="#", show_icon=True)
