from reflex.experimental import ClientStateVar

import app.utils.routes as routes

selected_base_color_cs = ClientStateVar.create("selected_base_color_cs", "Neutral")

base_theme_color = ClientStateVar.create("base_theme_color", "oklch(0.708 0 0)")

theme_color = ClientStateVar.create("theme_color", "")

chart_color = ClientStateVar.create("chart_color", "")

selected_theme_cs = ClientStateVar.create("selected_theme_cs", "Neutral")

selected_chart_cs = ClientStateVar.create("selected_chart_cs", "Neutral")

selected_style_cs = ClientStateVar.create("selected_style_cs", "Vega")

selected_font_cs = ClientStateVar.create("selected_font_cs", "Inter")

selected_radius_cs = ClientStateVar.create("selected_radius_cs", "Medium")


seed = ClientStateVar.create("seed", "")

darkmode = ClientStateVar.create("darkmode", False)

copy_preset_value = ClientStateVar.create("copy_preset_value", False)

theme_export_method = ClientStateVar.create("theme_export_method", "local")

theme_preset_option = ClientStateVar.create("theme_preset_option", "full")

css_output = ClientStateVar.create("cssoutput", "")

is_css_output_copied = ClientStateVar.create("is_css_output_copied", False)

is_rxconfig_copied = ClientStateVar.create("is_rxconfig_copied", False)

is_export_command_copied = ClientStateVar.create("is_export_command_copied", False)

welcome_open = ClientStateVar.create("welcome_open", False)

selected_component_category = ClientStateVar.create(
    "selected_component_category", "All"
)

selected_blocks_category = ClientStateVar.create("selected_blocks_category", "all")

search_items_cs = ClientStateVar.create(
    "search_items_cs",
    routes.GET_STARTED_URLS + routes.BASE_UI_COMPONENTS + routes.CHARTS_URLS,
)
