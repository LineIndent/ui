import reflex as rx

from components.ui.bubble import bubble


def bubble_group_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("Can you tell me what's the issue?"),
            variant="muted",
        ),
        bubble.group(
            bubble.root(
                bubble.content("You tell me!"),
                align="end",
            ),
            bubble.root(
                bubble.content("It worked yesterday. You broke it!"),
                align="end",
            ),
            bubble.root(
                bubble.content("Find the bug and fix it."),
                bubble.reactions(
                    rx.el.span("👀"),
                    aria_label="Reactions: eyes",
                    align="start",
                ),
                align="end",
            ),
        ),
        bubble.root(
            bubble.content(
                "Want me to diff yesterday's you against today's you? "
                "It's a bit embarrassing."
            ),
            variant="muted",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
