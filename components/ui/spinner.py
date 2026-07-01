import reflex as rx
from reflex_components_core.el import svg

from ..utils.twmerge import cn


def spinner(class_name: str = "", **props) -> rx.Component:
    return svg(
        svg.path(
            d="M21.9961 12C21.9961 17.5228 17.5189 22 11.9961 22C6.47325 22 1.99609 17.5228 1.99609 12C1.99609 6.47715 6.47325 2 11.9961 2",
        ),
        xmlns="http://www.w3.org/2000/svg",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="1.5",
        stroke_linecap="round",
        class_name=cn("size-4 animate-spin", class_name),
        data_slot="spinner",
        role="status",
        **props,
    )
