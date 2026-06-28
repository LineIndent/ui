---
title: "Spinner"
description: "An indicator that can be used to show a loading state."
order: 0
---

# Spinner
An indicator that can be used to show a loading state.

> **Note:** The Spinner component is a fully custom implementation using in-line **svg** with no external dependencies.

# Installation 
Copy the following code into your app directory.

--INSTALL(spinner)--

# Anatomy
Use the following composition to build a `Spinner` component.

--ANATOMY(spinner)--

# Examples

## Size
 
Use the `size-*` utility class to change the size of the spinner.
 
--DEMO(spinner_size)--

## Button
 
Add a spinner to a button to indicate a loading state. Place it before the label for a start position.
 
--DEMO(spinner_button)--

## Badge
 
Add a spinner to a badge to indicate a loading or syncing state.
 
--DEMO(spinner_badge)--

## Marker
 
Combine `Spinner` with `Marker` and the `shimmer` utility for animated streaming status indicators. Set `role="status"` so assistive technology announces the update.
 
--DEMO(spinner_marker)--

# API Reference
 
| Prop         | Type   | Default | Description                                      |
|--------------|--------|---------|--------------------------------------------------|
| `class_name` | `str`  | `""`    | Additional Tailwind classes applied to the icon. |
| `**props`    | `dict` | —       | Any valid HTML attribute forwarded to the element (`role`, `aria_label`, etc.). |
