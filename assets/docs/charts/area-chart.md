

# Area Chart

Area Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

# Usage
The chart tooltip components are available in the `base_ui` library.


```python
from typing import Literal

import reflex as rx

Display = Literal["show", "hide"]
Swatch = Literal["square", "line", "border"]


def _deep_merge(base: dict, override: dict) -> dict:
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
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
        """ + (
            """
            [&_.recharts-tooltip-label]:!border-l-3
            [&_.recharts-tooltip-label]:!border-[var(--chart-1)]
            [&_.recharts-tooltip-label]:!pl-2
            [&_.recharts-tooltip-label]:!py-0
            """
            if swatch == "border"
            else ""
        )

        lines = []
        for i in range(1, num_series + 1):
            if swatch == "border":
                lines.append(f"""
                    [&_.recharts-default-tooltip]:!py-2 !flex !flex-col !gap-y-0
                    [&_.recharts-tooltip-item:nth-child({i})]:!border-l-3
                    [&_.recharts-tooltip-item:nth-child({i})]:!border-[var(--chart-{i})]
                    [&_.recharts-tooltip-item:nth-child({i})]:!pl-2
                    [&_.recharts-tooltip-item:nth-child({i})]:!py-0
                """)
            else:
                lines.append(f"""
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!content-['']
                    [&_.recharts-tooltip-item:nth-child({i})]:before:{"!w-3" if swatch == "square" else "!w-8"}
                    {"[&_.recharts-tooltip-item:nth-child(" + str(i) + ")]:before:!flex-shrink-0" if swatch == "square" else ""}
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!h-3
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!rounded-sm
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!bg-[var(--chart-{i})]
                    [&_.recharts-tooltip-item:nth-child({i})]:before:!block
                """)

        return base + "\n".join(lines)


chart_tooltip = _ChartTooltip()
chart_tooltip_content = _ChartTooltipContent()
```


# Examples

## Basic
A minimal example showing a single series with a smooth gradient fill.

```python
def areachart_v1():

    return card.root(
        card.header(
            card.title("Area Chart"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.area_chart(
                chart_tooltip(label="show"),
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    class_name="opacity-30",
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
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
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(1, "border") + " w-full p-0",
    )
```


## Linear
Displays data using straight line segments between points.

```python
def areachart_v2():

    return card.root(
        card.header(
            card.title("Area Chart - Linear"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.area_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="linear",
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
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(1, "square") + " w-full p-0",
    )
```


## Step
Renders the chart with stepped transitions, ideal for discrete intervals.

```python
def areachart_v3():

    return card.root(
        card.header(
            card.title("Area Chart - Step"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.area_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="step",
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
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(1, "square") + " w-full p-0",
    )
```


## Stacked
Visualizes multiple data series stacked on top of each other for cumulative comparison.

```python
def areachart_v4():

    return card.root(
        card.header(
            card.title("Area Chart - Stacked"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.area_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    stack_id="a",
                    is_animation_active=False,
                ),
                rx.recharts.area(
                    data_key="mobile",
                    fill="var(--chart-2)",
                    stroke="var(--chart-2)",
                    stroke_width=2,
                    stack_id="a",
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
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(2, "square") + " w-full p-0",
    )
```


## Dynamic
Demonstrates how data or series can update interactively in real-time.

