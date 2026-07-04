---
title: "Kbd"
description: "Used to display textual user input from keyboard."
order: 0
---

# Kbd

Used to display textual user input from keyboard.

# Installation

Copy the following code into your app directory.

--INSTALL(kbd)--

# Usage

--USAGE(kbd)--

# Anatomy 
Use the following composition to build a `Kbd` component.

--ANATOMY(kbd)--

# Examples

## Group

Use the `kbd.group` component to group keyboard keys together.

--DEMO(kbd_as_group)--

## Button

Use the `kbd.root` component inside a `Button` component to display a keyboard key inside a button.

--DEMO(kbd_button)--

## Tooltip

You can use the `kbd.root` component inside a `Tooltip` component to display a tooltip with a keyboard key.

--DEMO(kbd_tooltip)--

## Input Group

You can use the `kbd.root` component inside a `input_group.addon` component to display a keyboard key inside an input group.

--DEMO(kbd_input_group)--

# API Reference

## kbd.root

Use the `kbd.root` component to display a keyboard key.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | ``      |

```python
kbd.root('Ctrl')
```

## kbd.group

Use the `kbd.group` component to group `kbd.root` components together.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | ``      |

```python
kbd.group(
    kbd.root('Ctrl')
    kbd.root('B')
)
```
