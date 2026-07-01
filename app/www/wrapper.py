import json
import random
import string
from typing import Literal

import reflex as rx

from components.icons.hugeicon import hi

Swatch = Literal["square", "line", "border"]


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
            create_copy_button(content=source),
            class_name="absolute right-0 translate-y-2/3 bg-secondary dark:bg-card z-20",
        ),
        rx.el.div(
            rx.el.code(
                dir_part + file_part,
                style={
                    "white-space": "pre",
                    "color": "var(--foreground)",
                    "font-size": "13px",
                    "padding": "1rem 0.75rem",
                    "display": "block",
                },
            ),
            id=f"code-panel-{toggle_height_id}",
            class_name="scrollbar-none flex-1 min-h-0 flex flex-col h-full relative overflow-x-auto",
        ),
        class_name="rounded-lg outline outline-input flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card",
    )


def file_codeblock_full(file_path: str, source: str) -> rx.Component:
    toggle_height_id = generate_component_id()
    parts = file_path.rsplit("/", 1)
    dir_part = parts[0] + "/" if len(parts) > 1 else ""
    file_part = parts[1] if len(parts) > 1 else parts[0]

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    dir_part,
                    rx.el.span(rx.el.strong(file_part)),
                    class_name="text-muted-foreground text-sm font-normal",
                ),
                class_name="flex px-[0.75rem] py-2",
            ),
            rx.el.div(
                rx.el.button(
                    "Expand",
                    class_name="!text-xs text-muted-foreground hover:text-foreground",
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
        class_name="rounded-lg outline outline-input flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card",
    )


def chart_util_wrapper(source: str):
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                create_copy_button(content=source),
                class_name="absolute top-2 right-2 z-10 bg-secondary dark:bg-card",
            ),
            rx.el.div(
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
            class_name="w-full border border-input rounded-lg mb-8 !overflow-hidden",
        ),
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
        class_name="w-full border border-input rounded-[1rem] flex flex-col mb-8 !overflow-hidden",
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
        class_name="w-full mt-4 mb-8 rounded-[0.625rem] outline outline-input flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card overflow-x-auto scrollbar-none",
    )


def cli_and_manual_installation_wrapper(
    cli_command: str, files: list[tuple[str, str]]
) -> rx.Component:
    """Tabbed wrapper for CLI and Manual installation instructions."""

    tab_list_style = {
        "border": "none",
        "boxShadow": "none",
        "background": "transparent",
    }

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
                        create_copy_button(content=cli_command),
                        class_name="w-full border-b border-input flex flex-row items-center justify-between pl-[0.75rem] py-2",
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
                rx.el.div(
                    rx.el.p(
                        "1. Copy and paste the following dependencies into your project.",
                        class_name="text-sm font-medium",
                    ),
                    rx.el.div(
                        *[
                            file_codeblock(file[0], file[1])
                            for i, file in enumerate(files[:-1])
                        ],
                        class_name="w-full flex flex-col gap-y-4",
                    ),
                    class_name="w-full flex flex-col gap-y-4",
                ),
                rx.el.div(
                    rx.el.p(
                        "2. Copy and paste the following component code into your project.",
                        class_name="text-sm font-medium",
                    ),
                    file_codeblock_full(files[-1][0], files[-1][1]),
                    class_name="w-full flex flex-col gap-y-4",
                ),
                class_name="flex flex-col gap-y-6",
            )
            if len(files) > 1
            else file_codeblock_full(files[-1][0], files[-1][1]),
            value="manual",
            class_name="mt-6",
        ),
        default_value="cli",
        class_name="mb-8",
    )


def tooltip_indicator(color: str, swatch: Swatch) -> rx.Component:
    if swatch == "square":
        return rx.el.span(
            style={
                "width": "12px",
                "height": "12px",
                "borderRadius": "3px",
                "background": color,
                "flexShrink": "0",
                "display": "block",
            }
        )
    elif swatch == "line":
        return rx.el.span(
            rx.el.span(
                style={
                    "width": "3px",
                    "height": "3px",
                    "borderRadius": "50%",
                    "background": color,
                    "display": "block",
                }
            ),
            rx.el.span(
                style={
                    "width": "3px",
                    "height": "3px",
                    "borderRadius": "50%",
                    "background": color,
                    "display": "block",
                }
            ),
            rx.el.span(
                style={
                    "width": "3px",
                    "height": "3px",
                    "borderRadius": "50%",
                    "background": color,
                    "display": "block",
                }
            ),
            style={"display": "flex", "flexDirection": "column", "gap": "2px"},
        )
    return rx.fragment()  # "border" swatch uses CSS border on the row itself


