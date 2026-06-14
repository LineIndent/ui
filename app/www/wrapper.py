import json
import random
import string

import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button


def get_ui_base_files():
    base_ui = open("components/ui/base_ui.py").read()
    components = open("components/ui/component.py").read()
    twmerge = open("components/utils/twmerge.py").read()
    return base_ui, components, twmerge


def styled_tab_trigger(label: str, value: str) -> rx.Component:
    base_tab_style = {
        "width": "flex-1",
        "border": "none",
        "background": "transparent",
        "&[data-state=active]": {
            "border": "none",
            "borderBottom": rx.color_mode_cond(
                "1.25px solid black", "1.25px solid white"
            ),
            "background": "transparent",
        },
        "&[data-state=inactive]": {
            "border": "none",
            "background": "transparent",
        },
        "&::before": {
            "display": "none",
        },
    }

    return rx.tabs.trigger(rx.el.p(label), value=value, style=base_tab_style)


def generate_component_id() -> str:
    """Generate a unique component ID."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


def create_copy_button(content: str) -> rx.Component:
    uid = generate_component_id()
    btn_id = f"btn-{uid}"
    icon_id = f"icon-{uid}"
    copy_icon_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="currentColor" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 15C9 12.1716 9 10.7574 9.87868 9.87868C10.7574 9 12.1716 9 15 9L16 9C18.8284 9 20.2426 9 21.1213 9.87868C22 10.7574 22 12.1716 22 15V16C22 18.8284 22 20.2426 21.1213 21.1213C20.2426 22 18.8284 22 16 22H15C12.1716 22 10.7574 22 9.87868 21.1213C9 20.2426 9 18.8284 9 16L9 15Z"/><path d="M16.9999 9C16.9975 6.04291 16.9528 4.51121 16.092 3.46243C15.9258 3.25989 15.7401 3.07418 15.5376 2.90796C14.4312 2 12.7875 2 9.5 2C6.21252 2 4.56878 2 3.46243 2.90796C3.25989 3.07417 3.07418 3.25989 2.90796 3.46243C2 4.56878 2 6.21252 2 9.5C2 12.7875 2 14.4312 2.90796 15.5376C3.07417 15.7401 3.25989 15.9258 3.46243 16.092C4.51121 16.9528 6.04291 16.9975 9 16.9999"/></svg>'
    tick_icon_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="currentColor" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 14.5C5 14.5 6.5 14.5 8.5 18C8.5 18 14.0588 8.83333 19 7"/></svg>'
    safe_content = json.dumps(content)

    return rx.el.button(
        hi("Copy01Icon", id=icon_id, class_name="size-4"),
        id=btn_id,
        class_name="px-[0.75rem]",
        on_click=rx.call_script(
            f"""
                const icon = document.getElementById('{icon_id}');
                navigator.clipboard.writeText({safe_content});

                // Swap to tick
                icon.innerHTML = `{tick_icon_svg}`;

                // Revert after 1.5s
                setTimeout(() => {{
                    icon.innerHTML = `{copy_icon_svg}`;
                }}, 1500);
            """
        ),
    )


def file_codeblock(file_path: str, source: str) -> rx.Component:
    toggle_height_id = generate_component_id()
    parts = file_path.rsplit("/", 1)
    dir_part = parts[0] + "/" if len(parts) > 1 else ""
    file_part = parts[1] if len(parts) > 1 else parts[0]

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.html(
                    """
                    <svg role="img" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><title>Python</title><path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z"/></svg>
                    """,
                    class_name="text-foreground size-4",
                ),
                rx.el.p(
                    dir_part,
                    rx.el.span(rx.el.strong(file_part)),
                    class_name="text-muted-foreground text-sm font-normal",
                ),
                class_name="flex flex-row gap-x-2 items-center px-[0.75rem] py-2",
            ),
            rx.el.div(
                button(
                    "Expand",
                    class_name="!text-sm text-foreground",
                    id=f"trigger-{toggle_height_id}",
                    on_click=rx.call_script(
                        f"""
                        const panel = document.getElementById('code-panel-{toggle_height_id}');
                        const btn = document.getElementById('trigger-{toggle_height_id}');

                        if (panel.style.maxHeight === 'none') {{
                            panel.style.maxHeight = '40vh';
                            panel.style.overflow = 'hidden';
                            panel.style.maskImage = 'linear-gradient(to bottom, black 65%, transparent 100%)';
                            panel.style.webkitMaskImage = 'linear-gradient(to bottom, black 65%, transparent 100%)';
                            btn.innerText = 'Expand';
                        }} else {{
                            panel.style.maxHeight = 'none';
                            panel.style.overflow = 'auto';
                            panel.style.maskImage = 'none';
                            panel.style.webkitMaskImage = 'none';
                            btn.innerText = 'Collapse';
                        }}
                        """
                    ),
                    size="sm",
                    variant="ghost",
                ),
                create_copy_button(content=source),
                class_name="flex flex-row gap-x-2 items-center",
            ),
            class_name="w-full border-b border-input flex flex-row items-center justify-between",
        ),
        rx.el.div(
            rx.el.code(
                source,
                style={
                    "white-space": "pre",
                    "color": "var(--foreground)",
                    "font-size": "13px",
                    "padding": "1rem 0.75rem",
                    "display": "block",
                },
            ),
            id=f"code-panel-{toggle_height_id}",
            style={
                "max-height": "40vh",
                "overflow": "hidden",
                "transition": "max-height 0.3s ease-in-out",
                "mask-image": "linear-gradient(to bottom, black 65%, transparent 100%)",
                "-webkit-mask-image": "linear-gradient(to bottom, black 65%, transparent 100%)",
            },
            class_name="scrollbar-none flex-1 min-h-0 flex flex-col h-full",
        ),
        class_name="rounded-radius outline outline-input flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card",
    )


def chart_util_wrapper(source: str):
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                create_copy_button(content=source),
                class_name="absolute top-2 right-2 z-10 bg-secondary dark:bg-card",
            ),
            rx.el.div(
                rx.el.pre(
                    rx.el.code(
                        source,
                        class_name="language-python",
                        on_mount=rx.call_script("Prism.highlightAll()"),
                    ),
                    style={
                        "padding": "1rem 0.75rem",
                    },
                    class_name="w-full h-full !bg-secondary dark:!bg-card !text-sm",
                ),
                class_name="max-h-[500px] overflow-auto scrollbar-none",
            ),
            class_name="bg-secondary dark:bg-card relative overflow-hidden",
        ),
        class_name="w-full border border-input rounded-radius mb-8 !overflow-hidden",
    )


def demo_wrapper(component: rx.Component, source: str) -> rx.Component:

    return rx.el.div(
        rx.el.div(
            component,
            class_name="min-h-[250px] flex items-center justify-center p-6",
        ),
        rx.el.div(
            rx.el.div(
                create_copy_button(content=source),
                class_name="absolute top-2 right-2 z-10 bg-secondary dark:bg-card",
            ),
            rx.el.div(
                rx.el.pre(
                    rx.el.code(
                        source,
                        class_name="language-python",
                        on_mount=rx.call_script("Prism.highlightAll()"),
                    ),
                    style={
                        "padding": "1rem 0.75rem",
                    },
                    class_name="w-full h-full !bg-secondary dark:!bg-card !text-sm",
                ),
                class_name="max-h-[250px] overflow-auto scrollbar-none",
            ),
            class_name="border-t border-input bg-secondary dark:bg-card relative overflow-hidden",
        ),
        class_name="w-full border border-input rounded-radius flex flex-col mb-8 !overflow-hidden",
    )


def usage_wrapper(import_path: str) -> rx.Component:
    """Wrapper for the usage section showing how to import the component."""
    return rx.el.div(
        rx.el.code(
            import_path,
            style={
                "white-space": "pre",
                "color": "var(--foreground)",
                "font-size": "13px",
                "padding": "1rem 0.75rem",
                "display": "block",
            },
        ),
        class_name="w-full mt-4 mb-8 rounded-[0.625rem] outline outline-input flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card",
    )


def cli_and_manual_installation_wrapper(
    cli_command: str, source: str, file_name: str
) -> rx.Component:
    """Tabbed wrapper for CLI and Manual installation instructions."""
    base_ui_source, components_source, twmerge_source = get_ui_base_files()

    tab_list_style = {
        "border": "none",
        "boxShadow": "none",
        "background": "transparent",
    }

    manual_title_style = "text-muted-foreground text-md font-semibold"

    return rx.tabs.root(
        rx.tabs.list(
            styled_tab_trigger("Command", "cli"),
            styled_tab_trigger("Manual", "manual"),
            style=tab_list_style,
        ),
        rx.tabs.content(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.html(
                                """
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="size-5" color="currentColor" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M7.5 7.5L8.72654 8.55719C9.24218 9.00163 9.5 9.22386 9.5 9.5C9.5 9.77614 9.24218 9.99836 8.72654 10.4428L7.5 11.5"></path>
                                    <path d="M11.5 12.5H15.5"></path>
                                    <path d="M12 21C15.7497 21 17.6246 21 18.9389 20.0451C19.3634 19.7367 19.7367 19.3634 20.0451 18.9389C21 17.6246 21 15.7497 21 12C21 8.25027 21 6.3754 20.0451 5.06107C19.7367 4.6366 19.3634 4.26331 18.9389 3.95491C17.6246 3 15.7497 3 12 3C8.25027 3 6.3754 3 5.06107 3.95491C4.6366 4.26331 4.26331 4.6366 3.95491 5.06107C3 6.3754 3 8.25027 3 12C3 15.7497 3 17.6246 3.95491 18.9389C4.26331 19.3634 4.6366 19.7367 5.06107 20.0451C6.3754 21 8.25027 21 12 21Z"></path>
                                </svg>
                                """,
                                class_name="text-foreground",
                            ),
                            rx.el.p(
                                "uv",
                                style={
                                    "font-size": "0.875rem",
                                    "line-height": "1",
                                    "display": "block",
                                    "overflow": "hidden",
                                },
                                class_name="text-foreground font-normal font-theme",
                            ),
                            class_name="flex flex-row gap-x-2 items-center px-[0.75rem] py-2",
                        ),
                        create_copy_button(content=cli_command),
                        class_name="w-full border-b border-input flex flex-row items-center justify-between",
                    ),
                    rx.el.div(
                        rx.el.code(
                            cli_command,
                            style={
                                "white-space": "pre",
                                "color": "var(--foreground)",
                                "font-size": "13px",
                                "padding": "1rem 0.75rem",
                                "display": "block",
                            },
                        ),
                        class_name="overflow-x-auto overflow-y-auto scrollbar-none flex-1 min-h-0",
                    ),
                    class_name="w-full flex-1 min-h-0 flex flex-col h-full",
                ),
                class_name="rounded-[0.625rem] outline outline-input flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card",
            ),
            value="cli",
            class_name="mt-6",
        ),
        rx.tabs.content(
            rx.el.div(
                rx.el.p("1. Base UI package library", class_name=manual_title_style),
                file_codeblock("components/ui/base_ui.py", base_ui_source),
                rx.el.p("2. Component library", class_name=manual_title_style),
                file_codeblock("components/ui/component.py", components_source),
                rx.el.p(
                    "3. Tailwind merge utility file", class_name=manual_title_style
                ),
                file_codeblock("components/utils/twmerge.py", twmerge_source),
                rx.el.p("4. UI component file", class_name=manual_title_style),
                file_codeblock(f"components/ui/{file_name.lower()}.py", source),
                class_name="flex flex-col gap-y-4",
            ),
            value="manual",
            class_name="mt-6",
        ),
        default_value="cli",
        class_name="mb-8",
    )
