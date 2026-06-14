import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

sport_data = [
    {"date": "Jan 23", "Running": 167, "Cycling": 145},
    {"date": "Feb 23", "Running": 125, "Cycling": 110},
    {"date": "Mar 23", "Running": 156, "Cycling": 149},
    {"date": "Apr 23", "Running": 165, "Cycling": 112},
    {"date": "May 23", "Running": 153, "Cycling": 138},
    {"date": "Jun 23", "Running": 124, "Cycling": 145},
    {"date": "Jul 23", "Running": 164, "Cycling": 134},
]

activities = ["Running", "Cycling"]
chart_colors = ["var(--chart-1)", "var(--chart-2)"]


def create_alternating_chart(active_key: str):
    return rx.recharts.bar_chart(
        chart_tooltip(),
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-30"
        ),
        *[
            rx.recharts.bar(
                is_animation_active=False,
                radius=4,
                data_key=key,
                fill=color,
                custom_attrs={"opacity": rx.cond(key == active_key, "0.25", "1")},
            )
            for key, color in zip(activities, chart_colors)
        ],
        rx.recharts.x_axis(
            data_key="date",
            axis_line=False,
            tick_size=10,
            tick_line=False,
            custom_attrs={"fontSize": "12px"},
            interval="preserveStartEnd",
        ),
        data=sport_data,
        width="100%",
        height=250,
    )


def barchart_v10():

    return card.root(
        card.header(
            rx.hstack(
                rx.el.div(
                    card.title("Sport Activities"),
                    card.description("Running vs Cycling load"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.tabs.root(
                    rx.tabs.list(
                        *[
                            rx.tabs.trigger(
                                rx.text(activity, class_name="text-xs font-semibold"),
                                value=str(i + 1),
                            )
                            for i, activity in enumerate(activities)
                        ]
                    ),
                    default_value="1",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
        ),
        card.content(
            rx.tabs.root(
                *[
                    rx.tabs.content(
                        create_alternating_chart(active),
                        value=str(i + 1),
                    )
                    for i, active in enumerate(activities)
                ],
                default_value="1",
                width="100%",
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
