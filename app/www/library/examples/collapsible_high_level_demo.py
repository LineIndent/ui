import reflex as rx
from components.ui.button import button
from components.ui.collapsible import collapsible


def collapsible_high_level_demo():
    return collapsible(
        trigger=button(
            "Trigger",
            varient="outline",
            class_name="w-full",
        ),
        content=rx.el.p(
            "This is the collapsible content. You can put anything here!",
            class_name="py-2 text-center",
        ),
        default_open=False,
        class_name="w-full max-w-xs",
    )
