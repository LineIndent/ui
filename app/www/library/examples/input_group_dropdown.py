import reflex as rx

from components.icons.hugeicon import hi
from components.ui.input_group import input_group
from components.ui.menu import menu


def input_group_dropdown() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(placeholder="Enter file name"),
            input_group.addon(
                menu.root(
                    menu.trigger(
                        render_=input_group.button(
                            hi("MoreHorizontal"),
                            variant="ghost",
                            aria_label="More",
                            size="icon-xs",
                        )
                    ),
                    menu.portal(
                        menu.positioner(
                            menu.popup(
                                menu.group(
                                    menu.item("Settings"),
                                    menu.item("Copy path"),
                                    menu.item("Open location"),
                                )
                            ),
                            align="end",
                        )
                    ),
                ),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Enter search query"),
            input_group.addon(
                menu.root(
                    menu.trigger(
                        render_=input_group.button(
                            "Search In... ",
                            hi("ChevronDownIcon", class_name="size-3 ml-1 inline"),
                            variant="ghost",
                            class_name="!pr-1.5 text-xs",
                        )
                    ),
                    menu.portal(
                        menu.positioner(
                            menu.popup(
                                menu.group(
                                    menu.item("Documentation"),
                                    menu.item("Blog Posts"),
                                    menu.item("Changelog"),
                                )
                            ),
                            align="end",
                        )
                    ),
                ),
                align="inline-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-4",
    )
