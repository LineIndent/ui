from components.ui.autocomplete import autocomplete


def autocomplete_custom_styling():
    return autocomplete(
        items=["feature", "fix", "bug", "docs", "internal", "mobile"],
        placeholder="Search tags...",
        input_class="h-10 rounded-full px-4 border-ring",
        popup_class="rounded-xl",
        item_class="rounded-full px-3",
        item_highlighted_class="bg-primary text-primary-foreground",
    )
