import reflex as rx

from components.ui.badge import badge
from components.ui.spinner import spinner


def spinner_badge():
    return rx.el.div(
        badge(spinner(), "Syncing"),
        badge(spinner(), "Updating", variant="secondary"),
        badge(spinner(), "Processing", variant="outline"),
        class_name="flex items-center gap-4",
    )
