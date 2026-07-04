import reflex as rx

from components.ui.badge import badge
from components.ui.button import button
from components.ui.card import card


def card_image() -> rx.Component:
    return card.root(
        rx.el.div(
            class_name="absolute inset-0 z-30 aspect-video bg-black/35",
        ),
        rx.el.img(
            src="https://avatar.vercel.sh/shadcn1",
            alt="Event cover",
            class_name="relative z-20 aspect-video w-full object-cover brightness-60 grayscale dark:brightness-40",
        ),
        card.header(
            card.action(
                badge("Featured", variant="secondary"),
            ),
            card.title("Design systems meetup"),
            card.description(
                "A practical talk on component APIs, accessibility, and shipping faster."
            ),
        ),
        card.footer(
            button("View Event", class_name="w-full"),
        ),
        class_name="relative mx-auto w-full max-w-sm pt-0",
    )
