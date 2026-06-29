import reflex as rx

from components.icons.hugeicon import hi
from components.ui.bubble import bubble
from components.ui.button import button
from components.ui.message import message


def message_with_actions():
    return rx.el.div(
        message.root(
            message.content(
                bubble.root(
                    bubble.content(
                        "The install failure is coming from the workspace package."
                    ),
                    variant="muted",
                ),
                message.footer(
                    button(
                        hi("Copy01Icon"),
                        variant="ghost",
                        size="sm",
                        aria_label="Copy",
                        title="Copy",
                    ),
                    button(
                        hi("ThumbsUpIcon"),
                        variant="ghost",
                        size="sm",
                        aria_label="Like",
                        title="Like",
                    ),
                    button(
                        hi("ThumbsDownIcon"),
                        variant="ghost",
                        size="sm",
                        aria_label="Dislike",
                        title="Dislike",
                    ),
                ),
            ),
        ),
        message.root(
            message.content(
                bubble.root(
                    bubble.content("Okay drop me a link. Taking a look..."),
                ),
                message.footer(
                    rx.el.span(
                        "Failed to send",
                        class_name="font-normal text-destructive",
                    ),
                    button(
                        hi("Refresh03Icon"),
                        variant="ghost",
                        size="sm",
                        title="Retry",
                        aria_label="Retry",
                    ),
                    class_name="gap-2",
                ),
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
