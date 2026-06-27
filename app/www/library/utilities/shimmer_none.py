import reflex as rx


def shimmer_none():
    return rx.el.div(
        rx.el.p("Generating response...", class_name="shimmer md:shimmer-none"),
        rx.el.p("shimmer md:shimmer-none", class_name="font-mono text-xs"),
        class_name="flex flex-col items-center gap-3 text-sm text-muted-foreground",
    )
