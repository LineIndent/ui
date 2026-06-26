import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"date": "Aug 01", "price": 21.2},
    {"date": "Aug 02", "price": 29.0},
    {"date": "Aug 03", "price": 48.5},
    {"date": "Aug 04", "price": 53.8},
    {"date": "Aug 05", "price": 57.7},
    {"date": "Aug 06", "price": 59.9},
    {"date": "Aug 07", "price": 41.4},
    {"date": "Aug 08", "price": 60.2},
    {"date": "Aug 09", "price": 62.8},
    {"date": "Aug 10", "price": 62.5},
    {"date": "Aug 11", "price": 63.6},
    {"date": "Aug 12", "price": 64.4},
    {"date": "Aug 13", "price": 65.1},
    {"date": "Aug 14", "price": 66.4},
    {"date": "Aug 15", "price": 71.6},
    {"date": "Aug 16", "price": 79.5},
    {"date": "Aug 17", "price": 102.8},
    {"date": "Aug 18", "price": 103.2},
    {"date": "Aug 19", "price": 105.4},
    {"date": "Aug 20", "price": 110.9},
    {"date": "Aug 21", "price": 67.7},
    {"date": "Aug 22", "price": 69.8},
    {"date": "Aug 23", "price": 79.5},
    {"date": "Aug 24", "price": 90.0},
    {"date": "Aug 25", "price": 91.2},
    {"date": "Aug 26", "price": 95.1},
    {"date": "Aug 27", "price": 99.8},
    {"date": "Aug 28", "price": 100.6},
    {"date": "Aug 29", "price": 102.8},
    {"date": "Aug 30", "price": 100.5},
    {"date": "Aug 31", "price": 111.6},
    {"date": "Sep 01", "price": 123.2},
    {"date": "Sep 02", "price": 125.8},
    {"date": "Sep 03", "price": 120.4},
    {"date": "Sep 04", "price": 121.9},
    {"date": "Sep 05", "price": 124.5},
    {"date": "Sep 06", "price": 127.7},
    {"date": "Sep 07", "price": 129.2},
    {"date": "Sep 08", "price": 130.8},
    {"date": "Sep 09", "price": 134.4},
    {"date": "Sep 10", "price": 136.0},
    {"date": "Sep 11", "price": 137.5},
    {"date": "Sep 12", "price": 131.1},
    {"date": "Sep 13", "price": 128.6},
    {"date": "Sep 14", "price": 124.2},
    {"date": "Sep 15", "price": 120.8},
    {"date": "Sep 16", "price": 118.3},
    {"date": "Sep 17", "price": 101.9},
    {"date": "Sep 18", "price": 121.5},
    {"date": "Sep 19", "price": 129.1},
    {"date": "Sep 20", "price": 131.6},
    {"date": "Sep 21", "price": 141.2},
    {"date": "Sep 22", "price": 142.8},
    {"date": "Sep 23", "price": 143.3},
    {"date": "Sep 24", "price": 149.9},
    {"date": "Sep 25", "price": 159.5},
    {"date": "Sep 26", "price": 173.3},
]

summary = [
    ("Open", "$153.56"),
    ("High", "$154.78"),
    ("Volume", "$48.14M"),
    ("Low", "$179.12"),
    ("Close", "$173.34"),
    ("Market Cap", "$1.58B"),
]


def _summary_list(items: list[tuple[str, str]]) -> rx.Component:
    return rx.el.ul(
        *[
            rx.el.li(
                rx.el.span(label, class_name="text-sm text-muted-foreground truncate"),
                rx.el.span(value, class_name="text-sm font-medium"),
                class_name="flex items-center justify-between gap-4 py-1.5 border-b border-input last:border-0",
            )
            for label, value in items
        ],
        class_name="w-full",
    )


def _chart(show_y_axis: bool) -> rx.Component:
    return rx.recharts.line_chart(
        chart_tooltip(),
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-50"
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
            custom_attrs={"fontSize": "12px"},
            hide=not show_y_axis,
        ),
        rx.recharts.line(
            data_key="price",
            stroke="var(--chart-1)",
            stroke_width=2,
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-1)", "stroke": "var(--chart-1)"},
        ),
        data=data,
        width="100%",
        height=250,
    )


def line_chart_01():
    return card.root(
        card.header(
            rx.el.p("Amazon, Inc. (AMZN)", class_name="text-sm text-muted-foreground"),
            rx.el.p("$173.30", class_name="mt-1 text-3xl font-semibold"),
            rx.el.p(
                rx.el.span("+$9.30 (8.6%)", class_name="text-emerald-600 font-medium"),
                " ",
                rx.el.span("Past 24 hours", class_name="text-muted-foreground"),
                class_name="mt-1 text-sm",
            ),
        ),
        card.content(
            rx.el.div(_chart(show_y_axis=False), class_name="sm:hidden"),
            rx.el.div(_chart(show_y_axis=True), class_name="hidden sm:block"),
            rx.el.div(
                _summary_list(summary[:3]),
                _summary_list(summary[3:]),
                class_name="mt-4 flex items-start gap-6",
            ),
        ),
        class_name=chart_tooltip_content([1], "square") + " w-full p-0",
    )
