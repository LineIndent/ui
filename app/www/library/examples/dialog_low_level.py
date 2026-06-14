import reflex as rx

from components.ui.button import button
from components.ui.dialog import dialog
from components.ui.input import input


def dialog_low_level():
    return dialog.root(
        dialog.trigger(render_=button("Open Dialog")),
        dialog.portal(
            dialog.backdrop(class_name="backdrop-blur-[5px]"),
            dialog.popup(
                rx.el.div(
                    rx.el.div(
                        dialog.title("Edit Profile"),
                        dialog.close(
                            render_=button(
                                rx.icon("x", class_name="size-4"),
                                variant="ghost",
                                size="icon-sm",
                                class_name="text-secondary-11",
                            ),
                        ),
                        class_name="flex justify-between items-baseline gap-1",
                    ),
                    dialog.description(
                        "Make changes to your profile here. Click save when you're done."
                    ),
                    class_name="flex flex-col gap-2",
                ),
                # Content section
                rx.el.div(
                    rx.el.div(
                        rx.el.p("Name", class_name="text-sm font-medium mb-2"),
                        input(placeholder="Enter your name"),
                    ),
                    rx.el.div(
                        rx.el.p("Email", class_name="text-sm font-medium mb-2"),
                        input(placeholder="Enter your email", type="email"),
                    ),
                    rx.el.div(
                        dialog.close(
                            render_=button(
                                "Cancel", variant="outline", class_name="flex-1"
                            ),
                        ),
                        button("Save Changes", class_name="flex-1"),
                        class_name="flex gap-2 w-full",
                    ),
                    class_name="flex flex-col gap-4",
                ),
                class_name="!w-full max-w-lg",
            ),
        ),
    )
