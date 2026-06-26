import reflex as rx
from reflex.experimental import ClientStateVar

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card
from components.ui.checkbox import checkbox
from components.ui.field import field

ShowComparison = ClientStateVar.create("show_comparison", False)

data = [
    {"date": "Jan 23", "This Year": 68560, "Last Year": 28560},
    {"date": "Feb 23", "This Year": 70320, "Last Year": 30320},
    {"date": "Mar 23", "This Year": 80233, "Last Year": 70233},
    {"date": "Apr 23", "This Year": 55123, "Last Year": 45123},
    {"date": "May 23", "This Year": 56000, "Last Year": 80600},
    {"date": "Jun 23", "This Year": 100000, "Last Year": 85390},
    {"date": "Jul 23", "This Year": 85390, "Last Year": 45340},
    {"date": "Aug 23", "This Year": 80100, "Last Year": 70120},
    {"date": "Sep 23", "This Year": 75090, "Last Year": 69450},
    {"date": "Oct 23", "This Year": 71080, "Last Year": 63345},
    {"date": "Nov 23", "This Year": 61210, "Last Year": 100330},
    {"date": "Dec 23", "This Year": 60143, "Last Year": 45321},
]


def _chart(show_y_axis: bool) -> rx.Component:
    return rx.recharts.bar_chart(
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
            width=55,
            tick_line=False,
            axis_line=False,
            tick_size=15,
            custom_attrs={"fontSize": "11px"},
            hide=not show_y_axis,
        ),
        rx.recharts.bar(
            data_key="This Year",
            fill="var(--chart-1)",
            is_animation_active=False,
            max_bar_size=40,
        ),
        rx.cond(
            ShowComparison.value,
            rx.recharts.bar(
                data_key="Last Year",
                fill="var(--chart-2)",
                is_animation_active=False,
                max_bar_size=40,
            ),
        ),
        data=data,
        width="100%",
        height=250,
    )


def bar_chart_01():
    return card.root(
        card.header(
            card.title("Sales overview"),
            card.description(
                "Lorem ipsum dolor sit amet, consetetur sadipscing elitr."
            ),
        ),
        rx.el.div(
            rx.cond(
                ShowComparison.value,
                rx.el.div(
                    rx.el.div(class_name="w-3 h-3 rounded-sm bg-chart-2"),
                    "Last Year",
                    class_name="text-sm flex flex-row gap-x-2 items-center",
                ),
            ),
            rx.el.div(
                rx.el.div(class_name="w-3 h-3 rounded-sm bg-chart-1"),
                "This Year",
                class_name="text-sm flex flex-row gap-x-2 items-center",
            ),
            class_name="flex flex-row gap-x-2 justify-end items-center",
        ),
        card.content(
            # Mobile: no y-axis
            rx.el.div(_chart(show_y_axis=False), class_name="sm:hidden"),
            # Desktop: with y-axis
            rx.el.div(_chart(show_y_axis=True), class_name="hidden sm:block"),
        ),
        card.footer(
            field.root(
                checkbox(
                    id="terms-checkbox-basic",
                    on_checked_change=ShowComparison.set_value(~ShowComparison.value),
                ),
                field.label(
                    "Show same period last year",
                    html_for="terms-checkbox-basic",
                ),
                orientation="horizontal",
            ),
        ),
        class_name=chart_tooltip_content([1, 2], "square") + " w-full p-0",
    )
