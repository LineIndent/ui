---
title: "Menu"
description: "Displays a menu to the user — such as a set of actions or functions — triggered by a button."
order: 13
---

# Menu

Displays a menu to the user — such as a set of actions or functions — triggered by a button.

# Installation

Copy the following code into your app directory.

--INSTALL(menu)--

# Usage

--USAGE(menu)--

# Anatomy 
Use the following composition to build a `Menu` component.

--ANATOMY(menu)--

# Example

## Basic

A basic dropdown menu with labels and separators.

--DEMO(menu_basic)--

## Submenu

Use `menu.submenu_root` to nest secondary actions.

--DEMO(menu_submenu)--

## Shortcuts

Add `menu.shortcut` to show keyboard hints.

--DEMO(menu_shortcuts)--

## Icons

Combine icons with labels for quick scanning.

--DEMO(menu_icons)--

## Checkboxes

Use `menu.checkbox_item` for toggles. 

--DEMO(menu_checkboxes)--

## Checkboxes Icons

Add icons to checkbox items.

--DEMO(menu_checkboxes_icons)--

## Radio Group

Use `menu.radio_group` for exclusive choices.

--DEMO(menu_radio_group)--

## Avatar 

An account switcher dropdown triggered by an avatar.

--DEMO(menu_avatar)--
