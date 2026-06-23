from components.ui.autocomplete import autocomplete


def autocomplete_grouping():
    return autocomplete(
        items=[
            {"group": "Fruits", "items": ["Apple", "Banana", "Mango"]},
            {"group": "Vegetables", "items": ["Carrot", "Broccoli"]},
            {"group": "Grains", "items": ["Rice", "Wheat", "Oats"]},
        ],
        placeholder="Search tags...",
        separator_class="bg-transparent",
        popup_class="mt-2",
        root_class="scrollbar-none",
    )
