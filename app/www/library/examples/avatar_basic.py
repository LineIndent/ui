import reflex as rx

from components.ui.avatar import avatar


def avatar_basic() -> rx.Component:
    return avatar.root(
        avatar.image(
            src="https://github.com/LineIndent.png",
            custom_attrs={"alt": "@lineindent"},
        ),
        avatar.fallback("AH"),
    )
