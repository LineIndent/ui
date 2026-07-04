---
title: "Input Group"
description: "Add addons, buttons, and helper content to inputs."
order: 0
---

# Input Group

Add addons, buttons, and helper content to inputs.

# Installation

Copy the following code into your app directory.

--INSTALL(input_group)--

# Usage

--USAGE(input_group)--

# Anatomy 
Use the following composition to build an `Input Group` component.

--ANATOMY(input_group)--

# Align

Use the `align` prop on `input_group.addon` to position the addon relative to the input.

>For proper focus management, **input_group.addon** should always be placed after **input_group.input** or **input_group.textarea** in the DOM. Use the **align** prop to visually position the addon.


## inline-start

Use `align="inline-start"` to position the addon at the start of the input. This is the default.

--DEMO(input_group_inline_start)--

## inline-end

Use `align="inline-end"` to position the addon at the end of the input.

--DEMO(input_group_inline_end)--

## block-start

Use `align="block-start"` to position the addon above the input.

--DEMO(input_group_block_start)--

## block-end

Use `align="block-end"` to position the addon below the input.

--DEMO(input_group_block_end)--

# Examples

## Icons
--DEMO(input_group_icons)--

## Text
--DEMO(input_group_text)--

## Button
--DEMO(input_group_button)--

## Spinner
--DEMO(input_group_spinner)--

## Dropdown
--DEMO(input_group_dropdown)--

# API Reference

## input_group.root

The main component that wraps inputs and addons.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` |         |


## input_group.addon

Displays icons, text, buttons, or other content alongside inputs.

>For proper focus navigation, the `input_group.addon` component should be placed after the input. Set the `align` prop to position the addon.

| Prop        | Type                                                             | Default          |
| ----------- | ---------------------------------------------------------------- | ---------------- |
| `align`     | `"inline-start" \| "inline-end" \| "block-start" \| "block-end"` | `"inline-start"` |
| `class_name` | `string`                                                         |                  |


>For **input_group.input**, use the **inline-start** or **inline-end** alignment. For **input_group.textarea**, use the **block-start** or **block-end** alignment.

The `input_group.addon` component can have multiple `input_group.button` components and icons.

## input_group.button

Displays buttons within input groups. See the [Button](/docs/components/button) docs for more information. 

| Prop        | Type                                                                          | Default   |
| ----------- | ----------------------------------------------------------------------------- | --------- |
| `size`      | `"xs" \| "icon-xs" \| "sm" \| "icon-sm"`                                      | `"xs"`    |
| `variant`   | `"default" \| "destructive" \| "outline" \| "secondary" \| "ghost" \| "link"` | `"ghost"` |
| `class_name` | `string`                                                                      |           |

## input_group.input

Replacement for `input()` when building input groups. This component has the input group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` |         |

All other props are passed through to the underlying `Input()` component.

## input_group.textarea

Replacement for `textarea()` when building input groups. This component has the textarea group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` |         |

All other props are passed through to the underlying `textarea()` component.
