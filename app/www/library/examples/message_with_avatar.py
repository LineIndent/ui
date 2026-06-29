import reflex as rx

from components.ui.avatar import avatar
from components.ui.bubble import bubble
from components.ui.message import message


def message_with_avatar():
    return rx.el.div(
        message.root(
            message.avatar(
                avatar.root(
                    avatar.image(src="/avatars/03.png", alt="@avatar"),
                    avatar.fallback("R"),
                ),
            ),
            message.content(
                bubble.root(
                    bubble.content("The build failed during dependency installation."),
                    variant="muted",
                ),
            ),
        ),
        message.root(
            message.avatar(
                avatar.root(
                    avatar.image(src="/avatars/01.png", alt="@avatar"),
                    avatar.fallback("R"),
                ),
            ),
            message.content(
                bubble.root(
                    bubble.content("Can you share the exact error?"),
                ),
            ),
            align="end",
        ),
        message.root(
            message.avatar(
                avatar.root(
                    avatar.image(src="/avatars/03.png", alt="@avatar"),
                    avatar.fallback("R"),
                ),
            ),
            message.content(
                bubble.group(
                    bubble.root(
                        bubble.content("Here's the error from the logs"),
                        variant="muted",
                    ),
                    bubble.root(
                        bubble.content(
                            "Something went wrong with the build. The libraries are not "
                            "installed correctly. Try running the build again."
                        ),
                        variant="muted",
                    ),
                ),
            ),
        ),
        class_name="flex w-full max-w-sm flex-col gap-6 py-12",
    )
