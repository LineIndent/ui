---
title: "Dialog"
description: "A window overlaid on either the primary window or another dialog window, rendering the content underneath inert."
order: 8
---

# Dialog

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

# Installation

Copy the following code into your app directory.

--INSTALL(["Dialog", "buridan add component dialog"])--

# Usage

--USAGE(dialog)--

# Anatomy 
Use the following composition to build a `Dialog`

--ANATOMY(dialog)--


# Examples


## High Level

Uses the simplified dialog() API with trigger, title, description, and content props for quick implementation.

--DEMO(dialog_high_level)--

## Low Level

Uses the low-level dialog.root(), dialog.trigger(), dialog.portal() etc. for full control over structure and styling

--DEMO(dialog_low_level)--
