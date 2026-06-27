import reflex as rx
from reflex.experimental import ClientStateVar

from components.ui.button import button

shimmer_key = ClientStateVar.create("shimmer_key", 0)


def shimmer_once():
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                "Generating response...",
                class_name=(
                    "shimmer text-sm text-muted-foreground "
                    "shimmer-duration-1100 shimmer-once"
                ),
            ),
            key=shimmer_key.value.to(str),
        ),
        button(
            "Replay",
            variant="outline",
            size="sm",
            on_click=shimmer_key.set_value(shimmer_key.value.to(int) + 1),
        ),
        class_name="flex flex-col items-center gap-4",
    )
