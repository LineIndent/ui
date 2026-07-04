

# Separator

Visually or semantically separates content.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component separator
```

### Manual Installation

```python
from typing import Literal

from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    SEPARATOR = "shrink-0 bg-input data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:w-px data-[orientation=vertical]:self-stretch"


class SeparatorComponent(BaseUIComponent):
    tag = "Separator"
    library = f"{PACKAGE_NAME}/separator"

    orientation: Var[Literal["horizontal", "vertical"]]

    @property
    def import_var(self):
        return ImportVar(tag="Separator", package_path="", install=False)

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "separator"
        if "orientation" not in props:
            props["orientation"] = "horizontal"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


separator = SeparatorComponent.create
```


# Usage


```python
from components.ui.separator import separator
```


# Anatomy 

Use the following composition to build a `Separator` component.


```python
separator()
```


# Examples

## Default

The default `orientation` is set to `horizontal`.


```python
def separator_horizontal() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div("buridan/ui", class_name="leading-none font-medium"),
            rx.el.div(
                "The UI Library for Reflex Devs.",
                class_name="text-muted-foreground",
            ),
            class_name="flex flex-col gap-1.5",
        ),
        separator(class_name="bg-zinc-200 dark:bg-zinc-800"),
        rx.el.div(
            "A set of beautifully designed components that you can customize, extend, and build on."
        ),
        class_name="flex max-w-sm flex-col gap-4 text-sm",
    )
```


## Vertical 

Use `orientation="vertical"` for a vertical separator.


```python
def separator_vertical() -> rx.Component:
    return rx.el.div(
        rx.el.div("Blog"),
        separator(orientation="vertical"),
        rx.el.div("Docs"),
        separator(orientation="vertical"),
        rx.el.div("Source"),
        class_name="flex h-5 items-center gap-4 text-sm",
    )
```


## Menu

Vertical separators between menu items with descriptions.


```python
def separator_menu() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span("Settings", class_name="font-medium"),
            rx.el.span(
                "Manage preferences", class_name="text-xs text-muted-foreground"
            ),
            class_name="flex flex-col gap-1",
        ),
        separator(orientation="vertical"),
        rx.el.div(
            rx.el.span("Account", class_name="font-medium"),
            rx.el.span(
                "Profile & security", class_name="text-xs text-muted-foreground"
            ),
            class_name="flex flex-col gap-1",
        ),
        separator(orientation="vertical", class_name="hidden md:block"),
        rx.el.div(
            rx.el.span("Help", class_name="font-medium"),
            rx.el.span("Support & docs", class_name="text-xs text-muted-foreground"),
            class_name="hidden flex-col gap-1 md:flex",
        ),
        class_name="flex items-center gap-2 text-sm md:gap-4",
    )
```


## List

Horizontal separators between list items.


```python
def separator_list() -> rx.Component:
    return rx.el.div(
        rx.el.dl(
            rx.el.dt("Item 1"),
            rx.el.dd("Value 1", class_name="text-muted-foreground"),
            class_name="flex items-center justify-between",
        ),
        separator(),
        rx.el.dl(
            rx.el.dt("Item 2"),
            rx.el.dd("Value 2", class_name="text-muted-foreground"),
            class_name="flex items-center justify-between",
        ),
        separator(),
        rx.el.dl(
            rx.el.dt("Item 3"),
            rx.el.dd("Value 3", class_name="text-muted-foreground"),
            class_name="flex items-center justify-between",
        ),
        class_name="flex w-full max-w-sm flex-col gap-2 text-sm",
    )
```

