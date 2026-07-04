import reflex as rx

from components.icons.hugeicon import hi
from components.ui.tabs import tabs


def tabs_icons() -> rx.Component:
    return tabs.root(
        tabs.list(
            tabs.indicator(),
            tabs.tab(
                hi("BrowserIcon"),
                "Preview",
                value="preview",
            ),
            tabs.tab(
                hi("CodeIcon"),
                "Code",
                value="code",
            ),
        ),
        default_value="preview",
    )
