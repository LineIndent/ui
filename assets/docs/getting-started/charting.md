

# Introduction
Reflex chart components compile to Recharts under the hood, making them highly customizable and easy to integrate with your data. By leveraging Reflex, you can effortlessly create interactive, dynamic charts with minimal configuration. Whether you're building line charts, bar charts, or complex data visualizations, Reflex streamlines the process while offering the flexibility of Recharts' robust features.

# Setting Up Your Environment
If you haven't done so already, make sure you have the latest version of Reflex installed on your machine. Visit the installation guide to walk you through the installation process.

# Data & State Management
Most charts in this guide use static data as an example. This approach helps keep the UI simple, clean, and the site fast. However, real-world applications will likely require the use of Reflex's **state** to build full-stack data applications, or any application that involves dynamic data handling.


> **Error: 'charting_state_example' not found in registry**


# Creating Your Chart
The Buridan UI library includes 7 chart types: [Area](/charts/area-charts), [Bar](/charts/bar-charts), [Line](/charts/line-charts), [Pie](/charts/pie-charts), [Doughnut](/charts/doughnut-charts), [Radar](/charts/radar-charts), and [Scatter](/charts/scatter-charts). For this walkthrough, we’ll focus on **Area Charts**. To set up the area chart, import your state class inside the file that will contain your area chart component, then create the following function:


> **Error: 'area_chart_example' not found in registry**


- `data_key`: Defines which field will be used for y-axis values.
- `data`: Links the chart to your state data array.

# Customization: Cartesian Grid
The Cartesian Grid component in Reflex allows you to customize the grid of your chart. By default, most charts come with a basic grid, but you can easily modify it to suit your design needs.

To add a customized Cartesian grid to your chart, use the following code snippet:


> **Error: 'cartesian_grid_example' not found in registry**


- `horizontal=True`: Enable horizontal lines.
- `vertical=False`: Disable vertical lines.
- `class_name="opacity-25"`: Low opacity for subtlety.

# Customization: XAxis
The XAxis component in Reflex allows you to customize the appearance and behavior of the horizontal axis in your chart. It controls things like axis labels, tick marks, and line visibility.The following also applies to the YAxis, however, in order to keep a consistent UI, the buridan charts typically lack the YAxis.

To customize the X Axis, you can use the following code snippet:


> **Error: 'xaxis_example' not found in registry**


- `axis_line=False`: Hide the axis line.
- `tick_line=False`: Hide tick marks.
- `interval="preserveStartEnd"`: Always show first and last ticks.

# Customization: Tooltip (Advanced)
The ToolTip component in Reflex is highly customizable and allows you to create rich, interactive tooltips for your charts. It provides a variety of props for controlling animations, styling, and behavior of the tooltip content. Since it has many props, we’ll focus on how you can customize its styles using a dictionary instead of a data class for a more flexible approach.

To customize the tooltip with a dictionary, use the following code snippet:


> **Error: 'tooltip_example' not found in registry**


In this example, we are using a dictionary to define various style properties for the tooltip, such as `item_style`, `label_style`, and `content_style`. These properties control the look and feel of the tooltip, from the color of the text to the layout of the content. The `general_style` prop is used to apply additional custom styles to specific parts of the tooltip.

# Final Thoughts
In this walkthrough, we covered how to set up and customize your Reflex charts. We explored setting up state, creating a chart, customizing the Cartesian grid, X axis, and advanced tooltip features. With Reflex, you can build highly interactive and customizable charts that are easy to integrate into your applications.
