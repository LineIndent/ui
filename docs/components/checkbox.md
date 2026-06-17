---
title: "Checkbox"
description: "A control that allows the user to toggle between checked and not checked."
order: 5
---

# Checkbox

A control that allows the user to toggle between checked and not checked.

# Installation

Copy the following code into your app directory.

--INSTALL(["checkbox", "buridan add component checkbox"])--

# Usage

--USAGE(checkbox)--

# Anatomy 
Use the following composition to build a `Checkbox`

--ANATOMY(checkbox)--

# Examples

## Basic

Pair the checkbox with `field.root` and `field.label` for proper layout and labeling.

--DEMO(checkbox_basic)--

## Description

Use `field.description` for helper text.

--DEMO(checkbox_description)--

## Disabled

Use the `disabled` prop to prevent interaction and add the `data-disabled` attribute to the component for disabled styles.

--DEMO(checkbox_disabled)--

## Group

Use multiple fields to create a checkbox list.

--DEMO(checkbox_group)--
