import reflex as rx

from components.ui.card import card

stats_data = [
    {"category": "Farming", "score": 7},
    {"category": "Fighting", "score": 6},
    {"category": "Aggressiveness", "score": 7},
    {"category": "Map Awareness", "score": 6},
    {"category": "Objective Control", "score": 6},
    {"category": "Positioning", "score": 7},
]


def radar_v6():

    return card.root(
        card.header(
            card.title("Radar Chart - Filled Grid"),
            card.description("Player performance across categories"),
        ),
        card.content(
            rx.recharts.radar_chart(
                rx.recharts.polar_grid(
                    grid_type="circle",
                    class_name="opacity-20 fill-primary stroke-input",
                ),
                rx.recharts.polar_angle_axis(
                    data_key="category",
                    axis_line_type="circle",
                    class_name="!text-xs stroke-input",
                ),
                rx.recharts.radar(
                    data_key="score",
                    dot=False,
                    fill="white",
                    stroke="none",
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
