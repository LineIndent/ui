import reflex as rx

from components.ui.button import button
from components.ui.checkbox import checkbox
from components.ui.field import field
from components.ui.input import input
from components.ui.select import select
from components.ui.textarea import textarea

months = [
    {"label": "MM", "value": ""},
    {"label": "01", "value": "01"},
    {"label": "02", "value": "02"},
    {"label": "03", "value": "03"},
    {"label": "04", "value": "04"},
    {"label": "05", "value": "05"},
    {"label": "06", "value": "06"},
    {"label": "07", "value": "07"},
    {"label": "08", "value": "08"},
    {"label": "09", "value": "09"},
    {"label": "10", "value": "10"},
    {"label": "11", "value": "11"},
    {"label": "12", "value": "12"},
]

years = [
    {"label": "YYYY", "value": ""},
    {"label": "2024", "value": "2024"},
    {"label": "2025", "value": "2025"},
    {"label": "2026", "value": "2026"},
    {"label": "2027", "value": "2027"},
    {"label": "2028", "value": "2028"},
    {"label": "2029", "value": "2029"},
]


def field_demo() -> rx.Component:
    return rx.el.div(
        rx.el.form(
            field.group(
                field.set(
                    field.legend("Payment Method"),
                    field.description("All transactions are secure and encrypted"),
                    field.group(
                        field.root(
                            field.label("Name on Card", html_for="checkout-card-name"),
                            input(
                                id="checkout-card-name",
                                placeholder="Evil Rabbit",
                                required=True,
                            ),
                        ),
                        field.root(
                            field.label("Card Number", html_for="checkout-card-number"),
                            input(
                                id="checkout-card-number",
                                placeholder="1234 5678 9012 3456",
                                required=True,
                            ),
                            field.description("Enter your 16-digit card number"),
                        ),
                        rx.el.div(
                            field.root(
                                field.label("Month", html_for="checkout-exp-month"),
                                select.root(
                                    select.trigger(
                                        select.value(),
                                        select.icon(),
                                        id="checkout-exp-month",
                                    ),
                                    select.portal(
                                        select.positioner(
                                            select.popup(
                                                select.group(
                                                    *[
                                                        select.item(
                                                            select.item_text(
                                                                item["label"]
                                                            ),
                                                            select.item_indicator(),
                                                            value=item["value"],
                                                        )
                                                        for item in months
                                                    ]
                                                )
                                            )
                                        )
                                    ),
                                    items=months,
                                    default_value="MM",
                                ),
                            ),
                            field.root(
                                field.label("Year", html_for="checkout-exp-year"),
                                select.root(
                                    select.trigger(
                                        select.value(),
                                        select.icon(),
                                        id="checkout-exp-year",
                                    ),
                                    select.portal(
                                        select.positioner(
                                            select.popup(
                                                select.group(
                                                    *[
                                                        select.item(
                                                            select.item_text(
                                                                item["label"]
                                                            ),
                                                            select.item_indicator(),
                                                            value=item["value"],
                                                        )
                                                        for item in years
                                                    ]
                                                )
                                            )
                                        )
                                    ),
                                    items=years,
                                    default_value="YYYY",
                                ),
                            ),
                            field.root(
                                field.label("CVV", html_for="checkout-cvv"),
                                input(
                                    id="checkout-cvv",
                                    placeholder="123",
                                    required=True,
                                ),
                            ),
                            class_name="grid grid-cols-3 gap-4",
                        ),
                    ),
                ),
                field.separator(),
                field.set(
                    field.legend("Billing Address"),
                    field.description(
                        "The billing address associated with your payment method"
                    ),
                    field.group(
                        field.root(
                            checkbox.root(
                                checkbox.indicator(),
                                id="checkout-same-as-shipping",
                                default_checked=True,
                            ),
                            field.label(
                                "Same as shipping address",
                                html_for="checkout-same-as-shipping",
                                class_name="font-normal",
                            ),
                            orientation="horizontal",
                        )
                    ),
                ),
                field.set(
                    field.group(
                        field.root(
                            field.label("Comments", html_for="checkout-comments"),
                            textarea(
                                id="checkout-comments",
                                placeholder="Add any additional comments",
                                class_name="resize-none",
                            ),
                        )
                    )
                ),
                field.root(
                    button("Submit", type="submit"),
                    button("Cancel", variant="outline", type="button"),
                    orientation="horizontal",
                ),
            )
        ),
        class_name="w-full max-w-md my-10",
    )
