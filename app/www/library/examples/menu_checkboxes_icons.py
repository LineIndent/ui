import reflex as rx
from reflex.experimental import ClientStateVar

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.menu import menu

email_notif = ClientStateVar.create("email_notif", True)
sms_notif = ClientStateVar.create("sms_notif", False)
push_notif = ClientStateVar.create("push_notif", True)


def menu_checkboxes_icons() -> rx.Component:
    return menu.root(
        email_notif,
        sms_notif,
        push_notif,
        menu.trigger(
            render_=button("Notifications", variant="outline"),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("Notification Preferences"),
                        menu.checkbox_item(
                            hi("Mail01Icon"),
                            "Email notifications",
                            menu.checkbox_item_indicator(),
                            default_checked=email_notif.value,
                            on_checked_change=email_notif.set_value,
                        ),
                        menu.checkbox_item(
                            hi("Message01Icon"),
                            "SMS notifications",
                            menu.checkbox_item_indicator(),
                            default_checked=sms_notif.value,
                            on_checked_change=sms_notif.set_value,
                        ),
                        menu.checkbox_item(
                            hi("Notification01Icon"),
                            "Push notifications",
                            menu.checkbox_item_indicator(),
                            default_checked=push_notif.value,
                            on_checked_change=push_notif.set_value,
                        ),
                    ),
                    class_name="w-48",
                ),
            ),
        ),
    )
