import reflex as rx
from components.ui.button import button
from components.ui.collapsible import collapsible


def collapsible_low_level_demo():
    return collapsible.root(
        collapsible.trigger(
            button(
                "Collapsible Trigger",
                varient="outline",
                class_name="w-full",
            ),
        ),
        rx.el.div(
            "@radix-ui/primitives",
            class_name="rounded-md border border-input px-4 py-2 font-mono text-sm",
        ),
        collapsible.panel(
            rx.el.div(
                rx.el.div(
                    "@radix-ui/colors",
                    class_name="rounded-md border border-input px-4 py-2 font-mono text-sm",
                ),
                rx.el.div(
                    "@stitches/react",
                    class_name="rounded-md border border-input px-4 py-2 font-mono text-sm",
                ),
                class_name="flex flex-col gap-4",
            ),
        ),
        class_name="w-full max-w-xs flex flex-col gap-2",
    )
