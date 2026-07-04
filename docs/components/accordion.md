---
title: "Accordion"
description: "A vertically stacked set of interactive headings that each reveal a section of content."
order: 0
---

# Accordion

A set of collapsible panels with headings.

# Installation

Copy the following code into your app directory.

--INSTALL(accordion)--

# Usage

--USAGE(accordion)--

# Anatomy 
Use the following composition to build an `Accordion` component.

--ANATOMY(accordion)--

# Examples

## Basic

A basic accordion that shows one item at a time. The first item is open by default.

--DEMO(accordion_basic)--

## Multiple

Use the `multiple` prop to allow multiple items to be open at the same time.

--DEMO(accordion_multiple)--

## Disabled

Use the `disabled` prop on `accordion.item` to disable individual items.

--DEMO(accordion_disabled)--

## Borders

Add `border` to the `accordion.root` and `border-b last:border-b-0` to the `accordion.item` to add borders to the items.

--DEMO(accordion_borders)--

## Card

Wrap the `accordion.root` in a `card` component.

--DEMO(accordion_card)--
