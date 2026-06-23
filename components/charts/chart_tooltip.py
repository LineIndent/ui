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
    def __call__(self, num_series: int, swatch: Swatch = "square") -> str:
        base = """
            [&_.recharts-tooltip-item-name]:!text-muted-foreground
            [&_.recharts-tooltip-item-separator]:!w-full
            [&_.recharts-tooltip-item]:!w-[8rem]
            [&_.recharts-tooltip-item]:!flex
            [&_.recharts-tooltip-item]:!items-center
            [&_.recharts-tooltip-item]:!gap-2
        """

        if swatch == "border":
            base += """
                [&_.recharts-tooltip-label]:!border-l-3
                [&_.recharts-tooltip-label]:!border-[var(--chart-1)]
                [&_.recharts-tooltip-label]:!pl-2
                [&_.recharts-tooltip-label]:!py-0
            """

        lines = []

        for i in range(1, num_series + 1):
            idx = str(i)

            if swatch == "border":
                lines.append(f"""
                    [&_.recharts-default-tooltip]:!py-2 !flex !flex-col !gap-y-0
                    [&_.recharts-tooltip-item:nth-child({idx})]:!border-l-3
                    [&_.recharts-tooltip-item:nth-child({idx})]:!border-[var(--chart-{idx})]
                    [&_.recharts-tooltip-item:nth-child({idx})]:!pl-2
                    [&_.recharts-tooltip-item:nth-child({idx})]:!py-0
                """)
            else:
                width = "!w-3" if swatch == "square" else "!w-8"
                shrink = (
                    f"[&_.recharts-tooltip-item:nth-child({idx})]:before:!flex-shrink-0"
                    if swatch == "square"
                    else ""
                )

                lines.append(f"""
                    [&_.recharts-tooltip-item:nth-child({idx})]:before:!content-['']
                    [&_.recharts-tooltip-item:nth-child({idx})]:before:{width}
                    {shrink}
                    [&_.recharts-tooltip-item:nth-child({idx})]:before:!h-3
                    [&_.recharts-tooltip-item:nth-child({idx})]:before:!rounded-sm
                    [&_.recharts-tooltip-item:nth-child({idx})]:before:!bg-[var(--chart-{idx})]
                    [&_.recharts-tooltip-item:nth-child({idx})]:before:!block
                """)

        return base + "\n".join(lines)


chart_tooltip = _ChartTooltip()
chart_tooltip_content = _ChartTooltipContent()
