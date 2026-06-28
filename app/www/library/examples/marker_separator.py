import reflex as rx

from components.ui.marker import marker


def marker_separator():
    return rx.el.div(
        marker.root(
            marker.content("Today"),
            variant="separator",
        ),
        marker.root(
            marker.content("Worked for 42s"),
            variant="separator",
        ),
        marker.root(
            marker.content("Conversation compacted"),
            variant="separator",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
