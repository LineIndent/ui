import reflex as rx

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"date": "Jan 23", "Organic": 232, "Sponsored": 0},
    {"date": "Feb 23", "Organic": 241, "Sponsored": 0},
    {"date": "Mar 23", "Organic": 291, "Sponsored": 0},
    {"date": "Apr 23", "Organic": 101, "Sponsored": 0},
    {"date": "May 23", "Organic": 318, "Sponsored": 0},
    {"date": "Jun 23", "Organic": 205, "Sponsored": 0},
    {"date": "Jul 23", "Organic": 372, "Sponsored": 0},
    {"date": "Aug 23", "Organic": 341, "Sponsored": 0},
    {"date": "Sep 23", "Organic": 387, "Sponsored": 120},
    {"date": "Oct 23", "Organic": 220, "Sponsored": 0},
    {"date": "Nov 23", "Organic": 372, "Sponsored": 0},
    {"date": "Dec 23", "Organic": 321, "Sponsored": 0},
]

summary = [
    ("Organic", "3,273", "chart-1"),
    ("Sponsored", "120", "chart-2"),
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
        fill=f"url(#{data_key})",
        stroke=f"var(--{color})",
        stroke_width=2,
        is_animation_active=False,
        dot=False,
        active_dot={"fill": f"var(--{color})", "stroke": f"var(--{color})"},
    )


def _chart(show_y_axis: bool, start_end_only: bool = False) -> rx.Component:
    return rx.recharts.area_chart(
        rx.el.svg.defs(
            _gradient("Organic", "chart-1"),
            _gradient("Sponsored", "chart-2"),
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
            tick_count=2 if start_end_only else None,
            tick_size=15,
            custom_attrs={"fontSize": "11px"},
        ),
        rx.recharts.y_axis(
            width=30,
            tick_line=False,
            axis_line=False,
            tick_size=15,
            custom_attrs={"fontSize": "11px"},
            hide=not show_y_axis,
        ),
        _area("Organic", "chart-1"),
        _area("Sponsored", "chart-2"),
        data=data,
        width="100%",
        height=220,
    )


def area_chart_02():
    return card.root(
        card.header(
            card.title("Follower metrics"),
            card.description("More power? Upgrade to get more insights."),
        ),
        card.content(
            rx.el.div(
                _chart(show_y_axis=False, start_end_only=True), class_name="sm:hidden"
            ),
            rx.el.div(
                _chart(show_y_axis=True, start_end_only=False),
                class_name="hidden sm:block",
            ),
            rx.el.ul(
                *[
                    rx.el.li(
                        rx.el.div(
                            rx.el.span(class_name=f"h-0.5 w-3 bg-{color}"),
                            rx.el.span(label, class_name="text-sm"),
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.span(value, class_name="text-sm font-medium"),
                        class_name="flex items-center justify-between py-2 border-b border-input last:border-0",
                    )
                    for label, value, color in summary
                ],
                class_name="mt-4 w-full",
            ),
        ),
        class_name=chart_tooltip_content([1, 2], "square") + " w-full p-0",
    )
