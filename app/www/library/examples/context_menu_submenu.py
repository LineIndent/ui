import reflex as rx

from components.ui.context_menu import context_menu


def context_menu_submenu() -> rx.Component:
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
                        context_menu.item(
                            "Copy",
                            context_menu.shortcut("⌘C"),
                        ),
                        context_menu.item(
                            "Cut",
                            context_menu.shortcut("⌘X"),
                        ),
                    ),
                    context_menu.sub(
                        context_menu.sub_trigger("More Tools"),
                        context_menu.positioner(
                            context_menu.popup(
                                context_menu.group(
                                    context_menu.item("Save Page..."),
                                    context_menu.item("Create Shortcut..."),
                                    context_menu.item("Name Window..."),
                                ),
                                context_menu.separator(),
                                context_menu.group(
                                    context_menu.item("Developer Tools"),
                                ),
                                context_menu.separator(),
                                context_menu.group(
                                    context_menu.item("Delete", variant="destructive"),
                                ),
                                class_name="shadow-lg",
                            ),
                            side="right",
                        ),
                    ),
                ),
            ),
        ),
    )