def tooltip_row(
    name: str,
    value: str,
    color: str,
    swatch: Swatch,
) -> rx.Component:
    row_style = {
        "display": "flex",
        "alignItems": "center",
        "gap": "8px",
    }
    if swatch == "border":
        row_style["borderLeft"] = f"2px solid {color}"
        row_style["paddingLeft"] = "8px"
        row_style["margin"] = "0"

    children = []
    if swatch != "border":
        children.append(tooltip_indicator(color, swatch))

    children += [
        rx.el.span(
            name,
            style={
                "fontSize": "13px",
                "color": "var(--color-text-secondary)",
                "minWidth": "72px",
            },
        ),
        rx.el.span(
            value, style={"fontSize": "13px", "color": "var(--color-text-primary)"}
        ),
    ]

    return rx.el.div(*children, style=row_style)


def tooltip_label(label: str, color: str, swatch: Swatch) -> rx.Component:
    label_style = {
        "margin": "0",
        "padding": "0 0 6px 8px" if swatch == "border" else "0 0 8px 0",
        "fontSize": "13px",
        "fontWeight": "500",
        "color": "var(--color-text-primary)",
    }
    if swatch == "border":
        label_style["borderLeft"] = f"2px solid {color}"

    return rx.el.p(label, style=label_style)


def tooltip_wrapper_demo(
    label: str | None,
    items: list[dict],
    swatch: Swatch = "square",
) -> rx.Component:
    children = []

    if label:
        children.append(
            tooltip_label(label, items[0]["color"] if items else "#3B82F6", swatch)
        )

    for item in items:
        children.append(
            tooltip_row(
                name=item["name"],
                value=item["value"],
                color=item["color"],
                swatch=swatch,
            )
        )

    return rx.el.div(
        *children,
        style={
            "background": "var(--bg-card)",
            "borderRadius": "0.75rem",
            "border": "1px solid var(--input)",
            "padding": "0.7rem",
            "width": "fit-content",
        },
        class_name="shadow-md",
    )


def tooltip_wrapper() -> rx.Component:
    mobile_container = rx.el.div(
        tooltip_wrapper_demo(
            label="Page Views",
            items=[
                {"name": "Desktop", "value": "186", "color": "#93C5FD"},
                {"name": "Mobile", "value": "80", "color": "#3B82F6"},
            ],
            swatch="square",
        ),
        tooltip_wrapper_demo(
            label="Page Views",
            items=[{"name": "Desktop", "value": "12,486", "color": "#3B82F6"}],
            swatch="border",
        ),
        tooltip_wrapper_demo(
            label=None,
            items=[{"name": "Chrome", "value": "1,286", "color": "#93C5FD"}],
            swatch="square",
        ),
        style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "gap": "16px",
            "padding": "24px",
        },
        class_name="!flex md:!hidden border border-input rounded-[1rem]",
    )

    desktop_container = rx.el.div(
        rx.el.div(
            tooltip_wrapper_demo(
                label="Page Views",
                items=[
                    {"name": "Desktop", "value": "186", "color": "#93C5FD"},
                    {"name": "Mobile", "value": "80", "color": "#3B82F6"},
                ],
                swatch="square",
            ),
            style={
                "position": "absolute",
                "top": "30px",
                "left": "50%",
                "transform": "translateX(-50%)",
            },
            class_name="transition-all duration-200 ease-out hover:-translate-y-1",
        ),
        rx.el.div(
            tooltip_wrapper_demo(
                label="Page Views",
                items=[{"name": "Desktop", "value": "12,486", "color": "#3B82F6"}],
                swatch="border",
            ),
            style={
                "position": "absolute",
                "bottom": "80px",
                "left": "16%",
            },
            class_name="transition-all duration-200 ease-out hover:-translate-y-1",
        ),
        rx.el.div(
            tooltip_wrapper_demo(
                label=None,
                items=[{"name": "Chrome", "value": "1,286", "color": "#93C5FD"}],
                swatch="square",
            ),
            style={
                "position": "absolute",
                "bottom": "35px",
                "right": "15%",
            },
            class_name="transition-all duration-200 ease-out hover:-translate-y-1",
        ),
        style={
            "position": "relative",
            "width": "100%",
            "height": "320px",
        },
        class_name="!hidden md:!block rounded-[1rem] border border-input",
    )

    return rx.el.div(mobile_container, desktop_container)
