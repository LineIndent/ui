---
title: "Marker"
description: "Displays an inline status, system note, bordered row, or labeled separator in a conversation."
order: 0
---

# Marker
The Marker component displays inline conversation markers such as status updates, system notes, bordered rows, and labeled separators. 


# Installation 
Copy the following code into your app directory.

--INSTALL(marker)--

# Anatomy
Use the following composition to build a `Marker` component.

--ANATOMY(marker)--

# Examples

## Variants

Use `variant` to switch between an inline marker, bordered row, and labeled separator.

--DEMO(marker_variants_demo)--

| Variant     | Description                                          |
| ----------- | ---------------------------------------------------- |
| `default`   | An inline marker for status, notes, and actions.     |
| `border`    | A default marker with a bottom border under the row. |
| `separator` | A centered label with divider lines on each side.    |

## Status

Set `role="status"` and include a [`Spinner`](/docs/components/spinner) for streaming or in-progress markers so updates are announced.

--DEMO(marker_status_demo)--

## Shimmer

Add the [`shimmer`](/docs/utilities/shimmer) utility class to `marker.content` for an animated streaming-text effect. The utility ships with the `buridan` package — see the shimmer docs for installation.

--DEMO(marker_shimmer)--

## Separator

Use the `separator` variant for labeled dividers, such as dates or section breaks, in a conversation.

--DEMO(marker_separator)--

## Border

Use the `border` variant for status rows that should keep the default marker alignment while separating the next row.

--DEMO(marker_border)--

## With Icon

Use `marker.icon` to render an icon alongside the content. Use `flex-col` to stack the icon above the content.

--DEMO(marker_with_icon)--

## Links and Buttons

Turn a marker into a link or button with.

--DEMO(marker_link_button)--

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
