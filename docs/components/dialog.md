---
title: "Dialog"
description: "Custom dialog component."
order: 8
---

# Dialog

Custom dialog component.

# Installation

Copy the following code into your app directory.

--INSTALL(["Dialog", "buridan add component dialog"])--

# Usage

--USAGE(dialog)--

# Anatomy 
Use the following composition to build a `Dialog`

--ANATOMY(dialog)--


# Examples

Below are examples demonstrating how the component can be used.

## High Level

Uses the simplified dialog() API with trigger, title, description, and content props for quick implementation.

--DEMO(dialog_high_level)--

## Low Level

Uses the low-level dialog.root(), dialog.trigger(), dialog.portal() etc. for full control over structure and styling

--DEMO(dialog_low_level)--
