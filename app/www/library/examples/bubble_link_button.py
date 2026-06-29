import reflex as rx

from components.ui.bubble import bubble


def bubble_link_button_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("How can I help you today?"),
            variant="muted",
        ),
        bubble.group(
            bubble.root(
                bubble.content(
                    rx.el.button(
                        "I forgot my password",
                        on_click=rx.toast("You clicked forgot password"),
                        class_name="w-full text-left",
                    )
                ),
                variant="tinted",
                align="end",
            ),
            bubble.root(
                bubble.content(
                    rx.el.button(
                        "I need help with my subscription",
                        on_click=rx.toast("You clicked help with subscription"),
                        class_name="w-full text-left",
                    )
                ),
                variant="tinted",
                align="end",
            ),
            bubble.root(
                bubble.content(
                    rx.el.button(
                        "Something else. Talk to a human.",
                        on_click=rx.toast(
                            "You clicked something else. Talk to a human."
                        ),
                        class_name="w-full text-left",
                    )
                ),
                variant="tinted",
                align="end",
            ),
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
