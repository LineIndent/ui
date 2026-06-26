import reflex as rx

from components.charts.chart_tooltip import (
    chart_tooltip,
    chart_tooltip_content,
)
from components.ui.card import card

data = [
    {"date": "Aug 01", "Market Index": 44.1, "Portfolio": 79.2},
    {"date": "Aug 02", "Market Index": 49.1, "Portfolio": 89.1},
    {"date": "Aug 03", "Market Index": 61.2, "Portfolio": 91.7},
    {"date": "Aug 04", "Market Index": 49.7, "Portfolio": 74.4},
    {"date": "Aug 05", "Market Index": 71.1, "Portfolio": 95.3},
    {"date": "Aug 06", "Market Index": 75.3, "Portfolio": 99.4},
    {"date": "Aug 07", "Market Index": 74.1, "Portfolio": 101.2},
    {"date": "Aug 08", "Market Index": 78.4, "Portfolio": 102.2},
    {"date": "Aug 09", "Market Index": 81.1, "Portfolio": 103.6},
    {"date": "Aug 10", "Market Index": 82.6, "Portfolio": 104.4},
    {"date": "Aug 11", "Market Index": 89.3, "Portfolio": 106.3},
    {"date": "Aug 12", "Market Index": 79.3, "Portfolio": 109.5},
    {"date": "Aug 13", "Market Index": 78.6, "Portfolio": 110.4},
    {"date": "Aug 14", "Market Index": 73.8, "Portfolio": 113.5},
    {"date": "Aug 15", "Market Index": 69.7, "Portfolio": 114.1},
    {"date": "Aug 16", "Market Index": 62.6, "Portfolio": 121.4},
    {"date": "Aug 17", "Market Index": 59.3, "Portfolio": 120.4},
    {"date": "Aug 18", "Market Index": 57.1, "Portfolio": 110.7},
    {"date": "Aug 19", "Market Index": 55.1, "Portfolio": 118.8},
    {"date": "Aug 20", "Market Index": 54.3, "Portfolio": 123.1},
    {"date": "Aug 21", "Market Index": 53.2, "Portfolio": 110.2},
    {"date": "Aug 22", "Market Index": 49.4, "Portfolio": 101.2},
    {"date": "Aug 23", "Market Index": 48.1, "Portfolio": 99.2},
    {"date": "Aug 24", "Market Index": 27.1, "Portfolio": 105.8},
    {"date": "Aug 25", "Market Index": 21.0, "Portfolio": 109.4},
    {"date": "Aug 26", "Market Index": 21.3, "Portfolio": 110.1},
    {"date": "Aug 27", "Market Index": 21.8, "Portfolio": 119.6},
    {"date": "Aug 28", "Market Index": 29.4, "Portfolio": 121.3},
    {"date": "Aug 29", "Market Index": 32.4, "Portfolio": 129.1},
    {"date": "Aug 30", "Market Index": 37.1, "Portfolio": 134.5},
    {"date": "Aug 31", "Market Index": 41.3, "Portfolio": 144.2},
    {"date": "Sep 01", "Market Index": 48.1, "Portfolio": 145.1},
    {"date": "Sep 02", "Market Index": 51.3, "Portfolio": 142.5},
    {"date": "Sep 03", "Market Index": 52.8, "Portfolio": 140.9},
    {"date": "Sep 04", "Market Index": 54.4, "Portfolio": 138.7},
    {"date": "Sep 05", "Market Index": 57.1, "Portfolio": 135.2},
    {"date": "Sep 06", "Market Index": 67.9, "Portfolio": 136.2},
    {"date": "Sep 07", "Market Index": 78.8, "Portfolio": 136.2},
    {"date": "Sep 08", "Market Index": 89.2, "Portfolio": 146.2},
    {"date": "Sep 09", "Market Index": 99.2, "Portfolio": 145.2},
    {"date": "Sep 10", "Market Index": 101.2, "Portfolio": 141.8},
    {"date": "Sep 11", "Market Index": 104.2, "Portfolio": 132.2},
    {"date": "Sep 12", "Market Index": 109.8, "Portfolio": 129.2},
    {"date": "Sep 13", "Market Index": 110.4, "Portfolio": 120.3},
    {"date": "Sep 14", "Market Index": 111.3, "Portfolio": 123.4},
    {"date": "Sep 15", "Market Index": 114.3, "Portfolio": 137.4},
    {"date": "Sep 16", "Market Index": 105.1, "Portfolio": 130.1},
    {"date": "Sep 17", "Market Index": 89.3, "Portfolio": 131.8},
    {"date": "Sep 18", "Market Index": 102.1, "Portfolio": 149.4},
    {"date": "Sep 19", "Market Index": 101.7, "Portfolio": 149.3},
    {"date": "Sep 20", "Market Index": 121.3, "Portfolio": 153.2},
    {"date": "Sep 21", "Market Index": 132.5, "Portfolio": 157.2},
    {"date": "Sep 22", "Market Index": 121.4, "Portfolio": 139.1},
    {"date": "Sep 23", "Market Index": 100.1, "Portfolio": 120.2},
    {"date": "Sep 24", "Market Index": 89.1, "Portfolio": 119.1},
    {"date": "Sep 25", "Market Index": 97.1, "Portfolio": 112.2},
    {"date": "Sep 26", "Market Index": 109.4, "Portfolio": 129.1},
]


