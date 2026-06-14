

# Pie Chart

Pie Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

# Examples
Below are examples demonstrating how these components and charts can be used.

## Basic
A minimal example showing proportional data distribution in a circular format.

```python
def piechart_v1():

    return card.root(
        card.header(
            card.title("Pie Chart"),
            card.description("Browser distribution - Last 6 months"),
        ),
        card.content(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.foreach(
                        range(5),
                        lambda color, index: rx.recharts.cell(
                            fill=f"var(--chart-{index + 1})",
                        ),
                    ),
                    data=data,
                    data_key="visitors",
                    name_key="browser",
                    stroke_width=2,
                    stroke="var(--background)",
                    is_animation_active=False,
                ),
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
        class_name="w-full p-0",
    )
```


## Hovering Labels
Displays labels that appear dynamically when hovering over chart segments.

```python
def piechart_v2():

    return card.root(
        card.header(
            card.title("Pie Chart - Hovering Labels"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.foreach(
                        range(5),
                        lambda color, index: rx.recharts.cell(
                            fill=f"var(--chart-{index + 1})",
                        ),
                    ),
                    data=data,
                    data_key="visitors",
                    name_key="browser",
                    stroke_width=2,
                    stroke="var(--background)",
                    label=True,
                    is_animation_active=False,
                ),
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
        class_name="w-full p-0",
    )
```


## Inner Labels
Shows labels positioned inside each pie segment for compact presentation.

```python
def piechart_v3():

    return card.root(
        card.header(
            card.title("Pie Chart - Inner Labels"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.recharts.label_list(
                        data_key="browser",
                        position="inside",
                        fill="var(--background)",
                        custom_attrs={"fontSize": "12px", "fontWeight": "bold"},
                    ),
                    rx.foreach(
                        range(5),
                        lambda color, index: rx.recharts.cell(
                            fill=f"var(--chart-{index + 1})",
                        ),
                    ),
                    data=data,
                    data_key="visitors",
                    name_key="browser",
                    stroke_width=2,
                    stroke="var(--background)",
                    is_animation_active=False,
                ),
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
        class_name="w-full p-0",
    )
```


## Legend
Adds a built-in legend for easy segment identification and reference.

```python
def piechart_v4():

    return card.root(
        card.header(
            card.title("Pie Chart - Legend"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.foreach(
                        range(5),
                        lambda color, index: rx.recharts.cell(
                            fill=f"var(--chart-{index + 1})",
                        ),
                    ),
                    data=data,
                    data_key="visitors",
                    name_key="browser",
                    stroke_width=2,
                    stroke="var(--background)",
                    is_animation_active=False,
                ),
                rx.recharts.legend(class_name="text-xs font-medium"),
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
        class_name="w-full p-0",
    )
```


## Doughnut
Renders the pie chart with a hollow center for a modern doughnut style.

```python
def piechart_v5():

    return card.root(
        card.header(
            card.title("Pie Chart - Doughnut"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.foreach(
                        range(5),
                        lambda color, index: rx.recharts.cell(
                            fill=f"var(--chart-{index + 1})",
                        ),
                    ),
                    data=data,
                    data_key="visitors",
                    name_key="browser",
                    stroke_width=2,
                    stroke="var(--background)",
                    inner_radius=60,
                    is_animation_active=False,
                ),
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
        class_name="w-full p-0",
    )
```


## Active
Demonstrates interactive segment highlighting and selection states.

```python
def piechart_v6():

    return card.root(
        card.header(
            card.title("Pie Chart - Active"),
            card.description("Showing total visitors for the last 6 months"),
        ),
        card.content(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.foreach(
                        range(5),
                        lambda color, index: rx.recharts.cell(
                            fill=f"var(--chart-{index + 1})",
                        ),
                    ),
                    data=data,
                    data_key="visitors",
                    name_key="browser",
                    stroke_width=2,
                    stroke="var(--background)",
                    inner_radius=60,
                    custom_attrs={
                        "activeIndex": 1,
                        "activeShape": {"outerRadius": 110},
                    },
                    is_animation_active=False,
                ),
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
        class_name="w-full p-0",
    )
```

