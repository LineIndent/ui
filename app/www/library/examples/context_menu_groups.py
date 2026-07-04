import reflex as rx

from components.ui.context_menu import context_menu


def context_menu_groups() -> rx.Component:
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
                        context_menu.group_label("File"),
                        context_menu.item(
                            "New File",
                            context_menu.shortcut("⌘N"),
                        ),
                        context_menu.item(
                            "Open File",
                            context_menu.shortcut("⌘O"),
                        ),
                        context_menu.item(
                            "Save",
                            context_menu.shortcut("⌘S"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.group_label("Edit"),
                        context_menu.item(
                            "Undo",
                            context_menu.shortcut("⌘Z"),
                        ),
                        context_menu.item(
                            "Redo",
                            context_menu.shortcut("⇧⌘Z"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.item(
                            "Cut",
                            context_menu.shortcut("⌘X"),
                        ),
                        context_menu.item(
                            "Copy",
                            context_menu.shortcut("⌘C"),
                        ),
                        context_menu.item(
                            "Paste",
                            context_menu.shortcut("⌘V"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.item(
                            "Delete",
                            context_menu.shortcut("⌫"),
                            variant="destructive",
                        ),
                    ),
                ),
            ),
        ),
    )
