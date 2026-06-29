import reflex as rx

from components.icons.hugeicon import hi
from components.ui.attachment import attachment
from components.ui.spinner import spinner


def attachment_states_demo():
    return rx.el.div(
        attachment.root(
            attachment.media(hi("Clock01Icon")),
            attachment.content(
                attachment.title("selected-file.pdf"),
                attachment.description("Ready to upload"),
            ),
            attachment.actions(
                attachment.action(
                    hi("Cancel01Icon"), aria_label="Remove selected-file.pdf"
                )
            ),
            state="idle",
        ),
        attachment.root(
            attachment.media(spinner()),
            attachment.content(
                attachment.title(
                    "design-system.zip",
                    class_name="shimmer",
                ),
                attachment.description("Uploading · 64%"),
            ),
            attachment.actions(
                attachment.action(hi("Cancel01Icon"), aria_label="Cancel upload")
            ),
            state="uploading",
        ),
        attachment.root(
            attachment.media(hi("File02Icon")),
            attachment.content(
                attachment.title("market-research.pdf"),
                attachment.description("Processing document"),
            ),
            attachment.actions(
                attachment.action(
                    hi("Cancel01Icon"), aria_label="Remove market-research.pdf"
                )
            ),
            state="processing",
        ),
        attachment.root(
            attachment.media(hi("FileExclamationPointIcon")),
            attachment.content(
                attachment.title("financial-model.xlsx"),
                attachment.description("Upload failed. Try again."),
            ),
            attachment.actions(
                attachment.action(hi("RefreshIcon"), aria_label="Retry upload"),
                attachment.action(
                    hi("Cancel01Icon"), aria_label="Remove financial-model.xlsx"
                ),
            ),
            state="error",
        ),
        attachment.root(
            attachment.media(hi("Tick02Icon")),
            attachment.content(
                attachment.title("uploaded-report.pdf"),
                attachment.description("Uploaded · 1.8 MB"),
            ),
            attachment.actions(
                attachment.action(
                    hi("Cancel01Icon"), aria_label="Remove uploaded-report.pdf"
                )
            ),
            state="done",
        ),
        class_name="w-full mx-auto max-w-sm py-12 flex flex-col gap-y-4",
    )
