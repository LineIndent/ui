import reflex as rx

from components.ui.marker import marker


def marker_shimmer():
    return rx.el.div(
        marker.root(
            marker.content("Thinking...", class_name="shimmer"),
            role="status",
        ),
        marker.root(
            marker.content("Reading 4 files", class_name="shimmer"),
            variant="separator",
            role="status",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
