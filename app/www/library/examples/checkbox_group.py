import reflex as rx

from components.ui.checkbox import checkbox
from components.ui.field import field


def checkbox_group() -> rx.Component:
    return rx.el.fieldset(
        rx.el.legend(
            "Show these items on the desktop:",
            class_name="mb-1.5 font-medium text-sm text-foreground",
        ),
        rx.el.p(
            "Select the items you want to show on the desktop.",
            class_name="mb-4 text-sm text-muted-foreground",
        ),
        rx.el.div(
            field.root(
                checkbox(id="hard-disks", default_checked=True),
                field.label(
                    "Hard disks", html_for="hard-disks", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox(id="ext-disks", default_checked=True),
                field.label(
                    "External disks", html_for="ext-disks", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox(id="cds-dvds"),
                field.label(
                    "CDs, DVDs, and iPods",
                    html_for="cds-dvds",
                    class_name="font-normal",
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox(id="servers"),
                field.label(
                    "Connected servers", html_for="servers", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            class_name="flex flex-col w-full",
        ),
    )
