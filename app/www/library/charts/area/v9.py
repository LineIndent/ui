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


def areachart_v9():

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

    return card.root(
        card.header(
            card.title("Area Chart - Step with Gradient"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.area_chart(
                rx.el.svg.defs(
                    gradient("desktop", "chart-1"),
                ),
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="url(#desktop)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="step",
                    is_animation_active=False,
                    active_dot={"fill": "var(--chart-1)"},
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
