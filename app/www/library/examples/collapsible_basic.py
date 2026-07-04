import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.collapsible import collapsible


def collapsible_basic() -> rx.Component:
    return rx.el.div(
        collapsible.root(
            collapsible.trigger(
                render_=button(
                    "How do I update my billing information?",
                    hi(
                        "ArrowDown01Icon",
                        class_name="size-4 ml-auto group-data-panel-open/button:rotate-180",
                    ),
                    variant="ghost",
                ),
                class_name="w-full py-3 text-left border-b border-input",
            ),
            collapsible.panel(
                rx.el.div(
                    "You can update your card details directly inside your account settings dashboard under the billing tab.",
                    class_name="py-3 text-sm text-muted-foreground leading-relaxed px-3",
                ),
            ),
        ),
        class_name="w-full max-w-sm",
    )
