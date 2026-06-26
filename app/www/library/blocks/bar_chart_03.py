import reflex as rx
from reflex.experimental import ClientStateVar

from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
from components.ui.card import card

data = [
    {"date": "Jan 23", "Running": 167, "Cycling": 145},
    {"date": "Feb 23", "Running": 125, "Cycling": 110},
    {"date": "Mar 23", "Running": 156, "Cycling": 149},
    {"date": "Apr 23", "Running": 165, "Cycling": 112},
    {"date": "May 23", "Running": 153, "Cycling": 138},
    {"date": "Jun 23", "Running": 124, "Cycling": 145},
    {"date": "Jul 23", "Running": 164, "Cycling": 134},
    {"date": "Aug 23", "Running": 123, "Cycling": 110},
    {"date": "Sep 23", "Running": 132, "Cycling": 113},
    {"date": "Oct 23", "Running": 124, "Cycling": 129},
    {"date": "Nov 23", "Running": 149, "Cycling": 101},
    {"date": "Dec 23", "Running": 129, "Cycling": 109},
]

_running_avg = round(sum(d["Running"] for d in data) / len(data))
_cycling_avg = round(sum(d["Cycling"] for d in data) / len(data))
_overall_avg = round((_running_avg + _cycling_avg) / 2)

ShowRunning = ClientStateVar.create("show_running", True)
ShowCycling = ClientStateVar.create("show_cycling", True)
AvgBPM = ClientStateVar.create("avg_bpm", _overall_avg)


def _legend_item(label: str, color: str, is_active: ClientStateVar) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.el.span(class_name=f"size-3 rounded-sm {color}"),
            rx.el.p(label, class_name="text-sm text-muted-foreground"),
            class_name="flex items-center gap-1.5",
        ),
        on_click=is_active.set_value(~is_active.value),
        class_name=rx.cond(
            is_active.value,
            "text-left opacity-100 cursor-pointer",
            "text-left opacity-40 cursor-pointer",
        ),
    )


def _chart(show_y_axis: bool) -> rx.Component:
    return rx.recharts.bar_chart(
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
            width=30,
            tick_line=False,
            axis_line=False,
            tick_size=15,
            custom_attrs={"fontSize": "11px"},
            hide=not show_y_axis,
        ),
        rx.recharts.bar(
            data_key="Running",
            fill="var(--chart-2)",
            is_animation_active=False,
            class_name=rx.cond(ShowRunning.value, "opacity-100", "opacity-50").to(str),
        ),
        rx.recharts.bar(
            data_key="Cycling",
            fill="var(--chart-3)",
            is_animation_active=False,
            class_name=rx.cond(ShowCycling.value, "opacity-100", "opacity-50").to(str),
        ),
        data=data,
        width="100%",
        height=300,
    )


def bar_chart_03():
    return card.root(
        card.header(
            card.title("Average BPM"),
            rx.el.p(
                rx.cond(
                    ShowRunning.value & ShowCycling.value,
                    str(_overall_avg),
                    rx.cond(
                        ShowRunning.value,
                        str(_running_avg),
                        rx.cond(
                            ShowCycling.value,
                            str(_cycling_avg),
                            "0",
                        ),
                    ),
                ),
                "bpm",
                class_name="text-3xl font-bold",
            ),
        ),
        rx.el.ul(
            _legend_item("Running", "bg-chart-2", ShowRunning),
            _legend_item("Cycling", "bg-chart-3", ShowCycling),
            class_name="flex gap-10 items-center justify-end",
        ),
        card.content(
            rx.el.div(_chart(show_y_axis=False), class_name="sm:hidden"),
            rx.el.div(_chart(show_y_axis=True), class_name="hidden sm:block"),
        ),
        class_name=chart_tooltip_content([2, 3], "square") + " w-full p-0",
    )
