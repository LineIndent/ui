import reflex as rx

from components.ui.field import field
from components.ui.switch import switch


def switch_choice_card() -> rx.Component:
    return field.group(
        field.label(
            field.root(
                field.content(
                    field.title("Share across devices"),
                    field.description(
                        "Focus is shared across devices, and turns off when you leave the app."
                    ),
                ),
                switch.root(id="switch-share"),
                orientation="horizontal",
            ),
            html_for="switch-share",
        ),
        field.label(
            field.root(
                field.content(
                    field.title("Enable notifications"),
                    field.description(
                        "Receive notifications when focus mode is enabled or disabled."
                    ),
                ),
                switch.root(id="switch-notifications", default_checked=True),
                orientation="horizontal",
            ),
            html_for="switch-notifications",
        ),
        class_name="w-full max-w-sm my-8",
    )
