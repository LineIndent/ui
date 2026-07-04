import reflex as rx
from reflex.experimental import ClientStateVar

from components.ui.button import button
from components.ui.card import card

selected_card_spacing = ClientStateVar.create("selected_card_spacing", "4")

spacing_options = [
    {
        "class_name": "[--card-spacing:--spacing(4)]",
        "label": "16px",
        "value": "4",
    },
    {
        "class_name": "[--card-spacing:--spacing(5)]",
        "label": "20px",
        "value": "5",
    },
    {
        "class_name": "[--card-spacing:--spacing(6)]",
        "label": "24px",
        "value": "6",
    },
    {
        "class_name": "[--card-spacing:--spacing(8)]",
        "label": "32px",
        "value": "8",
    },
]


def card_spacing() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            *[
                button(
                    item["label"],
                    variant="outline",
                    size="sm",
                    class_name=rx.cond(
                        selected_card_spacing.value == item["value"], "!bg-muted", ""
                    ),
                    on_click=selected_card_spacing.set_value(item["value"]),
                )
                for item in spacing_options
            ],
            class_name="flex gap-1 justify-start items-center w-full",
        ),
        card.root(
            card.header(
                card.title("Login to your account"),
                card.description("Enter your email below to login to your account"),
                card.action(
                    button("Sign Up", variant="link"),
                ),
            ),
            card.content(
                rx.el.form(
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Email",
                                html_for="email-spacing",
                                class_name="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                            ),
                            rx.el.input(
                                id="email-spacing",
                                type="email",
                                placeholder="m@example.com",
                                required=True,
                                class_name="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-sm shadow-xs transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium text-foreground placeholder:text-muted-foreground focus-visible:outline-hidden focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50",
                            ),
                            class_name="grid gap-2",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Password",
                                    html_for="password-spacing",
                                    class_name="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                                ),
                                rx.el.a(
                                    "Forgot your password?",
                                    href="#",
                                    class_name="ml-auto inline-block text-sm underline-offset-4 hover:underline",
                                ),
                                class_name="flex items-center",
                            ),
                            rx.el.input(
                                id="password-spacing",
                                type="password",
                                required=True,
                                class_name="flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-sm shadow-xs transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium text-foreground placeholder:text-muted-foreground focus-visible:outline-hidden focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50",
                            ),
                            class_name="grid gap-2",
                        ),
                        class_name="flex flex-col gap-6",
                    )
                )
            ),
            card.footer(
                button("Login", type="submit", class_name="w-full"),
                button("Login with Google", variant="outline", class_name="w-full"),
                class_name="flex-col gap-2",
            ),
            class_name=f"[--card-spacing:--spacing({selected_card_spacing.value})]",
        ),
        class_name="mx-auto grid w-full max-w-sm gap-4 my-10",
    )
