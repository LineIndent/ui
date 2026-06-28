

# Spinner
An indicator that can be used to show a loading state.

> **Note:** The Spinner component is a fully custom implementation using in-line **svg** with no external dependencies.

# Installation 
Copy the following code into your app directory.

### CLI

```bash
buridan add component spinner
```

### Manual Installation

```python
"""Spinner component."""

import reflex as rx
from reflex_components_core.el import svg

from ..utils.twmerge import cn


def spinner(class_name: str = "", **props) -> rx.Component:
    return svg(
        svg.path(
            opacity="0.2",
            d="M14.66 8a6.666 6.666 0 1 1-13.333 0 6.666 6.666 0 0 1 13.333 0Z",
            stroke="currentColor",
            stroke_width="1.5",
        ),
        svg.path(
            d="M13.413 11.877A6.666 6.666 0 1 1 10.26 1.728",
            stroke="currentColor",
            stroke_width="1.5",
        ),
        xmlns="http://www.w3.org/2000/svg",
        custom_attrs={"viewBox": "0 0 16 16"},
        class_name=cn("size-4 animate-spin fill-none", class_name),
        data_slot="spinner",
        role="status",
        **props,
    )
```


# Anatomy
Use the following composition to build a `Spinner` component.


```python
spinner()
```


# Examples

## Size
 
Use the `size-*` utility class to change the size of the spinner.
 

```python
def spinner_size():
    return rx.el.div(
        spinner(class_name="size-3"),
        spinner(class_name="size-4"),
        spinner(class_name="size-6"),
        spinner(class_name="size-8"),
        class_name="flex items-center gap-6",
    )
```


## Button
 
Add a spinner to a button to indicate a loading state. Place it before the label for a start position.
 

```python
def spinner_button():
    return rx.el.div(
        button(spinner(), "Loading...", disabled=True, size="sm"),
        button(spinner(), "Please wait", disabled=True, size="sm", variant="outline"),
        button(spinner(), "Processing", disabled=True, size="sm", variant="secondary"),
        class_name="flex flex-col items-center gap-4",
    )
```


## Badge
 
Add a spinner to a badge to indicate a loading or syncing state.
 

```python
def spinner_badge():
    return rx.el.div(
        badge(spinner(), "Syncing"),
        badge(spinner(), "Updating", variant="secondary"),
        badge(spinner(), "Processing", variant="outline"),
        class_name="flex items-center gap-4",
    )
```


## Marker
 
Combine `Spinner` with `Marker` and the `shimmer` utility for animated streaming status indicators. Set `role="status"` so assistive technology announces the update.
 

```python
def spinner_marker():
    return rx.el.div(
        marker.root(
            marker.icon(spinner()),
            marker.content("Thinking…", class_name="shimmer w-fit"),
            role="status",
        ),
        marker.root(
            marker.icon(spinner()),
            marker.content("Generating response…", class_name="shimmer w-fit"),
            variant="border",
            role="status",
        ),
        marker.root(
            marker.icon(spinner()),
            marker.content("Processing"),
            variant="separator",
            role="status",
        ),
        class_name="flex w-full max-w-sm flex-col gap-6",
    )
```


# API Reference
 
| Prop         | Type   | Default | Description                                      |
|--------------|--------|---------|--------------------------------------------------|
| `class_name` | `str`  | `""`    | Additional Tailwind classes applied to the icon. |
| `**props`    | `dict` | —       | Any valid HTML attribute forwarded to the element (`role`, `aria_label`, etc.). |
