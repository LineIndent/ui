import functools

import reflex as rx

from app.hooks import selected_blocks_category, selected_component_category
from app.www.wrapper import generate_component_id
from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.tooltip import tooltip


def open_in_reflex_build(
    icon_light,
    icon_dark,
    tooltip_content: str,
    href: str,
    icon_size: str = "size-5",
):
    return tooltip.provider(
        tooltip.root(
            tooltip.trigger(
                render_=rx.el.a(
                    rx.el.image(
                        rx.color_mode_cond(icon_light, icon_dark),
                        class_name=icon_size,
                    ),
                    href=href,
                    target="_blank",
                    rel="noopener noreferrer",
                )
            ),
            tooltip.portal(
                tooltip.positioner(
                    tooltip.popup(
                        rx.el.p(tooltip_content, class_name="!text-xs"),
                        class_name="rounded-radius p-2",
                    ),
                    side="top",
                    side_offset=8,
                ),
            ),
        ),
        delay=0,
    )


def block_card(func=None, *, label=""):
    """
    Decorator wrapper to wrap blocks
    """

    if func is None:
        return functools.partial(block_card, label=label)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inner_component = func(*args, **kwargs)
        cmd = f"uv run buridan add {func.__qualname__}"
        btn_id = generate_component_id()
        return rx.el.div(
            rx.el.div(
                button(
                    hi("TerminalIcon", class_name="size-4 shrink-0"),
                    cmd,
                    variant="outline",
                    size="sm",
                    id=btn_id,
                    on_click=rx.call_script(f"""
                        const btn = document.getElementById({btn_id!r});
                        navigator.clipboard.writeText({cmd!r});

                        const original = btn.innerText;
                        btn.innerText = "Copied!";

                        setTimeout(() => {{
                            btn.innerText = original;
                        }}, 1000);
                    """),
                    class_name="min-w-3xs",
                ),
                rx.el.p("︲", class_name="text-muted-foreground/50 font-thin h-6"),
                open_in_reflex_build(
                    icon_light="/svg/reflex/reflex_light.svg",
                    icon_dark="/svg/reflex/reflex_dark.svg",
                    tooltip_content="Open in Reflex Build",
                    href=f"https://build.reflex.dev/?prompt=Install and run pip install buridan-create and buridan init. Then run the following command: buridan add {func.__qualname__}",
                ),
                class_name="flex flex-row gap-x-2 items-center justify-end px-6 sm:px-2",
            ),
            rx.el.div(
                inner_component,
                class_name=" ".join(
                    [
                        "break-inside-avoid",
                        "w-full h-full",
                        "p-7",
                        "flex flex-col",
                    ]
                ),
            ),
            class_name=" ".join(
                [
                    "w-full flex flex-col",
                    "gap-y-2",
                ]
            )
            + rx.cond(
                (selected_blocks_category.value == "all")
                | (selected_blocks_category.value == label),
                " flex",
                " hidden",
            ).to(str),
        )

    return wrapper


def masonry_card(func=None, *, label="General"):
    """
    Decorator to wrap a component function inside a standard
    masonry-compatible div container with conditional visibility.
    """
    if func is None:
        return functools.partial(masonry_card, label=label)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inner_component = func(*args, **kwargs)

        return rx.el.div(
            inner_component,
            class_name=" ".join(
                [
                    "break-inside-avoid",
                    "w-full",
                    "bg-card",
                    "rounded-radius",
                    "border",
                    "border-input",
                    "p-card",
                    "flex flex-col",
                ]
            )
            + rx.cond(
                (selected_component_category.value == "All")
                | (selected_component_category.value == label),
                " flex",
                " hidden",
            ).to(str),
        )

    return wrapper
