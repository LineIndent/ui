import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

categories = ["Successful", "Refunded"]
EUROPE = [
    {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
    for month, successful, refunded in zip(
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        [12, 24, 48, 24, 34, 26, 12, 38, 23, 20, 24, 21],
        [0, 1, 4, 2, 0, 0, 0, 2, 1, 0, 0, 8],
    )
]

ASIA = [
    {"date": f"{month} 23", "Successful": successful, "Refunded": refunded}
    for month, successful, refunded in zip(
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        [31, 32, 44, 23, 35, 48, 33, 38, 41, 39, 32, 19],
        [1, 2, 3, 2, 1, 1, 1, 3, 2, 1, 1, 5],
    )
]


def create_chart(data: list[dict[str, str | int]]):
    return rx.recharts.bar_chart(
        chart_tooltip(),
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-30"
        ),
        rx.foreach(
            categories,
            lambda key, index: rx.recharts.bar(
                data_key=key,
                fill=f"var(--chart-{index + 1})",
                stack_id="_",
                is_animation_active=False,
            ),
        ),
        rx.recharts.x_axis(
            data_key="date",
            axis_line=False,
            tick_size=10,
            tick_line=False,
            custom_attrs={"fontSize": "12px"},
            interval=2,
        ),
        data=data,
        width="100%",
        height=250,
    )


def barchart_v8():

    return card.root(
        card.header(
            rx.hstack(
                rx.el.div(
                    card.title("Online Transactions"),
                    card.description("Global revenue distributions"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.tabs.root(
                    rx.tabs.list(
                        rx.tabs.trigger(
                            rx.text("Europe", class_name="text-xs font-semibold"),
                            value="1",
                        ),
                        rx.tabs.trigger(
                            rx.text("Asia", class_name="text-xs font-semibold"),
                            value="2",
                        ),
                    ),
                    default_value="1",
                    id="transactions-tabs",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
        ),
        card.content(
            rx.tabs.root(
                rx.tabs.content(create_chart(EUROPE), value="1"),
                rx.tabs.content(create_chart(ASIA), value="2"),
                default_value="1",
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
