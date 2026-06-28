

# Marker
The Marker component displays inline conversation markers such as status updates, system notes, bordered rows, and labeled separators. 


# Installation 
Copy the following code into your app directory.

### CLI

```bash
buridan add component marker
```

### Manual Installation

```python
"""Marker component — a flexible inline label with icon and content slots."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..utils.twmerge import cn

MarkerVariant = Literal["default", "separator", "border"]


class ClassNames:
    ROOT = (
        "group/marker relative flex min-h-4 w-full items-center gap-2 "
        "text-left text-sm text-muted-foreground"
    )

    VARIANTS: dict[str, str] = {
        "default": "",
        "separator": (
            "before:mr-1 before:h-px before:min-w-0 before:flex-1 before:bg-border "
            "after:ml-1 after:h-px after:min-w-0 after:flex-1 after:bg-border"
        ),
        "border": "border-b border-border pb-2",
    }

    ICON = "size-4 shrink-0"
    CONTENT = (
        "min-w-0 break-words "
        "group-data-[variant=separator]/marker:flex-none "
        "group-data-[variant=separator]/marker:text-center"
    )


def marker_root(
    *children,
    variant: MarkerVariant = "default",
    class_name: str = "",
    **props,
) -> rx.Component:
    """Root marker container."""
    return rx.el.div(
        *children,
        data_slot="marker",
        data_variant=variant,
        class_name=cn(
            ClassNames.ROOT,
            ClassNames.VARIANTS.get(variant, ""),
            class_name,
        ),
        **props,
    )


def marker_icon(*children, class_name: str = "", **props) -> rx.Component:
    """Icon slot — wraps any icon at a fixed size-4."""
    return rx.el.span(
        *children,
        data_slot="marker-icon",
        aria_hidden="true",
        class_name=cn(ClassNames.ICON, class_name),
        **props,
    )


def marker_content(*children, class_name: str = "", **props) -> rx.Component:
    """Content slot — handles text wrapping and separator alignment."""
    return rx.el.span(
        *children,
        data_slot="marker-content",
        class_name=cn(ClassNames.CONTENT, class_name),
        **props,
    )


class Marker(ComponentNamespace):
    """Marker namespace."""

    root = staticmethod(marker_root)
    icon = staticmethod(marker_icon)
    content = staticmethod(marker_content)

    class_names = ClassNames


marker = Marker()
```


# Anatomy
Use the following composition to build a `Marker` component.


```python
marker.root(
    marker.icon(),
    marker.content(),
)
```


# Examples

## Variants

Use `variant` to switch between an inline marker, bordered row, and labeled separator.


