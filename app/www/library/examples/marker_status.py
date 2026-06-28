import reflex as rx

from components.ui.marker import marker
from components.ui.spinner import spinner


def marker_status_demo():
    return rx.el.div(
        marker.root(
            marker.icon(spinner()),
            marker.content("Compacting conversation"),
            role="status",
        ),
        marker.root(
            marker.icon(spinner()),
            marker.content("Running tests"),
            variant="separator",
            role="status",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
