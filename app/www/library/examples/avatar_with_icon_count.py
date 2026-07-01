import reflex as rx

from components.icons.hugeicon import hi
from components.ui.avatar import avatar


def avatar_group_count_icon() -> rx.Component:
    return avatar.group(
        avatar.root(
            avatar.fallback("AH"),
        ),
        avatar.root(
            avatar.image(
                src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
                custom_attrs={"alt": "@reflex-dev"},
            ),
            avatar.fallback("CN"),
        ),
        avatar.root(
            avatar.image(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                custom_attrs={"alt": "LineIndent"},
            ),
            avatar.fallback("LI"),
        ),
        avatar.group_count(
            hi("PlusSignIcon"),
        ),
        class_name="grayscale",
    )
