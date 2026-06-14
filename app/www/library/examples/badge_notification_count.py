import reflex as rx
from components.ui.badge import badge


def badge_notification_count():
    return rx.box(
        badge(
            "1",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "5",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "10",
            variant="secondary",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "99+",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        class_name="flex items-center gap-2 p-8",
    )
