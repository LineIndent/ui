

# Skeleton

Custom skeleton component.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component skeleton
```

### Manual Installation

```python
"""Custom skeleton component."""

from reflex.components.component import Component
from reflex.vars.base import Var
from reflex_components_core.el import Div

from ..utils.twmerge import cn


class ClassNames:
    """Class names for skeleton component."""

    ROOT = "animate-pulse bg-secondary"


def skeleton_component(
    class_name: str | Var[str] = "",
) -> Component:
    """Skeleton component."""
    return Div.create(class_name=cn(ClassNames.ROOT, class_name))


skeleton = skeleton_component
```


# Usage


```python
from components.ui.skeleton import skeleton
```


# Anatomy 
Use the following composition to build a `Skeleton`


```python
skeleton_component()
```


# Examples

## General


```python
def skeleton_general():
    return skeleton_component(class_name="h-8 w-32 rounded-md")
```


## Card


```python
def skeleton_card():
    return card.root(
        card.header(
            skeleton_component(class_name="h-4 w-2/3 rounded-md"),
            skeleton_component(class_name="h-4 w-1/2 rounded-md"),
        ),
        card.content(
            skeleton_component(class_name="aspect-video w-full rounded-md"),
        ),
        class_name="w-full max-w-xs border border-input rounded-radius",
    )
```


## Table


```python
def skeleton_table():
    """Skeleton table matching shadcn SkeletonTable layout."""

    return rx.el.div(
        *[
            rx.el.div(
                skeleton_component(class_name="h-4 flex-1"),
                skeleton_component(class_name="h-4 w-24"),
                skeleton_component(class_name="h-4 w-20"),
                class_name="flex gap-4",
                key=str(i),
            )
            for i in range(5)
        ],
        class_name="flex w-full max-w-sm flex-col gap-2",
    )
```

