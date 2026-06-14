import reflex as rx


def list():
    return rx.el.ul(
        rx.el.li("Not all those who wander are lost."),
        rx.el.li("Even darkness must pass."),
        rx.el.li("Courage will now be your best defence."),
        class_name="my-6 ml-6 list-disc [&>li]:mt-2",
    )
