from components.icons.hugeicon import hi
from components.ui.select import select


def select_groups():
    fruits = [
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]

    vegetables = [
        {"label": "Carrot", "value": "carrot"},
        {"label": "Broccoli", "value": "broccoli"},
        {"label": "Spinach", "value": "spinach"},
    ]

    return select.root(
        select.trigger(
            select.value(),
            select.icon(
                # hi("ArrowDown01Icon", classs_name="size-4"),
            ),
            class_name="w-full max-w-48 flex items-center justify-between",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        select.group_label("Fruits"),
                        *[
                            select.item(
                                select.item_text(item["label"]),
                                select.item_indicator(
                                    # hi("Tick02Icon", class_name="size-4")
                                ),
                                value=item["value"],
                                class_name="flex flex-row items-center justify-between",
                            )
                            for item in fruits
                        ],
                    ),
                    select.separator(),
                    select.group(
                        select.group_label("Vegetables"),
                        *[
                            select.item(
                                select.item_text(item["label"]),
                                select.item_indicator(
                                    # hi("Tick02Icon", class_name="size-4")
                                ),
                                value=item["value"],
                                class_name="flex flex-row items-center justify-between",
                            )
                            for item in vegetables
                        ],
                    ),
                ),
            ),
        ),
        items=[*fruits, *vegetables],
        name="select_groups",
        default_value="banana",
    )
