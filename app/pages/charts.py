import reflex as rx

from app.templates.layout import layout_decorator
from app.www.library.charts.area.v5 import areachart_v5
from app.www.library.charts.area.v9 import areachart_v9
from app.www.library.charts.bar.v1 import barchart_v1
from app.www.library.charts.bar.v5 import barchart_v5
from app.www.library.charts.bar.v9 import barchart_v9
from app.www.library.charts.doughnut.v1 import doughnutchart_v1
from app.www.library.charts.line.v5 import linechart_v5
from app.www.library.charts.line.v7 import linechart_v7
from app.www.library.charts.line.v8 import linechart_v8
from app.www.library.charts.pie.v1 import piechart_v1
from app.www.library.charts.radar.v6 import radar_v6
from app.www.library.charts.scatter.v1 import scatterchart_v1
from components.ui.button import button

GRID_LAYOUT = " ".join(
    [
        "grid grid-cols-1 lg:grid-cols-3",
        "divide-y lg:divide-y-0",
        "lg:divide-x",
        "divide-input/40",
        "border-x border-input/40",
    ]
)


@layout_decorator(
    title="Beautiful Charts & Graphs",
    description="A collection of ready-to-use chart components built with Recharts. From basic charts to rich data displays, copy and paste into your apps.",
    ctas=[
        rx.el.a(button("Chart Theme", size="sm"), href="#"),
        rx.el.a(button("Documentation", variant="secondary", size="sm"), href="#"),
    ],
)
def chart_page():
    return rx.el.div(
        areachart_v5(),
        rx.el.hr(class_name="border border-input/40"),
        rx.el.div(
            linechart_v8(),
            barchart_v1(),
            doughnutchart_v1(),
            class_name=GRID_LAYOUT,
        ),
        rx.el.hr(class_name="border border-input/40"),
        barchart_v5(),
        rx.el.hr(class_name="border border-input/40"),
        rx.el.div(
            areachart_v9(),
            radar_v6(),
            scatterchart_v1(),
            class_name=GRID_LAYOUT,
        ),
        rx.el.hr(class_name="border border-input/40"),
        linechart_v7(),
        rx.el.hr(class_name="border border-input/40"),
        rx.el.div(
            linechart_v5(),
            barchart_v9(),
            piechart_v1(),
            class_name=GRID_LAYOUT,
        ),
        rx.el.hr(class_name="border border-input/40"),
        class_name=" ".join(
            [
                "max-w-[96rem] mx-auto px-0 md:px-6",
                "py-6 space-y-10",
            ]
        ),
    )
