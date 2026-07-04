import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.dialog import dialog


def dialog_sticky_footer() -> rx.Component:
    return dialog.root(
        dialog.trigger(render_=button("Sticky Footer", variant="outline")),
        dialog.portal(
            dialog.backdrop(),
            dialog.popup(
                dialog.header(
                    dialog.title("Sticky Footer"),
                    dialog.description(
                        "This dialog has a sticky footer that stays visible while the content scrolls."
                    ),
                ),
                rx.el.div(
                    *[
                        rx.el.p(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do "
                            "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
                            "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                            "reprehenderit in voluptate velit esse cillum dolore eu fugiat "
                            "nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
                            "sunt in culpa qui officia deserunt mollit anim id est laborum.",
                            class_name="mb-4 leading-normal",
                        )
                        for _ in range(10)
                    ],
                    class_name="-mx-4 no-scrollbar max-h-[50vh] overflow-y-auto px-4",
                ),
                dialog.footer(
                    dialog.close(render_=button("Close", variant="outline")),
                ),
                dialog.close(
                    render_=button(
                        hi("Cancel01Icon", class_name="size-4"),
                        variant="ghost",
                        size="icon-sm",
                        class_name=dialog.class_names.CLOSE,
                    )
                ),
            ),
        ),
    )
