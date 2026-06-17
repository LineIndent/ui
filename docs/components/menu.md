---
title: "Menu"
description: "Displays a menu to the user — such as a set of actions or functions — triggered by a button."
order: 13
---

# Menu

Displays a menu to the user — such as a set of actions or functions — triggered by a button.

# Installation

Copy the following code into your app directory.

--INSTALL(["Menu", "buridan add component menu"])--

# Usage

--USAGE(menu)--

# Anatomy 
Use the following composition to build a `Menu`

--ANATOMY(menu)--


# Example
A basic dropdown menu that opens when the user clicks a trigger button.

## High Level
Uses low-level API to create a menu component.

--DEMO(menu_high_level)--

## Submenu
Use `menu.submenu_root()` to nest secondary actions.

--DEMO(menu_submenu)--

## Checkboxes
Use `menu.checkbox_item()` for toggles. 

--DEMO(menu_checkboxes)--
