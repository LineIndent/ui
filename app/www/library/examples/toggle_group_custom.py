import reflex as rx
from reflex.experimental import ClientStateVar

from components.ui.field import field
from components.ui.toggle_group import toggle_group

font_weight = ClientStateVar.create("font_weight_selector", "normal")


def toggle_group_custom() -> rx.Component:

    return field.set(
        field.root(
            field.label("Font Weight"),
            toggle_group.root(
                toggle_group.item(
                    rx.el.span("Aa", class_name="text-2xl leading-none font-light"),
                    rx.el.span("Light", class_name="text-xs text-muted-foreground"),
                    value="light",
                    aria_label="Light",
                    class_name="flex !size-16 flex-col items-center justify-center rounded-xl",
                ),
                toggle_group.item(
                    rx.el.span("Aa", class_name="text-2xl leading-none font-normal"),
                    rx.el.span("Normal", class_name="text-xs text-muted-foreground"),
                    value="normal",
                    aria_label="Normal",
                    class_name="flex !size-16 flex-col items-center justify-center rounded-xl",
                ),
                toggle_group.item(
                    rx.el.span("Aa", class_name="text-2xl leading-none font-medium"),
                    rx.el.span("Medium", class_name="text-xs text-muted-foreground"),
                    value="medium",
                    aria_label="Medium",
                    class_name="flex !size-16 flex-col items-center justify-center rounded-xl",
                ),
                toggle_group.item(
                    rx.el.span("Aa", class_name="text-2xl leading-none font-bold"),
                    rx.el.span("Bold", class_name="text-xs text-muted-foreground"),
                    value="bold",
                    aria_label="Bold",
                    class_name="flex !size-16 flex-col items-center justify-center rounded-xl",
                ),
                on_value_change=font_weight.set_value,
                variant="outline",
                spacing=2,
                size="lg",
            ),
            field.description(
                "Use ",
                rx.el.code(
                    f"font-{font_weight.value}",
                    class_name="rounded-md bg-muted px-1 py-0.5 font-mono",
                ),
                " to set the font weight.",
            ),
        )
    )
