import reflex as rx
from reflex.experimental import ClientStateVar

from components.icons.hugeicon import hi
from components.ui.select import select
from components.ui.switch import switch

align_with_item_trigger = ClientStateVar.create("align_with_item_trigger", False)

items = ["apple", "banana", "orange", "grape", "blueberry", "pineapple"]


def select_align_with_items():

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p("Align Item", class_name="font-medium text-foreground"),
                rx.el.p(
                    "Toggle to align the item with the trigger.",
                    class_name="text-muted-foreground",
                ),
                class_name="flex flex-col gap-y-2 text-sm",
            ),
            switch.root(
                switch.thumb(),
                on_checked_change=align_with_item_trigger.set_value(
                    ~align_with_item_trigger.value
                ),
            ),
            class_name="flex flex-row items-start justify-between w-full",
        ),
        select.root(
            select.trigger(
                select.value(),
                select.icon(hi("ArrowDown01Icon", classs_name="size-4")),
                class_name="w-full flex items-center justify-between group",
            ),
            select.portal(
                select.positioner(
                    select.popup(
                        select.group(
                            select.group_label("Fruit"),
                            *[
                                select.item(
                                    select.item_text(fruit.capitalize()),
                                    select.item_indicator(
                                        hi("Tick02Icon", class_name="size-4")
                                    ),
                                    value=fruit,
                                    class_name="w-full !max-w-sm flex flex-row items-center justify-between",
                                )
                                for fruit in items
                            ],
                        ),
                    ),
                    side_offset=4,
                    align_item_with_trigger=align_with_item_trigger.value,
                ),
            ),
            name="example_select",
            default_value="blueberry",
        ),
        class_name="flex flex-col gap-y-4 max-w-sm",
    )
