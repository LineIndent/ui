---
title: "Textarea"
description: "Custom Textarea component."
order: 23
---

# Textarea

Custom Textarea component.

# Installation

Copy the following code into your app directory.

--INSTALL(["Textarea", "buridan add component textarea"])--

# Usage

--USAGE(textarea)--

# Anatomy 
Use the following composition to build a `Textarea`

--ANATOMY(textarea)--

# Examples

## Basic Demo
A standard multiline text area for general text input.

--DEMO(textarea_basic_demo)--

## Field
Use `field.root`, `field.label`, and `field.description` together with a form control (such as textarea) to build a structured field with a label and helper text.

--DEMO(textarea_field)--

## Disabled
Use the `disabled` prop on textarea to disable user input. Apply `data-disabled` on `field.root` to propagate disabled styling to all field-related elements and ensure consistent visual state handling.

--DEMO(textarea_disabled)--

## Invalid
Apply `data-disabled` on Field to represent a disabled state and propagate styling, and apply data-invalid to represent validation errors.

--DEMO(textarea_invalid)--
