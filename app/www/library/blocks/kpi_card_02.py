import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"date": "Jan 23", "users": 234, "sessions": 1432, "churn": 5.2},
    {"date": "Feb 23", "users": 431, "sessions": 1032, "churn": 4.3},
    {"date": "Mar 23", "users": 543, "sessions": 1089, "churn": 5.1},
    {"date": "Apr 23", "users": 489, "sessions": 988, "churn": 5.4},
    {"date": "May 23", "users": 391, "sessions": 642, "churn": 5.5},
    {"date": "Jun 23", "users": 582, "sessions": 786, "churn": 4.8},
    {"date": "Jul 23", "users": 482, "sessions": 673, "churn": 4.5},
    {"date": "Aug 23", "users": 389, "sessions": 761, "churn": 0},
    {"date": "Sep 23", "users": 521, "sessions": 793, "churn": 0},
    {"date": "Oct 23", "users": 434, "sessions": 543, "churn": 0},
    {"date": "Nov 23", "users": 332, "sessions": 678, "churn": 0},
    {"date": "Dec 23", "users": 275, "sessions": 873, "churn": 0},
]

categories = [
    {
        "name": "Monthly users",
        "key": "users",
        "color": 1,
        "avg": round(sum(d["users"] for d in data) / len(data)),
        "suffix": "",
    },
    {
        "name": "Monthly sessions",
        "key": "sessions",
        "color": 2,
        "avg": round(sum(d["sessions"] for d in data) / len(data)),
        "suffix": "",
    },
    {
        "name": "Monthly churn",
        "key": "churn",
        "color": 3,
        "avg": round(sum(d["churn"] for d in data) / len(data), 1),
        "suffix": "%",
    },
]


def _gradient(id_: str, color: int) -> rx.Component:
    return rx.el.svg.linear_gradient(
        rx.el.svg.stop(
            stop_color=f"var(--chart-{color})", offset="5%", stop_opacity=0.2
        ),
        rx.el.svg.stop(
            stop_color=f"var(--chart-{color})", offset="95%", stop_opacity=0.2
        ),
        x1=0,
        x2=0,
        y1=0,
        y2=1,
        id=id_,
    )


def _mini_chart(key: str, color: int) -> rx.Component:
    return rx.recharts.area_chart(
        chart_tooltip(label="hide"),
        rx.el.svg.defs(_gradient(key, color)),
        rx.recharts.x_axis(
            data_key="date",
            tick_line=False,
            axis_line=False,
            interval="preserveStartEnd",
            custom_attrs={"fontSize": "10px"},
        ),
        rx.recharts.y_axis(hide=True),
        rx.recharts.area(
            data_key=key,
            fill=f"url(#{key})",
            stroke=f"var(--chart-{color})",
            stroke_width=2,
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-1)", "stroke": f"var(--chart-{color})"},
        ),
        data=data,
        width="100%",
        height=100,
    )


def _kpi_mini_chart(
    name: str, key: str, color: int, avg: float, suffix: str
) -> rx.Component:
    return card.root(
        card.content(
            rx.el.p(name, class_name="text-sm text-muted-foreground"),
            rx.el.div(
                rx.el.span(
                    f"{avg:,}{suffix}",
                    class_name="text-xl font-semibold",
                ),
                rx.el.span(
                    "12-month avg",
                    class_name="text-sm text-muted-foreground",
                ),
                class_name="mt-1 flex items-baseline justify-between gap-2",
            ),
            _mini_chart(key, color),
        ),
        class_name=chart_tooltip_content([color], "square")
        + " w-full px-4 pt-4 pb-0 border border-input/80 rounded-2xl",
    )


def kpi_card_02():
    return rx.el.dl(
        *[_kpi_mini_chart(**item) for item in categories],
        class_name="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
    )
