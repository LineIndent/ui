import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"date": "Jan 23", "SolarPanels": 2890, "Inverters": 2338},
    {"date": "Feb 23", "SolarPanels": 2756, "Inverters": 2103},
    {"date": "Mar 23", "SolarPanels": 3322, "Inverters": 2194},
    {"date": "Apr 23", "SolarPanels": 3470, "Inverters": 2108},
    {"date": "May 23", "SolarPanels": 3475, "Inverters": 1812},
    {"date": "Jun 23", "SolarPanels": 3129, "Inverters": 1726},
    {"date": "Jul 23", "SolarPanels": 3490, "Inverters": 1982},
    {"date": "Aug 23", "SolarPanels": 2903, "Inverters": 2012},
    {"date": "Sep 23", "SolarPanels": 2643, "Inverters": 2342},
    {"date": "Oct 23", "SolarPanels": 2837, "Inverters": 2473},
    {"date": "Nov 23", "SolarPanels": 2954, "Inverters": 3848},
    {"date": "Dec 23", "SolarPanels": 3239, "Inverters": 3736},
]


def _chart(show_y_axis: bool) -> rx.Component:
    return rx.recharts.line_chart(
        chart_tooltip(),
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-50"
        ),
        rx.recharts.x_axis(
            data_key="date",
            tick_line=False,
            axis_line=False,
            tick_size=15,
            custom_attrs={"fontSize": "11px"},
            interval="preserveStartEnd",
        ),
        rx.recharts.y_axis(
            width=40,
            tick_line=False,
            axis_line=False,
            tick_size=15,
            custom_attrs={"fontSize": "11px"},
            hide=not show_y_axis,
        ),
        rx.recharts.line(
            data_key="SolarPanels",
            stroke="var(--chart-1)",
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-1)", "stroke": "var(--chart-1)"},
        ),
        rx.recharts.line(
            data_key="Inverters",
            stroke="var(--chart-2)",
            stroke_width=2,
            dot=False,
            is_animation_active=False,
            active_dot={"fill": "var(--chart-2)", "stroke": "var(--chart-2)"},
        ),
        data=data,
        width="100%",
        height=270,
    )


def line_chart_04():
    return card.root(
        card.header(
            card.title("Solar & Inverters"),
            card.description("Monthly spend category — Jan to Dec 23"),
        ),
        card.content(
            rx.el.div(
                # Y-axis label rotated on the left
                rx.el.p(
                    "Spend Category",
                    class_name="-rotate-90 text-xs text-muted-foreground whitespace-nowrap self-center h-fit w-[1rem]",
                ),
                # Chart
                rx.el.div(
                    rx.el.div(_chart(show_y_axis=False), class_name="sm:hidden"),
                    rx.el.div(_chart(show_y_axis=True), class_name="hidden sm:block"),
                    class_name="flex flex-col flex-1 min-w-0",
                ),
                class_name="flex flex-row gap-2 w-full",
            ),
            # X-axis label
            rx.el.p(
                "Month",
                class_name="text-xs text-muted-foreground text-center mt-1",
            ),
            # Legend
            rx.el.div(
                *[
                    rx.el.div(
                        rx.el.span(class_name=f"w-3 h-0.5 bg-chart-{i}"),
                        rx.el.span(label, class_name="text-sm text-muted-foreground"),
                        class_name="flex items-center gap-2",
                    )
                    for i, label in enumerate(["SolarPanels", "Inverters"], 1)
                ],
                class_name="mt-4 flex items-center justify-center gap-6",
            ),
            class_name="relative",
        ),
        class_name=chart_tooltip_content([1, 2], "line") + " w-full p-0",
    )
