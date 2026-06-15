

# Popover

Custom popover component.

# Installation

Copy the following code into your app directory.


> **Error: 'Popover' not found in registry**


# Usage


> **Error: 'popover' not found in registry**


# Anatomy 
Use the following composition to build a `Popover`


```python
popover.root(
    popover.trigger(),
    popover.portal(
        popover.backdrop(),
        popover.positioner(
            popover.popup(
                popover.header(
                    popover.title(),
                    popover.description(),
                ),
                popover.close(),
            ),
        ),
    ),
)
```



# Example
A basic popover that appears when the user clicks the trigger button.


## Basic
A simple popover with a header, title, and description.


> **Error: 'popover_basic' not found in registry**


## Aligns
Use the `align` prop to control the alignment.


> **Error: 'popover_aligns' not found in registry**

