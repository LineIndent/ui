import reflex as rx

from app.engine.actions import (
    APPLY_BASE_CHARTS_JS,
    APPLY_BASE_PRIMARY_JS,
    APPLY_SEED_JS,
    SHUFFLE_JS,
    TOGGLE_DARK_JS,
    _apply_base_theme_js,
    _apply_chart_color_js,
    _apply_color_theme_js,
    _apply_font_js,
    _apply_style_js,
    _patch_radius_js,
)
from app.hooks import (
    base_theme_color,
    chart_color,
    copy_preset_value,
    seed,
    selected_base_color_cs,
    selected_chart_cs,
    selected_component_category,
    selected_font_cs,
    selected_radius_cs,
    selected_style_cs,
    selected_theme_cs,
    theme_color,
)
from app.registry.colors import COLOR_THEMES
from app.registry.fonts import FONT_REGISTRY
from app.registry.radii import RADIUS_OPTIONS
from app.registry.styles import STYLE_REGISTRY
from app.registry.themes import BASE_THEMES
from app.templates.compiler import theme_export_compiler
from app.templates.reset import reset_theme_button
from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.dialog import dialog
from components.ui.input import input
from components.ui.select import select


def radius_icon() -> rx.Component:
    return rx.html(
        """
        <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            class="text-foreground"
        >
            <path
                fill="none"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 20v-5C4 8.925 8.925 4 15 4h5"
            />
        </svg>
        """
    )


def style_icon() -> rx.Component:
    return rx.html(
        """
        <svg
            xmlns="http://www.w3.org/2000/svg"
            width="128"
            height="128"
            viewBox="0 0 24 24"
            fill="none"
            role="img"
            color="currentColor"
            class="size-4"
        >
            <path
                d="M2.5 12C2.5 7.52166 2.5 5.28249 3.89124 3.89124C5.28249 2.5 7.52166 2.5 12 2.5C16.4783 2.5 18.7175 2.5 20.1088 3.89124C21.5 5.28249 21.5 7.52166 21.5 12C21.5 16.4783 21.5 18.7175 20.1088 20.1088C18.7175 21.5 16.4783 21.5 12 21.5C7.52166 21.5 5.28249 21.5 3.89124 20.1088C2.5 18.7175 2.5 16.4783 2.5 12Z"
                stroke="currentColor"
                stroke-width="2"
            />
        </svg>
        """
    )


def component_panel(desktop: bool = True) -> rx.Component:
    return select.root(
        select.trigger(
            rx.el.div(
                rx.el.div(
                    rx.el.p("Components", class_name="text-muted-foreground text-xs"),
                    rx.el.p(select.value(), class_name="text-primary"),
                    class_name="flex flex-col items-start",
                ),
                hi("KeyframesMultipleIcon", class_name="size-5"),
                class_name="w-full flex flex-row justify-between items-center",
            ),
            class_name="w-full rounded-xl p-2 !bg-transparent hover:!bg-secondary",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        select.item(
                            select.item_text("All"),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value="All",
                            class_name=(
                                "w-full flex flex-row items-center justify-between rounded-lg"
                            ),
                            on_click=selected_component_category.set_value("All"),
                        ),
                        select.item(
                            select.item_text("Tech"),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value="Tech",
                            class_name=(
                                "w-full flex flex-row items-center justify-between rounded-lg"
                            ),
                            on_click=selected_component_category.set_value("Tech"),
                        ),
                        select.item(
                            select.item_text("General"),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value="General",
                            class_name=(
                                "w-full flex flex-row items-center justify-between rounded-lg"
                            ),
                            on_click=selected_component_category.set_value("General"),
                        ),
                        select.item(
                            select.item_text("Healthcare"),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value="Healthcare",
                            class_name=(
                                "w-full flex flex-row items-center justify-between rounded-lg"
                            ),
                            on_click=selected_component_category.set_value(
                                "Healthcare"
                            ),
                        ),
                        select.item(
                            select.item_text("Finance"),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value="Finance",
                            class_name=(
                                "w-full flex flex-row items-center justify-between rounded-lg"
                            ),
                            on_click=selected_component_category.set_value("Finance"),
                        ),
                        select.item(
                            select.item_text("Charts"),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value="Charts",
                            class_name=(
                                "w-full flex flex-row items-center justify-between rounded-lg"
                            ),
                            on_click=selected_component_category.set_value("Charts"),
                        ),
                        class_name="p-1",
                    ),
                    class_name="rounded-xl border-0 dark bg-card/90 backdrop-blur-xl w-[250px]"
                    if desktop
                    else "rounded-xl border-0 dark bg-card/90 backdrop-blur-xl",
                ),
                side_offset=25,
                side="right" if desktop else "top",
                align="start",
                class_name="" if desktop else "w-full pl-3 pr-5",
            ),
        ),
        name="component_select",
        value=selected_component_category.value,
        on_value_change=selected_component_category.set_value,
    )


