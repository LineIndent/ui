import reflex as rx

from app.engine.actions import TOGGLE_DARK_JS
from app.hooks import seed, theme_preset_option
from app.templates.docsidebar import mobile_menu
from app.templates.searchbar import searchbar
from app.templates.utils import attach_tooltip
from components.icons.hugeicon import hi
from components.ui.button import button

NAV_LIST = [
    {"name": "Home", "path": "/"},
    {"name": "Docs", "path": "/docs/getting-started/introduction"},
    {"name": "Components", "path": "/components"},
    {"name": "Charts", "path": "/charts"},
    {"name": "Create", "path": "/create"},
]


def icon_wrapper(svg_str: str, class_name: str = "size-5"):
    return rx.el.div(rx.html(svg_str), class_name=f"flex items-center {class_name}")


def separator():
    return rx.el.p("︲", class_name="text-muted-foreground/50 font-thin")


def open_in_reflex_build() -> rx.Component:
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="size-5">
        <rect width="16" height="16" rx="2" class="fill-black dark:fill-white"/>
        <path d="M10 9V13H12V9H10Z M4 3V13H6V9H10V7H6V5H10V7H12V3H4Z" class="fill-white dark:fill-black"/>
    </svg>"""
    return rx.el.a(
        button(
            rx.el.div(
                rx.el.p("Open in", class_name="text-sm"),
                icon_wrapper(svg),
                class_name="flex flex-row items-center gap-x-2",
            ),
            variant="outline",
            size="sm",
        ),
        href=f"https://build.reflex.dev/?prompt=Install and run pip install buridan-create and buridan init --preset {seed.value} --include {theme_preset_option.value} then add app = rx.App(stylesheets=['globals.css'])",
        target="_blank",
    )


def light_and_dark_toggle() -> rx.Component:
    svg = """<svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="size-4 text-black dark:text-white transition-colors duration-200"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"/>
      <path d="M12 3l0 18"/>
      <path d="M12 9l4.65 -4.65"/>
      <path d="M12 14.3l7.37 -7.37"/>
      <path d="M12 19.6l8.85 -8.85"/>
    </svg>"""
    return attach_tooltip(
        func=button(
            icon_wrapper(svg, "size-4"),
            on_click=[rx.toggle_color_mode, rx.call_script(TOGGLE_DARK_JS)],
            variant="ghost",
            size="sm",
        ),
        label="Toggle Theme",
    )


def site_github() -> rx.Component:
    svg = """<svg viewBox="0 0 24 24" fill="currentColor" class="size-5"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6 -3.36-1.34 -3.36-1.34 -.46-1.16-1.11-1.47-1.11-1.47 -.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03 .89 1.52 2.34 1.08 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12c0-5.523-4.477-10-10-10z"/></svg>"""
    return rx.el.a(
        attach_tooltip(
            func=button(
                icon_wrapper(svg),
                variant="ghost",
                size="sm",
                class_name="text-foreground",
            ),
            label="GitHub",
        ),
        href="https://github.com/LineIndent/ui",
        class_name="no-underline",
    )


def navbar(with_create_page_cta: bool = False) -> rx.Component:
    actions = [
        searchbar(),
        light_and_dark_toggle(),
        separator(),
        site_github(),
        separator(),
        rx.el.a(
            button(hi("PlusSignIcon", class_name="size-4"), "New", size="sm"),
            href="/create",
        ),
    ]

    if with_create_page_cta:
        actions.extend(
            [
                open_in_reflex_build(),
                button(
                    "Get Code",
                    on_click=rx.call_script(
                        "document.getElementById('get-code-btn')?.click()"
                    ),
                    size="sm",
                ),
            ]
        )

    return rx.el.header(
        rx.el.div(
            rx.el.div(
                *[
                    rx.el.a(
                        button(item["name"], variant="ghost", size="sm"),
                        href=item["path"],
                    )
                    for item in NAV_LIST
                ],
                class_name="hidden md:flex flex-row items-center text-foreground",
            ),
            rx.el.div(mobile_menu(), class_name="flex md:hidden"),
            rx.el.div(*actions, class_name="flex flex-row gap-x-2 items-center"),
            class_name="w-full max-w-[96rem] mx-auto flex flex-row items-center justify-between px-2 md:px-7",
        ),
        class_name="sticky top-0 z-50 w-full h-13 bg-background flex items-center",
    )
