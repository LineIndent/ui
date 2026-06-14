from components.ui.select import select


def select_with_scroll_arrows():
    north_america = [
        {"label": "Eastern Standard Time", "value": "est"},
        {"label": "Central Standard Time", "value": "cst"},
        {"label": "Mountain Standard Time", "value": "mst"},
        {"label": "Pacific Standard Time", "value": "pst"},
        {"label": "Alaska Standard Time", "value": "akst"},
        {"label": "Hawaii Standard Time", "value": "hst"},
    ]

    europe_africa = [
        {"label": "Greenwich Mean Time", "value": "gmt"},
        {"label": "Central European Time", "value": "cet"},
        {"label": "Eastern European Time", "value": "eet"},
        {"label": "Central Africa Time", "value": "cat"},
        {"label": "East Africa Time", "value": "eat"},
    ]

    asia = [
        {"label": "Moscow Time", "value": "msk"},
        {"label": "India Standard Time", "value": "ist"},
        {"label": "China Standard Time", "value": "cst_china"},
        {"label": "Japan Standard Time", "value": "jst"},
    ]

    return select.root(
        select.trigger(
            select.value(),
            select.icon(),
            class_name="w-full max-w-64 flex items-center justify-between",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.scroll_up_arrow(),
                    select.list(
                        select.group(
                            select.group_label("North America"),
                            *[
                                select.item(
                                    select.item_text(i["label"]),
                                    select.item_indicator(),
                                    value=i["value"],
                                )
                                for i in north_america
                            ],
                        ),
                        select.group(
                            select.group_label("Europe & Africa"),
                            *[
                                select.item(
                                    select.item_text(i["label"]),
                                    select.item_indicator(),
                                    value=i["value"],
                                )
                                for i in europe_africa
                            ],
                        ),
                        select.group(
                            select.group_label("Asia"),
                            *[
                                select.item(
                                    select.item_text(i["label"]),
                                    select.item_indicator(),
                                    value=i["value"],
                                )
                                for i in asia
                            ],
                        ),
                        class_name="max-h-64 overflow-y-auto",
                    ),
                    select.scroll_down_arrow(),
                ),
            ),
        ),
        items=[
            {"label": "Select timezone", "value": None},
            *north_america,
            *europe_africa,
            *asia,
        ],
        name="timezone_select",
        default_value="est",
    )
