import reflex as rx

from components.ui.context_menu import context_menu


def context_menu_sides() -> rx.Component:
    return rx.el.div(
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (top)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (top)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="top",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (right)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (right)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="right",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (bottom)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (bottom)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="bottom",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (left)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (left)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="left",
                ),
            ),
        ),
        class_name="grid w-full max-w-sm grid-cols-2 gap-4",
    )
