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


def areachart_v10():
    series = [("mobile", "Mobile", "--chart-1"), ("desktop", "Desktop", "--chart-2")]

    return card.root(
        card.header(
            rx.hstack(
                rx.el.div(
                    card.title("Area Chart - Mixed"),
                    card.description("Showing total visitors for the last 6 months"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.hstack(
                    rx.foreach(
                        series,
                        lambda s: rx.hstack(
                            rx.box(class_name="size-2 rounded-full", bg=f"var({s[2]})"),
                            rx.text(
                                s[1],
                                class_name="text-xs font-medium",
                                color=rx.color("slate", 11),
                            ),
                            align="center",
                            spacing="2",
                        ),
                    ),
                    class_name="flex items-center gap-4",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
        ),
        card.content(
            rx.recharts.area_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="mobile",
                    fill="var(--chart-1)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    stack_id="a",
                    is_animation_active=False,
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="var(--chart-2)",
                    stroke="var(--chart-2)",
                    stroke_width=2,
                    stack_id="a",
                    is_animation_active=False,
                ),
                rx.recharts.x_axis(
                    data_key="month",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                rx.recharts.y_axis(
                    width=30,
                    axis_line=False,
                    min_tick_gap=50,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
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
        class_name=chart_tooltip_content([1, 2], "square") + " w-full p-0",
    )
