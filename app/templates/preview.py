import reflex as rx

from app.examples.components import (
    card_eight,
    card_eighteen,
    card_eleven,
    card_fifteen,
    card_five,
    card_four,
    card_fourteen,
    card_nine,
    card_nineteen,
    card_one,
    card_seven,
    card_seventeen,
    card_six,
    card_sixteen,
    card_ten,
    card_thirteen,
    card_three,
    card_twelve,
    card_twenty,
    card_twenty_eight,
    card_twenty_five,
    card_twenty_four,
    card_twenty_nine,
    card_twenty_one,
    card_twenty_seven,
    card_twenty_six,
    card_twenty_three,
    card_twenty_two,
    card_two,
)
from app.examples.utils import masonry_card
from app.hooks import theme
from app.www.library.charts.bar.v1 import barchart_v1
from app.www.library.charts.doughnut.v1 import doughnutchart_v1
from app.www.library.charts.line.v8 import linechart_v8


@masonry_card(label="Charts")
def line_chart():
    return linechart_v8()


@masonry_card(label="Charts")
def doughnut_chart():
    return doughnutchart_v1()


@masonry_card(label="Charts")
def bar_chart():
    return barchart_v1()


def preview() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        card_ten(),
                        card_fourteen(),
                        bar_chart(),
                        card_six(),
                        card_thirteen(),
                        card_sixteen(),
                        card_eleven(),
                        doughnut_chart(),
                        card_four(),
                        card_twelve(),
                        card_eight(),
                        card_seven(),
                        line_chart(),
                        card_nineteen(),
                        card_eighteen(),
                        card_twenty(),
                        card_seventeen(),
                        card_fifteen(),
                        card_nine(),
                        card_five(),
                        card_three(),
                        card_two(),
                        card_one(),
                        card_twenty_six(),
                        card_twenty_three(),
                        card_twenty_five(),
                        card_twenty_eight(),
                        card_twenty_nine(),
                        card_twenty_one(),
                        card_twenty_seven(),
                        card_twenty_two(),
                        card_twenty_four(),
                        class_name=" ".join(
                            [
                                "mx-auto",
                                "columns-1",
                                "sm:columns-3",
                                "md:columns-3",
                                "lg:columns-4",
                                "gap-10",
                                "space-y-10",
                            ]
                        ),
                    ),
                    class_name="sm:min-w-[1600px] w-full",
                ),
                class_name="w-full h-full border-1 border-input/90 rounded-2xl p-4 md:p-10 bg-secondary dark:bg-transparent overflow-auto scrollbar-none",
            ),
            class_name="w-full h-full",
        ),
        class_name="w-full flex-[2] min-h-0 order-first lg:order-none lg:flex-1 lg:min-w-0 lg:h-full",
        style=theme.value.to(dict),
    )
