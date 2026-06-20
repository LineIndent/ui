import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content

data = [
    {"month": "Jan", "desktop": 186, "mobile": 80},
    {"month": "Feb", "desktop": 305, "mobile": 200},
    {"month": "Mar", "desktop": 237, "mobile": 120},
    {"month": "Apr", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "Jun", "desktop": 214, "mobile": 140},
]


def chart_example_with_custom_legends():

    return rx.el.div(
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                horizontal=True, vertical=False, class_name="opacity-30"
            ),
            rx.recharts.bar(
                data_key="desktop",
                fill="var(--chart-1)",
                radius=4,
                is_animation_active=False,
            ),
            rx.recharts.bar(
                data_key="mobile",
                fill="var(--chart-2)",
                radius=4,
                is_animation_active=False,
            ),
            rx.recharts.x_axis(
                data_key="month",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            chart_tooltip(),
            data=data,
            width="100%",
            height=250,
            class_name=chart_tooltip_content(2, "square"),
        ),
        rx.el.div(
            rx.foreach(
                ["Desktop", "Mobile"],
                lambda device, index: rx.el.div(
                    rx.el.div(class_name=f"h-3 w-3 rounded-sm bg-chart-{index + 1}"),
                    rx.el.p(device, class_name="text-xs text-foreground"),
                    class_name="flex flex-row items-center gap-x-2",
                ),
            ),
            class_name="flex items-center gap-4 justify-center",
        ),
        class_name="w-full",
    )
