import reflex as rx

from components.ui.card import card

scat_data_1 = [
    {"name": "A", "x": 10, "y": 30},
    {"name": "B", "x": 20, "y": 50},
    {"name": "C", "x": 30, "y": 70},
    {"name": "D", "x": 40, "y": 20},
    {"name": "E", "x": 50, "y": 90},
    {"name": "F", "x": 60, "y": 40},
    {"name": "G", "x": 70, "y": 60},
    {"name": "H", "x": 80, "y": 100},
    {"name": "I", "x": 90, "y": 10},
    {"name": "J", "x": 100, "y": 80},
]

scat_data_2 = [
    {"name": "K", "x": 5, "y": 15},
    {"name": "L", "x": 15, "y": 40},
    {"name": "M", "x": 25, "y": 60},
    {"name": "N", "x": 35, "y": 10},
    {"name": "O", "x": 45, "y": 80},
    {"name": "P", "x": 55, "y": 30},
    {"name": "Q", "x": 65, "y": 50},
    {"name": "R", "x": 75, "y": 90},
    {"name": "S", "x": 85, "y": 20},
    {"name": "T", "x": 95, "y": 70},
]


def scatterchart_v1():

    return card.root(
        card.header(
            rx.el.div(
                card.title("Scatter Chart"),
                card.description("Showing multi-series distribution"),
                class_name="flex flex-col gap-y-1.5",
            )
        ),
        card.content(
            rx.recharts.scatter_chart(
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.scatter(
                    name="Data 1",
                    data=scat_data_1,
                    fill="var(--chart-1)",
                    is_animation_active=False,
                ),
                rx.recharts.scatter(
                    name="Data 2",
                    data=scat_data_2,
                    fill="var(--chart-2)",
                    is_animation_active=False,
                ),
                rx.recharts.y_axis(
                    data_key="y",
                    hide=True,
                ),
                rx.recharts.x_axis(
                    data_key="x",
                    type_="number",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                width="100%",
                height=210,
            ),
            rx.el.div(
                rx.foreach(
                    ["Data 1", "Data 2"],
                    lambda data, index: rx.el.div(
                        rx.el.div(
                            class_name=f"h-3 w-3 rounded-sm bg-chart-{index + 1}"
                        ),
                        rx.el.div(data, class_name="text-xs text-foreground"),
                        class_name="flex flex-row items-center gap-x-2",
                    ),
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="flex flex-col h-[250px] items-center justify-center",
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
        class_name="w-full p-0",
    )
