---
title: "Select"
description: "Custom select component."
order: 18
---

# Select
Custom select component.

# Installation
Copy the following code into your app directory.

--INSTALL(["Select", "buridan add component select"])--

# Usage
--USAGE(select)--

# Anatomy 
Use the following composition to build a `Select`
--ANATOMY(select)--

# Examples

## Align Item
Use `align_item_with_trigger` on `select.positioner()` to control whether the selected item aligns with the trigger. When true (default), the popup positions so the selected item appears over the trigger. When false, the popup aligns to the trigger edge.

--DEMO(select_align_with_items)--

## Groups
Use `select.group` to organize items into sections, `select.group_label` to label each section, and `select.separator` to visually divide groups.

--DEMO(select_groups)--

## Scrollable
Use `select.scroll_up_arrow` and `select.scroll_down_arrow` to provide navigation controls for scrolling through long lists of select items within the dropdown.

--DEMO(select_with_scroll_arrows)--
