import reflex as rx
from reflex.experimental import ClientStateVar

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.button_group import button_group
from components.ui.input import input
from components.ui.select import select

selected_currency = ClientStateVar.create("selected_currency", "$")

currencies = [
    {"label": "US Dollar", "value": "$"},
    {"label": "Euro", "value": "€"},
    {"label": "British Pound", "value": "£"},
]


def button_group_select() -> rx.Component:

    return button_group.root(
        button_group.root(
            select.root(
                select.trigger(
                    selected_currency.value,
                    select.icon(),
                    class_name="flex items-center gap-1",
                ),
                select.portal(
                    select.positioner(
                        select.popup(
                            select.group(
                                *[
                                    select.item(
                                        select.item_text(
                                            item["value"],
                                            " ",
                                            rx.el.span(
                                                item["label"],
                                                class_name="text-xs !text-muted-foreground",
                                            ),
                                            class_name="text-sm text-foreground",
                                        ),
                                        select.item_indicator(),
                                        value=item["value"],
                                        class_name="flex flex-row items-center justify-between",
                                    )
                                    for item in currencies
                                ]
                            ),
                        ),
                        align="start",
                    ),
                ),
                items=currencies,
                value=selected_currency.value,
                on_value_change=selected_currency.set_value,
                name="currency_select",
            ),
            input(placeholder="10.00", pattern="[0-9]*"),
        ),
        button_group.root(
            button(
                hi("ArrowRight01Icon"),
                aria_label="Send",
                size="icon",
                variant="outline",
            )
        ),
    )
