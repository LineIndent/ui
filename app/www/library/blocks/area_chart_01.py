import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"date": "Jan 23", "Actual costs": 42340, "Potential costs": 32330},
    {"date": "Feb 23", "Actual costs": 50120, "Potential costs": 40100},
    {"date": "Mar 23", "Actual costs": 45190, "Potential costs": 38240},
    {"date": "Apr 23", "Actual costs": 56420, "Potential costs": 31200},
    {"date": "May 23", "Actual costs": 40420, "Potential costs": 34900},
    {"date": "Jun 23", "Actual costs": 47010, "Potential costs": 36800},
    {"date": "Jul 23", "Actual costs": 47490, "Potential costs": 34560},
    {"date": "Aug 23", "Actual costs": 39610, "Potential costs": 31260},
    {"date": "Sep 23", "Actual costs": 45860, "Potential costs": 29240},
    {"date": "Oct 23", "Actual costs": 50910, "Potential costs": 31220},
    {"date": "Nov 23", "Actual costs": 49190, "Potential costs": 33020},
    {"date": "Dec 23", "Actual costs": 55190, "Potential costs": 36090},
]

summary = [
    ("Actual costs", "$540,690", "chart-1"),
    ("Potential costs", "$422,300", "chart-2"),
    ("Potential savings (%)", "-21.9%", None),
    ("Potential savings ($)", "$118,390", None),
]


def _gradient(id_: str, color: str) -> rx.Component:
    return rx.el.svg.linear_gradient(
        rx.el.svg.stop(stop_color=f"var(--{color})", offset="5%", stop_opacity=0.2),
        rx.el.svg.stop(stop_color=f"var(--{color})", offset="95%", stop_opacity=0.2),
        x1=0,
        x2=0,
        y1=0,
        y2=1,
        id=id_,
    )


def _area(data_key: str, color: str) -> rx.Component:
    return rx.recharts.area(
        data_key=data_key,
        fill=f"url(#{data_key.replace(' ', '_')})",
        stroke=f"var(--{color})",
        stroke_width=2,
        is_animation_active=False,
        active_dot={"fill": f"var(--{color})", "stroke": f"var(--{color})"},
        dot=False,
    )


def _chart(show_y_axis: bool) -> rx.Component:
    return rx.recharts.area_chart(
        rx.el.svg.defs(
            _gradient("Actual_costs", "chart-1"),
            _gradient("Potential_costs", "chart-2"),
        ),
        chart_tooltip(),
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-50"
        ),
        rx.recharts.x_axis(
            data_key="date",
            tick_line=False,
            axis_line=False,
            interval="preserveStartEnd",
        ),
        rx.recharts.y_axis(
            width=55,
            tick_line=False,
            axis_line=False,
            hide=not show_y_axis,
        ),
        _area("Actual costs", "chart-1"),
        _area("Potential costs", "chart-2"),
        data=data,
        width="100%",
        height=288,
    )


def area_chart_01():
    return card.root(
        card.header(
            card.title("Actual costs vs. potential costs"),
            card.description(
                "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt."
            ),
        ),
        card.content(
            rx.el.ul(
                *[
                    rx.el.li(
                        rx.el.div(
                            rx.el.span(
                                class_name=f"w-1 h-6 shrink-0 rounded-sm bg-{color}"
                            )
                            if color
                            else None,
                            rx.el.p(total, class_name="text-lg font-semibold"),
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.p(
                            category,
                            class_name="text-sm text-muted-foreground "
                            + ("pl-3" if color else ""),
                        ),
                    )
                    for category, total, color in summary
                ],
                class_name="grid grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
            ),
            rx.el.div(_chart(show_y_axis=False), class_name="sm:hidden"),
            rx.el.div(_chart(show_y_axis=True), class_name="hidden sm:block"),
        ),
        class_name=chart_tooltip_content([1, 2], "square") + " w-full p-0",
    )
