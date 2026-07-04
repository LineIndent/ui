import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.card import card


def card_small() -> rx.Component:
    feature_name = "Scheduled reports"

    return card.root(
        card.header(
            card.title(feature_name),
            card.description("Weekly snapshots. No more manual exports."),
        ),
        card.content(
            rx.el.ul(
                rx.el.li(
                    hi(
                        "ArrowRight01Icon",
                        class_name="mt-0.5 size-4 shrink-0 text-muted-foreground",
                    ),
                    rx.el.span("Choose a schedule (daily, or weekly)."),
                    class_name="flex gap-2",
                ),
                rx.el.li(
                    hi(
                        "ArrowRight01Icon",
                        class_name="mt-0.5 size-4 shrink-0 text-muted-foreground",
                    ),
                    rx.el.span("Send to channels or specific teammates."),
                    class_name="flex gap-2",
                ),
                rx.el.li(
                    hi(
                        "ArrowRight01Icon",
                        class_name="mt-0.5 size-4 shrink-0 text-muted-foreground",
                    ),
                    rx.el.span("Include charts, tables, and key metrics."),
                    class_name="flex gap-2",
                ),
                class_name="grid gap-2 py-2 text-sm",
            )
        ),
        card.footer(
            button(
                "Set up scheduled reports",
                size="sm",
                class_name="w-full",
            ),
            button(
                "See what's new",
                variant="outline",
                size="sm",
                class_name="w-full",
            ),
            class_name="flex-col gap-2",
        ),
        size="sm",
        class_name="mx-auto w-full max-w-xs my-10",
    )
