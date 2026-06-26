import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"month": "Jan", "desktop": 186, "mobile": 80, "tablet": 50},
    {"month": "Feb", "desktop": 305, "mobile": 200, "tablet": 120},
    {"month": "Mar", "desktop": 237, "mobile": 120, "tablet": 70},
    {"month": "Apr", "desktop": 73, "mobile": 190, "tablet": 30},
    {"month": "May", "desktop": 209, "mobile": 130, "tablet": 80},
]


def barchart_v9():

    return card.root(
        card.header(
            rx.el.div(
                card.title("Bar Chart - Multiple"),
                card.description("Showing total visitors for the last 6 months"),
                class_name="flex flex-col gap-y-1.5",
            ),
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
                    radius=4,
                    is_animation_active=False,
                ),
                rx.recharts.bar(
                    data_key="mobile",
                    fill="var(--chart-2)",
                    radius=4,
                    is_animation_active=False,
                ),
                rx.recharts.bar(
                    data_key="tablet",
                    fill="var(--chart-3)",
                    radius=4,
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
                data=data,
                width="100%",
                height=230,
            ),
            rx.el.div(
                rx.foreach(
                    ["Desktop", "Mobile", "Tablet"],
                    lambda device, index: rx.el.div(
                        rx.el.div(
                            class_name=f"h-3 w-3 rounded-sm bg-chart-{index + 1}"
                        ),
                        rx.el.p(device, class_name="text-xs text-foreground"),
                        class_name="flex flex-row items-center gap-x-2",
                    ),
                ),
                class_name="flex items-center gap-4 justify-center",
            ),
            class_name="flex flex-col h-[250px]",
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
        class_name=chart_tooltip_content([1, 2, 3], "square") + " w-full p-0",
    )
