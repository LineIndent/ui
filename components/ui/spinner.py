"""Spinner component."""

import reflex as rx
from reflex_components_core.el import svg

from ..utils.twmerge import cn


def spinner(class_name: str = "", **props) -> rx.Component:
    incoming_attrs = props.pop("custom_attrs", {})

    base_attrs = {"viewBox": "0 0 16 16"}

    merged_attrs = {**base_attrs, **incoming_attrs}

    return svg(
        svg.path(
            opacity="0.2",
            d="M14.66 8a6.666 6.666 0 1 1-13.333 0 6.666 6.666 0 0 1 13.333 0Z",
            stroke="currentColor",
            stroke_width="1.5",
        ),
        svg.path(
            d="M13.413 11.877A6.666 6.666 0 1 1 10.26 1.728",
            stroke="currentColor",
            stroke_width="1.5",
        ),
        xmlns="http://www.w3.org/2000/svg",
        custom_attrs=merged_attrs,
        class_name=cn("size-4 animate-spin fill-none", class_name),
        data_slot="spinner",
        role="status",
        **props,
    )
