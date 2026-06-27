import reflex as rx


def scroll_fade_size_items():
    return rx.el.div(
        *[
            rx.el.div(
                f"Item {index + 1}",
                class_name="rounded-lg bg-muted px-3 py-2.5 text-sm",
            )
            for index in range(8)
        ],
        class_name="flex flex-col gap-1.5 p-1.5",
    )


def scroll_fade_size():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_size_items(),
                    class_name="h-48 scroll-fade scrollbar-none overflow-y-auto scroll-fade-4",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-4",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_size_items(),
                    class_name="h-48 scroll-fade scrollbar-none overflow-y-auto scroll-fade-24",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-24",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto flex w-full max-w-xs flex-col gap-6",
    )
