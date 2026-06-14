import reflex as rx

from components.ui.card import card

data = [
    {"browser": "chrome", "visitors": 275, "fill": "var(--chart-1)"},
    {"browser": "safari", "visitors": 200, "fill": "var(--chart-2)"},
    {"browser": "firefox", "visitors": 187, "fill": "var(--chart-3)"},
    {"browser": "edge", "visitors": 173, "fill": "var(--chart-4)"},
    {"browser": "other", "visitors": 90, "fill": "var(--chart-5)"},
]


def doughnutchart_v1():

    return card.root(
        card.header(
            card.title("Doughnut Chart"),
            card.description("Browser distribution - Last 6 months"),
        ),
        card.content(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.foreach(
                        [1, 2, 3, 4, 5],
                        lambda color, index: rx.recharts.cell(
                            fill=f"var(--chart-{index + 1})",
                        ),
                    ),
                    data=data,
                    data_key="visitors",
                    name_key="browser",
                    inner_radius=60,
                    stroke_width=5,
                    stroke="var(--background)",
                    is_animation_active=False,
                    custom_attrs={"paddingAngle": 3, "cornerRadius": 5},
                ),
                width="100%",
                height=220,
            ),
            rx.el.div(
                rx.foreach(
                    ["chrome", "safari", "firefox", "edge", "other"],
                    lambda browser, index: rx.el.div(
                        rx.el.div(
                            class_name=f"w-3 h-3 rounded-sm bg-chart-{index + 1}"
                        ),
                        rx.el.p(
                            browser,
                            class_name="text-sm font-semibold text-foreground capitalize",
                        ),
                        class_name="flex flex-row gap-x-2 items-center",
                    ),
                ),
                class_name="w-full flex flex-row flex-wrap gap-2 items-center justify-center",
            ),
            class_name="flex flex-col h-[250px] items-center",
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
