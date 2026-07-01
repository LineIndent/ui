import reflex as rx

from components.ui.badge import badge


def badge_with_variants() -> rx.Component:
    return rx.el.div(
        badge("Default"),
        badge("Secondary", variant="secondary"),
        badge("Destructive", variant="destructive"),
        badge("Outline", variant="outline"),
        badge("Ghost", variant="ghost"),
        class_name="flex flex-wrap gap-2",
    )
