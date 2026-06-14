import reflex as rx

from components.icons.hugeicon import hi
from components.ui.toggle import toggle


def toggle_general():
    return rx.el.div(
        toggle(
            hi(
                "Bookmark02Icon",
                class_name="size-4",
            ),
            "Bookmark",
            icon_variant="fill",
        ),
        toggle(
            hi("TextUnderlineIcon", class_name="size-4"),
            "Underline",
        ),
        class_name="flex flex-row gap-x-2 items-center justify-center",
    )
