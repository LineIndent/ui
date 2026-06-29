import reflex as rx
from reflex.experimental import ClientStateVar

from components.icons.hugeicon import hi
from components.ui.bubble import bubble
from components.ui.collapsible import collapsible

open_var = ClientStateVar.create("open_var", False)
text_val = "The accessibility review found two focus states that were visually too subtle in dark mode.\n\nI checked the dialog, menu, and drawer paths because each one renders focusable controls inside a layered surface.\n\nThe dialog and drawer are fine. The menu needs the hover and focus tokens split so keyboard focus stays visible when the pointer is not involved.\n\nI also recommend keeping the change in the style file instead of the primitive so the other themes can choose their own focus treatment later."


def bubble_collapsible_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("How can I help you today?"),
            variant="muted",
        ),
        bubble.root(
            bubble.content(
                collapsible.root(
                    rx.el.div(
                        rx.cond(open_var.value, text_val, f"{text_val[:180]}..."),
                        class_name="whitespace-pre-line",
                    ),
                    collapsible.trigger(
                        rx.el.button(
                            rx.cond(open_var.value, "Show less", "Show more"),
                            rx.cond(
                                open_var.value,
                                hi("ArrowUp01Icon"),
                                hi("ArrowDown01Icon"),
                            ),
                            class_name="flex flex-row items-center gap-1 p-0 text-muted-foreground hover:underline",
                        ),
                    ),
                    open=open_var.value,
                    on_open_change=open_var.set_value,
                ),
            ),
            variant="muted",
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
