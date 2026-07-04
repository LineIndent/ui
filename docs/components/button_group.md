---
title: "Button Group"
description: "A container that groups related buttons together with consistent styling."
order: 3
---

# Button Group

A container that groups related buttons together with consistent styling.

# Installation

Copy the following code into your app directory.

--INSTALL(button_group)--

# Usage

--USAGE(button_group)--

# Anatomy 
Use the following composition to build a `Button Group` component.

--ANATOMY(button_group)--


# Accessibility

- The `button_group.root` component has the `role` attribute set to `group`.
- Use `Tab` to navigate between the buttons in the group.
- Use `aria-label` or `aria-labelledby` to label the button group.

# Examples

## Orientation

Set the `orientation` prop to change the button group layout.

--DEMO(button_group_orientation)--

## Size

Control the size of buttons using the `size` prop on individual buttons.

--DEMO(button_group_size)--

## Separator

The `button_group.separator` component visually divides buttons within a group.

Buttons with variant `outline` do not need a separator since they have a border. For other variants, a separator is recommended to improve the visual hierarchy.

--DEMO(button_group_separator)--

## Split

Create a split button group by adding two buttons separated by a `button_group.separator`.

--DEMO(button_group_split)--

## Input

Wrap an `input` component with buttons.

--DEMO(button_group_input)--

## Dropdown Menu

Create a split button group with a `menu` component.

--DEMO(button_group_dropdown)--


## Select

Pair with a `select` component.

--DEMO(button_group_select)--

# API Reference

## button_group.root

The `button_group.root` component is a container that groups related buttons together with consistent styling.

| Prop          | Type                         | Default        |
| ------------- | ---------------------------- | -------------- |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` |


## button_group.separator

The `button_group.separator` component visually divides buttons within a group.

| Prop          | Type                         | Default      |
| ------------- | ---------------------------- | ------------ |
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` |


## button_group.text

Use this component to display text within a button group.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `*children` | `rx.Component` | `false` |


The `button_group.text` accepts `*children` so any interactive component passed to it will be rendered. Use it to render a custom component as the text, for example a label.
