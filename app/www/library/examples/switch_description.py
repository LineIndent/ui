import reflex as rx

from components.ui.field import field
from components.ui.switch import switch


def switch_description() -> rx.Component:
    return field.root(
        field.content(
            field.label("Share across devices", html_for="switch-focus-mode"),
            field.description(
                "Focus is shared across devices, and turns off when you leave the app."
            ),
        ),
        switch.root(
            switch.thumb(),
            id="switch-focus-mode",
        ),
        orientation="horizontal",
        class_name="max-w-sm px-2",
    )
