import reflex as rx

from app.templates.utils import attach_tooltip
from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.dialog import dialog
from components.ui.input import input


def searchbar():
    return dialog.root(
        dialog.trigger(
            attach_tooltip(
                func=button(
                    hi("FileSearchIcon", class_name="size-4 shrink-0"),
                    id="buridan-search-trigger",
                    on_click=rx.call_script("window.openSearch()"),
                    variant="ghost",
                    size="sm",
                ),
                label="Search Docs",
            ),
        ),
        dialog.portal(
            dialog.backdrop(class_name="backdrop-blur-[4px]"),
            dialog.popup(
                rx.el.div(
                    input(
                        placeholder="Search Reflex & Buridan docs...",
                        id="buridan-search-input",
                        class_name="!text-foreground",
                    ),
                    rx.el.div(
                        id="buridan-search-results",
                        class_name="h-92 overflow-y-auto scrollbar-none",
                    ),
                    class_name="flex flex-col gap-y-4 w-full",
                ),
                class_name="!w-full max-w-xs sm:max-w-sm rounded-2xl bg-card p-2.5 flex flex-col overflow-hidden",
            ),
        ),
    )
