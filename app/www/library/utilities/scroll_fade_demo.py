import reflex as rx


def scroll_fade_demo():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                *[
                    rx.el.div(
                        f"Item {index + 1}",
                        class_name="rounded-lg bg-muted px-3 py-2.5 text-sm",
                    )
                    for index in range(12)
                ],
                class_name="flex flex-col gap-1.5 p-1.5",
            ),
            class_name="h-72 scroll-fade scrollbar-none overflow-y-auto",
        ),
        class_name="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border border-input",
    )
