import reflex as rx


def table_list():
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "Character",
                        class_name="border border-input px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    rx.el.th(
                        "Role",
                        class_name="border border-input px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    class_name="m-0 border-t border-input p-0 even:bg-muted",
                )
            ),
            rx.el.tbody(
                rx.el.tr(
                    rx.el.td(
                        "Frodo",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    rx.el.td(
                        "Ring Bearer",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    class_name="m-0 border-t border-input p-0 even:bg-muted",
                ),
                rx.el.tr(
                    rx.el.td(
                        "Gandlaf",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    rx.el.td(
                        "The Grey / White Wizard",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    class_name="m-0 border-t border-input p-0 even:bg-muted",
                ),
                rx.el.tr(
                    rx.el.td(
                        "Legolas",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    rx.el.td(
                        "Elven archer",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    class_name="m-0 border-t border-input p-0 even:bg-muted",
                ),
            ),
            class_name="w-full",
        ),
        class_name="my-6 w-full overflow-y-auto",
    )
