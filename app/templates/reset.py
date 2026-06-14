import reflex as rx

from app.engine.actions import RESET_JS
from app.hooks import selected_component_category
from components.ui.button import button
from components.ui.dialog import dialog


def reset_theme_button() -> rx.Component:
    """Reset theme button with confirmation dialog."""
    return dialog.root(
        dialog.trigger(
            rx.el.p("Reset", class_name="text-start"),
            class_name="w-full",
        ),
        dialog.portal(
            dialog.backdrop(class_name="backdrop-blur-[5px]"),
            dialog.popup(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Reset Theme",
                            class_name="text-foreground text-sm font-normal",
                        ),
                        rx.el.p(
                            "Are you sure you want to reset to the default theme? This will clear all your current customizations.",
                            class_name="text-muted-foreground text-sm font-light",
                        ),
                        class_name="w-full flex flex-col gap-y-1",
                    ),
                    rx.el.div(
                        dialog.close(
                            button("Cancel", variant="outline", class_name="w-full"),
                            class_name="flex-1",
                        ),
                        dialog.close(
                            button(
                                "Reset",
                                variant="destructive",
                                class_name="w-full",
                                on_click=[
                                    rx.call_script(RESET_JS),
                                    selected_component_category.set_value("All"),
                                ],
                            ),
                            class_name="flex-1",
                        ),
                        class_name="flex flex-row gap-x-6",
                    ),
                    class_name="flex flex-col gap-y-4 w-full",
                ),
                class_name="!w-full max-w-sm rounded-2xl dark bg-card p-5 flex flex-col",
            ),
        ),
    )
