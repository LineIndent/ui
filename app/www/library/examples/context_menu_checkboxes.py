import reflex as rx

from components.icons.hugeicon import hi
from components.ui.context_menu import context_menu


def context_menu_checkboxes() -> rx.Component:
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
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            "Show Bookmarks Bar",
                            default_checked=True,
                        ),
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            "Show Full URLs",
                        ),
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            "Show Developer Tools",
                            default_checked=True,
                        ),
                    ),
                ),
            ),
        ),
    )
