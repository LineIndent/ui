import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"month": "Jan", "desktop": 186, "mobile": 80},
    {"month": "Feb", "desktop": 305, "mobile": 200},
    {"month": "Mar", "desktop": 237, "mobile": 120},
    {"month": "Apr", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "Jun", "desktop": 214, "mobile": 140},
]


def barchart_v3():

    return card.root(
        card.header(
            card.title("Bar Chart - Legend"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.bar(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    stack_id="a",
                    radius=[0, 0, 4, 4],
                    is_animation_active=False,
                ),
                rx.recharts.bar(
                    data_key="mobile",
                    fill="var(--chart-2)",
                    stack_id="a",
                    radius=[4, 4, 0, 0],
                    is_animation_active=False,
                ),
                rx.recharts.y_axis(type_="number", hide=True),
                rx.recharts.x_axis(
                    data_key="month",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                rx.recharts.legend(),
                data=data,
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
        class_name=chart_tooltip_content(2, "square") + " w-full p-0",
    )
