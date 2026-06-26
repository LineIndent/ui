

# Bar Chart

Bar charts are ideal for visualizing categorical data and comparing multiple series side by side.
They can be stacked, oriented horizontally, or customized with legends and axes.

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
```


# Examples

## Multiple Series
A simple vertical bar chart comparing data categories.

```python
def barchart_v1():

    return card.root(
        card.header(
            card.title("Bar Chart - Multiple"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
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
            ),
            class_name="h-[250px]",
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
        class_name=chart_tooltip_content([1, 2], "square") + " w-full p-0",
    )
```


## Horizontal
Display multiple datasets within the same chart for comparison.

```python
def barchart_v2():

    return card.root(
        card.header(
            card.title("Bar Chart - Horizontal"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
                rx.recharts.bar(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    radius=4,
                    is_animation_active=False,
                ),
                rx.recharts.x_axis(type_="number", hide=True, tick_size=0),
                rx.recharts.y_axis(
                    data_key="month",
                    type_="category",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=data,
                layout="vertical",
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
        class_name=chart_tooltip_content([1], "square") + " w-full p-0",
    )
```


## Stacked with Legends
Combine related values by stacking bars for cumulative insights.

```python
def barchart_v3():

    return card.root(
        card.header(
            card.title("Bar Chart - Legend"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.bar(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    stack_id="a",
                    radius=[0, 0, 4, 4],
                    is_animation_active=False,
                ),
                rx.recharts.bar(
                    data_key="mobile",
                    fill="var(--chart-2)",
                    stack_id="a",
                    radius=[4, 4, 0, 0],
                    is_animation_active=False,
                ),
                rx.recharts.y_axis(type_="number", hide=True),
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
        class_name=chart_tooltip_content([1, 2], "square") + " w-full p-0",
    )
```


## Labeled
Flip the orientation to show bars horizontally for improved readability.

```python
def barchart_v4():

    return card.root(
        card.header(
            card.title("Bar Chart - Labeled"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.bar(
                    rx.recharts.label_list(
                        data_key="desktop",
                        position="top",
                        offset=10,
                    ),
                    data_key="desktop",
                    fill="var(--chart-1)",
                    radius=4,
                    is_animation_active=False,
                ),
                rx.recharts.y_axis(type_="number", hide=True),
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
                margin={"top": 20},
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
        class_name=chart_tooltip_content([1], "square") + " w-full p-0",
    )
```


## Dynamic
Demonstrate dynamic updates or data-driven interactivity in your bar chart.

```python
def barchart_v5():
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
    ]

    formatted_data = [
        {
            "date": datetime.strptime(item["date"], "%Y-%m-%d").strftime("%b %d"),
            "desktop": item["desktop"],
            "mobile": item["mobile"],
        }
        for item in data
    ]

    SelectedType = ClientStateVar.create("bar_selected", "mobile")

    return card.root(
        card.header(
            rx.hstack(
                rx.el.div(
                    card.title("Bar Chart - Dynamic"),
                    card.description("Showing total visitors for the last 6 months"),
                    class_name="flex flex-col gap-y-1.5",
                ),
                rx.el.select(
                    rx.el.option("Mobile", on_click=SelectedType.set_value("mobile")),
                    rx.el.option("Desktop", on_click=SelectedType.set_value("desktop")),
                    default_value="Mobile",
                    bg=rx.color("gray", 2),
                    border=f"1px solid {rx.color('gray', 4)}",
                    class_name="relative flex items-center whitespace-nowrap justify-center gap-2 py-2 rounded-lg shadow-sm px-3",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip("hide"),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.bar(
                    data_key=SelectedType.value,
                    fill="var(--chart-1)",
                    radius=[2, 2, 0, 0],
                    is_animation_active=False,
                ),
                rx.recharts.y_axis(type_="number", hide=True),
                rx.recharts.x_axis(
                    data_key="date",
                    axis_line=False,
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
        class_name=chart_tooltip_content([1], "square") + " w-full p-0",
    )
```


## Active
Add a built-in legend for clarity when displaying multiple series.

```python
def barchart_v6():

    return card.root(
        card.header(
            card.title("Bar Chart - Active"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-30"
                ),
                rx.recharts.bar(
                    data_key="desktop",
                    fill="var(--chart-1)",
                    stack_id="a",
                    radius=4,
                    stroke="stroke",
                    stroke_width=2,
                    is_animation_active=False,
                ),
                rx.recharts.y_axis(type_="number", hide=True),
                rx.recharts.x_axis(
                    data_key="month",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                data=modified_data,
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
        class_name=chart_tooltip_content([1], "square") + " w-full p-0",
    )
```


## Mixed Horizontal
Create a fully custom legend layout using Reflex components.

```python
def barchart_v7():

    return card.root(
        card.header(
            card.title("Bar Chart - Mixed"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
                rx.recharts.bar(
                    data_key="visitors",
                    fill="fill",
                    radius=4,
                    is_animation_active=False,
                ),
                rx.recharts.x_axis(type_="number", hide=True, tick_size=0),
                rx.recharts.y_axis(
                    data_key="browser",
                    type_="category",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=data,
                layout="vertical",
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
        class_name=chart_tooltip_content([1], "square") + " w-full p-0",
    )
```


## Custom Legends
Show how the chart adapts across different screen sizes and layouts.

```python
def barchart_v9():

    return card.root(
        card.header(
            rx.el.div(
                card.title("Bar Chart - Multiple"),
                card.description("Showing total visitors for the last 6 months"),
                class_name="flex flex-col gap-y-1.5",
            ),
        ),
        card.content(
            rx.recharts.bar_chart(
                chart_tooltip(),
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
                rx.recharts.bar(
                    data_key="tablet",
                    fill="var(--chart-3)",
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
                height=230,
            ),
            rx.el.div(
                rx.foreach(
                    ["Desktop", "Mobile", "Tablet"],
                    lambda device, index: rx.el.div(
                        rx.el.div(
                            class_name=f"h-3 w-3 rounded-sm bg-chart-{index + 1}"
                        ),
                        rx.el.p(device, class_name="text-xs text-foreground"),
                        class_name="flex flex-row items-center gap-x-2",
                    ),
                ),
                class_name="flex items-center gap-4 justify-center",
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
        class_name=chart_tooltip_content([1, 2, 3], "square") + " w-full p-0",
    )
```

