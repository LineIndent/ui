import reflex as rx

from components.ui.button import button
from components.ui.dialog import dialog


def dialog_high_level():
    return dialog(
        trigger=button("Open Dialog", variant="outline"),
        title="Are you absolutely sure?",
        description="This action cannot be undone. This will permanently delete your account and remove your data from our servers.",
        content=rx.flex(
            button("Cancel", variant="outline", class_name="flex-1"),
            button("Continue", class_name="flex-1"),
            class_name="flex gap-2 w-full",
        ),
        class_name="!w-full max-w-md",
    )
