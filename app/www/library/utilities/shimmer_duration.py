import reflex as rx


def shimmer_duration():
    return rx.el.div(
        rx.el.div(
            rx.el.p("Generating response...", class_name="shimmer"),
            rx.el.p("shimmer", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.p(
                "Generating response...", class_name="shimmer shimmer-duration-1000"
            ),
            rx.el.p("shimmer-duration-1000", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto grid w-full max-w-lg gap-6 text-center text-sm text-muted-foreground sm:grid-cols-2",
    )
