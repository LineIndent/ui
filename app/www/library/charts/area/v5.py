import datetime
import random

import reflex as rx
from reflex.experimental import ClientStateVar

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card


def areachart_v5():

    start_date = datetime.date(2024, 4, 1)
    data = [
        {
            "date": (start_date + datetime.timedelta(days=i)).strftime("%b %d"),
            "desktop": random.randint(80, 500),
            "mobile": random.randint(100, 550),
        }
        for i in range(91)
    ]

    SelectedRange = ClientStateVar.create("area_selected", data)

    def gradient(id_: str, color: str):
        return rx.el.svg.linear_gradient(
            rx.el.svg.stop(stop_color=f"var(--{color})", offset="5%", stop_opacity=0.8),
            rx.el.svg.stop(
                stop_color=f"var(--{color})", offset="95%", stop_opacity=0.1
            ),
            x1=0,
            x2=0,
            y1=0,
            y2=1,
            id=id_,
        )

    def area(data_key: str, color: str):
        return rx.recharts.area(
            data_key=data_key,
            fill=f"url(#{data_key})",
            stack_id="a",
            stroke=f"var(--{color})",
            animation_easing="linear",
            is_animation_active=False,
            active_dot={"fill": f"var(--{color})"},
        )

    select_options = [
        ("Last 3 Months", data),
        ("Last 30 Days", data[-30:]),
        ("Last 7 Days", data[-7:]),
    ]

    return card.root(
        card.header(
            rx.el.div(
                rx.el.div(
                    card.title("Area Chart - Dynamic"),
                    card.description("Showing total visitors for the last 6 months"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.el.select(
                    *[
                        rx.el.option(label, on_click=SelectedRange.set_value(value))
                        for label, value in select_options
                    ],
                    default_value="Last 3 Months",
                    class_name="relative flex items-center whitespace-nowrap justify-center gap-2 py-2 rounded-lg shadow-sm px-3 bg-secondary border border-input",
                ),
                class_name="flex flex-row flex-wrap gap-y-4 items-center justify-between",
            ),
        ),
        card.content(
            rx.recharts.area_chart(
                rx.el.svg.defs(
                    gradient("desktop", "chart-1"),
                    gradient("mobile", "chart-2"),
                ),
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                area("mobile", "chart-2"),
                area("desktop", "chart-1"),
                rx.recharts.x_axis(
                    data_key="date",
                    axis_line=False,
                    min_tick_gap=32,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                data=SelectedRange.value,
                width="100%",
                height=240,
            ),
            class_name="flex flex-col items-center h-[240px]",
        ),
        card.footer(
            rx.el.div(
                rx.foreach(
                    ["Desktop", "Mobile"],
                    lambda device, index: rx.el.div(
                        rx.el.div(
                            class_name=f"w-3 h-3 rounded-sm bg-chart-{index + 1}"
                        ),
                        rx.el.p(device, class_name="text-sm text-foreground"),
                        class_name="flex flex-row items-center gap-x-2",
                    ),
                ),
                class_name="py-4 px-4 flex w-full flex justify-center gap-8",
            ),
        ),
        class_name=chart_tooltip_content([1, 2], "square") + " w-full p-0",
    )
