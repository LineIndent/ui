from components.ui.autocomplete import autocomplete


def autocomplete_basic():
    return autocomplete(
        items=["feature", "fix", "bug", "docs", "internal", "mobile"],
        placeholder="Search tags...",
    )
