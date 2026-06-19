

# Scroll Area

Augments native scroll functionality for custom, cross-browser styling.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component scroll_area
```

### Manual Installation

```python
"""Custom scroll area component."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.core.cond import cond

from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    """Class names for scroll area components."""

    ROOT = "h-full outline-none focus:outline-none"
    VIEWPORT = "h-full overscroll-contain"
    CONTENT = ""
    SCROLLBAR_BASE = "flex touch-none p-0.5 opacity-0 transition-[colors,opacity] delay-200 select-none data-hovering:opacity-100 data-hovering:delay-0 data-hovering:duration-100 data-scrolling:opacity-100 data-scrolling:delay-0 data-scrolling:duration-100"
    SCROLLBAR_VERTICAL = "w-2"
    SCROLLBAR_HORIZONTAL = "h-2"
    THUMB = "w-full rounded-full bg-secondary"
    CORNER = "bg-secondary"


class ScrollAreaBaseComponent(BaseUIComponent):
    """Base component for scroll area components."""

    library = f"{PACKAGE_NAME}/scroll-area"

    @property
    def import_var(self):
        """Return the import variable for the scroll area component."""
        return ImportVar(tag="ScrollArea", package_path="", install=False)


class ScrollAreaRoot(ScrollAreaBaseComponent):
    """The root of the scroll area."""

    tag = "ScrollArea.Root"

    # Render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the scroll area root component."""
        props["data-slot"] = "scroll-area"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class ScrollAreaViewport(ScrollAreaBaseComponent):
    """The viewport of the scroll area."""

    tag = "ScrollArea.Viewport"

    # Render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the scroll area viewport component."""
        props["data-slot"] = "scroll-area-viewport"
        cls.set_class_name(ClassNames.VIEWPORT, props)
        return super().create(*children, **props)


class ScrollAreaContent(ScrollAreaBaseComponent):
    """A container for the content of the scroll area."""

    tag = "ScrollArea.Content"

    # Render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the scroll area content component."""
        props["data-slot"] = "scroll-area-content"
        cls.set_class_name(ClassNames.CONTENT, props)
        return super().create(*children, **props)


class ScrollAreaScrollbar(ScrollAreaBaseComponent):
    """The scrollbar of the scroll area."""

    tag = "ScrollArea.Scrollbar"

    # Orientation of the scrollbar
    orientation: Var[LiteralOrientation] = Var.create("vertical")

    # Whether to keep the HTML element in the DOM when the viewport isn't scrollable
    keep_mounted: Var[bool] = Var.create(False)

    # Render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the scroll area scrollbar component."""
        props["data-slot"] = "scroll-area-scrollbar"
        orientation = props.get("orientation", "vertical")

        scrollbar_classes = cn(
            ClassNames.SCROLLBAR_BASE,
            cond(
                orientation == "vertical",
                ClassNames.SCROLLBAR_VERTICAL,
                ClassNames.SCROLLBAR_HORIZONTAL,
            ),
        )

        cls.set_class_name(scrollbar_classes, props)
        return super().create(*children, **props)


class ScrollAreaThumb(ScrollAreaBaseComponent):
    """The thumb of the scrollbar."""

    tag = "ScrollArea.Thumb"

    # Render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the scroll area thumb component."""
        props["data-slot"] = "scroll-area-thumb"
        cls.set_class_name(ClassNames.THUMB, props)
        return super().create(*children, **props)


class ScrollAreaCorner(ScrollAreaBaseComponent):
    """A small rectangular area that appears at the intersection of horizontal and vertical scrollbars."""

    tag = "ScrollArea.Corner"

    # Render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the scroll area corner component."""
        props["data-slot"] = "scroll-area-corner"
        cls.set_class_name(ClassNames.CORNER, props)
        return super().create(*children, **props)


class HighLevelScrollArea(ScrollAreaRoot):
    """High level wrapper for the Scroll Area component."""

    # Orientation of the scroll area
    orientation: Var[LiteralOrientation] = Var.create("vertical")

    # Whether to keep the HTML element in the DOM when the viewport isn't scrollable
    keep_mounted: Var[bool] = Var.create(False)

    # Props for different component parts
    _scrollbar_props = {"orientation", "keep_mounted"}

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create a high level scroll area component.

        Args:
            *children: The content to be scrollable.
            **props: Additional properties to apply to the scroll area component.

        Returns:
            The scroll area component.
        """
        # Extract props for different parts
        scrollbar_props = {k: props.pop(k) for k in cls._scrollbar_props & props.keys()}

        return ScrollAreaRoot.create(
            ScrollAreaViewport.create(
                ScrollAreaContent.create(
                    *children,
                ),
            ),
            ScrollAreaScrollbar.create(
                ScrollAreaThumb.create(),
                **scrollbar_props,
            ),
            **props,
        )


class ScrollArea(ComponentNamespace):
    """Namespace for Scroll Area components."""

    root = staticmethod(ScrollAreaRoot.create)
    viewport = staticmethod(ScrollAreaViewport.create)
    content = staticmethod(ScrollAreaContent.create)
    scrollbar = staticmethod(ScrollAreaScrollbar.create)
    thumb = staticmethod(ScrollAreaThumb.create)
    corner = staticmethod(ScrollAreaCorner.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelScrollArea.create)


scroll_area = ScrollArea()
```


# Usage


```python
from components.ui.scroll_area import scroll_area
```


# Anatomy 
Use the following composition to build a `Scroll Area`


```python
scroll_area.root(
    scroll_area.viewport(
        scroll_area.content(),
    ),
    scroll_area.scrollbar(
        scroll_area.thumb(),
    ),
    scroll_area.corner(),
)
```



# Examples


## General
A simple vertical scroll area.


```python
def scroll_area_general():
    """A basic scroll area example."""
    return rx.el.div(
        scroll_area(
            rx.el.div(
                *[rx.el.p(f"buridan v0.{i}", class_name="p-2") for i in range(30)],
            ),
            class_name="h-72 w-48 rounded-md border border-input",
        ),
        class_name="py-6",
    )
```


## Horizontal
Use `scroll_area.scrollbar()` with `orientation="horizontal"` for horizontal scrolling.


```python
def scroll_area_horizontal():
    return scroll_area.root(
        scroll_area.viewport(
            scroll_area.content(
                *[
                    rx.el.figure(
                        rx.el.div(
                            rx.el.image(
                                src=work["art"],
                                alt=f"Photo by {work['artist']}",
                                class_name="aspect-[3/4] h-64 object-cover",
                            ),
                            class_name="overflow-hidden rounded-md",
                        ),
                        rx.el.figcaption(
                            "Photo by ",
                            rx.el.span(
                                work["artist"],
                                class_name="font-semibold text-foreground",
                            ),
                            class_name="pt-2 text-xs text-muted-foreground",
                        ),
                        class_name="shrink-0",
                    )
                    for work in works
                ],
                class_name="flex w-max space-x-4 p-4",
            ),
        ),
        scroll_area.scrollbar(scroll_area.thumb(), orientation="horizontal"),
        scroll_area.corner(),
        class_name="w-96 rounded-radius border border-input",
    )
```

