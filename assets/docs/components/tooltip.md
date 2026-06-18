

# Tooltip

A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.

# Installation

Copy the following code into your app directory.


> **Error: 'tooltip' not found in registry**


# Usage


> **Error: 'tooltip' not found in registry**


# Anatomy 
Use the following composition to build a `Tooltip`

```python
tooltip.root(
    tooltip.trigger(),
    tooltip.portal(
        tooltip.positioner(
            tooltip.popup(
                tooltip.arrow(),
                content=...,
            ),
        ),
    ),
)
```



# Examples


## General

A simple tooltip example. Use the `dealy` prop to change how fast the tootip shows.

> **Error: 'tooltip_general' not found in registry**


## Side
Use the `side` prop in `tooltip.positioner()` to change the position of the tooltip.

> **Error: 'tooltip_sides' not found in registry**

