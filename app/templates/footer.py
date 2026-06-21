import reflex as rx


def footer() -> rx.Component:
    return rx.el.p(
        rx.el.span(
            "Built by ",
            rx.el.a(
                "Line Indent",
                href="https://github.com/LineIndent",
                class_name="font-semibold underline",
            ),
            " at ",
            rx.el.a(
                "Reflex",
                href="https://reflex.dev",
                class_name="font-semibold underline",
            ),
        ),
        rx.el.span(
            ". The source code is available on ",
            rx.el.a(
                "GitHub",
                href="https://github.com/LineIndent/ui",
                class_name="font-semibold underline",
            ),
            ".",
            class_name="block sm:inline",
        ),
        class_name="w-full text-[13px] font-light",
    )
