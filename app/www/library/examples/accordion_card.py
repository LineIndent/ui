import reflex as rx

from components.ui.accordion import accordion
from components.ui.card import card

items = [
    {
        "value": "plans",
        "trigger": "What subscription plans do you offer?",
        "content": (
            "We offer three subscription tiers: Starter ($9/month), "
            "Professional ($29/month), and Enterprise ($99/month). Each plan "
            "includes increasing storage limits, API access, priority support, "
            "and team collaboration features."
        ),
    },
    {
        "value": "billing",
        "trigger": "How does billing work?",
        "content": (
            "Billing occurs automatically at the start of each billing cycle. "
            "We accept all major credit cards, PayPal, and ACH transfers for "
            "enterprise customers. You'll receive an invoice via email after "
            "each payment."
        ),
    },
    {
        "value": "cancel",
        "trigger": "How do I cancel my subscription?",
        "content": (
            "You can cancel your subscription anytime from your account "
            "settings. There are no cancellation fees or penalties. Your "
            "access will continue until the end of your current billing "
            "period."
        ),
    },
]


def accordion_card() -> rx.Component:
    return card.root(
        card.header(
            card.title("Subscription & Billing"),
            card.description(
                "Common questions about your account, plans, payments and "
                "cancellations."
            ),
        ),
        card.content(
            accordion.root(
                *[
                    accordion.item(
                        accordion.trigger(item["trigger"]),
                        accordion.panel(item["content"]),
                        value=item["value"],
                    )
                    for item in items
                ],
                default_value=["plans"],
            ),
        ),
        class_name="w-full max-w-sm",
    )
