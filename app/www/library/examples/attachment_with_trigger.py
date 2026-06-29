import reflex as rx

from components.icons.hugeicon import hi
from components.ui.attachment import attachment
from components.ui.dialog import dialog


def attachment_trigger_dialog_demo():
    return rx.el.div(
        dialog.root(
            attachment.root(
                attachment.media(hi("File01Icon")),
                attachment.content(
                    attachment.title("research-summary.pdf"),
                    attachment.description("Open preview dialog"),
                ),
                attachment.actions(
                    attachment.action(hi("Copy01Icon"), aria_label="Copy link"),
                    attachment.action(
                        hi("Cancel01Icon"), aria_label="Remove research-summary.pdf"
                    ),
                ),
                dialog.trigger(attachment.trigger(link=False)),
                class_name="w-full",
            ),
            dialog.portal(
                dialog.backdrop(class_name="backdrop-blur-[3px]"),
                dialog.popup(
                    dialog.title("research-summary.pdf"),
                    dialog.description(
                        "The attachment trigger fills the card and opens the dialog, "
                        "while the actions stay independently clickable above it."
                    ),
                    class_name="max-w-md rounded-2xl",
                ),
            ),
        ),
        class_name="mx-auto w-full max-w-sm py-12",
    )
