---
title: "Toggle"
description: "A two-state button that can be either on or off."
order: 25
---

# Toggle

A two-state button that can be either on or off.

# Installation

Copy the following code into your app directory.

--INSTALL(toggle)--

# Usage

--USAGE(toggle)--

# Anatomy 
Use the following composition to build a `Toggle` component.

--ANATOMY(toggle)--


# Examples

## Icon Toggle Variants
Use `toggle()` for a pressable on/off control. Control icon behavior with `icon_variant="fill"` to fill icons on press, or omit it and style manually using `data-[pressed] selectors` (e.g. text-* or fill-*).

--DEMO(toggle_general)--

## Pressed State
Use `default_pressed=True` to set the default pressed state of a toggle.

--DEMO(toggle_pressed_state)--

## Disabled
Set `disabled=True` to disable a toggle.

--DEMO(toggle_disabled)--
