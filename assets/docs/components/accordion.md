

# Accordion

A set of collapsible panels with headings.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component accordion
```

### Manual Installation

```python
from typing import Any, Literal

import reflex as rx
from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..icons.hugeicon import hi
from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]

ITEMS_TYPE = list[dict[str, str | Component]]


class ClassNames:
    ROOT = "flex w-full flex-col"

    ITEM = "not-last:border-b border-input"

    HEADER = "flex"

    TRIGGER = (
        "group/accordion-trigger relative flex flex-1 items-start justify-between "
        "rounded-lg border border-input border-transparent py-2.5 text-left text-sm font-medium "
        "transition-all outline-none hover:underline focus-visible:border-ring "
        "focus-visible:ring-3 focus-visible:ring-ring/50 focus-visible:after:border-ring "
        "aria-disabled:pointer-events-none aria-disabled:opacity-50 "
        "**:data-[slot=accordion-trigger-icon]:ml-auto "
        "**:data-[slot=accordion-trigger-icon]:size-4 "
        "**:data-[slot=accordion-trigger-icon]:text-muted-foreground"
    )

    TRIGGER_ICON_DOWN = (
        "pointer-events-none shrink-0 group-aria-expanded/accordion-trigger:hidden"
    )
    TRIGGER_ICON_UP = "pointer-events-none hidden shrink-0 group-aria-expanded/accordion-trigger:inline"

    PANEL = (
        "h-[var(--accordion-panel-height)] overflow-hidden text-sm "
        "transition-[height] duration-200 ease-out "
        "data-[ending-style]:h-0 data-[starting-style]:h-0"
    )

    PANEL_DIV = (
        "pt-0 pb-2.5 "
        "[&_a]:underline [&_a]:underline-offset-3 [&_a]:hover:text-foreground "
        "[&_p:not(:last-child)]:mb-4"
    )


class AccordionBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/accordion"

    @property
    def import_var(self):
        return ImportVar(tag="Accordion", package_path="", install=False)


class AccordionRoot(AccordionBaseComponent):
    tag = "Accordion.Root"

    default_value: Var[list[Any]]
    value: Var[list[Any]]
    on_value_change: EventHandler[passthrough_event_spec(list[str])]
    hidden_until_found: Var[bool]
    multiple: Var[bool]
    disabled: Var[bool]
    loop_focus: Var[bool]
    orientation: Var[LiteralOrientation]
    keep_mounted: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "accordion"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class AccordionItem(AccordionBaseComponent):
    tag = "Accordion.Item"

    value: Var[str]
    on_open_change: EventHandler[passthrough_event_spec(bool)]
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "accordion-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class AccordionHeader(AccordionBaseComponent):
    tag = "Accordion.Header"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "accordion-header"
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class AccordionTrigger(AccordionBaseComponent):
    tag = "Accordion.Trigger"

    native_button: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "accordion-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)

        trigger = super().create(
            *children,
            hi(
                "ArrowDown01Icon",
                data_slot="accordion-trigger-icon",
                class_name=ClassNames.TRIGGER_ICON_DOWN,
            ),
            hi(
                "ArrowUp01Icon",
                data_slot="accordion-trigger-icon",
                class_name=ClassNames.TRIGGER_ICON_UP,
            ),
            **props,
        )

        return AccordionHeader.create(trigger)


class AccordionPanel(AccordionBaseComponent):
    tag = "Accordion.Panel"

    hidden_until_found: Var[bool]
    keep_mounted: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "accordion-panel"
        inner_class = props.pop("class_name", "")
        cls.set_class_name(ClassNames.PANEL, props)

        return super().create(
            rx.el.div(*children, class_name=cn(ClassNames.PANEL_DIV, inner_class)),
            **props,
        )


class Accordion(ComponentNamespace):
    root = staticmethod(AccordionRoot.create)
    item = staticmethod(AccordionItem.create)
    header = staticmethod(AccordionHeader.create)
    trigger = staticmethod(AccordionTrigger.create)
    panel = staticmethod(AccordionPanel.create)
    class_names = ClassNames


