---
title: "Area Chart"
description: "A versatile chart for visualizing quantitative data trends over time or categories, supporting gradients, stacking, and custom legends."
order: 0
---

# Area Chart

Area Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

# Usage
The chart tooltip components are available in the `base_ui` library.

--CODE_FILE(_ChartTooltip)--

# Examples

## Basic
A minimal example showing a single series with a smooth gradient fill.
--DEMO(areachart_v1)--

## Linear
Displays data using straight line segments between points.
--DEMO(areachart_v2)--

## Step
Renders the chart with stepped transitions, ideal for discrete intervals.
--DEMO(areachart_v3)--

## Stacked
Visualizes multiple data series stacked on top of each other for cumulative comparison.
--DEMO(areachart_v4)--

## Dynamic
Demonstrates how data or series can update interactively in real-time.
--DEMO(areachart_v5)--

## Legend
Adds a built-in legend for easy series identification.
--DEMO(areachart_v6)--

## Axes
Shows full control over axis configuration, labels, and styling.
--DEMO(areachart_v7)--

## Custom Legends
Implements a user-defined legend layout for better presentation control.
--DEMO(areachart_v8)--

## Step with Gradient
Combines stepped transitions with a smooth color gradient for visual emphasis.
--DEMO(areachart_v9)--

## Custom Legend and Axes
A complete example with custom legends, axes, and advanced styling combined.
--DEMO(areachart_v10)--
