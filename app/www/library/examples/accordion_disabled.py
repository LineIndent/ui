import reflex as rx

from components.ui.accordion import accordion


def accordion_disabled() -> rx.Component:
    return accordion.root(
        accordion.item(
            accordion.trigger("Can I access my account history?"),
            accordion.panel(
                "Yes, you can view your complete account history including all "
                "transactions, plan changes, and support tickets in the Account "
                "History section of your dashboard."
            ),
            value="item-1",
        ),
        accordion.item(
            accordion.trigger("Premium feature information"),
            accordion.panel(
                "This section contains information about premium features. "
                "Upgrade your plan to access this content."
            ),
            value="item-2",
            disabled=True,
        ),
        accordion.item(
            accordion.trigger("How do I update my email address?"),
            accordion.panel(
                "You can update your email address in your account settings. "
                "You'll receive a verification email at your new address to "
                "confirm the change."
            ),
            value="item-3",
        ),
        class_name="max-w-sm",
    )