def menu_panel(desktop: bool = True) -> rx.Component:
    return select.root(
        select.trigger(
            rx.el.p("Menu", class_name="text-primary"),
            hi("EqualSignIcon", class_name="size-5"),
            class_name="w-full rounded-xl p-2 !bg-transparent hover:!bg-secondary",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        select.item(
                            select.item_text("Open Preset"),
                            on_click=rx.call_script(
                                "document.getElementById('preset-trigger-btn')?.click()"
                            ),
                        ),
                        select.item(
                            select.item_text("Shuffle"),
                            on_click=rx.call_script(SHUFFLE_JS),
                        ),
                        select.item(
                            select.item_text("Light/Dark"),
                            on_click=rx.call_script(TOGGLE_DARK_JS),
                        ),
                        select.separator(),
                        select.item(reset_theme_button()),
                        class_name="p-1",
                    ),
                    class_name="rounded-xl border-0 dark bg-card/90 backdrop-blur-xl "
                    + "w-[250px]"
                    if desktop
                    else "",
                ),
                side_offset=25,
                side="right" if desktop else "top",
                align="start",
                class_name="" if desktop else "w-full",
            ),
        ),
        name="menu_panel",
        default_value="Medium",
    )


def style_panel(desktop: bool = True) -> rx.Component:
    return select.root(
        select.trigger(
            rx.el.div(
                rx.el.div(
                    rx.el.p("Style", class_name="text-muted-foreground text-xs"),
                    rx.el.p(select.value(), class_name="text-primary"),
                    class_name="flex flex-col items-start",
                ),
                style_icon(),
                class_name="w-full flex flex-row justify-between items-center",
            ),
            class_name="w-full rounded-xl p-2 !bg-transparent hover:!bg-secondary",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        *[
                            select.item(
                                select.item_text(s["label"]),
                                select.item_indicator(
                                    hi("Tick02Icon", class_name="size-4")
                                ),
                                value=s["label"],
                                class_name=(
                                    "w-full flex flex-row items-center justify-between rounded-lg"
                                ),
                                on_click=rx.call_script(_apply_style_js(s["id"])),
                            )
                            for s in STYLE_REGISTRY
                        ],
                        class_name="p-1",
                    ),
                    class_name="rounded-xl border-0 dark bg-card/90 backdrop-blur-xl w-[250px]"
                    if desktop
                    else "rounded-xl border-0 dark bg-card/90 backdrop-blur-xl",
                ),
                side_offset=25,
                side="right" if desktop else "top",
                align="start",
                class_name="" if desktop else "w-full pl-3 pr-5",
            ),
        ),
        name="style_select",
        value=selected_style_cs.value,
        on_value_change=selected_style_cs.set_value,
    )


