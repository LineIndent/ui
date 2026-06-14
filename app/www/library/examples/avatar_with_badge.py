import reflex as rx
from components.ui.avatar import avatar


def avatar_with_badge():
    """Example showing avatar with status badge"""
    return rx.box(
        rx.box(
            avatar(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                alt="@LineIndent",
                fallback="CN",
                class_name="size-12",
            ),
            rx.box(
                class_name=(
                    "absolute bottom-0 right-0 size-3 rounded-full "
                    "bg-green-500 border-2 border-[var(--background)]"
                ),
            ),
            class_name="relative inline-block",
        ),
        class_name="p-8",
    )
