import reflex as rx

from components.ui.context_menu import context_menu


def context_menu_basic() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-input border-dashed text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.item("Back"),
                        context_menu.item("Forward", disabled=True),
                        context_menu.item("Reload"),
                    ),
                ),
            ),
        ),
    )
