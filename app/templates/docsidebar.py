from dataclasses import dataclass
from typing import List

import reflex as rx

import app.utils.routes as routes
from components.ui.button import button


@dataclass
class SidebarSection:
    """Configuration for a sidebar section."""

    title: str
    routes: list[dict]


SIDEBAR_SECTIONS = [
    SidebarSection(title="Getting Started", routes=routes.GET_STARTED_URLS),
    SidebarSection(title="Charts", routes=routes.CHARTS_URLS),
    SidebarSection(title="Components", routes=routes.BASE_UI_COMPONENTS),
]


def create_menu_item(data: dict, in_drawer):
    """Create a single menu item."""
    return button(
        rx.el.a(
            rx.el.p(
                data["title"],
                class_name="cursor-pointer"
                + rx.cond(in_drawer, "text-lg px-2", "text-sm").to(str),
            ),
            to=f"/{data['url']}",
            text_decoration="none",
        ),
        variant="ghost",
        size="sm",
        class_name="w-fit",
        id=data["url"],
    )


def create_sidebar_menu_items(routes: List[dict], in_drawer):
    """Create menu items from routes."""
    return rx.el.div(
        *[create_menu_item(route, in_drawer) for route in routes],
        class_name="w-full flex flex-col gap-y-0 justify-start",
    )


def create_section_content(section: SidebarSection, in_drawer):
    """Create content for a sidebar section."""
    return rx.el.div(
        rx.el.div(
            create_sidebar_menu_items(section.routes, in_drawer),
            class_name="flex flex-row h-full w-full gap-x-2",
        ),
        class_name="flex flex-col p-0 m-0",
    )


def sidebar_section(section: SidebarSection, in_drawer=False):
    """Create a complete sidebar section with title and content."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    section.title,
                    class_name="text-muted-foreground font-medium px-2 "
                    + rx.cond(in_drawer, "text-md px-2", "text-xs").to(str),
                ),
                class_name="flex flex-row items-center gap-x-2",
            ),
            class_name="w-full flex flex-row justify-between align-center items-center",
        ),
        create_section_content(section, in_drawer),
        class_name="flex flex-col w-full gap-y-2 py-4",
    )


def sidebar(in_drawer=False):
    """Main sidebar component."""
    content = rx.el.div(
        rx.el.div(class_name="py-5"),
        *[sidebar_section(section, in_drawer) for section in SIDEBAR_SECTIONS],
        rx.el.div(class_name="py-5"),
        class_name="flex flex-col max-w-[18rem] w-full h-full",
    )

    return rx.el.div(
        rx.el.div(content, id="sidebar"),
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
    )
