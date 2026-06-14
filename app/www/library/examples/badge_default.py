import reflex as rx
from components.ui.badge import badge


def badge_default():
    return rx.box(
        rx.box(
            badge("Badge"),
            badge("Secondary", variant="secondary"),
            badge("Destructive", variant="destructive"),
            badge("Outline", variant="outline"),
            class_name="flex w-full flex-wrap gap-2",
        ),
        rx.box(
            badge(
                rx.icon(tag="badge-check"),
                "Verified",
                variant="secondary",
                class_name="bg-blue-500 text-white dark:bg-blue-600",
            ),
            badge(
                "8",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "99",
                variant="destructive",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "20+",
                variant="outline",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            class_name="flex w-full flex-wrap gap-2",
        ),
        class_name="flex flex-col items-center gap-2 p-8",
    )

