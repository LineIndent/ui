---
title: "Tooltip"
description: "Tooltip component from base-ui components."
order: 27
---

# Tooltip

A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.

# Installation

Copy the following code into your app directory.

--INSTALL(["Tooltip", "buridan add component tooltip"])--

# Usage

--USAGE(tooltip)--

# Anatomy 
Use the following composition to build a `Tooltip`
--ANATOMY(tooltip)--


# Examples

Below are examples demonstrating how the component can be used.

## General

A simple tooltip example. Use the `dealy` prop to change how fast the tootip shows.
--DEMO(tooltip_general)--

## Side
Use the `side` prop in `tooltip.positioner()` to change the position of the tooltip.
--DEMO(tooltip_sides)--
