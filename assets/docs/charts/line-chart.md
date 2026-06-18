

# Line Chart

Line Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

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
A minimal example showing a single series with a smooth line connection.

```python
def linechart_v1():

    return card.root(
        card.header(
            card.title("Line Chart"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    data_key="desktop",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="natural",
                    dot=False,
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


## Linear
Displays data using straight line segments between points.

```python
def linechart_v2():

    return card.root(
        card.header(
            card.title("Line Chart - Linear"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    data_key="desktop",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="linear",
                    dot=False,
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


## Label
Shows data points with labels for clear value identification.

```python
def linechart_v3():

    return card.root(
        card.header(
            card.title("Line Chart - Label"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    rx.recharts.label_list(
                        position="top",
                        offset=20,
                        custom_attrs={"fontSize": "12px", "fontWeight": "bold"},
                    ),
                    data_key="desktop",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="linear",
                    dot=True,
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
                margin={"left": 20, "right": 20, "top": 25},
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


## Multiple
Visualizes multiple data series on the same chart for comparison.

```python
def linechart_v4():

    return card.root(
        card.header(
            card.title("Line Chart - Multiple"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    data_key="desktop",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="natural",
                    dot=False,
                    is_animation_active=False,
                ),
                rx.recharts.line(
                    data_key="mobile",
                    stroke="var(--chart-2)",
                    stroke_width=2,
                    type_="natural",
                    dot=False,
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


## Title Label
Includes a title and labels for comprehensive chart context.

```python
def linechart_v5():

    return card.root(
        card.header(
            card.title("Line Chart - Title Label"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip("hide"),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    rx.recharts.label_list(
                        position="top",
                        offset=20,
                        custom_attrs={"fontSize": "12px", "fontWeight": "bold"},
                        data_key="browser",
                    ),
                    data_key="visitors",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="natural",
                    dot=True,
                    is_animation_active=False,
                    active_dot={"fill": "var(--chart-1)"},
                ),
                data=data,
                width="100%",
                height=250,
                margin={"left": 25, "right": 20, "top": 25},
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


## Minimal
A clean, stripped-down version focusing on essential data visualization.

```python
def linechart_v6():

    return card.root(
        card.header(
            card.title("Line Chart - Minimal"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    data_key="visitors",
                    type_="natural",
                    dot=False,
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    is_animation_active=False,
                ),
                data=data,
                width="100%",
                height=250,
                margin={"left": 20, "right": 20, "top": 25},
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


## Dynamic
Demonstrates how data or series can update interactively in real-time.

```python
def linechart_v7():
    from reflex.experimental import ClientStateVar

    data = [
        {"date": "2024-04-01", "desktop": 222, "mobile": 150},
        {"date": "2024-04-02", "desktop": 97, "mobile": 180},
        {"date": "2024-04-03", "desktop": 167, "mobile": 120},
        {"date": "2024-04-04", "desktop": 242, "mobile": 260},
        {"date": "2024-04-05", "desktop": 373, "mobile": 290},
        {"date": "2024-04-06", "desktop": 301, "mobile": 340},
        {"date": "2024-04-07", "desktop": 245, "mobile": 180},
        {"date": "2024-04-08", "desktop": 409, "mobile": 320},
        {"date": "2024-04-09", "desktop": 59, "mobile": 110},
        {"date": "2024-04-10", "desktop": 261, "mobile": 190},
        {"date": "2024-04-11", "desktop": 327, "mobile": 350},
        {"date": "2024-04-12", "desktop": 292, "mobile": 210},
        {"date": "2024-04-13", "desktop": 342, "mobile": 380},
        {"date": "2024-04-14", "desktop": 137, "mobile": 220},
        {"date": "2024-05-31", "desktop": 178, "mobile": 230},
        {"date": "2024-06-01", "desktop": 178, "mobile": 200},
        {"date": "2024-06-02", "desktop": 470, "mobile": 410},
        {"date": "2024-06-03", "desktop": 103, "mobile": 160},
        {"date": "2024-06-04", "desktop": 439, "mobile": 380},
        {"date": "2024-06-05", "desktop": 88, "mobile": 140},
        {"date": "2024-06-06", "desktop": 294, "mobile": 250},
        {"date": "2024-06-07", "desktop": 323, "mobile": 370},
        {"date": "2024-06-08", "desktop": 385, "mobile": 320},
        {"date": "2024-06-09", "desktop": 438, "mobile": 480},
        {"date": "2024-06-10", "desktop": 155, "mobile": 200},
        {"date": "2024-06-11", "desktop": 92, "mobile": 150},
        {"date": "2024-06-12", "desktop": 492, "mobile": 420},
        {"date": "2024-06-13", "desktop": 81, "mobile": 130},
        {"date": "2024-06-14", "desktop": 426, "mobile": 380},
        {"date": "2024-06-15", "desktop": 307, "mobile": 350},
        {"date": "2024-06-16", "desktop": 371, "mobile": 310},
    ]

    formatted_data = [
        {
            "date": datetime.strptime(item["date"], "%Y-%m-%d").strftime("%b %d"),
            "desktop": item["desktop"],
            "mobile": item["mobile"],
        }
        for item in data
    ]

    SelectedType = ClientStateVar.create("selected_line", "mobile")

    return card.root(
        card.header(
            rx.el.div(
                rx.el.div(
                    card.title("Line Chart - Dynamic"),
                    card.description("Showing total visitors for the last 6 months"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.el.div(
                    rx.el.select(
                        rx.el.option(
                            "Mobile", on_click=SelectedType.set_value("mobile")
                        ),
                        rx.el.option(
                            "Desktop", on_click=SelectedType.set_value("desktop")
                        ),
                        default_value="Mobile",
                        class_name="relative flex items-center whitespace-nowrap justify-center gap-2 py-2 rounded-lg shadow-sm px-3 bg-secondary border border-input",
                    ),
                    class_name="flex flex-row items-center gap-x-2",
                ),
                class_name="w-full flex flex-row flex-wrap items-center justify-between gap-y-4",
            ),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip("hide"),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    data_key=SelectedType.value,
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="natural",
                    is_animation_active=False,
                    dot=False,
                    active_dot={"fill": "var(--chart-1)"},
                ),
                rx.recharts.y_axis(type_="number", hide=True),
                rx.recharts.x_axis(
                    data_key="date",
                    axis_line=False,
                    min_tick_gap=32,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                data=formatted_data,
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
        class_name=chart_tooltip_content(1, "line") + " w-full p-0",
    )
```


## Custom Legends
Implements a user-defined legend layout for better presentation control.

```python
def linechart_v8():

    return card.root(
        card.header(
            rx.hstack(
                rx.el.div(
                    card.title("Line Chart - Multiple"),
                    card.description("Showing total visitors for the last 6 months"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
        ),
        card.content(
            rx.recharts.line_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.line(
                    data_key="desktop",
                    stroke="var(--chart-1)",
                    stroke_width=2,
                    type_="linear",
                    dot=False,
                    is_animation_active=False,
                    active_dot={"fill": "var(--chart-1)"},
                ),
                rx.recharts.line(
                    data_key="mobile",
                    stroke="var(--chart-2)",
                    stroke_width=2,
                    type_="linear",
                    dot=False,
                    is_animation_active=False,
                    active_dot={"fill": "var(--chart-2)"},
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
                height=210,
            ),
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
            class_name="flex flex-col h-[250px]",
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

