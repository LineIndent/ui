import reflex as rx
from components.ui.avatar import avatar


def avatar_sizes():
    """Example showing different avatar sizes"""
    return rx.box(
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-6",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-8",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-10",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-12",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-16",
        ),
        class_name="flex items-center gap-4 p-8",
    )

