from dataclasses import dataclass
from typing import List

import reflex as rx

import app.utils.routes as routes
from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.select import select

HIGHLIGHT_SCRIPT = """
    const currentPath = window.location.pathname.substring(1);
    const activeElement = document.getElementById(currentPath);
    if (activeElement) {
        const sidebar = document.getElementById('sidebar');
            if (sidebar) {
                sidebar.querySelectorAll('.bg-secondary').forEach(el => {
                    el.classList.remove('bg-secondary');
                });
            }
        // 2. Add highlight to the current one
        activeElement.classList.add('bg-secondary');
        // 3. Scroll into view
        activeElement.scrollIntoView({
            behavior: 'instant',
            block: 'center'
        });
    }
"""


@dataclass
class SidebarSection:
    """Configuration for a sidebar section."""

    title: str
    routes: list[dict]


SIDEBAR_SECTIONS = [
    SidebarSection(title="Getting Started", routes=routes.GET_STARTED_URLS),
    SidebarSection(title="Resources", routes=routes.RESOURCES_URLS),
    SidebarSection(title="Utilities", routes=routes.UTILITIES),
    SidebarSection(title="Charts", routes=routes.CHARTS_URLS),
    SidebarSection(title="Components", routes=routes.BASE_UI_COMPONENTS),
]


def create_menu_item(data: dict):
    """Create a single menu item."""

    return button(
        rx.el.a(
            rx.el.p(data["title"], class_name="cursor-pointer"),
            to=f"/{data['url']}",
            text_decoration="none",
        )
        if data["url"] != "llms.txt"
        else rx.el.a(
            rx.el.p(data["title"], class_name="cursor-pointer"),
            href=f"/{data['url']}",
            text_decoration="none",
            reload_document=True,
        ),
        variant="ghost",
        size="sm",
        class_name="w-fit",
        id=data["url"],
    )


def create_sidebar_menu_items(routes: List[dict]):
    """Create menu items from routes."""
    return rx.el.div(
        *[create_menu_item(route) for route in routes],
        class_name="w-full flex flex-col gap-y-0 justify-start",
    )


def create_section_content(section: SidebarSection):
    """Create content for a sidebar section."""
    return rx.el.div(
        rx.el.div(
            create_sidebar_menu_items(section.routes),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )


def sidebar_section(section: SidebarSection):
    """Create a complete sidebar section with title and content."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    section.title,
                    class_name="text-muted-foreground font-medium px-2 text-xs",
                ),
                class_name="flex flex-row items-center gap-x-2",
            ),
            class_name="w-full flex flex-row justify-between align-center items-center",
        ),
        create_section_content(section),
        class_name="flex flex-col w-full gap-y-2 py-4",
    )


def sidebar():
    """Main sidebar component."""
    content = rx.el.div(
        rx.el.div(class_name="py-5"),
        *[sidebar_section(section) for section in SIDEBAR_SECTIONS],
        rx.el.div(class_name="py-5"),
        class_name="flex flex-col max-w-[18rem] w-full h-full",
    )

    return rx.el.div(
        rx.el.div(content, id="doc-sidebar"),
        class_name=(
            "hidden lg:flex flex-col "
            "max-w-[18rem] w-full "
            "sticky top-32 "
            "h-[calc(100svh-16rem)] "
            "overflow-y-auto scrollbar-none "
            "sm:mask-[linear-gradient(to_bottom,transparent_0%,black_15%,black_85%,transparent_100%)] "
            "sm:mask-size-[100%_100%] "
            "sm:mask-repeat-no-repeat "
        ),
        on_mount=rx.call_script(HIGHLIGHT_SCRIPT),
    )


def mobile_menu():
    from app.templates.navbar import NAV_LIST

    return select.root(
        select.trigger(
            button(
                hi(
                    "Add01Icon",
                    class_name="size-5 transition-transform duration-50 ease-in-out group-aria-[expanded=true]:rotate-45",
                ),
                rx.el.p("Menu", class_name="text-md"),
                variant="ghost",
                class_name="w-full flex items-center justify-start group !text-foreground group",
                size="sm",
            ),
            class_name="border-none p-0 group",
        ),
        select.portal(
            select.backdrop(
                class_name="fixed top-13 inset-x-0 bottom-0 backdrop-blur-[5px] transition-all"
            ),
            select.positioner(
                select.popup(
                    select.list(
                        select.group(
                            select.group_label("Pages"),
                            *[
                                select.item(
                                    rx.el.a(
                                        select.item_text(route["name"]),
                                        to=f"{route['path']}",
                                        text_decoration="none",
                                        class_name="w-full flex flex-row items-center justify-between",
                                    ),
                                    value=route["name"],
                                )
                                for route in NAV_LIST
                            ],
                        ),
                        *[
                            select.group(
                                select.group_label(section.title),
                                *[
                                    select.item(
                                        rx.el.a(
                                            select.item_text(route["title"]),
                                            to=f"/{route['url']}",
                                            text_decoration="none",
                                            class_name="w-full flex flex-row items-center justify-between",
                                        ),
                                        value=route["title"],
                                    )
                                    for route in section.routes
                                ],
                            )
                            for section in SIDEBAR_SECTIONS
                        ],
                        class_name="max-h-96 overflow-y-auto w-full",
                    ),
                    class_name="w-full",
                ),
                side_offset=15,
                side="bottom",
                class_name="w-full pl-3 pr-5",
            ),
            class_name="w-full h-full",
        ),
        name="mobile_sidebar",
    )
