import reflex as rx

from components.ui.tabs import tabs


def tabs_line() -> rx.Component:
    return tabs.root(
        tabs.list(
            tabs.indicator(),
            tabs.tab("Overview", value="overview"),
            tabs.tab("Analytics", value="analytics"),
            tabs.tab("Reports", value="reports"),
            variant="line",
        ),
        default_value="overview",
    )
