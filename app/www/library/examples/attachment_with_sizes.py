import reflex as rx

from components.icons.hugeicon import hi
from components.ui.attachment import attachment


def attachment_sizes_demo():
    return rx.el.div(
        attachment.root(
            attachment.media(hi("File02Icon")),
            attachment.content(
                attachment.title("Default attachment"),
                attachment.description("PDF · 2.4 MB"),
            ),
            size="default",
        ),
        attachment.root(
            attachment.media(hi("File02Icon")),
            attachment.content(
                attachment.title("Small attachment"),
                attachment.description("PDF · 2.4 MB"),
            ),
            size="sm",
        ),
        attachment.root(
            attachment.media(hi("File02Icon")),
            attachment.content(
                attachment.title("Extra small attachment"),
            ),
            size="xs",
        ),
        class_name="mx-auto w-full max-w-sm py-12 flex flex-col gap-y-4",
    )
