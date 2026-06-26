import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"hour": "00:00", "temperature": 12.8},
    {"hour": "01:00", "temperature": 12.4},
    {"hour": "02:00", "temperature": 12.2},
    {"hour": "03:00", "temperature": 11.9},
    {"hour": "04:00", "temperature": 11.7},
    {"hour": "05:00", "temperature": 11.5},
    {"hour": "06:00", "temperature": 11.3},
    {"hour": "07:00", "temperature": 11.2},
    {"hour": "08:00", "temperature": 11.5},
    {"hour": "09:00", "temperature": 12.0},
    {"hour": "10:00", "temperature": 13.0},
    {"hour": "11:00", "temperature": 14.2},
    {"hour": "12:00", "temperature": 15.5},
    {"hour": "13:00", "temperature": 16.8},
    {"hour": "14:00", "temperature": 17.5},
    {"hour": "15:00", "temperature": 18.1},
    {"hour": "16:00", "temperature": 18.2},
    {"hour": "17:00", "temperature": 17.8},
    {"hour": "18:00", "temperature": 17.2},
    {"hour": "19:00", "temperature": 16.5},
    {"hour": "20:00", "temperature": 15.8},
    {"hour": "21:00", "temperature": 14.9},
    {"hour": "22:00", "temperature": 14.2},
    {"hour": "23:00", "temperature": 13.5},
]


def _chart(show_y_axis: bool) -> rx.Component:
    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-50"
        ),
        rx.recharts.x_axis(
            data_key="hour",
            tick_line=False,
            axis_line=False,
            interval="preserveStartEnd",
            label={
                "value": "24H Temperature Readout (Zurich)",
                "position": "insideBottom",
                "offset": -5,
                "style": {"fill": "var(--muted-foreground)", "fontSize": "12px"},
            },
        ),
        rx.recharts.y_axis(
            width=40,
            tick_line=False,
            axis_line=False,
            hide=not show_y_axis,
        ),
        rx.recharts.bar(
            data_key="temperature",
            fill="var(--chart-1)",
            is_animation_active=False,
        ),
        data=data,
        width="100%",
        height=300,
    )


def bar_chart_04():
    return card.root(
        card.header(
            card.title("Temperature"),
            card.description("Zurich — 24 hour readout"),
        ),
        card.content(
            rx.el.div(_chart(show_y_axis=False), class_name="sm:hidden"),
            rx.el.div(_chart(show_y_axis=True), class_name="hidden sm:block"),
        ),
        class_name=chart_tooltip_content([1], "square") + " w-full p-0",
    )
