---
title: "Textarea"
description: "Displays a form textarea or a component that looks like a textarea."
order: 23
---

# Textarea

Displays a form textarea or a component that looks like a textarea.

# Installation

Copy the following code into your app directory.

--INSTALL(textarea)--

# Usage

--USAGE(textarea)--

# Anatomy 
Use the following composition to build a `Textarea` component.

--ANATOMY(textarea)--

# Examples

## Basic
A standard multiline text area for general text input.

--DEMO(textarea_basic_demo)--

## Field
Use `field.root`, `field.label`, and `field.description` together with a form control (such as textarea) to build a structured field with a label and helper text.

--DEMO(textarea_field)--

## Disabled
Use the `disabled` prop on textarea to disable user input. Apply `data-disabled` on `field.root` to propagate disabled styling to all field-related elements and ensure consistent visual state handling.

--DEMO(textarea_disabled)--

## Invalid
Use the `aria-invalid` prop to mark the textarea as invalid. To style the invalid state, add the `data-invalid` attribute to the `field.root` component.

--DEMO(textarea_invalid)--
