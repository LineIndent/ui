import reflex as rx


def paragraph():
    return rx.el.p(
        "I have seen many an oak grow from acorn to ruinous age.",
        class_name="leading-7 [&:not(:first-child)]:mt-6",
    )
