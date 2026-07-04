import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.collapsible import collapsible


def file_item(name: str, root_level: bool = False) -> rx.Component:
    padding_class = "pl-2" if root_level else "pl-9"

    return rx.el.div(
        hi("DocumentCodeIcon", class_name="size-4 text-muted-foreground/70 shrink-0"),
        rx.el.span(name, class_name="text-sm tracking-tight text-foreground/80"),
        class_name=f"flex items-center gap-2 {padding_class} py-1 hover:bg-muted/40 rounded-md transition-colors cursor-pointer",
    )


def folder_item(name: str, *children: rx.Component) -> rx.Component:
    return collapsible.root(
        collapsible.trigger(
            render_=button(
                hi("FolderIcon", class_name="size-4 text-muted-foreground shrink-0"),
                rx.el.span(name, class_name="text-sm font-medium truncate"),
                hi(
                    "ArrowRight01Icon",
                    class_name="size-3.5 ml-auto text-muted-foreground/70 transition-transform duration-200 group-data-panel-open/button:rotate-90",
                ),
                variant="ghost",
                size="sm",
                class_name="w-full justify-start gap-2 h-8 px-2 font-normal hover:bg-muted/60",
            ),
            class_name="w-full",
        ),
        collapsible.panel(
            rx.el.div(
                *children,
                class_name="pl-4 border-l border-border/60 ml-4 mt-0.5 flex flex-col gap-0.5",
            ),
        ),
        class_name="w-full",
    )


def collapsible_nested() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                "WORKSPACE EXPLORER",
                class_name="text-[10px] font-bold tracking-wider text-muted-foreground",
            ),
            class_name="px-2 pb-2 mb-1 border-b border-border/40",
        ),
        folder_item(
            "src",
            folder_item(
                "components",
                folder_item(
                    "ui",
                    file_item("button.py"),
                    file_item("card.py"),
                    file_item("collapsible.py"),
                ),
                file_item("navbar.py"),
                file_item("sidebar.py"),
            ),
            folder_item(
                "state",
                file_item("base_state.py"),
                file_item("auth_state.py"),
            ),
            file_item("main.py"),
        ),
        folder_item(
            "public",
            file_item("favicon.ico"),
            file_item("logo.svg"),
        ),
        file_item("rxconfig.py", root_level=True),
        file_item("requirements.txt", root_level=True),
        class_name="w-full max-w-xs p-3 bg-background border border-input rounded-xl shadow-xs select-none",
    )
