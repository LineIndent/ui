---
title: "CLI"
description: "Learn how to use the Buridan UI Command Line Interface to manage components and themes."
order: 3
---

# buridan

Use the buridan CLI to add components, apply themes, and manage your Buridan UI project.

# Installation

```bash
pip install buridan-create
```

All commands must be run from your Reflex project root, where `rxconfig.py` is located.

# create

Open the Buridan UI theme builder in your browser. Use it to customize your design system and generate a unique preset ID.

```bash
buridan create
```

# init

Initialize Buridan UI in your project. This command sets up CSS utilities (shimmer, scrollbar) in `assets/globals.css` and updates `rxconfig.py` with the required Tailwind configuration.

```bash
buridan init
```

# apply

Apply a theme preset to your project. Generates `:root` and `.dark` CSS variable blocks in `assets/globals.css` based on the preset ID from the theme builder.

```bash
buridan apply --preset <ID>
```

Arguments:
- `--preset`: The theme preset ID from the Buridan UI theme builder. Use `b0` for the default theme.

Example:

```bash
buridan apply --preset b0
buridan apply --preset b2D0wqNxT
```

# add

Add components and their dependencies to your project.

```bash
buridan add <name>
```

You can add multiple components at once:

```bash
buridan add button input select
```

Blocks (charts, dashboards, etc.) can be added the same way:

```bash
buridan add line_chart_01
```

Components are placed in `components/`, blocks in `blocks/`. Dependencies are resolved and added automatically.

> **Note:** Components require a theme to render correctly. Run `buridan apply` before using components.

# list

Display all available components and blocks.

```bash
buridan list
```

# Recommended workflow

```bash
buridan create                    # build your theme, copy the preset ID
buridan init                      # set up utilities and Tailwind config
buridan apply --preset <ID>       # apply your theme
buridan add button input select   # add the components you need
```
