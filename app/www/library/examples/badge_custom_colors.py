import reflex as rx

from components.ui.badge import badge


def badge_custom_colors() -> rx.Component:
    return rx.el.div(
        badge(
            "Blue",
            class_name="bg-blue-50 text-blue-700 dark:bg-blue-950 dark:text-blue-300",
        ),
        badge(
            "Green",
            class_name="bg-green-50 text-green-700 dark:bg-green-950 dark:text-green-300",
        ),
        badge(
            "Sky",
            class_name="bg-sky-50 text-sky-700 dark:bg-sky-950 dark:text-sky-300",
        ),
        badge(
            "Purple",
            class_name="bg-purple-50 text-purple-700 dark:bg-purple-950 dark:text-purple-300",
        ),
        badge(
            "Red",
            class_name="bg-red-50 text-red-700 dark:bg-red-950 dark:text-red-300",
        ),
        class_name="flex flex-wrap gap-2",
    )
