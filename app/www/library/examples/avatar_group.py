import reflex as rx

from components.ui.avatar import avatar


def avatar_as_group() -> rx.Component:
    return avatar.group(
        avatar.root(
            avatar.image(
                src="/avatars/01.png",
                custom_attrs={"alt": "@avatar-1"},
            ),
            avatar.fallback("RD"),
        ),
        avatar.root(
            avatar.image(
                src="/avatars/02.png",
                custom_attrs={"alt": "@avatar-2"},
            ),
            avatar.fallback("LI"),
        ),
        avatar.root(
            avatar.fallback("AH"),
        ),
        class_name="grayscale",
    )
