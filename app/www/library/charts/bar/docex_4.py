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


def chart_example_with_custom_tooltip():

    return rx.recharts.bar_chart(
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
        class_name=chart_tooltip_content([1, 2], "square"),
    )
