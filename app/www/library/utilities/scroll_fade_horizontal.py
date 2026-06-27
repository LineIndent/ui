import reflex as rx

tags = [
    "Design",
    "Engineering",
    "Marketing",
    "Product",
    "Research",
    "Sales",
    "Support",
    "Operations",
    "Finance",
    "Legal",
    "People",
    "Security",
]


def scroll_fade_horizontal():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                *[
                    rx.el.div(
                        tag,
                        class_name="shrink-0 rounded-lg bg-muted px-3 py-2.5 text-sm",
                    )
                    for tag in tags
                ],
                class_name="flex w-max gap-1.5 p-1.5",
            ),
            class_name="scroll-fade-x scrollbar-none overflow-x-auto",
        ),
        class_name="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border border-input",
    )
