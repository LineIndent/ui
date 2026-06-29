import reflex as rx

from components.icons.hugeicon import hi
from components.ui.attachment import attachment
from components.ui.bubble import bubble
from components.ui.message import message


def message_with_attachment():
    return rx.el.div(
        message.root(
            message.content(
                attachment.root(
                    attachment.media(
                        rx.el.img(
                            src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80",
                            alt="Workspace",
                        ),
                        variant="image",
                    ),
                    orientation="vertical",
                ),
                bubble.root(
                    bubble.content(
                        "Here's the image. Can you add it to the PDF? "
                        "Use it for the cover page."
                    ),
                ),
            ),
            align="end",
        ),
        message.root(
            message.content(
                bubble.root(
                    bubble.content(
                        "Done. Here's the PDF with the image added as the cover page."
                    ),
                    variant="muted",
                ),
                attachment.root(
                    attachment.media(
                        hi("File02Icon"),
                    ),
                    attachment.content(
                        attachment.title("sales-dashboard.pdf"),
                        attachment.description("PDF · 2.4 MB"),
                    ),
                    attachment.actions(
                        attachment.action(
                            hi("Download02Icon"),
                            title="Download",
                            aria_label="Download",
                        ),
                    ),
                ),
            ),
        ),
        message.root(
            message.content(
                bubble.root(
                    bubble.content("Thanks. Looks good."),
                ),
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
