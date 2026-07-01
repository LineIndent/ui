import reflex as rx

from components.icons.hugeicon import hi
from components.ui.avatar import avatar


def avatar_badge_icon() -> rx.Component:
    return avatar.root(
        avatar.image(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            custom_attrs={"alt": "Reflex Dev"},
        ),
        avatar.fallback("RD"),
        avatar.badge(
            hi("PlusSignIcon"),
        ),
    )
