import reflex as rx

from components.icons.hugeicon import hi
from components.ui.bubble import bubble
from components.ui.button import button
from components.ui.popover import popover


def bubble_popover_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("Run the build script."),
            align="end",
        ),
        bubble.root(
            bubble.content("Failed to run the command."),
            bubble.reactions(
                popover.root(
                    popover.trigger(
                        render_=button(
                            hi("InformationCircleIcon"),
                            variant="ghost",
                            aria_label="Show error details",
                            class_name="w-6 h-6 aria-expanded:text-destructive",
                        )
                    ),
                    popover.portal(
                        popover.backdrop(),
                        popover.positioner(
                            popover.popup(
                                popover.header(
                                    popover.title(
                                        "Command failed with exit code 1",
                                        class_name="text-sm",
                                    ),
                                    popover.description(
                                        "ENOENT: no such file or directory, open pnpm-lock.yaml",
                                        class_name="text-sm",
                                    ),
                                ),
                            ),
                        ),
                    ),
                )
            ),
            variant="destructive",
        ),
        class_name="flex w-full max-w-sm flex-col gap-4 py-12",
    )