```python
def marker_variants_demo():
    return rx.el.div(
        # Default Marker
        marker.root(
            marker.content("A default marker for inline notes."),
        ),
        # Separator Marker
        marker.root(
            marker.content("A separator marker"),
            variant="separator",
        ),
        # Border Marker
        marker.root(
            marker.content("A border marker for row boundaries."),
            variant="border",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


| Variant     | Description                                          |
| ----------- | ---------------------------------------------------- |
| `default`   | An inline marker for status, notes, and actions.     |
| `border`    | A default marker with a bottom border under the row. |
| `separator` | A centered label with divider lines on each side.    |

## Status

Set `role="status"` and include a [`Spinner`](/docs/components/spinner) for streaming or in-progress markers so updates are announced.


```python
def marker_status_demo():
    return rx.el.div(
        marker.root(
            marker.icon(spinner()),
            marker.content("Compacting conversation"),
            role="status",
        ),
        marker.root(
            marker.icon(spinner()),
            marker.content("Running tests"),
            variant="separator",
            role="status",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


## Shimmer

Add the [`shimmer`](/docs/utilities/shimmer) utility class to `marker.content` for an animated streaming-text effect. The utility ships with the `buridan` package — see the shimmer docs for installation.


```python
def marker_shimmer():
    return rx.el.div(
        marker.root(
            marker.content("Thinking...", class_name="shimmer"),
            role="status",
        ),
        marker.root(
            marker.content("Reading 4 files", class_name="shimmer"),
            variant="separator",
            role="status",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


## Separator

Use the `separator` variant for labeled dividers, such as dates or section breaks, in a conversation.


```python
def marker_separator():
    return rx.el.div(
        marker.root(
            marker.content("Today"),
            variant="separator",
        ),
        marker.root(
            marker.content("Worked for 42s"),
            variant="separator",
        ),
        marker.root(
            marker.content("Conversation compacted"),
            variant="separator",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


## Border

Use the `border` variant for status rows that should keep the default marker alignment while separating the next row.


```python
def marker_border():
    return rx.el.div(
        marker.root(
            marker.icon(hi("GitBranchIcon")),
            marker.content("Switched to release-candidate"),
            variant="border",
        ),
        marker.root(
            marker.icon(hi("Search01Icon")),
            marker.content("Reviewed 8 related files"),
            variant="border",
        ),
        marker.root(
            marker.icon(hi("File01Icon")),
            marker.content("Opened implementation notes"),
            variant="border",
        ),
        class_name="flex w-full max-w-sm flex-col gap-3 py-12",
    )
```


## With Icon

Use `marker.icon` to render an icon alongside the content. Use `flex-col` to stack the icon above the content.


```python
def marker_with_icon():
    return rx.el.div(
        marker.root(
            marker.icon(hi("GitBranchIcon")),
            marker.content("Switched to a new branch"),
        ),
        marker.root(
            marker.icon(hi("Search01Icon")),
            marker.content("Explored 4 files"),
            variant="separator",
        ),
        marker.root(
            marker.icon(hi("BookOpenCheckIcon")),
            marker.content("Syncing completed"),
            class_name="flex-col",
        ),
        class_name="flex w-full max-w-sm flex-col gap-12 py-12",
    )
```


## Links and Buttons

Turn a marker into a link or button with.


```python
def marker_link_button():
    return rx.el.div(
        marker.root(
            rx.el.a(
                marker.icon(hi("GitBranchIcon")),
                marker.content("View the pull request"),
                href="#links-and-buttons",
                class_name="group flex flex-row items-center gap-x-2 underline transition-colors hover:text-foreground",
            ),
            variant="default",
        ),
        marker.root(
            rx.el.button(
                marker.icon(
                    hi("ArrowMoveUpRightIcon"),
                    class_name="group-hover:text-foreground transition-colors",
                ),
                marker.content(
                    "Revert this change",
                    class_name="group-hover:text-foreground transition-colors",
                ),
                type="button",
                class_name="group flex flex-row items-center gap-x-2 transition-colors",
                on_click=rx.toast("You clicked the revert button"),
            ),
            variant="default",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12 justify-center",
    )
```


## Accessibility

`marker.root` is presentational by default. The correct semantics depend on how you use it, so choose the role based on intent rather than relying on a single default.

## Status and Progress

For streaming or progress markers such as "Thinking..." or a running tool, set `role="status"` so assistive tech announces the update as it appears. `marker.root` forwards `role` to the underlying element.

```python
marker.root(
    marker.icon(spinner()),
    marker.content("Compacting conversation"),
    role="status",
)
```

## Labeled Separators

A `separator` that carries text, such as a date or a section label, needs no role. The divider lines are decorative CSS pseudo-elements, and the text is announced as ordinary content.

```python
marker.root(
    marker.content("Today"),
    variant="separator",
)
```

> **Note:** Do not add `role="separator"` to a labeled divider. A separator takes its accessible name from `aria-label`, not from its text, and its contents are treated as presentational, so the visible label would not be announced. Reserve `role="separator"` for a divider with no meaningful text.

## Bordered Markers

A bordered marker keeps the same semantics as the default marker. The bottom border is decorative, so choose `role="status"` or no role based on the marker's purpose.

```python
marker.root(
    marker.icon(rx.icon("file-text", size=14)),
    marker.content("Opened implementation notes"),
    variant="border",
)
```

## Decorative Icons

`marker.icon` is decorative and hidden from assistive tech with `aria-hidden`, so the adjacent `marker.content` carries the meaning. For an icon-only marker, provide an `aria_label` so it is not announced as empty.

```python
marker.root(
    marker.icon(rx.icon("check", size=14)),
    aria_label="Synced",
)
```

## Interactive Markers

When a marker links or triggers an action, render it as an `rx.link` or pass `on_click` so it is focusable and exposes the correct role.

```python
rx.link(
    marker.root(
        marker.icon(rx.icon("file-text", size=14)),
        marker.content("Explored 4 files"),
    ),
    href="/files",
)
```

# API Reference

## marker.root

The root marker element.

| Prop         | Type                                      | Default     | Description                                      |
|--------------|-------------------------------------------|-------------|--------------------------------------------------|
| `variant`    | `"default" \| "border" \| "separator"`   | `"default"` | The marker layout.                               |
| `class_name` | `str`                                     | `""`        | Additional classes to apply to the root element. |
| `**props`    | `dict`                                    | —           | Any valid HTML attribute (`role`, `aria_label`). |

## marker.icon

A decorative icon slot. Hidden from assistive tech with `aria-hidden`.

| Prop         | Type  | Default | Description                                   |
|--------------|-------|---------|-----------------------------------------------|
| `class_name` | `str` | `""`    | Additional classes to apply to the icon slot. |

## marker.content

The marker text content.

| Prop         | Type  | Default | Description                                      |
|--------------|-------|---------|--------------------------------------------------|
| `class_name` | `str` | `""`    | Additional classes to apply to the content slot. |
| `**props`    | `dict`| —       | Any valid HTML attribute forwarded to the span.  |
