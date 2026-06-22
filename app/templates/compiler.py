import reflex as rx

from app.engine.actions import ADD_SWATCHES_JS, FORMAT_CSS_JS
from app.hooks import (
    css_output,
    is_css_output_copied,
    is_export_command_copied,
    is_rxconfig_copied,
    seed,
    theme_export_method,
    theme_preset_option,
)
from app.templates.config import rxconfig
from app.www.wrapper import styled_tab_trigger
from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.dialog import dialog
from components.ui.tabs import tabs

SYNC_BUTTON_STYLES_JS = """
    ({OPTIONS}).forEach(m => {
        const btn = document.getElementById('{BUTTON_PREFIX}-btn-' + m);
        const activeCheck = document.getElementById('{CHECK_ACTIVE_PREFIX}-' + m);
        const inactiveCheck = document.getElementById('{CHECK_INACTIVE_PREFIX}-' + m);

        if (!btn) return;

        if (m === {TARGET_VALUE}) {
            btn.classList.add('border-primary', 'dark:border-input', 'bg-secondary');
            btn.classList.remove('border-input/90');

            activeCheck?.classList.replace('hidden', 'flex');
            inactiveCheck?.classList.replace('block', 'hidden');
        } else {
            btn.classList.remove('border-primary', 'dark:border-input', 'bg-secondary');
            btn.classList.add('border-input/90');

            activeCheck?.classList.replace('flex', 'hidden');
            inactiveCheck?.classList.replace('hidden', 'block');
        }
    });
"""


def select_radio_option_row(
    title: str, description: str, group_name: str, value: str, default_on: bool = False
) -> rx.Component:
    return rx.el.label(
        rx.el.div(
            rx.el.p(title, class_name="text-foreground font-medium text-sm"),
            rx.el.p(
                description,
                class_name="text-muted-foreground max-w-[24rem] text-xs font-light leading-normal",
            ),
            class_name="flex flex-col gap-y-1",
        ),
        rx.el.div(
            rx.el.input(
                type="radio",
                name=group_name,
                value=value,
                default_checked=default_on,
                class_name="peer sr-only",
            ),
            rx.el.div(
                rx.el.span(
                    "✓",
                    class_name="text-primary-foreground text-[11px] font-bold hidden",
                ),
                class_name=(
                    "flex size-4 items-center justify-center rounded-[4px] transition-colors "
                    "border border-input bg-transparent "
                    "peer-checked:bg-primary peer-checked:border-primary "
                    "[&_span]:peer-checked:block"
                ),
            ),
            class_name="flex items-center",
        ),
        class_name=(
            "w-full rounded-2xl px-4 py-2.5 flex flex-row items-center justify-between "
            "text-left transition-all cursor-pointer border-1 "
            "border-input/90 bg-transparent hover:bg-secondary/20 "
            "has-[:checked]:border-primary has-[:checked]:dark:border-input has-[:checked]:bg-secondary/60"
        ),
    )


def select_local_or_reflex_build_option(
    title: str,
    description: str,
    method: str,
) -> rx.Component:

    sync_script = (
        SYNC_BUTTON_STYLES_JS.replace("{OPTIONS}", "['local', 'online']")
        .replace("{BUTTON_PREFIX}", "method")
        .replace("{CHECK_ACTIVE_PREFIX}", "method-checkmark-active")
        .replace("{CHECK_INACTIVE_PREFIX}", "method-checkmark-inactive")
        .replace("{TARGET_VALUE}", f"'{method}'")
    )

    click_script = f"""
        sessionStorage.setItem("theme_export_method", "{method}");
        refs['_client_state_setTheme_export_method']('{method}');
        {sync_script}
    """

    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(title, class_name="text-foreground font-medium text-sm"),
                    rx.el.p(
                        description,
                        class_name="text-muted-foreground max-w-[24rem] text-xs font-light leading-normal",
                    ),
                    class_name="flex flex-col gap-y-1",
                ),
                rx.el.div(
                    rx.el.div(class_name="size-0 rounded-[4px] bg-primary-foreground"),
                    id=f"method-checkmark-active-{method}",
                    class_name="size-4 rounded-[4px] bg-primary hidden items-center justify-center",
                ),
                rx.el.div(
                    id=f"method-checkmark-inactive-{method}",
                    class_name="size-4 rounded-[4px] border border-input block",
                ),
                class_name="flex flex-row w-full items-center justify-between",
            ),
            class_name="!w-full flex flex-col gap-y-1",
        ),
        id=f"method-btn-{method}",
        on_click=rx.call_script(click_script),
        class_name="w-full rounded-2xl px-4 py-2.5 text-left text-sm transition-all border-1 border-input/90 flex items-center",
    )


