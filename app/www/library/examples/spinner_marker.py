import reflex as rx

from components.ui.marker import marker
from components.ui.spinner import spinner


def spinner_marker():
    return rx.el.div(
        marker.root(
            marker.icon(spinner()),
            marker.content("Thinking…", class_name="shimmer w-fit"),
            role="status",
        ),
        marker.root(
            marker.icon(spinner()),
            marker.content("Generating response…", class_name="shimmer w-fit"),
            variant="border",
            role="status",
        ),
        marker.root(
            marker.icon(spinner()),
            marker.content("Processing"),
            variant="separator",
            role="status",
        ),
        class_name="flex w-full max-w-sm flex-col gap-6",
    )
