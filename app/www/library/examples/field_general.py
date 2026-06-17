import reflex as rx

from components.ui.button import button
from components.ui.checkbox import checkbox
from components.ui.field import field
from components.ui.input import input
from components.ui.textarea import textarea


def field_demo() -> rx.Component:
    return rx.el.div(
        rx.el.form(
            rx.el.div(
                rx.el.fieldset(
                    rx.el.legend("Payment Method", class_name="font-medium mb-1"),
                    rx.el.p(
                        "All transactions are secure and encrypted",
                        class_name="text-sm text-muted-foreground mb-4",
                    ),
                    rx.el.div(
                        field.root(
                            field.label("Name on Card", html_for="name"),
                            field.control(
                                render_=input(
                                    id="name",
                                    placeholder="Evil Rabbit",
                                    class_name="!w-full",
                                ),
                                class_name="w-full",
                            ),
                            orientation="vertical",
                        ),
                        field.root(
                            field.label("Card Number", html_for="card"),
                            field.control(
                                render_=rx.el.div(
                                    input(
                                        id="card",
                                        placeholder="1234 5678 9012 3456",
                                        class_name="!w-full",
                                    ),
                                    class_name="w-full flex-1",
                                ),
                                class_name="w-full",
                            ),
                            field.description("Enter your 16-digit card number"),
                            orientation="vertical",
                        ),
                        class_name="flex flex-col w-full gap-y-2",
                    ),
                ),
                rx.el.fieldset(
                    rx.el.legend("Billing Address", class_name="font-medium mb-2"),
                    rx.el.p(
                        "The billing address associated with your payment method",
                        class_name="text-sm text-muted-foreground mb-3",
                    ),
                    field.root(
                        field.control(render_=checkbox()),
                        field.label(
                            "Same as shipping address",
                            html_for="shipping",
                            class_name="text-sm",
                        ),
                        orientation="horizontal",
                    ),
                ),
                field.root(
                    field.label("Comments", html_for="comments"),
                    field.control(
                        render_=textarea(
                            id="comments",
                            placeholder="Add any additional comments",
                            class_name="resize-none",
                        )
                    ),
                    orientation="vertical",
                ),
                field.root(
                    rx.el.div(
                        button("Submit", type="submit"),
                        button("Cancel", variant="outline", type="button"),
                        class_name="flex flex-row gap-x-4",
                    ),
                    orientation="horizontal",
                ),
                class_name="w-full flex flex-col gap-y-4",
            ),
            class_name="w-full flex",
        ),
        class_name="w-full max-w-md py-4",
    )
