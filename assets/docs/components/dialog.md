

# Dialog

Custom dialog component.

# Installation

Copy the following code into your app directory.


> **Error: 'Dialog' not found in registry**


# Usage


> **Error: 'dialog' not found in registry**


# Anatomy 
Use the following composition to build a `Dialog`


```python
dialog.root(
    dialog.trigger(),
    dialog.portal(
        dialog.backdrop(),
        dialog.popup(
            dialog.title(),
            dialog.description(),
            dialog.close(),
        ),
    ),
)
```



# Examples

Below are examples demonstrating how the component can be used.

## High Level

Uses the simplified dialog() API with trigger, title, description, and content props for quick implementation.


> **Error: 'dialog_high_level' not found in registry**


## Low Level

Uses the low-level dialog.root(), dialog.trigger(), dialog.portal() etc. for full control over structure and styling


> **Error: 'dialog_low_level' not found in registry**

