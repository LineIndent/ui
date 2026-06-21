---
title: "Autocomplete"
description: "An input that suggests options as you type."
order: 0
---

# Autocomplete

An input that suggests options as you type.

> **Note:** The Autocomplete component is a fully custom implementation with no external dependencies. All filtering, keyboard navigation, and popup positioning happen client-side in the browser with no server round trips.

# Installation

Copy the following code into your app directory.

--INSTALL(autocomplete)--

# Usage

--USAGE(autocomplete)--

# Anatomy 
Use the following composition to build an `Autocomplete`

--ANATOMY(autocomplete)--

# Examples

## Basic

A minimal autocomplete with a static list of items.

--DEMO(autocomplete_basic)--

## Selected Value

Wire up `on_select_item` to capture the selected value.

--DEMO(autocomplete_select_value)--

## Large List

Autocomplete works efficiently with large lists — filtering happens entirely in the browser.

--DEMO(autocomplete_large_list)--

## Custom Styling

Override any part of the component by passing a `*_class` prop. Classes are merged with the defaults via `cn`.

--DEMO(autocomplete_custom_styling)--

## Empty State

When no items match the query, the empty state is shown automatically.

--DEMO(autocomplete_empty_state)--

# API Reference

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `items` | `list[str]` | `[]` | The list of items to display in the dropdown. |
| `placeholder` | `str` | `None` | Placeholder text shown inside the input when empty. |
| `on_change_query` | `EventHandler` | `None` | Fired on every keystroke with the current input value. |
| `on_select_item` | `EventHandler` | `None` | Fired when an item is selected, with the selected value as argument. |
| `root_class` | `str` | `None` | Additional Tailwind classes merged onto the root wrapper. |
| `input_class` | `str` | `None` | Additional Tailwind classes merged onto the input element. |
| `popup_class` | `str` | `None` | Additional Tailwind classes merged onto the dropdown popup. |
| `list_class` | `str` | `None` | Additional Tailwind classes merged onto the scrollable list. |
| `item_class` | `str` | `None` | Additional Tailwind classes merged onto each list item. |
| `item_highlighted_class` | `str` | `None` | Additional Tailwind classes merged onto the currently highlighted item. |
| `empty_class` | `str` | `None` | Additional Tailwind classes merged onto the empty state element. |
