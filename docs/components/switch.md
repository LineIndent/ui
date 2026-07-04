---
title: "Switch"
description: "A control that allows the user to toggle between checked and not checked."
order: 0
---

# Switch

A control that allows the user to toggle between checked and not checked.

# Installation 
Copy the following code into your app directory.

--INSTALL(switch)--

# Usage

--USAGE(switch)--


# Anatomy
Use the following composition to build a `Switch` component.

--ANATOMY(switch)--

# Examples

## Description

A standard switch layout featuring a secondary descriptive text block nested alongside the core `field.label` and `switch.root` within a vertical `field.root` layout.

--DEMO(switch_description)--

## Choice Card

Card-style selection where `field.label` wraps the entire `field.root` layout pattern to create a fully clickable target container.

--DEMO(switch_choice_card)--

## Disabled

Pass the `disabled=True` prop directly to the `switch.root` component to deactivate user input. Pass the `data_disabled="true"` attribute to the `field.root` layout component for contextual styling.

--DEMO(switch_disabled)--

## Invalid

Pass the `aria_invalid="true"` prop to the `switch.root` component to explicitly communicate an unfulfilled state. Pass the `data_invalid="true"` attribute to the `field.root` container layout to trigger error typography theme changes automatically.

--DEMO(switch_invalid)--

## Size

Use the `size` property on `switch.root` to scale the toggle boundaries down to `"sm"` or return to `"default"`. Stack components smoothly inside a unified layout using a `field.group` block.

--DEMO(switch_sizes)--
