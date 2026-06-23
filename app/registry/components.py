"""Buridan UI Component Registry."""

COMPONENT_REGISTRY = {
    # --- Utilities ---
    "twmerge": {
        "files": ["components/utils/twmerge.py"],
        "dependencies": [],
    },
    "component": {
        "files": ["components/ui/component.py"],
        "dependencies": ["twmerge"],
    },
    "base_ui": {
        "files": ["components/ui/base_ui.py"],
        "dependencies": ["component"],
    },
    # --- Icons ---
    "hugeicon": {
        "files": ["components/icons/hugeicon.py"],
        "dependencies": ["component"],
    },
    "others_icons": {
        "files": ["components/icons/others.py"],
        "dependencies": ["twmerge"],
    },
    # --- Charts ---
    "charts": {
        "files": ["components/charts/chart_tooltip.py"],
        "dependencies": [],
    },
    "chart_tooltip": {
        "files": ["components/charts/chart_tooltip.py"],
        "dependencies": [],
    },
    # --- UI Components ---
    "accordion": {
        "files": ["components/ui/accordion.py"],
        "dependencies": ["button", "hugeicon", "base_ui"],
    },
    "autocomplete": {
        "files": ["components/ui/autocomplete.py"],
        "dependencies": ["twmerge"],
    },
    "avatar": {
        "files": ["components/ui/avatar.py"],
        "dependencies": ["base_ui"],
    },
    "badge": {
        "files": ["components/ui/badge.py"],
        "dependencies": ["component"],
    },
    "breadcrumb": {
        "files": ["components/ui/breadcrumb.py"],
        "dependencies": [],
    },
    "button": {
        "files": ["components/ui/button.py"],
        "dependencies": ["others_icons", "component"],
    },
    "card": {
        "files": ["components/ui/card.py"],
        "dependencies": ["component"],
    },
    "checkbox": {
        "files": ["components/ui/checkbox.py"],
        "dependencies": ["hugeicon", "twmerge", "base_ui"],
    },
    "collapsible": {
        "files": ["components/ui/collapsible.py"],
        "dependencies": ["base_ui"],
    },
    "context_menu": {
        "files": ["components/ui/context_menu.py"],
        "dependencies": ["twmerge", "base_ui", "button"],
    },
    "dialog": {
        "files": ["components/ui/dialog.py"],
        "dependencies": ["hugeicon", "base_ui", "button"],
    },
    "field": {
        "files": ["components/ui/field.py"],
        "dependencies": ["base_ui"],
    },
    "frame": {
        "files": ["components/ui/frame.py"],
        "dependencies": ["twmerge"],
    },
    "heatmap": {
        "files": ["components/ui/heatmap.py"],
        "dependencies": ["twmerge"],
    },
    "input": {
        "files": ["components/ui/input.py"],
        "dependencies": [],
    },
    "input_group": {
        "files": ["components/ui/input_group.py"],
        "dependencies": [],
    },
    "kbd": {
        "files": ["components/ui/kbd.py"],
        "dependencies": [],
    },
    "link": {
        "files": ["components/ui/link.py"],
        "dependencies": ["hugeicon", "twmerge"],
    },
    "menu": {
        "files": ["components/ui/menu.py"],
        "dependencies": ["hugeicon", "others_icons", "twmerge", "base_ui", "button"],
    },
    "metric": {
        "files": ["components/ui/metric.py"],
        "dependencies": ["twmerge", "component"],
    },
    "popover": {
        "files": ["components/ui/popover.py"],
        "dependencies": ["twmerge", "base_ui"],
    },
    "scroll_area": {
        "files": ["components/ui/scroll_area.py"],
        "dependencies": ["twmerge", "base_ui"],
    },
    "select": {
        "files": ["components/ui/select.py"],
        "dependencies": ["hugeicon", "others_icons", "twmerge", "base_ui", "button"],
    },
    "skeleton": {
        "files": ["components/ui/skeleton.py"],
        "dependencies": ["twmerge"],
    },
    "slider": {
        "files": ["components/ui/slider.py"],
        "dependencies": ["base_ui"],
    },
    "switch": {
        "files": ["components/ui/switch.py"],
        "dependencies": ["base_ui"],
    },
    "table": {
        "files": ["components/ui/table.py"],
        "dependencies": ["twmerge", "component"],
    },
    "tabs": {
        "files": ["components/ui/tabs.py"],
        "dependencies": ["base_ui"],
    },
    "textarea": {
        "files": ["components/ui/textarea.py"],
        "dependencies": ["component"],
    },
    "timeline": {
        "files": ["components/ui/timeline.py"],
        "dependencies": ["twmerge"],
    },
    "toggle": {
        "files": ["components/ui/toggle.py"],
        "dependencies": ["twmerge", "base_ui"],
    },
    "toggle_group": {
        "files": ["components/ui/toggle_group.py"],
        "dependencies": ["base_ui"],
    },
    "tooltip": {
        "files": ["components/ui/tooltip.py"],
        "dependencies": ["others_icons", "base_ui"],
    },
    "typography": {
        "files": ["components/ui/typography.py"],
        "dependencies": [],
    },
}
