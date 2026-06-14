import reflex as rx

from app.hooks import welcome_open
from components.ui.button import button
from components.ui.dialog import dialog


def welcome_dialog() -> rx.Component:
    """A welcome dialog that shows on first visit."""

    # Script to mark welcome as seen in localStorage and close state
    close_script = """
        localStorage.setItem("has_seen_welcome", "true");
        if (refs['_client_state_setWelcome_open']) refs['_client_state_setWelcome_open'](false);
    """

    return dialog.root(
        dialog.portal(
            dialog.backdrop(class_name="backdrop-blur-[5px]"),
            dialog.popup(
                rx.el.div(
                    rx.el.image(
                        src="/logo.webp",
                        class_name="w-full h-56 object-cover rounded-t-xl",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Build your theme system for Reflex",
                            class_name="text-foreground text-md font-medium",
                        ),
                        rx.el.p(
                            "Customize everything from the ground up. Pick your font, color scheme, and more.",
                            class_name="text-foreground text-sm font-light",
                        ),
                        rx.el.p(
                            "Based on the popular shadcn/ui.",
                            class_name="text-foreground text-sm font-light",
                        ),
                        class_name="w-full flex flex-col gap-y-2 px-3",
                    ),
                    rx.el.div(
                        button(
                            "Get Started",
                            class_name="w-full",
                            on_click=rx.call_script(close_script),
                        ),
                        class_name="w-full pt-2 dark px-3 pb-3",
                    ),
                    class_name="flex flex-col gap-y-4 w-full",
                ),
                class_name="!w-full max-w-sm rounded-2xl dark bg-card p-1.5 flex flex-col overflow-hidden",
            ),
        ),
        open=welcome_open.value,
        on_open_change=rx.call_script(close_script),
    )
