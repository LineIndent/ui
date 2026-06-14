

# Radar Chart

Radar Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

# Examples
Below are examples demonstrating how these components and charts can be used.

## Basic
A minimal example showing multivariate data in a radial layout with filled areas.

```python
def radar_v1():

    return card.root(
        card.header(
            card.title("Radar Chart"),
            card.description("Player performance across categories"),
        ),
        card.content(
            rx.recharts.radar_chart(
                rx.recharts.polar_grid(class_name="opacity-30"),
                rx.recharts.polar_angle_axis(
                    data_key="category",
                    custom_attrs={"fontSize": "12px"},
                ),
                rx.recharts.radar(
                    data_key="score",
                    stroke="var(--chart-1)",
                    fill="var(--chart-1)",
                    fill_opacity=0.6,
                    is_animation_active=False,
                ),
                data=stats_data,
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


## Stroke with Dots
Displays data points with visible markers along the radar lines for clarity.

```python
def radar_v2():

    return card.root(
        card.header(
            card.title("Radar Chart - Dots"),
            card.description("Detailed performance metrics"),
        ),
        card.content(
            rx.recharts.radar_chart(
                rx.recharts.polar_grid(class_name="opacity-30"),
                rx.recharts.polar_angle_axis(
                    data_key="category",
                    custom_attrs={"fontSize": "12px"},
                ),
                rx.recharts.radar(
                    data_key="score",
                    dot=True,
                    stroke="var(--chart-1)",
                    fill="var(--chart-1)",
                    fill_opacity=0.6,
                    is_animation_active=False,
                ),
                data=stats_data,
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


## Stacked
Visualizes multiple data series layered on top of each other for comparison.

```python
def radar_v3():

    return card.root(
        card.header(
            card.title("Radar Chart - Stacked"),
            card.description("Comparing score against average"),
        ),
        card.content(
            rx.recharts.radar_chart(
                rx.recharts.polar_grid(class_name="opacity-30"),
                rx.recharts.polar_angle_axis(
                    data_key="category",
                    custom_attrs={"fontSize": "12px"},
                ),
                rx.recharts.radar(
                    data_key="average",
                    stroke="var(--chart-2)",
                    fill="var(--chart-2)",
                    fill_opacity=0.4,
                    is_animation_active=False,
                ),
                rx.recharts.radar(
                    data_key="score",
                    stroke="var(--chart-1)",
                    fill="var(--chart-1)",
                    fill_opacity=0.7,
                    is_animation_active=False,
                ),
                data=stats_data,
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


## Lines Only
Shows only the outline strokes without filled areas for a cleaner look.

```python
def radar_v4():

    return card.root(
        card.header(
            card.title("Radar Chart - Lines Only"),
            card.description("Linear comparison between score and average"),
        ),
        card.content(
            rx.recharts.radar_chart(
                rx.recharts.polar_grid(class_name="opacity-30"),
                rx.recharts.polar_angle_axis(
                    data_key="category",
                    custom_attrs={"fontSize": "12px"},
                ),
                rx.recharts.radar(
                    data_key="average",
                    stroke="var(--chart-2)",
                    fill="none",
                    stroke_width=2,
                    is_animation_active=False,
                ),
                rx.recharts.radar(
                    data_key="score",
                    stroke="var(--chart-1)",
                    fill="none",
                    stroke_width=2,
                    is_animation_active=False,
                ),
                data=stats_data,
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


## Circle Grid
Uses circular grid lines instead of polygon shapes for the background.

```python
def radar_v5():

    return card.root(
        card.header(
            card.title("Radar Chart - Circle Grid"),
            card.description("Performance visual with circular boundaries"),
        ),
        card.content(
            rx.recharts.radar_chart(
                rx.recharts.polar_grid(grid_type="circle", class_name="opacity-30"),
                rx.recharts.polar_angle_axis(
                    data_key="category",
                    custom_attrs={"fontSize": "12px"},
                ),
                rx.recharts.radar(
                    data_key="score",
                    dot=True,
                    stroke="var(--chart-1)",
                    fill="var(--chart-1)",
                    fill_opacity=0.6,
                    is_animation_active=False,
                ),
                data=stats_data,
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


## Filled Grid
Renders the grid with filled background sections for enhanced visual contrast.

```python
def radar_v6():

    return card.root(
        card.header(
            card.title("Radar Chart - Filled Grid"),
            card.description("Player performance across categories"),
        ),
        card.content(
            rx.recharts.radar_chart(
                rx.recharts.polar_grid(
                    grid_type="circle",
                    class_name="opacity-20 fill-primary stroke-input",
                ),
                rx.recharts.polar_angle_axis(
                    data_key="category",
                    axis_line_type="circle",
                    class_name="!text-xs stroke-input",
                ),
                rx.recharts.radar(
                    data_key="score",
                    dot=False,
                    fill="white",
                    stroke="none",
                    is_animation_active=False,
                ),
                data=stats_data,
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

