import reflex as rx
from reflex.experimental import ClientStateVar

from components.icons.hugeicon import hi
from components.ui.context_menu import context_menu

selected_user = ClientStateVar.create("selected_user", "pedro")
selected_theme = ClientStateVar.create("selected_theme", "light")


def context_menu_radio() -> rx.Component:
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
                        context_menu.group_label("People"),
                        context_menu.radio_group(
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "Pedro Duarte",
                                value="pedro",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "Colm Tuite",
                                value="colm",
                            ),
                            value=selected_user.value,
                            on_value_change=selected_user.set_value,
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.group_label("Theme"),
                        context_menu.radio_group(
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "Light",
                                value="light",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "Dark",
                                value="dark",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "System",
                                value="system",
                            ),
                            value=selected_theme.value,
                            on_value_change=selected_theme.set_value,
                        ),
                    ),
                ),
            ),
        ),
    )
