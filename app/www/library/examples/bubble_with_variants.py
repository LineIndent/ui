import reflex as rx

from components.ui.bubble import bubble


def bubble_with_variants():
    return rx.el.div(
        bubble.root(
            bubble.content("This is the default primary bubble."),
            variant="default",
        ),
        bubble.root(
            bubble.content("This is the secondary variant."),
            variant="secondary",
            align="end",
        ),
        bubble.root(
            bubble.content(
                "This one is muted. It uses a lower emphasis color for the chat bubble."
            ),
            bubble.reactions(
                rx.el.span("👍"),
                role="img",
                aria_label="Reaction: thumbs up",
            ),
            variant="muted",
        ),
        bubble.root(
            bubble.content(
                "This one is tinted. The tint is a softer color derived from the primary color."
            ),
            variant="tinted",
            align="end",
        ),
        bubble.root(
            bubble.content("We can also use an outlined variant."),
            variant="outline",
        ),
        bubble.root(
            bubble.content("Or a destructive variant with a reaction."),
            bubble.reactions(
                rx.el.span("🔥"),
                role="img",
                aria_label="Reaction: fire",
            ),
            variant="destructive",
            align="end",
        ),
        bubble.root(
            bubble.content(
                rx.markdown(
                    """
                    Ghost bubbles work for assistant text, **markdown**, and other content that should not be framed.

                    This is perfect for assistant messages that should not have a frame and can take the full width of the container. You can also render `code` in it.

                    Ghost bubbles are full width and can take the full width of the container.
                    """
                )
            ),
            variant="ghost",
        ),
        class_name="flex w-full max-w-sm flex-col gap-12 py-12",
    )
