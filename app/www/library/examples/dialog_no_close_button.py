import reflex as rx

from components.ui.button import button
from components.ui.dialog import dialog


def dialog_no_close_button() -> rx.Component:
    return dialog.root(
        dialog.trigger(render_=button("No Close Button", variant="outline")),
        dialog.portal(
            dialog.backdrop(),
            dialog.popup(
                dialog.header(
                    dialog.title("No Close Button"),
                    dialog.description(
                        "This dialog doesn't have a close button in the top-right corner."
                    ),
                ),
            ),
        ),
    )