def font_panel(desktop: bool = True) -> rx.Component:
    categories = {"sans": "Sans Serif", "serif": "Serif", "mono": "Monospace"}

    return select.root(
        select.trigger(
            rx.el.div(
                rx.el.div(
                    rx.el.p("Font Family", class_name="text-muted-foreground text-xs"),
                    rx.el.p(select.value(), class_name="text-primary"),
                    class_name="flex flex-col items-start",
                ),
                hi("TextFontIcon", class_name="size-4"),
                class_name="w-full flex flex-row justify-between items-center",
            ),
            class_name="w-full rounded-xl p-2 !bg-transparent hover:!bg-secondary",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    *[
                        select.group(
                            select.group_label(
                                categories[cat_id],
                                class_name="text-[10px] font-semibold uppercase",
                            ),
                            *[
                                select.item(
                                    select.item_text(f["label"]),
                                    select.item_indicator(
                                        hi("Tick02Icon", class_name="size-4")
                                    ),
                                    value=f["label"],
                                    class_name="w-full flex flex-row items-center justify-between rounded-lg px-2 py-1.5 text-sm cursor-pointer hover:bg-accent hover:text-accent-foreground",
                                    on_click=rx.call_script(_apply_font_js(f["id"])),
                                )
                                for f in FONT_REGISTRY
                                if f.get("category") == cat_id
                            ],
                            class_name="p-1",
                        )
                        for cat_id in categories
                    ],
                    class_name="h-[40vh] overflow-y-auto rounded-xl border-0 dark bg-card/90 backdrop-blur-xl w-[250px] scrollbar-none"
                    if desktop
                    else "h-[40vh] overflow-y-auto rounded-xl border-0 dark bg-card/90 backdrop-blur-xl scrollbar-none",
                ),
                side_offset=25,
                side="right" if desktop else "top",
                align="start",
                class_name="" if desktop else "w-full pl-3 pr-5",
            ),
        ),
        name="font_select",
        value=selected_font_cs.value,
        on_value_change=selected_font_cs.set_value,
    )


def base_color_panel(desktop: bool = True) -> rx.Component:
    rows = [BASE_THEMES[i : i + 3] for i in range(0, len(BASE_THEMES), 3)]

    return select.root(
        select.trigger(
            rx.el.div(
                rx.el.div(
                    rx.el.p("Base Color", class_name="text-muted-foreground text-xs"),
                    rx.el.p(select.value(), class_name="text-primary"),
                    class_name="flex flex-col items-start",
                ),
                rx.el.div(
                    style={"backgroundColor": base_theme_color.value},
                    class_name="size-4 rounded-full",
                ),
                class_name="w-full flex flex-row justify-between items-center",
            ),
            class_name="w-full rounded-xl p-2 !bg-transparent hover:!bg-secondary",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        *[
                            select.item(
                                select.item_text(t["label"]),
                                select.item_indicator(
                                    hi("Tick02Icon", class_name="size-4")
                                ),
                                value=t["label"],
                                class_name=(
                                    "w-full flex flex-row items-center justify-between rounded-lg"
                                ),
                                on_click=[
                                    base_theme_color.set_value(t["light"]["ring"]),
                                    selected_base_color_cs.set_value(t["label"]),
                                    rx.call_script(_apply_base_theme_js(t["id"])),
                                ],
                            )
                            for row in rows
                            for t in row
                        ],
                        class_name="p-1",
                    ),
                    class_name="rounded-xl border-0 dark bg-card/90 backdrop-blur-xl w-[250px]"
                    if desktop
                    else "rounded-xl border-0 dark bg-card/90 backdrop-blur-xl",
                ),
                side_offset=25,
                side="right" if desktop else "top",
                align="start",
                class_name="" if desktop else "w-full pl-3 pr-5",
            ),
        ),
        name="base_color_select",
        value=selected_base_color_cs.value,
        on_value_change=selected_base_color_cs.set_value,
    )


