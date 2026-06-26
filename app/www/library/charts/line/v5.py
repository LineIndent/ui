import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"browser": "chrome", "visitors": 275},
    {"browser": "safari", "visitors": 200},
    {"browser": "firefox", "visitors": 187},
    {"browser": "edge", "visitors": 173},
    {"browser": "other", "visitors": 90},
]


def linechart_v5():

    return card.root(
        card.header(
            card.title("Line Chart - Title Label"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip("hide"),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    rx.recharts.label_list(
                        position="top",
                        offset=20,
                        custom_attrs={"fontSize": "12px", "fontWeight": "bold"},
                        data_key="browser",
                    ),
                    data_key="visitors",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="natural",
                    dot=True,
                    is_animation_active=False,
                    active_dot={"fill": "var(--chart-1)"},
                ),
                data=data,
                width="100%",
                height=250,
                margin={"left": 25, "right": 20, "top": 25},
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
        class_name=chart_tooltip_content([1], "square") + " w-full p-0",
    )
