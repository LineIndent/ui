import reflex as rx

from components.ui.accordion import accordion

items = [
    {
        "value": "notifications",
        "trigger": "Notification Settings",
        "content": (
            "Manage how you receive notifications. You can enable email alerts "
            "for updates or push notifications for mobile devices."
        ),
    },
    {
        "value": "privacy",
        "trigger": "Privacy & Security",
        "content": (
            "Control your privacy settings and security preferences. Enable "
            "two-factor authentication, manage connected devices, review active "
            "sessions, and configure data sharing preferences. You can also "
            "download your data or delete your account."
        ),
    },
    {
        "value": "billing",
        "trigger": "Billing & Subscription",
        "content": (
            "View your current plan, payment history, and upcoming invoices. "
            "Update your payment method, change your subscription tier, or "
            "cancel your subscription."
        ),
    },
]


def accordion_multiple() -> rx.Component:
    return accordion.root(
        *[
            accordion.item(
                accordion.trigger(item["trigger"]),
                accordion.panel(item["content"]),
                value=item["value"],
            )
            for item in items
        ],
        multiple=True,
        default_value=["notifications"],
        class_name="max-w-sm",
    )
