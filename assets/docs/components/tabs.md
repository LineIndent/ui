

# Tabs

A set of layered sections of content—known as tab panels—that are displayed one at a time.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component tabs
```

### Manual Installation

```python
"""Custom tabs component."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    """Class names for tabs components."""

    LIST = (
        "relative bg-muted text-muted-foreground inline-flex h-9 w-full w-fit items-center "
        "justify-center rounded-radius p-[3px] "
        "data-[orientation=vertical]:flex data-[orientation=vertical]:flex-col "
        "data-[orientation=vertical]:h-auto "
        "data-[orientation=vertical]:p-1 data-[orientation=vertical]:gap-1"
    )
    TAB = (
        "relative z-[1] flex items-center justify-center text-sm font-medium "
        "text-foreground dark:text-muted-foreground "
        "data-[selected]:text-foreground "
        "rounded-radius px-2 py-1 transition-all "
        "data-[orientation=vertical]:justify-start data-[orientation=vertical]:w-full "
        "data-[orientation=vertical]:text-left"
    )
    ROOT = (
        "flex flex-col gap-2 "
        "data-[orientation=vertical]:flex-row data-[orientation=vertical]:gap-4"
    )

    INDICATOR = (
        "absolute z-[0] rounded-radius bg-background shadow-sm dark:border dark:border-input dark:bg-input/30 "
        "transition-all duration-200 ease-in-out "
        "[left:var(--active-tab-left)] [top:var(--active-tab-top)] "
        "[width:var(--active-tab-width)] [height:var(--active-tab-height)]"
    )
    PANEL = "flex flex-col gap-2"


class TabsBaseComponent(BaseUIComponent):
    """Base component for tabs components."""

    library = f"{PACKAGE_NAME}/tabs"

    @property
    def import_var(self):
        """Return the import variable for the tabs component."""
        return ImportVar(tag="Tabs", package_path="", install=False)


class TabsRoot(TabsBaseComponent):
    """Groups the tabs and the corresponding panels. Renders a <div> element."""

    tag = "Tabs.Root"

    # The default value. Use when the component is not controlled. When the value is null, no Tab will be selected. Defaults to 0.
    default_value: Var[str | int]

    # The value of the currently selected Tab. Use when the component is controlled. When the value is null, no Tab will be selected.
    value: Var[str | int]

    # Callback invoked when new value is being set.
    on_value_change: EventHandler[passthrough_event_spec(str | dict)]

    # The component orientation (layout flow direction). Defaults to "horizontal".
    orientation: Var[LiteralOrientation]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tabs root component."""
        props["data-slot"] = "tabs"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class TabsList(TabsBaseComponent):
    """Groups the individual tab buttons. Renders a <div> element."""

    tag = "Tabs.List"

    # Whether to automatically change the active tab on arrow key focus. Otherwise, tabs will be activated using Enter or Spacebar key press. Defaults to True.
    activate_on_focus: Var[bool]

    # Whether to loop keyboard focus back to the first item when the end of the list is reached while using the arrow keys. Defaults to True.
    loop: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tabs list component."""
        props["data-slot"] = "tabs-list"
        cls.set_class_name(ClassNames.LIST, props)
        return super().create(*children, **props)


class TabsTab(TabsBaseComponent):
    """An individual interactive tab button that toggles the corresponding panel. Renders a <button> element."""

    tag = "Tabs.Tab"

    # The value of the Tab. When not specified, the value is the child position index.
    value: Var[str | int]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # Whether the Tab is disabled. Defaults to false.
    disabled: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tabs tab component."""
        props["data-slot"] = "tabs-tab"
        cls.set_class_name(ClassNames.TAB, props)
        return super().create(*children, **props)


