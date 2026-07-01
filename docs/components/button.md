---
title: "Button"
description: "Displays a button or a component that looks like a button."
order: 3
---

# Button

Displays a button or a component that looks like a button.

# Installation

Copy the following code into your app directory.

--INSTALL(button)--

# Usage

--USAGE(button)--

# Anatomy 
Use the following composition to build a `Button` component.

--ANATOMY(button)--

# Examples

## Sizes

Use the `size` prop to change the size of the button.

--DEMO(button_size)--

## Default

--DEMO(button_default)--

## Secondary

--DEMO(button_secondary)--

## Outline

--DEMO(button_outline)--

## Ghost

--DEMO(button_ghost)--

## Link

--DEMO(button_link)--

## Destructive

--DEMO(button_destructive)--

## Icon

--DEMO(button_icon)--

## With Icon

Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the icon for the correct spacing.

--DEMO(button_with_icon)--

## Rounded

Use the `rounded-full` class to make the button rounded.

--DEMO(button_rounded)--

## Spinner

Render a `spinner()` component inside the button to show a loading state. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the spinner for the correct spacing.

--DEMO(button_loading)--

## As Link

You can use the `button_variants` helper function to make a link look like a button.

Do **not** use `button(rx.el.a(...))` for links. The Base UI `Button` component always applies `role="button"`, which overrides the semantic link role on `<a>` elements. Use `button_variants` with a plain `rx.el.a` tag instead to cleanly generate the necessary classes as a dynamic Reflex `Var`.

--DEMO(button_render)--


# API Reference

## Button

The `Button` component is a wrapper around the `button` element that adds a variety of styles and functionality.

| Prop      | Type                                                                                 | Default     |
| --------- | ------------------------------------------------------------------------------------ | ----------- |
| `variant` | `"default" \| "outline" \| "ghost" \| "destructive" \| "secondary" \| "link"`        | `"default"` |
| `size`    | `"default" \| "xs" \| "sm" \| "lg" \| "icon" \| "icon-xs" \| "icon-sm" \| "icon-lg"` | `"default"` |
