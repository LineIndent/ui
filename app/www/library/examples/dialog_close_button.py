import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.dialog import dialog
from components.ui.input import input


def dialog_close_button() -> rx.Component:
    return dialog.root(
        dialog.trigger(render_=button("Share", variant="outline")),
        dialog.portal(
            dialog.backdrop(),
            dialog.popup(
                dialog.header(
                    dialog.title("Share link"),
                    dialog.description(
                        "Anyone who has this link will be able to view this."
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label("Link", html_for="link", class_name="sr-only"),
                        input(
                            id="link",
                            default_value="https://ui.buridan.com/docs/getting-started/installation",
                            read_only=True,
                        ),
                        class_name="grid flex-1 gap-2",
                    ),
                    class_name="flex items-center gap-2",
                ),
                dialog.footer(
                    dialog.close(render_=button("Close", type="button")),
                    class_name="sm:justify-start",
                ),
                dialog.close(
                    render_=button(
                        hi("Cancel01Icon", class_name="size-4"),
                        variant="ghost",
                        size="icon-sm",
                        class_name=dialog.class_names.CLOSE,
                    )
                ),
                class_name="sm:max-w-md",
            ),
        ),
    )
