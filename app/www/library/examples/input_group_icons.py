import reflex as rx

from components.icons.hugeicon import hi
from components.ui.input_group import input_group


def input_group_icons() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(placeholder="Search..."),
            input_group.addon(
                hi("Search01Icon", class_name="text-muted-foreground"),
                align="inline-start",
            ),
        ),
        input_group.root(
            input_group.input(type="email", placeholder="Enter your email"),
            input_group.addon(
                hi("Mail01Icon", class_name="text-muted-foreground"),
                align="inline-start",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Card number"),
            input_group.addon(
                hi("CreditCardIcon", class_name="text-muted-foreground"),
                align="inline-start",
            ),
            input_group.addon(
                hi("Tick02Icon", class_name="text-muted-foreground"),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Card number"),
            input_group.addon(
                hi("StarIcon", class_name="text-muted-foreground"),
                hi("InformationCircleIcon", class_name="text-muted-foreground"),
                align="inline-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-6",
    )