```python
def areachart_v5():

    start_date = datetime.date(2024, 4, 1)
    data = [
        {
            "date": (start_date + datetime.timedelta(days=i)).strftime("%b %d"),
            "desktop": random.randint(80, 500),
            "mobile": random.randint(100, 550),
        }
        for i in range(91)
    ]

    SelectedRange = ClientStateVar.create("area_selected", data)

    def gradient(id_: str, color: str):
        return rx.el.svg.linear_gradient(
            rx.el.svg.stop(stop_color=f"var(--{color})", offset="5%", stop_opacity=0.8),
            rx.el.svg.stop(
                stop_color=f"var(--{color})", offset="95%", stop_opacity=0.1
            ),
            x1=0,
            x2=0,
            y1=0,
            y2=1,
            id=id_,
        )

    def area(data_key: str, color: str):
        return rx.recharts.area(
            data_key=data_key,
            fill=f"url(#{data_key})",
            stack_id="a",
            stroke=f"var(--{color})",
            animation_easing="linear",
            is_animation_active=False,
            active_dot={"fill": f"var(--{color})"},
        )

    select_options = [
        ("Last 3 Months", data),
        ("Last 30 Days", data[-30:]),
        ("Last 7 Days", data[-7:]),
    ]

    return card.root(
        card.header(
            rx.el.div(
                rx.el.div(
                    card.title("Area Chart - Dynamic"),
                    card.description("Showing total visitors for the last 6 months"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.el.select(
                    *[
                        rx.el.option(label, on_click=SelectedRange.set_value(value))
                        for label, value in select_options
                    ],
                    default_value="Last 3 Months",
                    class_name="relative flex items-center whitespace-nowrap justify-center gap-2 py-2 rounded-lg shadow-sm px-3 bg-secondary border border-input",
                ),
                class_name="flex flex-row flex-wrap gap-y-4 items-center justify-between",
            ),
        ),
        card.content(
            rx.recharts.area_chart(
                rx.el.svg.defs(
                    gradient("desktop", "chart-1"),
                    gradient("mobile", "chart-2"),
                ),
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                area("mobile", "chart-2"),
                area("desktop", "chart-1"),
                rx.recharts.x_axis(
                    data_key="date",
                    axis_line=False,
                    min_tick_gap=32,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                data=SelectedRange.value,
                width="100%",
                height=240,
            ),
            class_name="flex flex-col items-center h-[240px]",
        ),
        card.footer(
            rx.el.div(
                rx.foreach(
                    ["Desktop", "Mobile"],
                    lambda device, index: rx.el.div(
                        rx.el.div(
                            class_name=f"w-3 h-3 rounded-sm bg-chart-{index + 1}"
                        ),
                        rx.el.p(device, class_name="text-sm text-foreground"),
                        class_name="flex flex-row items-center gap-x-2",
                    ),
                ),
                class_name="py-4 px-4 flex w-full flex justify-center gap-8",
            ),
        ),
        class_name=chart_tooltip_content(2, "square") + " w-full p-0",
    )
```


## Legend
Adds a built-in legend for easy series identification.

```python
def areachart_v6():

    return card.root(
        card.header(
            card.title("Area Chart - Legend"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.area_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="mobile",
                    fill="var(--chart-1)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    stack_id="a",
                    is_animation_active=False,
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="var(--chart-2)",
                    stroke="var(--chart-2)",
                    stroke_width=2,
                    stack_id="a",
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
                rx.recharts.legend(),
                data=data,
                width="100%",
                height=250,
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(2, "square") + " w-full p-0",
    )
```


## Axes
Shows full control over axis configuration, labels, and styling.

```python
def areachart_v7():

    return card.root(
        card.header(
            card.title("Area Chart - Axes"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.area_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="mobile",
                    fill="var(--chart-1)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    stack_id="a",
                    is_animation_active=False,
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="var(--chart-2)",
                    stroke="var(--chart-2)",
                    stroke_width=2,
                    stack_id="a",
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
                rx.recharts.y_axis(
                    width=30,
                    axis_line=False,
                    min_tick_gap=50,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=data,
                width="100%",
                height=250,
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(2, "square") + " w-full p-0",
    )
```


## Custom Legends
Implements a user-defined legend layout for better presentation control.

