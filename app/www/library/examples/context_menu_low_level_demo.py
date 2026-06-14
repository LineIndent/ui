import reflex as rx
from components.ui.context_menu import context_menu


def context_menu_low_level_demo():
    return context_menu.root(
        context_menu.trigger(
            "Right click here",
            class_name="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.item(
                        rx.flex(
                            "Back",
                            rx.text(
                                "⌘[",
                                class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                            ),
                            class_name="w-full justify-between items-center",
                        ),
                        class_name="pl-8",
                    ),
                    context_menu.item(
                        rx.flex(
                            "Forward",
                            rx.text(
                                "⌘]",
                                class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                            ),
                            class_name="w-full justify-between items-center",
                        ),
                        disabled=True,
                        class_name="pl-8",
                    ),
                    context_menu.item(
                        rx.flex(
                            "Reload",
                            rx.text(
                                "⌘R",
                                class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                            ),
                            class_name="w-full justify-between items-center",
                        ),
                        class_name="pl-8",
                    ),
                    context_menu.submenu_root(
                        context_menu.submenu_trigger(
                            rx.flex(
                                "More Tools",
                                rx.icon(
                                    "chevron-right",
                                    class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                                ),
                                class_name="w-full justify-between items-center",
                            ),
                            class_name="pl-8",
                        ),
                        context_menu.portal(
                            context_menu.positioner(
                                context_menu.popup(
                                    context_menu.item("Save Page..."),
                                    context_menu.item("Create Shortcut..."),
                                    context_menu.item("Name Window..."),
                                    context_menu.separator(),
                                    context_menu.item("Developer Tools"),
                                    context_menu.separator(),
                                    context_menu.item(
                                        "Delete",
                                        class_name="text-destructive focus:bg-destructive/10 dark:focus:bg-destructive/20 focus:text-destructive data-[variant=destructive]:*:[svg]:!text-destructive",
                                    ),
                                    class_name="w-44",
                                ),
                            ),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.checkbox_item(
                        context_menu.checkbox_item_indicator(
                            rx.icon(tag="check", class_name="size-4"),
                        ),
                        "Show Bookmarks",
                    ),
                    context_menu.checkbox_item(
                        context_menu.checkbox_item_indicator(
                            rx.icon(tag="check", class_name="size-4"),
                        ),
                        "Show Full URLs",
                    ),
                    context_menu.separator(),
                    context_menu.radio_group(
                        context_menu.group(
                            context_menu.group_label(
                                "People",
                                class_name="pl-8",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    rx.icon(
                                        tag="circle", class_name="size-2 fill-current"
                                    ),
                                ),
                                "Pedro Duarte",
                                value="pedro",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    rx.icon(
                                        tag="circle", class_name="size-2 fill-current"
                                    ),
                                ),
                                "Colm Tuite",
                                value="colm",
                            ),
                        ),
                        value="pedro",
                    ),
                    class_name="w-52",
                ),
            ),
        ),
    )
