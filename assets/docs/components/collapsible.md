

# Collapsible

An interactive component which expands/collapses a panel.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component collapsible
```

### Manual Installation

```python
from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    ROOT = "flex flex-col justify-center text-secondary-12"
    TRIGGER = "group flex items-center gap-2"
    PANEL = "flex h-[var(--collapsible-panel-height)] flex-col justify-end overflow-hidden text-sm data-[ending-style]:h-0 data-[starting-style]:h-0"


class CollapsibleBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/collapsible"

    @property
    def import_var(self):
        return ImportVar(tag="Collapsible", package_path="", install=False)


class CollapsibleRoot(CollapsibleBaseComponent):
    tag = "Collapsible.Root"

    default_open: Var[bool]
    open: Var[bool]
    on_open_change: EventHandler[passthrough_event_spec(bool)]
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "collapsible"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CollapsibleTrigger(CollapsibleBaseComponent):
    tag = "Collapsible.Trigger"

    native_button: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "collapsible-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class CollapsiblePanel(CollapsibleBaseComponent):
    tag = "Collapsible.Panel"

    hidden_until_found: Var[bool]
    keep_mounted: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "collapsible-panel"
        cls.set_class_name(ClassNames.PANEL, props)
        return super().create(*children, **props)


class Collapsible(ComponentNamespace):
    root = staticmethod(CollapsibleRoot.create)
    trigger = staticmethod(CollapsibleTrigger.create)
    panel = staticmethod(CollapsiblePanel.create)
    class_names = ClassNames


collapsible = Collapsible()
```


# Usage


```python
from components.ui.collapsible import Collapsible
```


# Anatomy 
Use the following composition to build a `Collapsible` component.


```python
collapsible.root(
    collapsible.trigger(),
    collapsible.panel(),
)
```


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


```python
def collapsible_basic() -> rx.Component:
    return rx.el.div(
        collapsible.root(
            collapsible.trigger(
                render_=button(
                    "How do I update my billing information?",
                    hi(
                        "ArrowDown01Icon",
                        class_name="size-4 ml-auto group-data-panel-open/button:rotate-180",
                    ),
                    variant="ghost",
                ),
                class_name="w-full py-3 text-left border-b border-input",
            ),
            collapsible.panel(
                rx.el.div(
                    "You can update your card details directly inside your account settings dashboard under the billing tab.",
                    class_name="py-3 text-sm text-muted-foreground leading-relaxed px-3",
                ),
            ),
        ),
        class_name="w-full max-w-sm",
    )
```


## Nested

Use nested collapsibles to build a file tree.


```python
def collapsible_nested() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                "WORKSPACE EXPLORER",
                class_name="text-[10px] font-bold tracking-wider text-muted-foreground",
            ),
            class_name="px-2 pb-2 mb-1 border-b border-border/40",
        ),
        folder_item(
            "src",
            folder_item(
                "components",
                folder_item(
                    "ui",
                    file_item("button.py"),
                    file_item("card.py"),
                    file_item("collapsible.py"),
                ),
                file_item("navbar.py"),
                file_item("sidebar.py"),
            ),
            folder_item(
                "state",
                file_item("base_state.py"),
                file_item("auth_state.py"),
            ),
            file_item("main.py"),
        ),
        folder_item(
            "public",
            file_item("favicon.ico"),
            file_item("logo.svg"),
        ),
        file_item("rxconfig.py", root_level=True),
        file_item("requirements.txt", root_level=True),
        class_name="w-full max-w-xs p-3 bg-background border border-input rounded-xl shadow-xs select-none",
    )
```


## Interactive


```python
def collapsible_interactive() -> rx.Component:
    return rx.el.div(
        collapsible.root(
            collapsible.trigger(
                render_=button(
                    rx.el.div(
                        rx.el.div(
                            "JD",
                            class_name="flex size-8 items-center justify-center rounded-full bg-primary/10 text-xs font-bold text-primary",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "John Doe",
                                class_name="text-sm font-semibold text-foreground text-left leading-none",
                            ),
                            rx.el.p(
                                "pro_plan_member",
                                class_name="text-[10px] font-mono text-muted-foreground mt-0.5 text-left",
                            ),
                            class_name="flex flex-col",
                        ),
                        class_name="flex items-center gap-3",
                    ),
                    hi(
                        "ArrowDown01Icon",
                        class_name="size-4 ml-auto text-muted-foreground transition-transform duration-200 group-data-panel-open/button:rotate-180",
                    ),
                    variant="ghost",
                    class_name="w-full h-14 px-3 hover:bg-muted/50 rounded-xl",
                ),
                class_name="w-full",
            ),
            collapsible.panel(
                rx.el.div(
                    rx.el.a(
                        hi("UserIcon", class_name="size-4 text-muted-foreground"),
                        rx.el.span("Edit Profile", class_name="text-xs font-medium"),
                        href="#",
                        class_name="flex items-center gap-2.5 px-3 py-2 rounded-lg hover:bg-muted/70 text-foreground/80 transition-colors",
                    ),
                    rx.el.a(
                        hi("Settings01Icon", class_name="size-4 text-muted-foreground"),
                        rx.el.span(
                            "Security & API Keys", class_name="text-xs font-medium"
                        ),
                        href="#",
                        class_name="flex items-center gap-2.5 px-3 py-2 rounded-lg hover:bg-muted/70 text-foreground/80 transition-colors",
                    ),
                    rx.el.a(
                        hi("Logout01Icon", class_name="size-4 text-destructive/70"),
                        rx.el.span(
                            "Log Out", class_name="text-xs font-medium text-destructive"
                        ),
                        href="#",
                        class_name="flex items-center gap-2.5 px-3 py-2 rounded-lg hover:bg-destructive/10 text-destructive transition-colors",
                    ),
                    class_name="pt-2 px-1 flex flex-col gap-1 border-t border-border/40 mt-1",
                )
            ),
        ),
        class_name="w-full max-w-xs p-2 bg-background border border-input rounded-2xl shadow-xs",
    )
```

