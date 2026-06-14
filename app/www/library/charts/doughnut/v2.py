import reflex as rx

from components.ui.card import card

data = [
    {"browser": "chrome", "visitors": 275, "fill": "var(--chart-1)"},
    {"browser": "safari", "visitors": 200, "fill": "var(--chart-2)"},
    {"browser": "firefox", "visitors": 187, "fill": "var(--chart-3)"},
    {"browser": "edge", "visitors": 173, "fill": "var(--chart-4)"},
    {"browser": "other", "visitors": 90, "fill": "var(--chart-5)"},
]


def doughnutchart_v2():

    total_visitors = sum(item["visitors"] for item in data)

    return card.root(
        card.header(
            card.title("Doughnut Chart - Stacked"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        str(total_visitors),
                        class_name="text-3xl font-bold text-foreground",
                    ),
                    rx.el.p(
                        "Visitors",
                        class_name="text-xs text-muted-foreground",
                    ),
                    class_name="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 flex flex-col items-center justify-center",
                ),
                rx.recharts.pie_chart(
                    #
                    rx.recharts.pie(
                        data=data,
                        data_key="visitors",
                        name_key="browser",
                        inner_radius=60,
                        stroke_width=5,
                        stroke="var(--background)",
                        is_animation_active=False,
                    ),
                    width="100%",
                    height=250,
                ),
                class_name="relative w-full",
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
        # ,
        class_name="w-full p-0",
    )