accordion = Accordion()
```


# Usage


```python
from components.ui.accordion import Accordion
```


# Anatomy 
Use the following composition to build an `Accordion` component.


```python
accordion.root(
    accordion.item(
        accordion.header(
            accordion.trigger(),
        ),
        accordion.panel(),
    ),
    accordion.item(
        accordion.header(
            accordion.trigger(),
        ),
        accordion.panel(),
    ),
)
```


# Examples

## Basic

A basic accordion that shows one item at a time. The first item is open by default.


```python
def accordion_basic():
    return rx.el.div(
        accordion.root(
            accordion.item(
                accordion.trigger("Models"),
                accordion.panel(
                    rx.el.p("- Genesis launched a new era of exploration."),
                    rx.el.p("- Explorer uncovered new planets beyond our reach."),
                    rx.el.p("- Voyager 1 ventured into interstellar space."),
                    rx.el.p("- Apollo landed humans on the Moon."),
                ),
                value="section-1",
            ),
            accordion.item(
                accordion.trigger("Spacecraft"),
                accordion.panel(
                    rx.el.p("- Curiosity sent back valuable data from Mars."),
                    rx.el.p("- The Hubble Telescope captured distant galaxies."),
                    rx.el.p("- James Webb will explore the universe's origins."),
                    rx.el.p("- The ISS orbits Earth, conducting critical experiments."),
                ),
                value="section-2",
            ),
            accordion.item(
                accordion.trigger("Space Discoveries"),
                accordion.panel(
                    rx.el.p("- Saturn's rings have fascinated scientists for years."),
                    rx.el.p("- The Mars Rover is studying the planet's surface."),
                    rx.el.p(
                        "- NASA's Artemis program aims to return humans to the Moon."
                    ),
                    rx.el.p("- Solar missions help us understand space weather."),
                ),
                value="section-3",
            ),
            class_name="w-full max-w-md mx-auto",
            default_value=["section-1"],
        ),
        class_name="h-[45vh] w-full justify-center pt-10 px-8",
    )
```


## Multiple

Use the `multiple` prop to allow multiple items to be open at the same time.


```python
def accordion_multiple() -> rx.Component:
    return accordion.root(
        *[
            accordion.item(
                accordion.trigger(item["trigger"]),
                accordion.panel(item["content"]),
                value=item["value"],
            )
            for item in items
        ],
        multiple=True,
        default_value=["notifications"],
        class_name="max-w-sm",
    )
```


## Disabled

Use the `disabled` prop on `accordion.item` to disable individual items.


```python
def accordion_disabled() -> rx.Component:
    return accordion.root(
        accordion.item(
            accordion.trigger("Can I access my account history?"),
            accordion.panel(
                "Yes, you can view your complete account history including all "
                "transactions, plan changes, and support tickets in the Account "
                "History section of your dashboard."
            ),
            value="item-1",
        ),
        accordion.item(
            accordion.trigger("Premium feature information"),
            accordion.panel(
                "This section contains information about premium features. "
                "Upgrade your plan to access this content."
            ),
            value="item-2",
            disabled=True,
        ),
        accordion.item(
            accordion.trigger("How do I update my email address?"),
            accordion.panel(
                "You can update your email address in your account settings. "
                "You'll receive a verification email at your new address to "
                "confirm the change."
            ),
            value="item-3",
        ),
        class_name="max-w-sm",
    )
```


## Borders

Add `border` to the `accordion.root` and `border-b last:border-b-0` to the `accordion.item` to add borders to the items.


```python
def accordion_borders() -> rx.Component:
    return accordion.root(
        *[
            accordion.item(
                accordion.trigger(item["trigger"]),
                accordion.panel(item["content"]),
                value=item["value"],
                class_name="border-b px-4 last:border-b-0",
            )
            for item in items
        ],
        default_value=["billing"],
        class_name="max-w-sm rounded-lg border border-input",
    )
```


## Card

Wrap the `accordion.root` in a `card` component.


```python
def accordion_card() -> rx.Component:
    return card.root(
        card.header(
            card.title("Subscription & Billing"),
            card.description(
                "Common questions about your account, plans, payments and "
                "cancellations."
            ),
        ),
        card.content(
            accordion.root(
                *[
                    accordion.item(
                        accordion.trigger(item["trigger"]),
                        accordion.panel(item["content"]),
                        value=item["value"],
                    )
                    for item in items
                ],
                default_value=["plans"],
            ),
        ),
        class_name="w-full max-w-sm",
    )
```