def select_preset_option(
    title: str,
    description: str,
    method: str,
) -> rx.Component:

    sync_script = (
        SYNC_BUTTON_STYLES_JS.replace("{OPTIONS}", "['full', 'theme']")
        .replace("{BUTTON_PREFIX}", "preset")
        .replace("{CHECK_ACTIVE_PREFIX}", "preset-checkmark-active")
        .replace("{CHECK_INACTIVE_PREFIX}", "preset-checkmark-inactive")
        .replace("{TARGET_VALUE}", f"'{method}'")
    )

    click_script = f"""
        sessionStorage.setItem("theme_preset_option", "{method}");
        refs['_client_state_setTheme_preset_option']('{method}');
        {sync_script}
    """

    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(title, class_name="text-foreground font-medium text-sm"),
                    rx.el.p(
                        description,
                        class_name="text-muted-foreground max-w-[24rem] text-xs font-light leading-normal",
                    ),
                    class_name="flex flex-col gap-y-1",
                ),
                rx.el.div(
                    rx.el.div(class_name="size-0 rounded-[4px] bg-primary-foreground"),
                    id=f"preset-checkmark-active-{method}",
                    class_name="size-4 rounded-[4px] bg-primary hidden items-center justify-center",
                ),
                rx.el.div(
                    id=f"preset-checkmark-inactive-{method}",
                    class_name="size-4 rounded-[4px] border border-input block",
                ),
                class_name="flex flex-row w-full items-center justify-between",
            ),
            class_name="!w-full flex flex-col gap-y-1",
        ),
        id=f"preset-btn-{method}",
        on_click=rx.call_script(click_script),
        class_name="w-full rounded-2xl px-4 py-2.5 text-left text-sm transition-all border-1 border-input/90 flex items-center",
    )


def theme_cli_prompt() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    rx.cond(theme_export_method.value == "local", "uv", "prompt"),
                    class_name="text-muted-foreground text-sm font-normal px-[1rem] py-2",
                ),
                rx.el.div(
                    rx.cond(
                        theme_export_method.value == "online",
                        rx.el.a(
                            "Open in Reflex Build",
                            class_name="text-xs font-light text-foreground",
                            href=f"https://build.reflex.dev/?prompt=Install and run pip install buridan-create and buridan init --preset {seed.value} --include {theme_preset_option.value} then add app = rx.App(stylesheets=['globals.css'])",
                            target="_blank",
                            rel="noopener noreferrer",
                        ),
                    ),
                    rx.el.button(
                        rx.cond(
                            is_export_command_copied.value,
                            hi(
                                "Tick01Icon",
                                class_name="size-4 text-foreground",
                            ),
                            hi(
                                "Copy01Icon",
                                class_name="size-4 text-foreground",
                            ),
                        ),
                        variant="outline",
                        class_name="pr-[1rem] py-2",
                        on_click=[
                            rx.call_function(is_export_command_copied.set_value(True)),
                            rx.set_clipboard(
                                rx.cond(
                                    theme_export_method.value == "local",
                                    f"uv run buridan init --preset {seed.value} --include {theme_preset_option.value}",
                                    f"https://build.reflex.dev/?prompt=Install and run pip install buridan-create and buridan init --preset {seed.value} --include {theme_preset_option.value} then add app = rx.App(stylesheets=['globals.css'])",
                                ),
                            ),
                        ],
                        on_mouse_down=rx.call_function(
                            is_export_command_copied.set_value(False)
                        ).debounce(1500),
                    ),
                    class_name="flex flex-row items-center gap-x-4",
                ),
                class_name="w-full border-b border-input flex flex-row items-center justify-between",
            ),
            rx.el.div(
                rx.el.code(
                    rx.cond(
                        theme_export_method.value == "local",
                        f"uv run buridan init --preset {seed.value} --include {theme_preset_option.value}  ",
                        f"Run this in the project terminal: `pip install buridan-create && buridan init --preset {seed.value} --include {theme_preset_option.value}` Then add this to your main app file: `app = rx.App(stylesheets=['globals.css'])`",
                    ),
                    style={
                        "white-space": "pre",
                        "color": "var(--foreground)",
                        "font-size": "13px",
                        "padding": "1rem 1rem",
                        "display": "block",
                    },
                ),
                class_name="overflow-x-auto overflow-y-auto scrollbar-none flex-1 min-h-0 pr-[1rem]",
            ),
            class_name="w-full flex-1 min-h-0 flex flex-col h-full",
        ),
        class_name="rounded-[0.625rem] outline outline-input flex-1 min-h-0 flex flex-col",
    )


