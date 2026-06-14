from components.ui.tabs import tabs


def tabs_disabled():
    return tabs.root(
        tabs.list(
            tabs.indicator(),
            tabs.tab(
                "Home",
                value="home",
            ),
            tabs.tab(
                "Disabled",
                value="settings",
                disabled=True,
            ),
        ),
        default_value="home",
    )
