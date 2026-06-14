import reflex as rx

from app.hooks import (
    base_theme_color,
    chart_color,
    copy_preset_value,
    css_output,
    darkmode,
    seed,
    selected_base_color_cs,
    selected_chart_cs,
    selected_font_cs,
    selected_radius_cs,
    selected_style_cs,
    selected_theme_cs,
    theme,
    theme_color,
    theme_export_method,
    theme_preset_option,
)
from app.templates.options import (
    base_color_panel,
    chart_color_panel,
    component_panel,
    font_panel,
    get_code_menu,
    menu_panel,
    open_preset_menu,
    preset_copy_button,
    radius_panel,
    shuffle_button,
    style_panel,
    theme_panel,
)


def sidebar_mobile() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(style_panel(desktop=False), class_name="p-3 w-[12rem] shrink-0"),
            rx.el.div(
                base_color_panel(desktop=False), class_name="p-3 w-[12rem] shrink-0"
            ),
            rx.el.div(theme_panel(desktop=False), class_name="p-3 w-[12rem] shrink-0"),
            rx.el.div(
                chart_color_panel(desktop=False), class_name="p-3 w-[12rem] shrink-0"
            ),
            rx.el.div(font_panel(desktop=False), class_name="p-3 w-[12rem] shrink-0"),
            rx.el.div(radius_panel(desktop=False), class_name="p-3 w-[12rem] shrink-0"),
            rx.el.div(
                component_panel(desktop=False), class_name="p-3 w-[12rem] shrink-0"
            ),
            class_name="flex flex-row overflow-x-auto scrollbar-none w-full min-w-0",
        ),
        rx.el.div(
            rx.el.div(preset_copy_button(), class_name="w-full sm:w-1/2 shrink-0"),
            rx.el.div(open_preset_menu(), class_name="w-full sm:w-1/3 shrink-0"),
            rx.el.div(shuffle_button(), class_name="w-full sm:w-1/3 shrink-0"),
            class_name="p-3 flex items-center gap-3 bg-secondary/50 border-t border-input/90 overflow-x-auto whitespace-nowrap scrollbar-none",
        ),
        class_name="flex lg:hidden w-full h-auto !overflow-hidden flex flex-col border border-input/90 text-sm text-card-foreground dark isolate rounded-2xl bg-card/90",
    )


def sidebar_desktop() -> rx.Component:
    return rx.el.aside(
        rx.el.div(menu_panel(), class_name="p-3 sticky top-0"),
        rx.el.div(
            rx.el.div(style_panel(), class_name="flex flex-col gap-y-3 p-3"),
            rx.el.div(
                base_color_panel(),
                theme_panel(),
                chart_color_panel(),
                class_name="flex flex-col gap-y-3 p-3",
            ),
            rx.el.div(font_panel(), class_name="flex flex-col gap-y-3 p-3"),
            rx.el.div(radius_panel(), class_name="flex flex-col gap-y-3 p-3"),
            rx.el.div(component_panel(), class_name="flex flex-col gap-y-3 p-3"),
            class_name="flex-1 min-h-0 overflow-y-auto scrollbar-none divide-y divide-input",
        ),
        rx.el.div(
            preset_copy_button(),
            open_preset_menu(),
            shuffle_button(),
            class_name="p-3 flex-shrink-0 flex flex-col gap-y-3 bg-secondary/50",
        ),
        rx.el.div(get_code_menu(), class_name="p-3 flex-shrink-0 bg-secondary/50"),
        class_name="hidden lg:flex w-full max-w-[12rem] shrink-0 !overflow-hidden flex-col border border-input/90 divide-y divide-input h-full text-sm text-card-foreground dark isolate rounded-2xl bg-card/90",
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        base_theme_color,
        chart_color,
        copy_preset_value,
        darkmode,
        seed,
        selected_base_color_cs,
        selected_chart_cs,
        selected_font_cs,
        selected_radius_cs,
        selected_style_cs,
        selected_theme_cs,
        theme,
        theme_color,
        theme_export_method,
        theme_preset_option,
        css_output,
        sidebar_mobile(),
        sidebar_desktop(),
        class_name="w-full flex-initial h-auto min-h-0 min-w-0 max-w-full lg:flex-1 lg:h-full lg:w-[12rem] lg:max-w-[12rem] lg:shrink-0",
    )