def theme_export_compiler() -> rx.Component:

    open_script = f"""
        const val = sessionStorage.getItem('theme_export_method') || 'local';
        const val_preset = sessionStorage.getItem('theme_preset_option') || 'full';

        refs['_client_state_setTheme_export_method'](val);

        setTimeout(() => {{

            {
        SYNC_BUTTON_STYLES_JS.replace("{OPTIONS}", "['local', 'online']")
        .replace("{BUTTON_PREFIX}", "method")
        .replace("{CHECK_ACTIVE_PREFIX}", "method-checkmark-active")
        .replace("{CHECK_INACTIVE_PREFIX}", "method-checkmark-inactive")
        .replace("{TARGET_VALUE}", "val")
    }

        }}, 30);

        refs['_client_state_setTheme_preset_option'](val_preset);

        setTimeout(() => {{

            {
        SYNC_BUTTON_STYLES_JS.replace("{OPTIONS}", "['full', 'theme']")
        .replace("{BUTTON_PREFIX}", "preset")
        .replace("{CHECK_ACTIVE_PREFIX}", "preset-checkmark-active")
        .replace("{CHECK_INACTIVE_PREFIX}", "preset-checkmark-inactive")
        .replace("{TARGET_VALUE}", "val_preset")
    }

        }}, 30);
    """

    return dialog.root(
        dialog.trigger(
            button(
                "Get Code",
                variant="default",
                class_name="w-full rounded-xl",
                id="get-code-btn",
                on_click=[rx.call_script(FORMAT_CSS_JS), rx.call_script(open_script)],
            ),
            class_name="w-full",
        ),
        dialog.portal(
            dialog.backdrop(class_name="backdrop-blur-[5px]"),
            dialog.popup(
                rx.el.div(
                    tabs.root(
                        tabs.list(
                            tabs.indicator(
                                class_name="rounded-lg flex items-center justify-center"
                            ),
                            tabs.tab(
                                rx.el.p("New Project"),
                                value="project",
                                class_name="border-none flex items-center w-full",
                                on_click=rx.call_script(open_script),
                            ),
                            tabs.tab(
                                "Theme",
                                value="theme",
                                class_name="border-none flex items-center w-full",
                                on_click=rx.call_script(ADD_SWATCHES_JS),
                            ),
                            class_name="relative z-0 flex gap-1 rounded-none bg-transparent w-full mb-4",
                        ),
                        tabs.panel(
                            rx.el.div(
                                rx.el.div(
                                    rx.el.p(
                                        "Pick Export Method",
                                        class_name="text-foreground text-sm font-normal",
                                    ),
                                    rx.el.p(
                                        "Choose where you plan to use your theme.",
                                        class_name="text-muted-foreground text-sm font-light pb-1",
                                    ),
                                    rx.el.div(
                                        select_local_or_reflex_build_option(
                                            title="Local Development",
                                            description="Local Reflex app with your custom theme.",
                                            method="local",
                                        ),
                                        select_local_or_reflex_build_option(
                                            title="Reflex Build",
                                            description="AI prompt matching your theme preset.",
                                            method="online",
                                        ),
                                        class_name="w-full flex flex-col items-stretch gap-y-3 py-3",
                                    ),
                                    class_name="w-full flex flex-col gap-y-0",
                                ),
                                rx.el.div(
                                    rx.el.p(
                                        "Apply Preset",
                                        class_name="text-foreground text-sm font-normal",
                                    ),
                                    rx.el.p(
                                        "Pick which parts of the preset to apply.",
                                        class_name="text-muted-foreground text-sm font-light pb-1",
                                    ),
                                    rx.el.div(
                                        select_preset_option(
                                            title="Full Preset",
                                            description="All the preset, including components, theme, and fonts.",
                                            method="full",
                                        ),
                                        select_preset_option(
                                            title="Theme Tokens",
                                            description="Theme tokens only, like colors and radii.",
                                            method="theme",
                                        ),
                                        class_name="w-full flex flex-col items-stretch gap-y-3 py-3",
                                    ),
                                    class_name="w-full flex flex-col gap-y-0 py-3",
                                ),
                                rx.el.div(
                                    theme_cli_prompt(),
                                    class_name="w-full flex flex-col gap-y-0 py-3",
                                ),
                                class_name="w-full flex flex-col gap-y-0",
                            ),
                            value="project",
                            class_name="w-full",
                        ),
                        tabs.panel(
                            rx.el.div(
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.p(
                                            "Theme Tokens",
                                            class_name="text-foreground text-sm font-normal",
                                        ),
                                        rx.el.p(
                                            "Copy the CSS variables for this preset into your assets folder.",
                                            class_name="text-muted-foreground text-sm font-light pb-2",
                                        ),
                                        class_name="w-full flex flex-col gap-y-1",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.div(
                                                rx.el.p(
                                                    "globals.css",
                                                    class_name="text-muted-foreground text-sm font-normal px-[0.75rem] py-2",
                                                ),
                                                rx.el.button(
                                                    rx.cond(
                                                        is_css_output_copied.value,
                                                        hi(
                                                            "Tick01Icon",
                                                            class_name="size-4 text-foreground",
                                                        ),
                                                        hi(
                                                            "Copy01Icon",
                                                            class_name="size-4 text-foreground",
                                                        ),
                                                    ),
                                                    variant="outline",
                                                    class_name="px-[0.75rem] py-2",
                                                    on_click=[
                                                        rx.call_function(
                                                            is_css_output_copied.set_value(
                                                                True
                                                            )
                                                        ),
                                                        rx.set_clipboard(
                                                            css_output.value
                                                        ),
                                                    ],
                                                    on_mouse_down=rx.call_function(
                                                        is_css_output_copied.set_value(
                                                            False
                                                        )
                                                    ).debounce(1500),
                                                ),
                                                class_name="w-full border-b border-input flex flex-row items-center justify-between",
                                            ),
                                            rx.el.div(
                                                rx.el.code(
                                                    css_output.value,
                                                    id="css-export-block",
                                                    style={
                                                        "white-space": "pre",
                                                        "color": "var(--foreground)",
                                                        "font-size": "13px",
                                                        "padding": "1rem 0.75rem",
                                                        "display": "block",
                                                    },
                                                ),
                                                class_name="overflow-x-auto overflow-y-auto scrollbar-none flex-1 min-h-0",
                                            ),
                                            class_name="w-full flex-1 min-h-0 flex flex-col h-full",
                                        ),
                                        class_name="rounded-[0.625rem] outline outline-input flex-1 min-h-0 flex flex-col",
                                    ),
                                    class_name="w-full flex flex-col gap-y-2 flex-1 min-h-0",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.p(
                                            "Reflex Configuration",
                                            class_name="text-foreground text-sm font-normal",
                                        ),
                                        rx.el.p(
                                            "Copy the extended tailwind config into your rxconfig.py file",
                                            class_name="text-muted-foreground text-sm font-light pb-2",
                                        ),
                                        class_name="w-full flex flex-col gap-y-1",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.div(
                                                rx.el.p(
                                                    "rxconfig.py",
                                                    class_name="text-muted-foreground text-sm font-normal px-[0.75rem] py-2",
                                                ),
                                                rx.el.button(
                                                    rx.cond(
                                                        is_rxconfig_copied.value,
                                                        hi(
                                                            "Tick01Icon",
                                                            class_name="size-4 text-foreground",
                                                        ),
                                                        hi(
                                                            "Copy01Icon",
                                                            class_name="size-4 text-foreground",
                                                        ),
                                                    ),
                                                    variant="outline",
                                                    class_name="px-[0.75rem] py-2",
                                                    on_click=[
                                                        rx.call_function(
                                                            is_rxconfig_copied.set_value(
                                                                True
                                                            )
                                                        ),
                                                        rx.set_clipboard(
                                                            css_output.value
                                                        ),
                                                    ],
                                                    on_mouse_down=rx.call_function(
                                                        is_rxconfig_copied.set_value(
                                                            False
                                                        )
                                                    ).debounce(1500),
                                                ),
                                                class_name="w-full border-b border-input flex flex-row items-center justify-between",
                                            ),
                                            rx.el.div(
                                                rx.el.code(
                                                    rxconfig,
                                                    id="reflex-config-block",
                                                    style={
                                                        "white-space": "pre",
                                                        "color": "var(--foreground)",
                                                        "font-size": "13px",
                                                        "padding": "1rem 0.75rem",
                                                        "display": "block",
                                                    },
                                                ),
                                                class_name="overflow-x-auto overflow-y-auto scrollbar-none flex-1 min-h-0",
                                            ),
                                            class_name="w-full flex-1 min-h-0 flex flex-col h-full",
                                        ),
                                        class_name="rounded-[0.625rem] outline outline-input flex-1 min-h-0 flex flex-col",
                                    ),
                                    class_name="w-full flex flex-col gap-y-2 flex-1 min-h-0",
                                ),
                                class_name="w-full h-full flex flex-col gap-y-4 flex-1 min-h-0",
                            ),
                            class_name="w-full h-full flex flex-col flex-1 min-h-0",
                            value="theme",
                        ),
                        class_name="flex flex-col flex-1 min-h-0",
                        default_value="project",
                    ),
                    class_name="flex flex-col gap-y-4 !w-full h-full",
                ),
                class_name="!w-full max-w-md rounded-2xl dark bg-card h-[92vh] p-6 flex flex-col",
            ),
        ),
        on_open_change=rx.call_script(open_script),
    )
