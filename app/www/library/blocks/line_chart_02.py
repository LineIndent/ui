import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"date": "Jan 23", "Munich": 42340, "Zurich": 22320, "Vienna": 12410},
    {"date": "Feb 23", "Munich": 50120, "Zurich": 32310, "Vienna": 10300},
    {"date": "Mar 23", "Munich": 45190, "Zurich": 23450, "Vienna": 10900},
    {"date": "Apr 23", "Munich": 56420, "Zurich": 13400, "Vienna": 7900},
    {"date": "May 23", "Munich": 40420, "Zurich": 16400, "Vienna": 12310},
    {"date": "Jun 23", "Munich": 47010, "Zurich": 18350, "Vienna": 10250},
    {"date": "Jul 23", "Munich": 47490, "Zurich": 19950, "Vienna": 12650},
    {"date": "Aug 23", "Munich": 39610, "Zurich": 10910, "Vienna": 4650},
    {"date": "Sep 23", "Munich": 45860, "Zurich": 24740, "Vienna": 12650},
    {"date": "Oct 23", "Munich": 50910, "Zurich": 15740, "Vienna": 10430},
    {"date": "Nov 23", "Munich": 4919, "Zurich": 2874, "Vienna": 2081},
    {"date": "Dec 23", "Munich": 5519, "Zurich": 2274, "Vienna": 1479},
]


summary = [
    {
        "location": "Munich",
        "address": "Maximilianstrasse",
        "color": "-chart-1",
        "type": "Flagship",
        "total": "$460.2K",
        "change": "+0.7%",
        "change_type": "positive",
    },
    {
        "location": "Zurich",
        "address": "Bahnhofstrasse",
        "color": "-chart-2",
        "type": "In-Store",
        "total": "$237.3K",
        "change": "-1.2%",
        "change_type": "negative",
    },
    {
        "location": "Vienna",
        "address": "Stephansplatz",
        "color": "-chart-3",
        "type": "In-Store",
        "total": "$118.2K",
        "change": "+4.6%",
        "change_type": "positive",
    },
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
            interval="preserveStartEnd",
            custom_attrs={"fontSize": "11px"},
        ),
        rx.recharts.y_axis(
            width=50,
            tick_line=False,
            axis_line=False,
            tick_size=15,
            custom_attrs={"fontSize": "12px"},
            hide=not show_y_axis,
        ),
        rx.recharts.line(
            data_key="Munich",
            stroke="var(--chart-1)",
            stroke_width=2,
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-1)", "stroke": "var(--chart-1)"},
        ),
        rx.recharts.line(
            data_key="Zurich",
            stroke="var(--chart-2)",
            stroke_width=2,
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-2)", "stroke": "var(--chart-2)"},
        ),
        rx.recharts.line(
            data_key="Vienna",
            stroke="var(--chart-3)",
            stroke_width=2,
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-3)", "stroke": "var(--chart-3)"},
        ),
        data=data,
        width="100%",
        height=270,
    )


def _summary_item(item: dict) -> rx.Component:
    is_positive = item["change_type"] == "positive"

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                class_name=f"size-3 rounded-sm bg{item['color']}",
            ),
            rx.el.div(
                rx.el.p(
                    item["location"],
                    class_name="text-sm font-medium",
                ),
                rx.el.span(
                    item["type"],
                    class_name="rounded bg-muted px-1.5 py-0.5 text-xs",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center gap-2",
        ),
        rx.el.div(
            rx.el.span(
                item["address"],
                class_name="text-xs text-muted-foreground",
            ),
        ),
        rx.el.div(
            rx.el.p(
                item["change"],
                class_name=(
                    "text-sm font-medium "
                    + ("text-emerald-600" if is_positive else "text-red-600")
                ),
            ),
            rx.el.span(
                item["total"],
                class_name="text-xs text-muted-foreground",
            ),
            class_name="text-right",
        ),
        class_name="flex items-center justify-between py-2 border-b border-input last:border-0",
    )


def line_chart_02():
    return card.root(
        card.header(
            rx.el.p("Revenue", class_name="text-sm text-muted-foreground"),
            rx.el.p("$815,700", class_name="text-3xl font-semibold"),
        ),
        card.content(
            rx.el.div(_chart(show_y_axis=True), class_name="hidden sm:block"),
            rx.el.div(_chart(show_y_axis=False), class_name="sm:hidden"),
            rx.el.div(
                *[_summary_item(item) for item in summary],
                class_name="mt-4 flex flex-col",
            ),
        ),
        class_name=chart_tooltip_content([1, 2, 3], "line") + " w-full p-0",
    )