summary = [
    ("Portfolio value", "$37,081.89"),
    ("Invested", "$19,698.65"),
    ("Cashflow", "$20,033.74"),
    ("Price gain", "+$15,012.39"),
    ("Realized", "+$177.4"),
    ("Dividends (gross)", "+$490.97"),
]


def _chart(show_y_axis: bool) -> rx.Component:
    return rx.recharts.line_chart(
        chart_tooltip(),
        rx.recharts.cartesian_grid(
            horizontal=True,
            vertical=False,
            class_name="opacity-50",
        ),
        rx.recharts.x_axis(
            data_key="date",
            tick_line=False,
            axis_line=False,
            tick_size=15,
            custom_attrs={"fontSize": "11px"},
            interval="preserveStartEnd",
        ),
        rx.recharts.y_axis(
            width=30,
            tick_line=False,
            axis_line=False,
            tick_size=15,
            custom_attrs={"fontSize": "11px"},
            hide=not show_y_axis,
        ),
        rx.recharts.line(
            data_key="Portfolio",
            stroke="var(--chart-1)",
            stroke_width=2,
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-1)", "stroke": "var(--chart-1)"},
        ),
        rx.recharts.line(
            data_key="Market Index",
            stroke="var(--chart-2)",
            stroke_width=2,
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-2)", "stroke": "var(--chart-2)"},
        ),
        data=data,
        width="100%",
        height=280,
    )


def _summary_list(items):
    return rx.el.ul(
        *[
            rx.el.li(
                rx.el.span(
                    label,
                    class_name="text-sm text-muted-foreground",
                ),
                rx.el.span(
                    value,
                    class_name=(
                        "text-sm font-medium "
                        if not value.startswith("+")
                        else "text-sm font-medium text-emerald-600"
                    ),
                ),
                class_name=(
                    "flex items-center justify-between "
                    "gap-4 py-1.5 border-b border-input "
                    "last:border-0"
                ),
            )
            for label, value in items
        ],
        class_name="w-full",
    )


def line_chart_03():
    return card.root(
        card.header(
            rx.el.p(
                "Portfolio performance",
                class_name="text-sm text-muted-foreground",
            ),
            rx.el.p(
                "$37,081.89",
                class_name="mt-1 text-3xl font-semibold",
            ),
            rx.el.p(
                rx.el.span(
                    "+$430.90 (4.1%)",
                    class_name="text-emerald-600 font-medium",
                ),
                " ",
                rx.el.span(
                    "Past 24 hours",
                    class_name="text-muted-foreground",
                ),
                class_name="mt-1 text-sm",
            ),
        ),
        card.content(
            rx.el.div(
                _chart(show_y_axis=False),
                class_name="sm:hidden",
            ),
            rx.el.div(
                _chart(show_y_axis=True),
                class_name="hidden sm:block",
            ),
            rx.el.p(
                "Portfolio summary",
                class_name="mt-6 mb-3 text-sm font-medium",
            ),
            rx.el.div(
                _summary_list(summary[:3]),
                _summary_list(summary[3:]),
                class_name="flex gap-8",
            ),
        ),
        class_name=(chart_tooltip_content([1, 2], "square") + " w-full p-0"),
    )
