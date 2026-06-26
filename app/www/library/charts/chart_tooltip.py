from typing import Literal

import reflex as rx

Display = Literal["show", "hide"]
Swatch = Literal["square", "line", "border"]


def _deep_merge(base: dict, override: dict) -> dict:
    result = base.copy()
    for key, value in override.items():
        if isinstance(result.get(key), dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


class _ChartTooltip:
    def __call__(
        self,
        label: Display = "show",
        is_animation_active: bool = False,
        separator: str = "",
        cursor: bool = False,
        item_style: dict = {},
        label_style: dict = {},
        content_style: dict = {},
    ) -> rx.Component:
        defaults = {
            "is_animation_active": is_animation_active,
            "separator": separator,
            "cursor": cursor,
            "item_style": _deep_merge(
                {
                    "color": "currentColor",
                    "display": "flex",
                    "paddingBottom": "0px",
                    "justifyContent": "space-between",
                    "textTransform": "capitalize",
                },
                item_style,
            ),
            "label_style": _deep_merge(
                {
                    "display": "none" if label == "hide" else "flex",
                    "fontWeight": "500",
                },
                label_style,
            ),
            "content_style": _deep_merge(
                {
                    "background": "var(--background)",
                    "borderColor": "var(--input)",
                    "borderRadius": "0.85rem",
                    "padding": "0.25rem 0.65rem",
                    "position": "relative",
                },
                content_style,
            ),
        }

        return rx.recharts.graphing_tooltip(**defaults)


class _ChartTooltipContent:
    def __call__(self, chart_colors: list[int], swatch: Swatch = "square") -> str:
        base = """
            [&_.recharts-tooltip-item-name]:!text-muted-foreground
            [&_.recharts-tooltip-item-separator]:!w-full
            [&_.recharts-tooltip-item]:!min-w-[8rem]
            [&_.recharts-tooltip-item]:!flex
            [&_.recharts-tooltip-item]:!items-center
            [&_.recharts-tooltip-item]:!gap-2
        """

        if swatch == "border":
            # Single vertical left border on the tooltip label using first color
            first_color = chart_colors[0]
            base += f"""
                [&_.recharts-tooltip-label]:!border-l-2
                [&_.recharts-tooltip-label]:!border-[var(--chart-{first_color})]
                [&_.recharts-tooltip-label]:!pl-2
                [&_.recharts-tooltip-label]:!py-0
            """
            return base

        lines = []
        for i, color_idx in enumerate(chart_colors, 1):
            if swatch == "line":
                lines.append(f"""
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!content-['']
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!w-3
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!h-0.5
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!rounded-full
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!flex-shrink-0
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!bg-[var(--chart-{color_idx})]
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!block
                """)
            else:  # square
                lines.append(f"""
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!content-['']
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!w-3
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!h-3
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!rounded-sm
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!flex-shrink-0
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!bg-[var(--chart-{color_idx})]
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!block
                """)

        return base + "\n".join(lines)


chart_tooltip = _ChartTooltip()
chart_tooltip_content = _ChartTooltipContent()
