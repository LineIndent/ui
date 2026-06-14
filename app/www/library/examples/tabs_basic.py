import reflex as rx

from components.ui.card import card
from components.ui.tabs import tabs


def tabs_basic():
    return rx.el.div(
        tabs.root(
            tabs.list(
                tabs.indicator(),
                tabs.tab("Overview", value="overview"),
                tabs.tab("Analytics", value="analytics"),
                tabs.tab("Reports", value="reports"),
                tabs.tab("Settings", value="settings"),
            ),
            tabs.panel(
                card.root(
                    card.header(
                        card.title("Overview"),
                        card.description(
                            "View your key metrics and recent project activity. Track progress across all your active projects."
                        ),
                    ),
                    card.content("You have 12 active projects and 3 pending tasks."),
                    class_name="ring-1 ring-foreground/10 rounded-[1rem] dark:bg-card",
                ),
                value="overview",
            ),
            tabs.panel(
                card.root(
                    card.header(
                        card.title("Analytics"),
                        card.description(
                            "Track performance and user engagement metrics. Monitor trends and identify growth opportunities."
                        ),
                    ),
                    card.content("Page views are up 25% compared to last month."),
                    class_name="ring-1 ring-foreground/10 rounded-[1rem] dark:bg-card",
                ),
                value="analytics",
            ),
            tabs.panel(
                card.root(
                    card.header(
                        card.title("Reports"),
                        card.description(
                            "Generate and download your detailed reports. Export data in multiple formats for analysis."
                        ),
                    ),
                    card.content("You have 5 reports ready and available to export."),
                    class_name="ring-1 ring-foreground/10 rounded-[1rem] dark:bg-card",
                ),
                value="reports",
            ),
            tabs.panel(
                card.root(
                    card.header(
                        card.title("Settings"),
                        card.description(
                            "Manage your account preferences and options. Customize your experience to fit your needs."
                        ),
                    ),
                    card.content("Configure notifications, security, and themes."),
                    class_name="ring-1 ring-foreground/10 rounded-[1rem]",
                ),
                value="settings",
            ),
            default_value="overview",
            class_name="w-[400px]",
        ),
        class_name="flex justify-center w-full",
    )
