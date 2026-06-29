import reflex as rx

from components.ui.bubble import bubble


def bubble_alignment_demo():
    return rx.el.div(
        bubble.root(
            bubble.content(
                "This bubble is aligned to the start. This is the default alignment."
            ),
            variant="muted",
            align="start",
        ),
        bubble.root(
            bubble.content(
                "This bubble is aligned to the end. Use this for user messages."
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
