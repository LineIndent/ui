import reflex as rx


def shimmer_reverse():
    return rx.el.div(
        rx.el.div(
            rx.el.p("Generating response...", class_name="shimmer shimmer-reverse"),
            rx.el.p("shimmer reverse", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        class_name="flex text-center items-center gap-2 text-sm text-muted-foreground",
    )
