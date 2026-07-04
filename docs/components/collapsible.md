---
title: "Collapsible"
description: "An interactive component which expands/collapses a panel."
order: 6
---

# Collapsible

An interactive component which expands/collapses a panel.

# Installation

Copy the following code into your app directory.

--INSTALL(collapsible)--

# Usage

--USAGE(collapsible)--

# Anatomy 
Use the following composition to build a `Collapsible` component.

--ANATOMY(collapsible)--

# Controlled State

Use the `open` and `on_open_change` props to control the state.

```python
import reflex as rx
from components.ui.collapsible import collapsible

class ControlledCollapsibleState(rx.State):
    is_open: bool = False

    def toggle_open(self, open_state: bool):
        self.is_open = open_state

def controlled_example() -> rx.Component:
    return collapsible.root(
        collapsible.trigger(Toggle),
        collapsible.panel("Content"),
        open=ControlledCollapsibleState.is_open,
        on_open_change=ControlledCollapsibleState.toggle_open,
    )
```

# Examples

## Basic

--DEMO(collapsible_basic)--

## Nested

Use nested collapsibles to build a file tree.

--DEMO(collapsible_nested)--

## Interactive

--DEMO(collapsible_interactive)--
