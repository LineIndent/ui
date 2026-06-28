import reflex as rx

from components.icons.hugeicon import hi
from components.ui.marker import marker


def marker_link_button():
    return rx.el.div(
        marker.root(
            rx.el.a(
                marker.icon(hi("GitBranchIcon")),
                marker.content("View the pull request"),
                href="#links-and-buttons",
                class_name="group flex flex-row items-center gap-x-2 underline transition-colors hover:text-foreground",
            ),
            variant="default",
        ),
        marker.root(
            rx.el.button(
                marker.icon(
                    hi("ArrowMoveUpRightIcon"),
                    class_name="group-hover:text-foreground transition-colors",
                ),
                marker.content(
                    "Revert this change",
                    class_name="group-hover:text-foreground transition-colors",
                ),
                type="button",
                class_name="group flex flex-row items-center gap-x-2 transition-colors",
                on_click=rx.toast("You clicked the revert button"),
            ),
            variant="default",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12 justify-center",
    )
