import functools

import reflex as rx

from app.hooks import selected_component_category


def masonry_card(func=None, *, label="General"):
    """
    Decorator to wrap a component function inside a standard
    masonry-compatible div container with conditional visibility.
    """
    if func is None:
        return functools.partial(masonry_card, label=label)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inner_component = func(*args, **kwargs)

        return rx.el.div(
            inner_component,
            class_name=" ".join(
                [
                    "break-inside-avoid",
                    "w-full",
                    "bg-card",
                    "rounded-radius",
                    "border",
                    "border-input",
                    "p-card",
                    "flex flex-col",
                ]
            )
            + rx.cond(
                (selected_component_category.value == "All")
                | (selected_component_category.value == label),
                " flex",
                " hidden",
            ).to(str),
        )

    return wrapper
