import reflex as rx

from app.examples.utils import block_card
from app.templates.layout import layout_decorator
from app.www.library.blocks.bar_chart_01 import bar_chart_01
from app.www.library.blocks.bar_chart_02 import bar_chart_02
from app.www.library.blocks.bar_chart_03 import bar_chart_03
from app.www.library.blocks.line_chart_01 import line_chart_01
from app.www.library.blocks.line_chart_02 import line_chart_02
from app.www.library.blocks.line_chart_03 import line_chart_03
from components.ui.button import button

GRID_LAYOUT = " ".join(
    [
        "grid grid-cols-1 lg:grid-cols-2",
        "divide-y lg:divide-y-0",
        "lg:divide-x",
        "[&>div]:p-4 items-stretch",
        "divide-input/60",
        "border-x border-input/40",
    ]
)


@layout_decorator(
    title="Building Blocks for Dashboards",
    description="Clean, modern building blocks for Reflex dashboards. Copy and paste into your apps. Open Source. Extensible.",
    ctas=[
        rx.el.a(
            button("Create Your Own", size="sm"),
            href="/create",
        ),
        rx.el.a(
            button("View Components", variant="secondary", size="sm"),
            href="/components",
        ),
    ],
)
def blocks_page():
    return rx.el.div(
        rx.el.div(
            block_card(bar_chart_01)(),
            block_card(bar_chart_02)(),
            class_name=GRID_LAYOUT,
        ),
        rx.el.hr(class_name="border border-input/40"),
        block_card(bar_chart_03)(),
        rx.el.hr(class_name="border border-input/40"),
        rx.el.div(
            block_card(line_chart_01)(),
            block_card(line_chart_02)(),
            class_name=GRID_LAYOUT,
        ),
        block_card(line_chart_03)(),
        # rx.el.div(barchart_v5(), class_name="w-full p-7"),
        # rx.el.hr(class_name="border border-input/40"),
        # rx.el.div(
        #     areachart_v9(), radar_v6(), scatterchart_v1(), class_name=GRID_LAYOUT
        # ),
        # rx.el.hr(class_name="border border-input/40"),
        # rx.el.div(linechart_v7(), class_name="w-full p-7"),
        # rx.el.hr(class_name="border border-input/40"),
        # rx.el.div(linechart_v5(), barchart_v9(), piechart_v1(), class_name=GRID_LAYOUT),
        # rx.el.hr(class_name="border border-input/40"),
        class_name=" ".join(
            [
                "max-w-[96rem] mx-auto px-0 md:px-8",
                "py-6 space-y-10",
            ]
        ),
    )
