---
title: "Heatmap"
description: "A heatmap component to visualize data density over time."
order: 0
---

# Heatmap

A heatmap component to visualize data density over time.

> **Note:** The Heatmap component is a fully custom implementation with no external dependencies. It's a JavaScript component with a Python API used in Reflex.

# Installation

Copy the following code into your app directory.

--INSTALL(heatmap)--

# Usage

--USAGE(heatmap)--

# Anatomy 
Use the following composition to build a `Heatmap` component.

--ANATOMY(heatmap)--

# Examples

## GitHub-Style HeatMap 

Classic GitHub contribution graph — discrete mode, default green scale.

--DEMO(heatmap_github)--

## Interpolated HeatMap 

Set the `interpolation` prop to `linear` and pass in custom colors for continuous data visualization.

--DEMO(heatmap_blue_linear)--

## Square Root HeatMap 

Set the `interpolation` prop to `sqrt` and pass in custom colors. `sqrt` scaling makes low values more visible — good when most activity is sparse.

--DEMO(heatmap_red_sqrt)--

## Discrete Color Mode 

Set the `color_mode` prop to `discrete` with a custom 5-level purple color scale. Pass any list of hex colors to color_scale — more levels = finer granularity.

--DEMO(heatmap_purple_discrete)--

## Cell Size

Set the `cell_size` prop to a number to change cell size. Setting the `interpolation` to `log` is ideal when a few extreme values dominate — compresses the high end.

--DEMO(heatmap_large_cells)--

## Minimal HeatMap

Set the `show_dow` and `show_months` props to `False` and lower the `cell_size` to get a compact, minimal heatmap. Useful as a sparkline-style indicator embedded in a dashboard card.

--DEMO(heatmap_compact)--

# API Reference

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `data` | `list[dict]` | — | **Required.** List of `{"date": "YYYY-MM-DD", "value": int}` entries. Dates not in the list render as empty cells. |
| `start_date` | `str` | — | **Required.** Start of the date range in `YYYY-MM-DD` format. |
| `end_date` | `str` | — | **Required.** End of the date range in `YYYY-MM-DD` format. |
| `color_mode` | `str` | `"discrete"` | Color strategy. `"discrete"` maps values to a fixed color scale. `"interpolate"` blends smoothly between `min_color` and `max_color`. |
| `color_scale` | `list[str]` | GitHub green scale | Discrete mode only. List of hex color strings ordered from empty → max intensity. The first entry is always used for zero-value cells. |
| `min_color` | `str` | `"#9be9a8"` | Interpolate mode only. Hex color for the lowest non-zero value. |
| `max_color` | `str` | `"#216e39"` | Interpolate mode only. Hex color for the highest value. |
| `interpolation` | `str` | `"linear"` | Interpolate mode only. Scaling function applied before color blending. `"linear"` is uniform. `"sqrt"` makes low values more visible. `"log"` compresses high-end outliers. |
| `cell_size` | `int` | `14` | Width and height of each cell in pixels. Also scales the border radius and font size proportionally. |
| `gap` | `int` | `3` | Gap between cells in pixels. |
| `show_dow` | `bool` | `True` | Whether to show Mon / Wed / Fri labels on the left axis. |
| `show_months` | `bool` | `True` | Whether to show month labels along the top axis. |
| `value_label` | `str` | `"contributions"` | Word appended to the count in the tooltip, e.g. `"commits"` → `"3 commits · Mon Jan 1 2025"`. |
| `root_class` | `str` | `"w-full overflow-x-auto"` | Tailwind classes applied to the outermost div. Controls scroll and outer layout. |
| `wrapper_class` | `str` | `"inline-block"` | Tailwind classes applied to the inner SVG wrapper div. |

## Data format

```python
data = [
    {"date": "2025-01-01", "value": 3},
    {"date": "2025-06-15", "value": 12},
]
```

Dates must be strings in `YYYY-MM-DD` format. Values must be non-negative integers.
Dates outside the `start_date`/`end_date` range are ignored. Dates within the range
that are missing from `data` render as empty cells using `var(--secondary)`.

## Color Modes

## Discrete

Values are bucketed into `len(color_scale)` levels using a linear scale from `0` to `max(value)`.
The default scale is a 5-level GitHub-style green:

```python
color_scale = [
    "var(--secondary)",  # 0  — empty
    "#9be9a8",           # 1  — low
    "#40c463",           # 2
    "#30a14e",           # 3
    "#216e39",           # 4  — high
]
```

Pass any number of hex strings to customize. More levels give finer granularity.

## Interpolate

Colors are blended smoothly between `min_color` and `max_color` using the chosen `interpolation` function.
Zero-value cells always use `var(--secondary)` regardless of `min_color`.

| Interpolation | Best for |
|---------------|----------|
| `"linear"` | Evenly distributed values |
| `"sqrt"` | Sparse data where low values need visibility |
| `"log"` | Data with extreme outliers that would wash out lower values |
