import reflex as rx

from components.ui.bubble import bubble
from components.ui.message import message


def message_header_footer():
    return rx.el.div(
        message.root(
            message.content(
                message.header("Olivia"),
                bubble.root(
                    bubble.content("I already checked the logs."),
                    variant="muted",
                ),
            ),
        ),
        message.root(
            message.content(
                bubble.root(
                    bubble.content(
                        "Send the report to the team. Ping @lineindent if you need help."
                    ),
                ),
                message.footer(
                    rx.el.div(
                        "Read ",
                        rx.el.span("Yesterday", class_name="font-normal"),
                    ),
                ),
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
