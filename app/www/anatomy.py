# app/www/anatomy.py

ANATOMY = {
    "accordion": """accordion.root(
    accordion.item(
        accordion.header(
            accordion.trigger(),
        ),
        accordion.panel(),
    ),
    accordion.item(
        accordion.header(
            accordion.trigger(),
        ),
        accordion.panel(),
    ),
)""",
    "frame": """frame.root(
    frame.panel(
        frame.header(
            frame.title(),
            frame.description(),
        ),
        frame.footer(),
    ),
)""",
    "heatmap": """heatmap()""",
    "autocomplete": """autocomplete(
    items=[...],
)""",
    "avatar": """avatar.root(
    avatar.image(),
    avatar.fallback(),
)""",
    "badge": """badge()""",
    "breadcrumb": """breadcrumb(
    breadcrumb_list(
        breadcrumb_item(
            breadcrumb_link(),
        ),
        breadcrumb_separator(),
        breadcrumb_item(
            breadcrumb_page(),
        ),
    ),
)""",
    "button": """button()""",
    "card": """card.root(
    card.header(
        card.title(),
        card.description(),
    ),
    card.content(),
    card.footer(),
)""",
    "checkbox": """checkbox.root(
    checkbox.indicator(),
)""",
    "collapsible": """collapsible.root(
    collapsible.trigger(),
    collapsible.panel(),
)""",
    "context_menu": """context_menu.root(
    context_menu.trigger(),
    context_menu.portal(
        context_menu.positioner(
            context_menu.popup(
                context_menu.item(),
                context_menu.separator(),
                context_menu.group(
                    context_menu.group_label(),
                    context_menu.item(),
                ),
                context_menu.checkbox_item(
                    context_menu.checkbox_item_indicator(),
                ),
                context_menu.radio_group(
                    context_menu.radio_item(
                        context_menu.radio_item_indicator(),
                    ),
                ),
                context_menu.submenu_root(
                    context_menu.submenu_trigger(),
                    context_menu.portal(
                        context_menu.positioner(
                            context_menu.popup(),
                        ),
                    ),
                ),
            ),
        ),
    ),
)""",
    "dialog": """dialog.root(
    dialog.trigger(),
    dialog.portal(
        dialog.backdrop(),
        dialog.popup(
            dialog.title(),
            dialog.description(),
            dialog.close(),
        ),
    ),
)""",
    "input": """input()""",
    "input_group": """# Input with addons
input_with_addons(
    prefix=...,
    suffix=...,
)

# Textarea with footer
textarea_with_footer(
    footer_text=...,
)""",
    "kbd": """kbd()
# or
kbd_group(
    kbd(),
    kbd(),
)""",
    "link": """link()""",
    "marker": """marker.root(
    marker.icon(),
    marker.content(),
)
""",
    "spinner": """spinner()""",
    "menu": """menu.root(
    menu.trigger(),
    menu.portal(
        menu.positioner(
            menu.popup(
                menu.item(),
                menu.separator(),
                menu.group(
                    menu.group_label(),
                    menu.item(),
                ),
                menu.checkbox_item(
                    menu.checkbox_item_indicator(),
                ),
                menu.radio_group(
                    menu.radio_item(
                        menu.radio_item_indicator(),
                    ),
                ),
                menu.submenu_root(
                    menu.submenu_trigger(),
                    menu.portal(
                        menu.positioner(
                            menu.popup(),
                        ),
                    ),
                ),
            ),
        ),
    ),
)""",
    "metric": """metric(
    label=...,
    value=...,
    trend=...,
)""",
    "popover": """popover.root(
    popover.trigger(),
    popover.portal(
        popover.backdrop(),
        popover.positioner(
            popover.popup(
                popover.header(
                    popover.title(),
                    popover.description(),
                ),
                popover.close(),
            ),
        ),
    ),
)""",
    "scroll_area": """scroll_area.root(
    scroll_area.viewport(
        scroll_area.content(),
    ),
    scroll_area.scrollbar(
        scroll_area.thumb(),
    ),
    scroll_area.corner(),
)""",
    "select": """select.root(
    select.trigger(
        select.value(),
        select.icon(),
    ),
    select.portal(
        select.positioner(
            select.popup(
                select.group(
                    select.group_label(),
                    select.item(
                        select.item_text(),
                        select.item_indicator(),
                    ),
                ),
                select.separator(),
            ),
        ),
    ),
)""",
    "skeleton": """skeleton_component()""",
    "slider": """slider.root(
    slider.control(
        slider.track(
            slider.indicator(),
            slider.thumb(),
        ),
    ),
)""",
    "switch": """switch.root(
    switch.thumb(),
)""",
    "table": """table.root(
    table.header(
        table.row(
            table.head(),
        ),
    ),
    table.body(
        table.row(
            table.cell(),
        ),
    ),
    table.footer(),
    table.caption(),
)""",
    "tabs": """tabs.root(
    tabs.list(
        tabs.tab(),
        tabs.indicator(),
    ),
    tabs.panel(),
)""",
    "textarea": """textarea()""",
    "theme_switcher": """theme_switcher()""",
    "toggle": """toggle()""",
    "toggle_group": """toggle_group(
    toggle(),
    toggle(),
)""",
    "tooltip": """tooltip.root(
    tooltip.trigger(),
    tooltip.portal(
        tooltip.positioner(
            tooltip.popup(
                tooltip.arrow(),
                content=...,
            ),
        ),
    ),
)""",
    "field": """field.root(
    field.label(),
    field.control(),
    field.description(),
    field.item(),
    field.error(),
    field.validity(),
)
""",
    "timeline": """timeline.root(
    timeline.item(
        timeline.indicator(),
        timeline.separator(),
        timeline.header(
            timeline.date(),
            timeline.title(),
        ),
        timeline.content(),
    ),
)
""",
}
