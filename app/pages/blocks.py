import reflex as rx

from app.examples.utils import block_card
from app.hooks import selected_blocks_category
from app.templates.layout import layout_decorator
from app.www.library.blocks.area_chart_01 import area_chart_01
from app.www.library.blocks.area_chart_02 import area_chart_02
from app.www.library.blocks.bar_chart_01 import bar_chart_01
from app.www.library.blocks.bar_chart_02 import bar_chart_02
from app.www.library.blocks.bar_chart_03 import bar_chart_03
from app.www.library.blocks.bar_chart_04 import bar_chart_04
from app.www.library.blocks.kpi_card_01 import kpi_card_01
from app.www.library.blocks.kpi_card_02 import kpi_card_02
from app.www.library.blocks.line_chart_01 import line_chart_01
from app.www.library.blocks.line_chart_02 import line_chart_02
from app.www.library.blocks.line_chart_03 import line_chart_03
from app.www.library.blocks.line_chart_04 import line_chart_04
from components.ui.button import BUTTON_VARIANTS, button

BLOCKS = [
    {"name": "All", "value": "all"},
    {"name": "Bar Charts", "value": "bar"},
    {"name": "Line Charts", "value": "line"},
    {"name": "Area Charts", "value": "area"},
    {"name": "KPI Cards", "value": "kpi"},
]


@layout_decorator(
    title="Building Blocks for Dashboards",
    description="Clean, modern building blocks for Reflex dashboards. Copy and paste into your apps. Open Source. Extensible.",
    ctas=[
        rx.el.a(button("Create Your Own"), href="/create"),
        rx.el.a(button("View Components", variant="secondary"), href="/components"),
    ],
)
def blocks_page():
    return rx.el.div(
        rx.el.div(
            *[
                button(
                    item["name"],
                    size="sm",
                    on_click=selected_blocks_category.set_value(item["value"]),
                    class_name="transition-none "
                    + rx.cond(
                        selected_blocks_category.value == item["value"],
                        BUTTON_VARIANTS["variant"]["default"],
                        BUTTON_VARIANTS["variant"]["outline"],
                    ).to(str),
                )
                for item in BLOCKS
            ],
            class_name="w-full max-w-7xl mx-auto flex flex-row flex-wrap gap-4 items-center justify-center sm:justify-start p-7",
        ),
        block_card(func=bar_chart_01, label="bar")(),
        block_card(func=bar_chart_02, label="bar")(),
        block_card(func=bar_chart_03, label="bar")(),
        block_card(func=bar_chart_04, label="bar")(),
        block_card(func=line_chart_01, label="line")(),
        block_card(func=line_chart_02, label="line")(),
        block_card(func=line_chart_03, label="line")(),
        block_card(func=line_chart_04, label="line")(),
        block_card(func=area_chart_01, label="area")(),
        block_card(func=area_chart_02, label="area")(),
        block_card(func=kpi_card_01, label="kpi")(),
        block_card(func=kpi_card_02, label="kpi")(),
        class_name=" ".join(
            [
                "w-full max-w-7xl mx-auto px-0",
                "divide-y divide-input/90",
                "py-6 space-y-10",
                "[&>*:first-child]:border-b-0",
            ]
        ),
    )
