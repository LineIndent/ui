


# Charts

Beautiful charts. Built using Recharts. Copy and paste into your apps.

A collection of chart components that you can copy and paste into your apps. Charts are designed to look great out of the box. They work well with the other components and are fully customizable to fit your project. 

For an overview of whats available, checkout the [Charts](/charts) page. 

# Component

Reflex wraps [Recharts](https://recharts.github.io/) under the hood. This means you build your own charts using Recharts components and only bring in your theme tokens and custom components like `chart_tooltip` when and where you need it.

```chart
import reflex as rx

rx.recharts.area_chart(
    rx.recharts.cartesian_grid(),
    rx.recharts.x_axis(),
    rx.recharts.y_axis(),
    rx.recharts.area(),
    rx.recharts.area(),
    rx.recharts.tooltip(),
)
```

We do not wrap Recharts. This means you're not locked into an abstraction. When a new Recharts version is released, you can follow the official upgrade path to upgrade your charts.

# Installation

buridan/ui provides a custom `chart_tooltip` that can be used to match the overall theme tokens generated. 

### CLI

```bash
buridan add component chart_tooltip
```

### Manual Installation

```python
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
```


# Your First Chart

Let's build your first chart. We'll build a bar chart, add a grid, axis, tooltip and legend.

## Defining your data

The following data represents the number of desktop and mobile users for each month.

>**Note:** All of our examples use static data in a specific data structure. You are not limited to either static data or the structure. For dynamic data, use [rx.State](https://reflex.dev/docs/state/overview) instead.

```example_chart.py
data = [
    {"month": "Jan", "desktop": 186, "mobile": 80},
    {"month": "Feb", "desktop": 305, "mobile": 200},
    {"month": "Mar", "desktop": 237, "mobile": 120},
    {"month": "Apr", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "Jun", "desktop": 214, "mobile": 140},
]
```

## Build your chart

You can now build your chart using Recharts components.


```python
def chart_example():

    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="desktop",
            fill="var(--chart-1)",
            radius=4,
            is_animation_active=False,
        ),
        rx.recharts.bar(
            data_key="mobile",
            fill="var(--chart-2)",
            radius=4,
            is_animation_active=False,
        ),
        data=data,
        width="100%",
        height=250,
    )
```


## Add a Grid

Let's add a grid to the chart.

```example_chart.py
rx.recharts.cartesian_grid(
    horizontal=True, vertical=False, class_name="opacity-30"
)
```


```python
def chart_example_with_grid():

    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-30"
        ),
        rx.recharts.bar(
            data_key="desktop",
            fill="var(--chart-1)",
            radius=4,
            is_animation_active=False,
        ),
        rx.recharts.bar(
            data_key="mobile",
            fill="var(--chart-2)",
            radius=4,
            is_animation_active=False,
        ),
        data=data,
        width="100%",
        height=250,
    )
```


## Add an Axis

To add an x-axis to the chart, we'll use the `rx.recharts.x_axis()` component.

```example_chart.py
rx.recharts.x_axis(
    data_key="month",
    axis_line=False,
    tick_size=10,
    tick_line=False,
    custom_attrs={"fontSize": "12px"},
    interval="preserveStartEnd",
)
```


```python
def chart_example_with_x_axis():

    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-30"
        ),
        rx.recharts.bar(
            data_key="desktop",
            fill="var(--chart-1)",
            radius=4,
            is_animation_active=False,
        ),
        rx.recharts.bar(
            data_key="mobile",
            fill="var(--chart-2)",
            radius=4,
            is_animation_active=False,
        ),
        rx.recharts.x_axis(
            data_key="month",
            axis_line=False,
            tick_size=10,
            tick_line=False,
            custom_attrs={"fontSize": "12px"},
            interval="preserveStartEnd",
        ),
        data=data,
        width="100%",
        height=250,
    )
```


## Add Tooltip

So far we've only used components from Recharts. They look great out of the box thanks to some customization in the chart component.

To add a tooltip, we'll use the custom `chart_tooltip` and `chart_tooltip_content` components from chart.

>**Note**: A small comment regarding the custom tooltip. Because of the way Recharts is composed and the way it's wrapped in Reflex, the custom tooltip, as of now, works only for Area, Bar, and Line charts.

To use the custom tooltip, first import it at the top of your chart file.

```chart_example.py
from components.charts.chart_tooltip import chart_tooltip, chart_tooltip_content
```

Add the component to your chart and pass in the props.

```example_chart.py
rx.recharts.bar_chart(
    ...,
    chart_tooltip(),
    data=data,
    width="100%",
    height=250,
    class_name=chart_tooltip_content(2, "square"),
)
```


```python
def chart_example_with_custom_tooltip():

    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(
            horizontal=True, vertical=False, class_name="opacity-30"
        ),
        rx.recharts.bar(
            data_key="desktop",
            fill="var(--chart-1)",
            radius=4,
            is_animation_active=False,
        ),
        rx.recharts.bar(
            data_key="mobile",
            fill="var(--chart-2)",
            radius=4,
            is_animation_active=False,
        ),
        rx.recharts.x_axis(
            data_key="month",
            axis_line=False,
            tick_size=10,
            tick_line=False,
            custom_attrs={"fontSize": "12px"},
            interval="preserveStartEnd",
        ),
        chart_tooltip(),
        data=data,
        width="100%",
        height=250,
        class_name=chart_tooltip_content(2, "square"),
    )
```


Hover to see the tooltips. Easy, right? Two components, and we've got a beautiful tooltip.


## Add Legend

We'll do the same for the legend. Although there's no API for legends the way we created one for tooltips, the same logic still applies. 

Add the component to your chart.

```example_chart.py
rx.el.div(
    rx.foreach(
        ["Desktop", "Mobile"],
        lambda device, index: rx.el.div(
            rx.el.div(
                class_name=f"h-3 w-3 rounded-sm bg-chart-{index + 1}"
            ),
            rx.el.p(device, class_name="text-xs text-foreground"),
            class_name="flex flex-row items-center gap-x-2",
        ),
    ),
    class_name="flex items-center gap-4 justify-center",
)
```


```python
def chart_example_with_custom_legends():

    return rx.el.div(
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(
                horizontal=True, vertical=False, class_name="opacity-30"
            ),
            rx.recharts.bar(
                data_key="desktop",
                fill="var(--chart-1)",
                radius=4,
                is_animation_active=False,
            ),
            rx.recharts.bar(
                data_key="mobile",
                fill="var(--chart-2)",
                radius=4,
                is_animation_active=False,
            ),
            rx.recharts.x_axis(
                data_key="month",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            chart_tooltip(),
            data=data,
            width="100%",
            height=250,
            class_name=chart_tooltip_content(2, "square"),
        ),
        rx.el.div(
            rx.foreach(
                ["Desktop", "Mobile"],
                lambda device, index: rx.el.div(
                    rx.el.div(class_name=f"h-3 w-3 rounded-sm bg-chart-{index + 1}"),
                    rx.el.p(device, class_name="text-xs text-foreground"),
                    class_name="flex flex-row items-center gap-x-2",
                ),
            ),
            class_name="flex items-center gap-4 justify-center",
        ),
        class_name="w-full",
    )
```


Done. You've built your first chart!

# Theming

Charts have built-in support for theming. You can use css variables (recommended) or color values in any color format, such as hex, hsl or oklch.

## CSS Variables

Define your colors in your CSS file.

```assets/globals.css
:root {
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
}

.dark {
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
}
```

## hex, hsl, or oklch

You can also define your colors directly in the chart component. Use the color format you prefer.

```chart_example.py
rx.recharts.bar(data_key="mobile", fill="var(--chart-2)")
rx.recharts.bar(data_key="mobile", fill="#2563eb")
rx.recharts.bar(data_key="mobile", fill="oklch(0.5 0.2 240)")
```

You can also include colors in your data structure and utlize `rx.foreach` for more concise codebase.

```example_chart.py
data = [
    {"month": "Jan", "desktop": 186, "mobile": 80, "fill": "#2563eb"},
    {"month": "Feb", "desktop": 305, "mobile": 200, "fill": "oklch(0.5 0.2 240)"},
]
```

# Tooltip

A chart tooltip contains a label and swatch type. You can use a combination of these to customize your tooltip.

```chart_tooltip.py
Display = Literal["show", "hide"]
Swatch = Literal["square", "line", "border"]
```


> **Warning: Unknown command 'tooltip'**


You can turn on/off any of these using the `display` prop and customize the indicator style using the `swatch` prop.

## Props

Use the following props to customize the tooltip.

**chart_tooltip()**

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `"show" \| "hide"` | `"show"` | Whether to render the tooltip label above the items. |
| `is_animation_active` | `bool` | `False` | Whether to animate the tooltip on appearance. |
| `separator` | `str` | `""` | String placed between the item name and value. |
| `cursor` | `bool` | `False` | Whether to show the cursor line/highlight on hover. |
| `item_style` | `dict` | `{}` | Style overrides merged onto each tooltip item row. |
| `label_style` | `dict` | `{}` | Style overrides merged onto the label element. |
| `content_style` | `dict` | `{}` | Style overrides merged onto the tooltip container. |

**chart_tooltip_content()**

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `num_series` | `int` | — | Number of data series in the chart. Must match the number of `rx.recharts.bar` / `line` / `area` components. |
| `swatch` | `"square" \| "line" \| "border"` | `"square"` | Indicator style per item. `square` = small filled box, `line` = wide pill, `border` = left accent line per series using `--chart-{i}`. |

>**chart_tooltip_content()** returns a string of Tailwind classes and must be passed to the **chart component's** class_name, not to **chart_tooltip()**.
