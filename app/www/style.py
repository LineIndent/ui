import random
import string

import reflex as rx

# --- Markdown Styles ---
# PARAGRAPH_CLASS = "text-sm leading-7 mb-4"
# HEADING_1_CLASS = "text-2xl"
# HEADING_2_CLASS = "text-xl mt-2"
# LIST_ITEM_CLASS = "text-sm text-slate-11"
# LINK_CLASS = "text-accent-8"

PARAGRAPH_CLASS = "text-sm leading-7 mb-4"

HEADING_1_CLASS = "text-2xl font-semibold mt-8 mb-3 first:mt-0"

HEADING_2_CLASS = "text-xl font-semibold mt-6 mb-2"

LIST_ITEM_CLASS = "text-sm leading-7 text-slate-11"

LINK_CLASS = "text-accent-8 underline-offset-2 hover:underline"


# --- Helper functions to generate ClientStateVar names ---
def generate_component_id():
    """Generate a unique component ID."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


# --- Helper error functions during parsing ---
def render_parse_error(msg: str):
    return rx.el.p(msg, class_name="text-sm text-red-500")


# --- Helper functions ---
def render_heading(level: int, text: str) -> rx.Component:
    return rx.heading(
        text, class_name=HEADING_1_CLASS if level == 1 else HEADING_2_CLASS, id=text
    )


def render_paragraph(text: str) -> rx.Component:
    return rx.text(text, class_name=PARAGRAPH_CLASS)


def render_list_item(text: str) -> rx.Component:
    return rx.list_item(rx.text(text, class_name=LIST_ITEM_CLASS))


def render_link(text: str, **props) -> rx.Component:
    return rx.link(text, class_name=LINK_CLASS, **props)


# --- Final Component Map ---
markdown_component_map = {
    "h1": lambda text: render_heading(1, text),
    "h2": lambda text: render_heading(2, text),
    "p": render_paragraph,
    "li": render_list_item,
    "a": render_link,
    "code": lambda text: rx.el.span(text, class_name="bg-secondary rounded-md p-1"),
}
