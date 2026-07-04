import reflex as rx
from reflex.experimental import ClientStateVar

from components.icons.hugeicon import hi
from components.ui.input_group import input_group

_input_copy = ClientStateVar.create("_input_copy", False)
_input_star = ClientStateVar.create("_input_star", False)


def input_group_button() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(
                placeholder="https://ui.buridan.dev/",
                read_only=True,
            ),
            input_group.addon(
                input_group.button(
                    rx.cond(
                        _input_copy.value,
                        hi("Tick02Icon"),
                        hi("Copy01Icon"),
                    ),
                    aria_label="Copy",
                    title="Copy",
                    size="icon-xs",
                    on_click=[
                        _input_copy.set_value(True),
                        rx.set_clipboard("https://ui.buridan.dev/"),
                    ],
                    on_mouse_down=rx.call_function(
                        _input_copy.set_value(False)
                    ).debounce(1500),
                ),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.addon(
                input_group.button(
                    hi("InformationCircleIcon"),
                    variant="secondary",
                    size="icon-xs",
                ),
                align="inline-start",
            ),
            input_group.addon(
                "https://",
                class_name="pl-1.5 text-muted-foreground",
                align="inline-start",
            ),
            input_group.input(id="input-secure-19"),
            input_group.addon(
                input_group.button(
                    hi(
                        "StarIcon",
                        class_name=rx.cond(
                            _input_star.value,
                            "text-blue-600 fill-blue-600",
                            "",
                        ),
                    ),
                    size="icon-xs",
                    on_click=_input_star.set_value(~_input_star.value),
                ),
                align="inline-end",
            ),
            class_name="[--radius:9999px]",
        ),
        input_group.root(
            input_group.input(placeholder="Type to search..."),
            input_group.addon(
                input_group.button(
                    "Search",
                    variant="secondary",
                ),
                align="inline-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-6",
    )
