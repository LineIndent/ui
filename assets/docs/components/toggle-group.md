

# Toggle Group

Custom toggle group component.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component toggle_group
```

### Manual Installation

```python
"""Custom toggle group component."""

from typing import Literal

from reflex.components.component import Component
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    """Class names for toggle group components."""

    ROOT = ""


class ToggleGroupBaseComponent(BaseUIComponent):
    """Base component for toggle group components."""

    library = f"{PACKAGE_NAME}/toggle-group"

    @property
    def import_var(self):
        """Return the import variable for the toggle group component."""
        return ImportVar(tag="ToggleGroup", package_path="", install=False)


class ToggleGroupRoot(ToggleGroupBaseComponent):
    """Provides a shared state to a series of toggle buttons."""

    tag = "ToggleGroup"

    # The open state of the toggle group represented by an array of the values of all pressed toggle buttons. This is the uncontrolled counterpart of value.
    default_value: Var[list[str | int]]

    # The open state of the toggle group represented by an array of the values of all pressed toggle buttons. This is the controlled counterpart of default_value.
    value: Var[list[str | int]]

    # Callback fired when the pressed states of the toggle group changes.
    on_value_change: EventHandler[passthrough_event_spec(list[str | int], dict)]

    # When false only one item in the group can be pressed. If any item in the group becomes pressed, the others will become unpressed. When true multiple items can be pressed. Defaults to False.
    multiple: Var[bool]

    # Whether the toggle group should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether to loop keyboard focus back to the first item when the end of the list is reached while using the arrow keys. Defaults to True.
    loop: Var[bool]

    # The component orientation (layout flow direction). Defaults to "horizontal".
    orientation: Var[LiteralOrientation]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the toggle group root component."""
        props["data-slot"] = "toggle-group"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


toggle_group = ToggleGroupRoot.create
```


# Usage


```python
from components.ui.toggle_group import toggle_group
```


# Anatomy 
Use the following composition to build a `Toggle Group`


```python
toggle_group(
    toggle(),
    toggle(),
)
```


# Examples

## General

A basic toggle group with single-selection mode, allowing only one active toggle at a time.


```python
def toggle_group_general():
    return toggle_group(
        toggle(hi("TextBoldIcon"), value="bold", class_name=toggle_style),
        toggle(hi("TextItalicIcon"), value="italic", class_name=toggle_style),
        toggle(hi("TextUnderlineIcon"), value="underline", class_name=toggle_style),
        default_value=["bold"],
        class_name="flex gap-px rounded-md border border-input bg-background p-0.5",
    )
```


## Multiple Selection

Set `multiple=True` on the `toggle_group()` to allow multiple selections at the same time. 


```python
def toggle_group_multiple_selection():
    return toggle_group(
        toggle(hi("TextAlignLeftIcon"), value="left", class_name=toggle_style),
        toggle(hi("TextAlignCenterIcon"), value="center", class_name=toggle_style),
        toggle(hi("TextAlignRightIcon"), value="right", class_name=toggle_style),
        default_value=["left", "right"],
        multiple=True,
        class_name="flex gap-px rounded-md border border-input bg-background p-0.5",
    )
```

