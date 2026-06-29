import reflex as rx

from components.ui.bubble import bubble


def bubble_reactions_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("I don't need tests, I know my code works."),
            bubble.reactions(
                rx.el.span("👍"),
                rx.el.span("😮"),
                align="start",
                role="img",
                aria_label="Reactions: thumbs up, surprised",
            ),
            variant="muted",
            align="end",
        ),
        bubble.root(
            bubble.content(
                "Bold. Fine I'll add some tests. I'll let you know when they're done."
            ),
            bubble.reactions(
                rx.el.span("👀"),
                rx.el.span("🚀"),
                rx.el.span("+2"),
                role="img",
                aria_label="Reactions: eyes, rocket, and 2 more",
            ),
            variant="muted",
        ),
        bubble.root(
            bubble.content(
                "Tests passed on the first try. All 142 of them. Looking good!"
            ),
            bubble.reactions(
                rx.el.span("🎉"),
                rx.el.span("👏"),
                side="top",
                align="start",
                role="img",
                aria_label="Reactions: party popper, clapping hands",
            ),
            variant="default",
            align="end",
        ),
        bubble.root(
            bubble.content("Are you sure I can run this command?"),
            bubble.reactions(
                rx.el.button(
                    "Yes, run it",
                    on_click=rx.toast.success("You clicked yes, running command..."),
                    class_name="px-2 py-0.5 text-xs hover:bg-accent rounded-md",
                ),
            ),
            variant="destructive",
        ),
        class_name="flex w-full max-w-sm flex-col gap-12 py-12",
    )
