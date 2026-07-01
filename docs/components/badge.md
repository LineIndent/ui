---
title: "Badge"
description: "Displays a badge or a component that looks like a badge."
order: 2
---

# Badge

Displays a badge or a component that looks like a badge.

# Installation

Copy the following code into your app directory.

--INSTALL(badge)--

# Usage

--USAGE(badge)--

# Anatomy 
Use the following composition to build a `Badge` component.

--ANATOMY(badge)--

# Examples

## Variants

Use the `variant` prop to change the variant of the badge.

--DEMO(badge_with_variants)--

## With Icons

You can render an icon inside the badge. Use `data-icon="inline-start"` to render the icon on the left and `data-icon="inline-end"` to render the icon on the right.

--DEMO(badge_with_icon)--

## With Spinner

You can render a spinner inside the badge. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` prop to the spinner.

--DEMO(badge_with_spinner)--

## Link

You can pass in `rx.el.a` to turn a badge into a link. The `badge` component accepts `*children` so any interactive element can be passed to it. 

--DEMO(badge_as_link)--

## Custom Colors

You can customize the colors of a badge by adding custom classes such as `bg-green-50 dark:bg-green-800` to the `badge` component.

--DEMO(badge_custom_colors)--


# API Reference

## badge

The `badge` component displays a badge or a component that looks like a badge.

| Prop        | Type                                                                          | Default     |
| ----------- | ----------------------------------------------------------------------------- | ----------- |
| `variant`   | `"default" \| "secondary" \| "destructive" \| "outline" \| "ghost" \| "link"` | `"default"` |
| `class_name` | `string`                                                                      | -           |
