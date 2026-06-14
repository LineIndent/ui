

# Collapsible

Custom collapsible component.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component collapsible
```

### Manual Installation

```python
"""Custom collapsible component."""

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    """Class names for collapsible components."""

    ROOT = "flex flex-col justify-center text-secondary-12"
    TRIGGER = "group flex items-center gap-2"
    PANEL = "flex h-[var(--collapsible-panel-height)] flex-col justify-end overflow-hidden text-sm transition-all ease-out data-[ending-style]:h-0 data-[starting-style]:h-0"


class CollapsibleBaseComponent(BaseUIComponent):
    """Base component for collapsible components."""

    library = f"{PACKAGE_NAME}/collapsible"

    @property
    def import_var(self):
        """Return the import variable for the collapsible component."""
        return ImportVar(tag="Collapsible", package_path="", install=False)


class CollapsibleRoot(CollapsibleBaseComponent):
    """Groups all parts of the collapsible. Renders a <div> element."""

    tag = "Collapsible.Root"

    # Whether the collapsible panel is initially open. To render a controlled collapsible, use the `open` prop instead. Defaults to False.
    default_open: Var[bool]

    # Whether the collapsible panel is currently open. To render an uncontrolled collapsible, use the `default_open` prop instead.
    open: Var[bool]

    # Event handler called when the panel is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool)]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the collapsible root component."""
        props["data-slot"] = "collapsible"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CollapsibleTrigger(CollapsibleBaseComponent):
    """A button that opens and closes the collapsible panel. Renders a <button> element."""

    tag = "Collapsible.Trigger"

    # Whether the component renders a native `<button>` element when replacing it via the `render` prop. Set to `false` if the rendered element is not a button (e.g. `<div>`). Defaults to True.
    native_button: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the collapsible trigger component."""
        props["data-slot"] = "collapsible-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class CollapsiblePanel(CollapsibleBaseComponent):
    """A panel with the collapsible contents. Renders a <div> element."""

    tag = "Collapsible.Panel"

    # Allows the browser's built-in page search to find and expand the panel contents. Overrides the `keep_mounted` prop and uses `hidden="until-found"` to hide the element without removing it from the DOM. Defaults to False.
    hidden_until_found: Var[bool]

    # Whether to keep the element in the DOM while the panel is hidden. This prop is ignored when `hidden_until_found` is used. Defaults to False.
    keep_mounted: Var[bool]

    # Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a `ReactElement` or a function that returns the element to render.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the collapsible panel component."""
        props["data-slot"] = "collapsible-panel"
        cls.set_class_name(ClassNames.PANEL, props)
        return super().create(*children, **props)


class HighLevelCollapsible(CollapsibleRoot):
    """High level collapsible component."""

    # The trigger component.
    trigger: Var[Component | None]

    # The content component.
    content: Var[str | Component | None]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the collapsible component."""
        trigger = props.pop("trigger", None)
        content = props.pop("content", None)

        return CollapsibleRoot.create(
            CollapsibleTrigger.create(render_=trigger) if trigger else None,
            CollapsiblePanel.create(
                content,
                *children,
            ),
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "trigger",
            "content",
        ]


class Collapsible(ComponentNamespace):
    """Namespace for Collapsible components."""

    root = staticmethod(CollapsibleRoot.create)
    trigger = staticmethod(CollapsibleTrigger.create)
    panel = staticmethod(CollapsiblePanel.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelCollapsible.create)


collapsible = Collapsible()
```


# Usage


> **Error processing usage for collapsible: module, class, method, function, traceback, frame, or code object was expected, got Collapsible**


# Anatomy 
Use the following composition to build a `Collapsible`


```python
collapsible.root(
    collapsible.trigger(),
    collapsible.panel(),
)
```



# Examples

Below are examples demonstrating how the component can be used.

## High Level Demo

Uses the simplified collapsible() API with trigger and content props for quick implementation.


```python
def collapsible_high_level_demo():
    return collapsible(
        trigger=button(
            "Trigger",
            varient="outline",
            class_name="w-full",
        ),
        content=rx.el.p(
            "This is the collapsible content. You can put anything here!",
            class_name="py-2 text-center",
        ),
        default_open=False,
        class_name="w-full max-w-xs",
    )
```


## Low Level Demo

Uses the low-level collapsible.root(), collapsible.panel(), and ClientStateVar for full control over state and structure.


```python
def collapsible_low_level_demo():
    return collapsible.root(
        collapsible.trigger(
            button(
                "Collapsible Trigger",
                varient="outline",
                class_name="w-full",
            ),
        ),
        rx.el.div(
            "@radix-ui/primitives",
            class_name="rounded-md border border-input px-4 py-2 font-mono text-sm",
        ),
        collapsible.panel(
            rx.el.div(
                rx.el.div(
                    "@radix-ui/colors",
                    class_name="rounded-md border border-input px-4 py-2 font-mono text-sm",
                ),
                rx.el.div(
                    "@stitches/react",
                    class_name="rounded-md border border-input px-4 py-2 font-mono text-sm",
                ),
                class_name="flex flex-col gap-4",
            ),
        ),
        class_name="w-full max-w-xs flex flex-col gap-2",
    )
```