```python
def areachart_v8():
    series = [("desktop", "Desktop", "--chart-1"), ("mobile", "Mobile", "--chart-2")]

    def create_gradient(var_name):
        return rx.el.svg.linear_gradient(
            rx.el.svg.stop(
                stop_color=f"var({var_name})", offset="5%", stop_opacity=0.8
            ),
            rx.el.svg.stop(
                stop_color=f"var({var_name})", offset="95%", stop_opacity=0.1
            ),
            x1=0,
            x2=0,
            y1=0,
            y2=1,
            id=var_name.strip("-"),
        )

    return card.root(
        card.header(
            rx.hstack(
                rx.el.div(
                    card.title("Area Chart - Gradient"),
                    card.description("Showing total visitors for the last 6 months"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.hstack(
                    rx.foreach(
                        series,
                        lambda s: rx.hstack(
                            rx.box(class_name="size-2 rounded-full", bg=f"var({s[2]})"),
                            rx.text(
                                s[1],
                                class_name="text-xs font-medium",
                                color=rx.color("slate", 11),
                            ),
                            align="center",
                            spacing="2",
                        ),
                    ),
                    class_name="flex items-center gap-4",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
        ),
        card.content(
            rx.recharts.area_chart(
                rx.el.svg.defs(
                    *(create_gradient(s[2]) for s in series),
                ),
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                *(
                    rx.recharts.area(
                        data_key=s[0],
                        fill=f"url(#{s[2].strip('-')})",
                        stroke=f"var({s[2]})",
                        stroke_width=2,
                        stack_id="1",
                        is_animation_active=False,
                    )
                    for s in series
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
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(2, "square") + " w-full p-0",
    )
```


## Step with Gradient
Combines stepped transitions with a smooth color gradient for visual emphasis.

```python
def areachart_v9():

    def gradient(id_: str, color: str):
        return rx.el.svg.linear_gradient(
            rx.el.svg.stop(stop_color=f"var(--{color})", offset="5%", stop_opacity=0.8),
            rx.el.svg.stop(
                stop_color=f"var(--{color})", offset="95%", stop_opacity=0.1
            ),
            x1=0,
            x2=0,
            y1=0,
            y2=1,
            id=id_,
        )

    return card.root(
        card.header(
            card.title("Area Chart - Step with Gradient"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.area_chart(
                rx.el.svg.defs(
                    gradient("desktop", "chart-1"),
                ),
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="url(#desktop)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="step",
                    is_animation_active=False,
                    active_dot={"fill": "var(--chart-1)"},
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
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(1, "square") + " w-full p-0",
    )
```


## Custom Legend and Axes
A complete example with custom legends, axes, and advanced styling combined.

```python
def areachart_v10():
    series = [("mobile", "Mobile", "--chart-1"), ("desktop", "Desktop", "--chart-2")]

    return card.root(
        card.header(
            rx.hstack(
                rx.el.div(
                    card.title("Area Chart - Mixed"),
                    card.description("Showing total visitors for the last 6 months"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.hstack(
                    rx.foreach(
                        series,
                        lambda s: rx.hstack(
                            rx.box(class_name="size-2 rounded-full", bg=f"var({s[2]})"),
                            rx.text(
                                s[1],
                                class_name="text-xs font-medium",
                                color=rx.color("slate", 11),
                            ),
                            align="center",
                            spacing="2",
                        ),
                    ),
                    class_name="flex items-center gap-4",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
        ),
        card.content(
            rx.recharts.area_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.area(
                    data_key="mobile",
                    fill="var(--chart-1)",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    stack_id="a",
                    is_animation_active=False,
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill="var(--chart-2)",
                    stroke="var(--chart-2)",
                    stroke_width=2,
                    stack_id="a",
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
                rx.recharts.y_axis(
                    width=30,
                    axis_line=False,
                    min_tick_gap=50,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=data,
                width="100%",
                height=250,
            ),
        ),
        card.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Trending up by 5.2% this month ",
                        class_name="flex items-center gap-2 leading-none font-medium",
                    ),
                    rx.el.div(
                        "January - June 2024",
                        class_name="flex items-center gap-2 leading-none text-muted-foreground",
                    ),
                    class_name="grid gap-2",
                ),
                class_name="flex w-full items-start gap-2 text-sm",
            )
        ),
        class_name=chart_tooltip_content(2, "square") + " w-full p-0",
    )
```

