import reflex as rx

from components.ui.card import card

data = [
    {
        "name": "Monthly active users",
        "stat": "996",
        "change": "+1.3%",
        "color": "bg-chart-1",
    },
    {
        "name": "Monthly sessions",
        "stat": "1,672",
        "change": "+9.1%",
        "color": "bg-chart-2",
    },
    {
        "name": "Monthly user growth",
        "stat": "5.1%",
        "change": "-4.8%",
        "color": "bg-chart-3",
    },
]


def _kpi_card(name: str, stat: str, change: str, color: str) -> rx.Component:
    is_positive = change.startswith("+")
    return card.root(
        rx.el.div(
            rx.el.div(class_name=f"w-1 shrink-0 rounded {color}"),
            rx.el.div(
                rx.el.span(name, class_name="truncate text-sm text-muted-foreground"),
                rx.el.span(
                    change,
                    class_name="text-sm font-medium "
                    + ("text-emerald-600" if is_positive else "text-red-600"),
                ),
                class_name="flex w-full items-center justify-between gap-3 truncate",
            ),
            class_name="flex gap-3",
        ),
        rx.el.div(
            rx.el.p(stat, class_name="text-3xl font-semibold"),
            class_name="mt-2 pl-4",
        ),
        class_name="w-full border border-input/80 rounded-2xl",
    )


def kpi_card_01():
    return rx.el.dl(
        *[_kpi_card(**item) for item in data],
        class_name="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
    )
