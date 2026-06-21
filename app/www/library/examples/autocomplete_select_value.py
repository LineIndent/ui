import reflex as rx

from components.ui.autocomplete import autocomplete


def autocomplete_select_value():
    return autocomplete(
        items=["feature", "fix", "bug", "docs", "internal", "mobile"],
        placeholder="Search and select...",
        on_select_item=lambda value: rx.toast(value),
    )
