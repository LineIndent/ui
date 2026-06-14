import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"month": "Jan", "desktop": 186},
    {"month": "Feb", "desktop": 305},
    {"month": "Mar", "desktop": 237},
    {"month": "Apr", "desktop": 73},
    {"month": "May", "desktop": 209},
    {"month": "Jun", "desktop": 214},
]


def barchart_v2():

    return card.root(
        card.header(
            card.title("Bar Chart - Horizontal"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
                rx.recharts.bar(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    radius=4,
                    is_animation_active=False,
                ),
                rx.recharts.x_axis(type_="number", hide=True, tick_size=0),
                rx.recharts.y_axis(
                    data_key="month",
                    type_="category",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=data,
                layout="vertical",
                width="100%",
                height=250,
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(1, "square") + " w-full p-0",
    )
