import reflex as rx

from components.ui.frame import frame


def frame_no_border():
    return frame.root(
        frame.header(
            frame.title("No Outer Border"),
            frame.description(
                "This frame uses variant='ghost' to remove the outer border."
            ),
        ),
        frame.panel(
            rx.el.p(
                "The outer container of this frame has no border, only the background and panels are visible.",
                class_name="text-muted-foreground text-sm",
            ),
        ),
        stacked=True,
        dense=True,
        variant="ghost",
        class_name="w-full max-w-md",
    )
