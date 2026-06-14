import reflex as rx
from components.ui.avatar import avatar


def avatar_general():
    return rx.box(
        avatar(
            src="https://avatars.githubusercontent.com/u/84860195?v=4",
            alt="@LineIndent",
            fallback="CN",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/198465274?s=200&v=4",
            alt="@buridan-ui",
            fallback="BUI",
            class_name="rounded-lg",
        ),
        rx.box(
            avatar(
                src="",
                alt="@buridan-ui",
                fallback="BU",
            ),
            avatar(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                alt="@buridan-ui",
                fallback="BUI",
            ),
            avatar(
                src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
                alt="@reflex",
                fallback="RE",
            ),
            class_name=(
                "flex -space-x-2 "
                "*:data-[slot=avatar]:ring-2 *:data-[slot=avatar]:ring-[var(--background)] "
                "*:data-[slot=avatar]:grayscale"
            ),
        ),
        class_name="flex flex-row flex-wrap items-center gap-12 p-8",
    )

