import reflex as rx

from components.ui.card import card

data = [
    {"browser": "chrome", "visitors": 275},
    {"browser": "safari", "visitors": 200},
    {"browser": "firefox", "visitors": 187},
    {"browser": "edge", "visitors": 173},
    {"browser": "other", "visitors": 90},
]


def piechart_v4():

    return card.root(
        card.header(
            card.title("Pie Chart - Legend"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.foreach(
                        range(5),
                        lambda color, index: rx.recharts.cell(
                            fill=f"var(--chart-{index + 1})",
                        ),
                    ),
                    data=data,
                    data_key="visitors",
                    name_key="browser",
                    stroke_width=2,
                    stroke="var(--background)",
                    is_animation_active=False,
                ),
                rx.recharts.legend(class_name="text-xs font-medium"),
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
        class_name="w-full p-0",
    )
