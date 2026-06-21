import reflex as rx

from components.ui.frame import frame


def frame_basic():
    return frame.root(
        frame.header(
            frame.title("Section header"),
            frame.description("Description for the section"),
        ),
        frame.panel(
            rx.el.h2("Separated Panel", class_name="text-sm font-semibold"),
            rx.el.p("Section description", class_name="text-muted-foreground text-sm"),
        ),
        frame.panel(
            rx.el.h2("Separated Panel", class_name="text-sm font-semibold"),
            rx.el.p("Section description", class_name="text-muted-foreground text-sm"),
        ),
        class_name="w-full max-w-md",
    )