class TabsIndicator(TabsBaseComponent):
    """A visual indicator that can be styled to match the position of the currently active tab. Renders a <span> element."""

    tag = "Tabs.Indicator"

    # Whether to render itself before React hydrates. This minimizes the time that the indicator isn't visible after server-side rendering. Defaults to False.
    render_before_hydration: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tabs indicator component."""
        props["data-slot"] = "tabs-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class TabsPanel(TabsBaseComponent):
    """A panel displayed when the corresponding tab is active. Renders a <div> element."""

    tag = "Tabs.Panel"

    # The value of the TabPanel. It will be shown when the Tab with the corresponding value is selected. If not provided, it will fall back to the index of the panel. It is recommended to explicitly provide it, as it's required for the tab panel to be rendered on the server.
    value: Var[str | int]

    # Whether to keep the HTML element in the DOM while the panel is hidden. Defaults to False.
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tabs panel component."""
        props["data-slot"] = "tabs-panel"
        cls.set_class_name(ClassNames.PANEL, props)
        return super().create(*children, **props)


class Tabs(ComponentNamespace):
    """Namespace for Tabs components."""

    root = __call__ = staticmethod(TabsRoot.create)
    list = staticmethod(TabsList.create)
    tab = staticmethod(TabsTab.create)
    panel = staticmethod(TabsPanel.create)
    indicator = staticmethod(TabsIndicator.create)
    class_names = ClassNames


tabs = Tabs()
```


# Usage


> **Error processing usage for tabs: module, class, method, function, traceback, frame, or code object was expected, got Tabs**


# Anatomy 
Use the following composition to build a `Tabs`


```python
tabs.root(
    tabs.list(
        tabs.tab(),
        tabs.indicator(),
    ),
    tabs.panel(),
)
```



# Example

## Basic

```python
def tabs_basic():
    return rx.el.div(
        tabs.root(
            tabs.list(
                tabs.indicator(),
                tabs.tab("Overview", value="overview"),
                tabs.tab("Analytics", value="analytics"),
                tabs.tab("Reports", value="reports"),
                tabs.tab("Settings", value="settings"),
            ),
            tabs.panel(
                card.root(
                    card.header(
                        card.title("Overview"),
                        card.description(
                            "View your key metrics and recent project activity. Track progress across all your active projects."
                        ),
                    ),
                    card.content("You have 12 active projects and 3 pending tasks."),
                    class_name="ring-1 ring-foreground/10 rounded-[1rem] dark:bg-card",
                ),
                value="overview",
            ),
            tabs.panel(
                card.root(
                    card.header(
                        card.title("Analytics"),
                        card.description(
                            "Track performance and user engagement metrics. Monitor trends and identify growth opportunities."
                        ),
                    ),
                    card.content("Page views are up 25% compared to last month."),
                    class_name="ring-1 ring-foreground/10 rounded-[1rem] dark:bg-card",
                ),
                value="analytics",
            ),
            tabs.panel(
                card.root(
                    card.header(
                        card.title("Reports"),
                        card.description(
                            "Generate and download your detailed reports. Export data in multiple formats for analysis."
                        ),
                    ),
                    card.content("You have 5 reports ready and available to export."),
                    class_name="ring-1 ring-foreground/10 rounded-[1rem] dark:bg-card",
                ),
                value="reports",
            ),
            tabs.panel(
                card.root(
                    card.header(
                        card.title("Settings"),
                        card.description(
                            "Manage your account preferences and options. Customize your experience to fit your needs."
                        ),
                    ),
                    card.content("Configure notifications, security, and themes."),
                    class_name="ring-1 ring-foreground/10 rounded-[1rem]",
                ),
                value="settings",
            ),
            default_value="overview",
            class_name="w-[400px]",
        ),
        class_name="flex justify-center w-full",
    )
```


## Vertical
Use `orientation="vertical"` for vertical tabs.

```python
def tabs_vertical():
    return rx.el.div(
        tabs.root(
            tabs.list(
                tabs.indicator(),
                tabs.tab("Account", value="account"),
                tabs.tab("Password", value="password"),
                tabs.tab("Notifications", value="notifications"),
            ),
            default_value="account",
            orientation="vertical",
        ),
        class_name="flex justify-center text-sm",
    )
```


## Disabled
Use `disabled=True` to disable a tab.

```python
def tabs_disabled():
    return tabs.root(
        tabs.list(
            tabs.indicator(),
            tabs.tab(
                "Home",
                value="home",
            ),
            tabs.tab(
                "Disabled",
                value="settings",
                disabled=True,
            ),
        ),
        default_value="home",
    )
```

