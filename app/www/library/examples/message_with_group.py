import reflex as rx

from components.ui.avatar import avatar
from components.ui.bubble import bubble
from components.ui.message import message


def message_with_group():
    return rx.el.div(
        message.group(
            message.root(
                message.avatar(),
                message.content(
                    bubble.root(
                        bubble.content("I checked the registry addresses."),
                        variant="muted",
                    ),
                ),
            ),
            message.root(
                message.avatar(
                    avatar.root(
                        avatar.image(src="/avatars/02.png", alt="@avatar"),
                        avatar.fallback("CN"),
                    ),
                ),
                message.content(
                    bubble.root(
                        bubble.content(
                            "The component and example JSON now live under the UI registry."
                        ),
                        variant="muted",
                    ),
                ),
            ),
        ),
        class_name="flex w-full max-w-sm flex-col gap-6 py-12",
    )
