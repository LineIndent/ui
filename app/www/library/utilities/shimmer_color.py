import reflex as rx


def shimmer_color():
    return rx.el.div(
        rx.el.p(
            "Generating response", class_name="shimmer shimmer-color-blue-500/60 w-fit"
        ),
        rx.el.p(
            "Generating response", class_name="shimmer shimmer-color-[#378ADD] w-fit"
        ),
        class_name="flex flex-col items-center gap-2 text-sm text-muted-foreground",
    )
