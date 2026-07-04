import reflex as rx

from components.ui.button import button
from components.ui.card import card


def card_edge_to_edge() -> rx.Component:
    return card.root(
        card.header(
            card.title("Terms of Service"),
            card.description("Review the terms before accepting the agreement."),
        ),
        card.content(
            rx.el.div(
                rx.el.p(
                    "These terms govern your use of the workspace, including access to shared documents, project files, and collaboration tools."
                ),
                rx.el.p(
                    "You are responsible for the content you upload and for ensuring that your team has the appropriate permissions to view or edit it."
                ),
                rx.el.p(
                    "We may update features or limits as the service evolves. When those changes materially affect your workflow, we will notify your workspace administrators."
                ),
                rx.el.p(
                    "By continuing, you agree to keep your account credentials secure and to follow your organization's acceptable use policies."
                ),
                class_name="-mx-(--card-spacing) max-h-48 space-y-4 overflow-y-scroll border-input border-t bg-muted/50 px-(--card-spacing) py-4 text-sm leading-relaxed",
            ),
            class_name="-mb-(--card-spacing)",
        ),
        card.footer(
            button("Decline", variant="outline"),
            button("Accept"),
            class_name="justify-end gap-2",
        ),
        class_name="mx-auto w-full max-w-sm",
    )
