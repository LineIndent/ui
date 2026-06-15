import hashlib
import json
import random
import string

import reflex as rx

from components.icons.hugeicon import hi

PARAGRAPH_CLASS = "text-sm leading-7 mb-4"

HEADING_1_CLASS = "text-2xl font-semibold mt-8 mb-3 first:mt-0"

HEADING_2_CLASS = "text-xl font-semibold mt-6 mb-2"

LIST_ITEM_CLASS = "text-sm leading-7 text-slate-11"

LINK_CLASS = "text-accent-8 underline-offset-2 hover:underline"


# --- Helper error functions during parsing ---
def render_parse_error(msg: str):
    return rx.el.p(msg, class_name="text-sm text-red-500")


# --- Helper functions ---
def render_heading(level: int, text: str) -> rx.Component:
    return rx.el.header(
        text, class_name=HEADING_1_CLASS if level == 1 else HEADING_2_CLASS, id=text
    )


def render_paragraph(text: str) -> rx.Component:
    return rx.el.p(text, class_name=PARAGRAPH_CLASS)


def render_list_item(text: str) -> rx.Component:
    return rx.list_item(rx.el.p(text, class_name=LIST_ITEM_CLASS))


def render_link(text: str, **props) -> rx.Component:
    return rx.el.a(text, class_name=LINK_CLASS, **props)


def render_pre(*children, **props) -> rx.Component:
    # code name -> language = props.get(["langauge"])
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "uv",
                    class_name="text-muted-foreground text-sm font-normal px-[1rem] py-2",
                ),
                class_name="w-full border-b border-input/70 flex flex-row items-center justify-between",
            ),
            rx.el.div(
                rx.el.code(
                    *children,
                    style={
                        "white-space": "pre",
                        "color": "var(--foreground)",
                        "font-size": "13px",
                        "padding": "1rem 1rem",
                        "display": "block",
                    },
                ),
                class_name="overflow-x-auto overflow-y-auto scrollbar-none flex-1 min-h-0 pr-[1rem]",
            ),
            class_name="w-full flex-1 min-h-0 flex flex-col h-full",
        ),
        class_name="rounded-radius flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card",
    )


# --- Final Component Map ---
markdown_component_map = {
    "h1": lambda text: render_heading(1, text),
    "h2": lambda text: render_heading(2, text),
    "p": render_paragraph,
    "li": render_list_item,
    "a": render_link,
    "code": lambda text: rx.el.span(text, class_name="bg-secondary rounded-md p-1"),
    "pre": render_pre,
}
