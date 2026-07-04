---
title: "Context Menu"
description: "Displays a menu of actions triggered by a right click."
order: 7
---

# Context Menu

Displays a menu of actions triggered by a right click.

# Installation

Copy the following code into your app directory.

--INSTALL(context_menu)--

# Usage

--USAGE(context_menu)--

# Anatomy 

Use the following composition to build a `Context Menu` component.

--ANATOMY(context_menu)--

A Context Menu is built by composing a root trigger with an overlay surface.

```composition
context_menu.root
├── context_menu.trigger
└── context_menu.portal
    └── context_menu.positioner
        └── context_menu.popup
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   ├── context_menu.item
            │   └── context_menu.item
            ├── context_menu.separator
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   ├── context_menu.checkbox_item
            │   │   └── context_menu.checkbox_item_indicator
            │   └── context_menu.checkbox_item
            │       └── context_menu.checkbox_item_indicator
            ├── context_menu.separator
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   └── context_menu.radio_group
            │       ├── context_menu.radio_item
            │       │   └── context_menu.radio_item_indicator
            │       └── context_menu.radio_item
            │           └── context_menu.radio_item_indicator
            └── context_menu.sub
                ├── context_menu.sub_trigger
                └── context_menu.positioner
                    └── context_menu.popup
                        └── context_menu.group
                            ├── context_menu.item
                            └── context_menu.item
```

# Examples

## Basic

A simple context menu with a few actions.

--DEMO(context_menu_basic)--

## Submenu

Use `context_menu.sub` to nest secondary actions.

--DEMO(context_menu_submenu)--

## Shortcuts

Use `context_menu.shortcut` to show keyboard hints.

--DEMO(context_menu_shortcuts)--

## Groups

Group related actions and separate them with dividers.

--DEMO(context_menu_groups)--

## Checkboxes

Use `context_menu.checkbox_item` for toggles.

--DEMO(context_menu_checkboxes)--

## Radio

Use `context_menu.radio_item` for exclusive choices.

--DEMO(context_menu_radio)--


## Sides

Control submenu placement with side and align props.

--DEMO(context_menu_sides)--
