import reflex as rx

from components.ui.card import card

stats_data = [
    {"category": "Farming", "score": 6, "average": 8},
    {"category": "Fighting", "score": 8, "average": 9},
    {"category": "Aggressiveness", "score": 5, "average": 8},
    {"category": "Map Awareness", "score": 9, "average": 9},
    {"category": "Objective Control", "score": 7, "average": 8},
    {"category": "Positioning", "score": 6, "average": 9},
]


def radar_v3():

    return card.root(
        card.header(
            card.title("Radar Chart - Stacked"),
            card.description("Comparing score against average"),
        ),
        card.content(
            rx.recharts.radar_chart(
                rx.recharts.polar_grid(class_name="opacity-30"),
                rx.recharts.polar_angle_axis(
                    data_key="category",
                    custom_attrs={"fontSize": "12px"},
                ),
                rx.recharts.radar(
                    data_key="average",
                    stroke="var(--chart-2)",
                    fill="var(--chart-2)",
                    fill_opacity=0.4,
                    is_animation_active=False,
                ),
                rx.recharts.radar(
                    data_key="score",
                    stroke="var(--chart-1)",
                    fill="var(--chart-1)",
                    fill_opacity=0.7,
                    is_animation_active=False,
                ),
                data=stats_data,
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