def theme_panel(desktop: bool = True) -> rx.Component:
    # rows = [COLOR_THEMES[i : i + 3] for i in range(0, len(COLOR_THEMES), 3)]

    sorted_themes = sorted(COLOR_THEMES, key=lambda x: x["label"])

    rows = [sorted_themes[i : i + 3] for i in range(0, len(sorted_themes), 3)]

    return select.root(
        select.trigger(
            rx.el.div(
                rx.el.div(
                    rx.el.p("Theme", class_name="text-muted-foreground text-xs"),
                    rx.el.p(
                        rx.cond(
                            theme_color.value,
                            select.value(),
                            selected_base_color_cs.value,
                        ),
                        class_name="text-primary",
                    ),
                    class_name="flex flex-col items-start",
                ),
                rx.el.div(
                    style={
                        "backgroundColor": rx.cond(
                            theme_color.value, theme_color.value, base_theme_color.value
                        )
                    },
                    class_name="size-4 rounded-full",
                ),
                class_name="w-full flex flex-row justify-between items-center",
            ),
            class_name="w-full rounded-xl p-2 !bg-transparent hover:!bg-secondary",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        select.item(
                            select.item_text(selected_base_color_cs.value),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value=selected_base_color_cs.value,
                            class_name=(
                                "w-full flex flex-row items-center justify-between rounded-lg"
                            ),
                            on_click=[
                                theme_color.set_value(""),
                                rx.call_script(APPLY_BASE_PRIMARY_JS),
                            ],
                        ),
                        select.separator(),
                        *[
                            select.item(
                                select.item_text(t["label"]),
                                select.item_indicator(
                                    hi("Tick02Icon", class_name="size-4")
                                ),
                                value=t["label"],
                                class_name=(
                                    "w-full flex flex-row items-center justify-between rounded-lg"
                                ),
                                on_click=[
                                    theme_color.set_value(t["light"]["primary"]),
                                    rx.call_script(_apply_color_theme_js(t["id"])),
                                ],
                            )
                            for row in rows
                            for t in row
                        ],
                        class_name="p-1",
                    ),
                    class_name="rounded-xl border-0 dark bg-card/90 backdrop-blur-xl w-[250px]"
                    if desktop
                    else "rounded-xl border-0 dark bg-card/90 backdrop-blur-xl",
                ),
                side_offset=25,
                side="right" if desktop else "top",
                align="start",
                class_name="" if desktop else "w-full pl-3 pr-5",
            ),
        ),
        name="theme_panel",
        value=selected_theme_cs.value,
        on_value_change=selected_theme_cs.set_value,
    )


def chart_color_panel(desktop: bool = True) -> rx.Component:
    # rows = [COLOR_THEMES[i : i + 3] for i in range(0, len(COLOR_THEMES), 3)]

    sorted_themes = sorted(COLOR_THEMES, key=lambda x: x["label"])

    rows = [sorted_themes[i : i + 3] for i in range(0, len(sorted_themes), 3)]

    return select.root(
        select.trigger(
            rx.el.div(
                rx.el.div(
                    rx.el.p("Chart Color", class_name="text-muted-foreground text-xs"),
                    rx.el.p(
                        rx.cond(
                            chart_color.value,
                            select.value(),
                            selected_base_color_cs.value,
                        ),
                        class_name="text-primary",
                    ),
                    class_name="flex flex-col items-start",
                ),
                rx.el.div(
                    style={
                        "backgroundColor": rx.cond(
                            chart_color.value, chart_color.value, base_theme_color.value
                        )
                    },
                    class_name="size-4 rounded-full",
                ),
                class_name="w-full flex flex-row justify-between items-center",
            ),
            class_name="w-full rounded-xl p-2 !bg-transparent hover:!bg-secondary",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        select.item(
                            select.item_text(selected_base_color_cs.value),
                            select.item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            value=selected_base_color_cs.value,
                            class_name=(
                                "w-full flex flex-row items-center justify-between rounded-lg"
                            ),
                            on_click=[
                                chart_color.set_value(""),
                                rx.call_script(APPLY_BASE_CHARTS_JS),
                            ],
                        ),
                        select.separator(),
                        *[
                            select.item(
                                select.item_text(t["label"]),
                                select.item_indicator(
                                    hi("Tick02Icon", class_name="size-4")
                                ),
                                value=t["label"],
                                class_name=(
                                    "w-full flex flex-row items-center justify-between rounded-lg"
                                ),
                                on_click=[
                                    chart_color.set_value(t["light"]["primary"]),
                                    rx.call_script(_apply_chart_color_js(t["id"])),
                                ],
                            )
                            for row in rows
                            for t in row
                        ],
                        class_name="p-1",
                    ),
                    class_name="rounded-xl border-0 dark bg-card/90 backdrop-blur-xl w-[250px]"
                    if desktop
                    else "rounded-xl border-0 dark bg-card/90 backdrop-blur-xl",
                ),
                side_offset=25,
                side="right" if desktop else "top",
                align="start",
                class_name="" if desktop else "w-full pl-3 pr-5",
            ),
        ),
        name="chart_color_panel",
        value=selected_chart_cs.value,
        on_value_change=selected_chart_cs.set_value,
    )


