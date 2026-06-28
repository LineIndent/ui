import reflex as rx

from components.icons.hugeicon import hi
from components.ui.marker import marker


def marker_with_icon():
    return rx.el.div(
        marker.root(
            marker.icon(hi("GitBranchIcon")),
            marker.content("Switched to a new branch"),
        ),
        marker.root(
            marker.icon(hi("Search01Icon")),
            marker.content("Explored 4 files"),
            variant="separator",
        ),
        marker.root(
            marker.icon(hi("BookOpenCheckIcon")),
            marker.content("Syncing completed"),
            class_name="flex-col",
        ),
        class_name="flex w-full max-w-sm flex-col gap-12 py-12",
    )
