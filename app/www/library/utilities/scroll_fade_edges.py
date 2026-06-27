import reflex as rx

items = [
    "Inbox triage",
    "Design review",
    "API contract",
    "QA pass",
    "Launch notes",
    "Metrics follow-up",
]

tags = [
    "Design",
    "Engineering",
    "Marketing",
    "Product",
    "Research",
    "Sales",
    "Support",
    "Operations",
]


def scroll_fade_edge_items():
    return rx.el.div(
        *[
            rx.el.div(
                item,
                class_name="rounded-lg bg-muted px-3 py-2.5 text-sm",
            )
            for item in items
        ],
        class_name="flex flex-col gap-1.5 p-1.5",
    )


def scroll_fade_edge_tags():
    return rx.el.div(
        *[
            rx.el.div(
                tag,
                class_name="shrink-0 rounded-xl bg-muted px-4 py-2.5 text-sm",
            )
            for tag in tags
        ],
        class_name="flex w-max gap-1.5 p-1.5",
    )


def scroll_fade_edge():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_edge_items(),
                    class_name="h-36 scroll-fade-t scrollbar-none overflow-y-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-t",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_edge_items(),
                    class_name="h-36 scroll-fade-b scrollbar-none overflow-y-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-b",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_edge_tags(),
                    class_name="scroll-fade-s scrollbar-none overflow-x-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-s",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_edge_tags(),
                    class_name="scroll-fade-e scrollbar-none overflow-x-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-e",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto flex max-w-xs min-w-0 flex-col gap-6",
    )