def radius_panel(desktop: bool = True) -> rx.Component:
    return select.root(
        select.trigger(
            rx.el.div(
                rx.el.div(
                    rx.el.p("Radius", class_name="text-muted-foreground text-xs"),
                    rx.el.p(select.value(), class_name="text-primary"),
                    class_name="flex flex-col items-start",
                ),
                radius_icon(),
                class_name="w-full flex flex-row justify-between items-center",
            ),
            class_name="w-full rounded-xl p-2 !bg-transparent hover:!bg-secondary",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        *[
                            select.item(
                                select.item_text(label),
                                select.item_indicator(
                                    hi("Tick02Icon", class_name="size-4")
                                ),
                                value=label,
                                class_name=(
                                    "w-full flex flex-row items-center justify-between rounded-lg"
                                ),
                                on_click=rx.call_script(_patch_radius_js(value)),
                            )
                            for label, value in RADIUS_OPTIONS
                        ],
                        class_name="p-1",
                    ),
                    class_name="rounded-xl border-0 dark bg-card/90 backdrop-blur-xl w-[250px]"
                    if desktop
                    else "rounded-xl border-0 dark bg-card/90 backdrop-blur-xl",
                ),
                side_offset=25,
                side="right" if desktop else "top",
                align="start",
                class_name="" if desktop else "w-full pl-3 pr-5",
            ),
        ),
        name="radius_select",
        value=selected_radius_cs.value,
    )


def shuffle_button() -> rx.Component:
    return button(
        "Shuffle",
        variant="outline",
        class_name="w-full rounded-xl !bg-transparent hover:!bg-secondary",
        on_click=rx.call_script(SHUFFLE_JS),
    )


def preset_copy_button() -> rx.Component:
    return button(
        rx.cond(
            copy_preset_value.value,
            "Copied",
            f"--preset {seed.value}",
        ),
        variant="outline",
        class_name="w-full rounded-xl !bg-transparent hover:!bg-secondary",
        on_click=[
            rx.call_function(copy_preset_value.set_value(True)),
            rx.set_clipboard(f"{seed.value}"),
        ],
        on_mouse_down=rx.call_function(copy_preset_value.set_value(False)).debounce(
            1500
        ),
    )


def open_preset_menu() -> rx.Component:
    return dialog.root(
        dialog.trigger(
            button(
                "Open Preset",
                variant="outline",
                class_name="w-full rounded-xl !bg-transparent hover:!bg-secondary",
                id="preset-trigger-btn",
            ),
            class_name="w-full",
        ),
        dialog.portal(
            dialog.backdrop(class_name="backdrop-blur-[5px]"),
            dialog.popup(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Open Theme Preset",
                            class_name="text-foreground text-sm font-normal",
                        ),
                        rx.el.p(
                            "Paste a preset ID to load a theme configuration.",
                            class_name="text-muted-foreground text-sm font-light",
                        ),
                        class_name="w-full flex flex-col gap-y-1",
                    ),
                    input(
                        placeholder="ex: b2D0wqNxT",
                        id="seed-input-el",
                        class_name="rounded-lg text-foreground",
                    ),
                    rx.el.div(
                        dialog.close(
                            button("Cancel", variant="outline", class_name="w-full"),
                            class_name="flex-1",
                        ),
                        dialog.close(
                            button(
                                "Open",
                                class_name="w-full",
                                on_click=rx.call_script(APPLY_SEED_JS),
                            ),
                            class_name="flex-1",
                        ),
                        class_name="flex flex-row gap-x-6",
                    ),
                    class_name="flex flex-col gap-y-4 w-full",
                ),
                class_name="!w-full max-w-sm rounded-2xl dark bg-card p-5 flex flex-col",
            ),
        ),
    )


def get_code_menu() -> rx.Component:
    return theme_export_compiler()
