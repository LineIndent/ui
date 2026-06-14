import reflex as rx
from components.ui.badge import badge


def badge_status():
    return rx.box(
        badge("New", variant="default"),
        badge("Popular", variant="secondary"),
        badge("Sale", variant="destructive"),
        badge("Draft", variant="outline"),
        badge(
            rx.icon(tag="star"),
            "Featured",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )

