

# Breadcrumb

Displays the path to the current resource using a hierarchy of links.

# Installation

Copy the following code into your app directory.


> **Error: 'breadcrumb' not found in registry**



# Anatomy 
Use the following composition to build a `Breadcrumb`


```python
breadcrumb(
    breadcrumb_list(
        breadcrumb_item(
            breadcrumb_link(),
        ),
        breadcrumb_separator(),
        breadcrumb_item(
            breadcrumb_page(),
        ),
    ),
)
```


# Examples

## Basic Demo
A basic breadcrumb showing the default navigation structure.


> **Error: 'breadcrumb_basic_demo' not found in registry**


## Simple Breadcrumb
A minimal breadcrumb with plain text links.


> **Error: 'breadcrumb_simple_breadcrumb' not found in registry**


## Icon Breadcrumb
A breadcrumb that includes icons alongside link labels.


> **Error: 'breadcrumb_icon_breadcrumb' not found in registry**


## Custom Separator
A breadcrumb with a customized separator between items.


> **Error: 'breadcrumb_custom_separator' not found in registry**
