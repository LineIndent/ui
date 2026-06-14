---
title: "CLI"
description: "Learn how to use the Buridan UI Command Line Interface to manage components and themes."
order: 3
---

# buridan

Use the buridan CLI to add components and themes to your project.

## Installation

Install the CLI using pip:

```bash
pip install buridan-create
```

## Usage

All `buridan` commands must be executed from your Reflex project root, where the `rxconfig.py` file is located.

## init

Initialize Buridan UI in your project. This command generates the `assets/globals.css` file and updates your `rxconfig.py` with the required Tailwind configuration and theme tokens.

```bash
buridan init --preset <ID>
```

Arguments:
- `--preset`: The theme preset ID from the Buridan UI creator.
- `--include`: Specify `full` to include all available components or `theme-only` for just the CSS and configuration. Defaults to `full`.

## add

Add specific components and their required dependencies to your project.

```bash
buridan add <name>
```

You can add multiple components at once:

```bash
buridan add button input select
```

This command automatically resolves and adds any required utilities, icons, or base components while maintaining the correct directory structure.

## list

Display all available components that can be added to your project.

```bash
buridan list
```
