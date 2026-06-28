import reflex as rx

from components.ui.marker import marker


def marker_variants_demo():
    return rx.el.div(
        # Default Marker
        marker.root(
            marker.content("A default marker for inline notes."),
        ),
        # Separator Marker
        marker.root(
            marker.content("A separator marker"),
            variant="separator",
        ),
        # Border Marker
        marker.root(
            marker.content("A border marker for row boundaries."),
            variant="border",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
