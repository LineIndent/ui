import reflex as rx
from components.ui.badge import badge


def badge_with_icons():
    return rx.box(
        badge(
            rx.icon(tag="check"),
            "Success",
            variant="secondary",
            class_name="bg-green-500 text-white dark:bg-green-600",
        ),
        badge(
            rx.icon(tag="x"),
            "Error",
            variant="destructive",
        ),
        badge(
            rx.icon(tag="triangle-alert"),
            "Warning",
            variant="secondary",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        badge(
            rx.icon(tag="info"),
            "Info",
            variant="secondary",
            class_name="bg-blue-500 text-white dark:bg-blue-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )

