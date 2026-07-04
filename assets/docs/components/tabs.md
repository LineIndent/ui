

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
from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    ROOT = (
        "group/tabs flex gap-2 data-[orientation=horizontal]:flex-col "
        "data-[orientation=vertical]:flex-row data-[orientation=vertical]:gap-4"
    )

    LIST = (
        "group/tabs-list relative inline-flex w-fit items-center justify-center rounded-lg p-[3px] "
        "text-muted-foreground bg-muted "
        "group-data-[orientation=horizontal]/tabs:h-8 group-data-[orientation=vertical]/tabs:h-fit "
        "group-data-[orientation=vertical]/tabs:flex-col group-data-[orientation=vertical]/tabs:p-1 group-data-[orientation=vertical]/tabs:gap-1 "
        "data-[variant=line]:rounded-none data-[variant=line]:bg-transparent data-[variant=line]:gap-1"
    )

    TAB = (
        "relative inline-flex h-[calc(100%-1px)] flex-1 items-center justify-center gap-1.5 "
        "rounded-md border border-transparent px-1.5 py-0.5 text-sm font-medium whitespace-nowrap "
        "text-foreground/60 transition-all hover:text-foreground "
        "focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1 "
        "disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none "
        "dark:text-muted-foreground dark:hover:text-foreground "
        "group-data-[orientation=vertical]/tabs:w-full group-data-[orientation=vertical]/tabs:justify-start "
        "data-[active]:text-foreground "
        "group-data-[variant=default]/tabs-list:data-[active]:bg-background "
        "dark:group-data-[variant=default]/tabs-list:data-[active]:border-input "
        "dark:group-data-[variant=default]/tabs-list:data-[active]:bg-input/30 "
        "group-data-[variant=default]/tabs-list:data-[active]:shadow-sm "
        "group-data-[variant=line]/tabs-list:data-[active]:bg-transparent "
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    )

    INDICATOR = (
        "absolute z-[0] transition-all duration-200 ease-in-out "
        "group-data-[variant=default]/tabs-list:rounded-lg "
        "group-data-[variant=default]/tabs-list:bg-background "
        "group-data-[variant=default]/tabs-list:shadow-sm "
        "dark:group-data-[variant=default]/tabs-list:border dark:group-data-[variant=default]/tabs-list:border-input "
        "dark:group-data-[variant=default]/tabs-list:bg-input/30 "
        "group-data-[variant=line]/tabs-list:bg-foreground "
        "group-data-[variant=line]/tabs-list:!h-[2px] "
        "group-data-[variant=line]/tabs-list:!top-[auto] "
        "group-data-[variant=line]/tabs-list:!bottom-0 "
        "[left:var(--active-tab-left)] [top:var(--active-tab-top)] "
        "[width:var(--active-tab-width)] [height:var(--active-tab-height)]"
    )

    PANEL = "flex-1 text-sm outline-none flex flex-col gap-2"


class TabsBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/tabs"

    @property
    def import_var(self):
        return ImportVar(tag="Tabs", package_path="", install=False)


class TabsRoot(TabsBaseComponent):
    tag = "Tabs.Root"
    default_value: Var[str | int]
    value: Var[str | int]
    on_value_change: EventHandler[passthrough_event_spec(str | dict)]
    orientation: Var[LiteralOrientation]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class TabsList(TabsBaseComponent):
    tag = "Tabs.List"
    activate_on_focus: Var[bool]
    loop: Var[bool]
    variant: Var[Literal["default", "line"]]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs-list"
        if "variant" in props:
            props["data-variant"] = props.pop("variant")
        else:
            props["data-variant"] = "default"

        cls.set_class_name(ClassNames.LIST, props)
        return super().create(*children, **props)


class TabsTab(TabsBaseComponent):
    tag = "Tabs.Tab"
    value: Var[str | int]
    native_button: Var[bool]
    disabled: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs-trigger"
        cls.set_class_name(ClassNames.TAB, props)
        return super().create(*children, **props)


class TabsIndicator(TabsBaseComponent):
    tag = "Tabs.Indicator"
    render_before_hydration: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class TabsPanel(TabsBaseComponent):
    tag = "Tabs.Panel"
    value: Var[str | int]
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs-content"
        cls.set_class_name(ClassNames.PANEL, props)
        return super().create(*children, **props)


class Tabs(ComponentNamespace):
    root = __call__ = staticmethod(TabsRoot.create)
    list = staticmethod(TabsList.create)
    tab = staticmethod(TabsTab.create)
    panel = staticmethod(TabsPanel.create)
    indicator = staticmethod(TabsIndicator.create)
    class_names = ClassNames


tabs = Tabs()
```


# Usage


```python
from components.ui.tabs import tabs
```


# Anatomy 
Use the following composition to build a `Tabs` component.


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


## Line
Use the `variant="line"` prop on `tabs.list` for a line style.

```python
def tabs_line() -> rx.Component:
    return tabs.root(
        tabs.list(
            tabs.indicator(),
            tabs.tab("Overview", value="overview"),
            tabs.tab("Analytics", value="analytics"),
            tabs.tab("Reports", value="reports"),
            variant="line",
        ),
        default_value="overview",
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


## Icons

```python
def tabs_icons() -> rx.Component:
    return tabs.root(
        tabs.list(
            tabs.indicator(),
            tabs.tab(
                hi("BrowserIcon"),
                "Preview",
                value="preview",
            ),
            tabs.tab(
                hi("CodeIcon"),
                "Code",
                value="code",
            ),
        ),
        default_value="preview",
    )
```

