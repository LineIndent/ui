import reflex as rx

from components.icons.hugeicon import hi
from components.ui.marker import marker


def marker_border():
    return rx.el.div(
        marker.root(
            marker.icon(hi("GitBranchIcon")),
            marker.content("Switched to release-candidate"),
            variant="border",
        ),
        marker.root(
            marker.icon(hi("Search01Icon")),
            marker.content("Reviewed 8 related files"),
            variant="border",
        ),
        marker.root(
            marker.icon(hi("File01Icon")),
            marker.content("Opened implementation notes"),
            variant="border",
        ),
        class_name="flex w-full max-w-sm flex-col gap-3 py-12",
    )
