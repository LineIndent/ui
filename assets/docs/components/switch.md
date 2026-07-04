

# Switch

A control that allows the user to toggle between checked and not checked.

# Installation 
Copy the following code into your app directory.

### CLI

```bash
buridan add component switch
```

### Manual Installation

```python
from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralSwitchSize = Literal["default", "sm"]


class ClassNames:
    ROOT = (
        "peer group/switch relative inline-flex shrink-0 items-center rounded-full "
        "border border-transparent transition-all outline-none "
        "after:absolute after:-inset-x-3 after:-inset-y-2 "
        "focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 "
        "aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 "
        "data-[size=default]:h-[18.4px] data-[size=default]:w-[32px] "
        "data-[size=sm]:h-[14px] data-[size=sm]:w-[24px] "
        "dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 "
        "data-checked:bg-primary data-unchecked:bg-input dark:data-unchecked:bg-input/80 "
        "data-disabled:cursor-not-allowed data-disabled:opacity-50"
    )

    THUMB = (
        "pointer-events-none block rounded-full bg-background ring-0 transition-transform "
        "group-data-[size=default]/switch:size-4 group-data-[size=sm]/switch:size-3 "
        "group-data-[size=default]/switch:data-checked:translate-x-[calc(100%-2px)] "
        "group-data-[size=sm]/switch:data-checked:translate-x-[calc(100%-2px)] "
        "dark:data-checked:bg-primary-foreground "
        "group-data-[size=default]/switch:data-unchecked:translate-x-0 "
        "group-data-[size=sm]/switch:data-unchecked:translate-x-0 "
        "dark:data-unchecked:bg-foreground"
    )


class SwitchBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/switch"

    @property
    def import_var(self):
        return ImportVar(tag="Switch", package_path="", install=False)


class SwitchRoot(SwitchBaseComponent):
    tag = "Switch.Root"

    name: Var[str]
    default_checked: Var[bool]
    checked: Var[bool]
    on_checked_change: EventHandler[passthrough_event_spec(bool)]
    native_button: Var[bool]
    disabled: Var[bool]
    read_only: Var[bool]
    required: Var[bool]
    input_ref: Var[str]
    size: Var[LiteralSwitchSize]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "switch"

        # Pull or default size prop and put it in data attribute
        size = props.pop("size", "default")
        props["data-size"] = size

        cls.set_class_name(ClassNames.ROOT, props)

        # If no explicit thumb/child is given, auto-inject it like Shadcn does!
        if not children:
            children = (SwitchThumb.create(),)

        return super().create(*children, **props)


class SwitchThumb(SwitchBaseComponent):
    tag = "Switch.Thumb"
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "switch-thumb"
        cls.set_class_name(ClassNames.THUMB, props)
        return super().create(*children, **props)


class Switch(ComponentNamespace):
    root = staticmethod(SwitchRoot.create)
    thumb = staticmethod(SwitchThumb.create)
    class_names = ClassNames


switch = Switch()
```


# Usage


```python
from components.ui.switch import Switch
```



# Anatomy
Use the following composition to build a `Switch` component.


```python
switch.root(
    switch.thumb(),
)
```


# Examples

## Description

A standard switch layout featuring a secondary descriptive text block nested alongside the core `field.label` and `switch.root` within a vertical `field.root` layout.


```python
def switch_description() -> rx.Component:
    return field.root(
        field.content(
            field.label("Share across devices", html_for="switch-focus-mode"),
            field.description(
                "Focus is shared across devices, and turns off when you leave the app."
            ),
        ),
        switch.root(
            switch.thumb(),
            id="switch-focus-mode",
        ),
        orientation="horizontal",
        class_name="max-w-sm px-2",
    )
```


## Choice Card

Card-style selection where `field.label` wraps the entire `field.root` layout pattern to create a fully clickable target container.


```python
def switch_choice_card() -> rx.Component:
    return field.group(
        field.label(
            field.root(
                field.content(
                    field.title("Share across devices"),
                    field.description(
                        "Focus is shared across devices, and turns off when you leave the app."
                    ),
                ),
                switch.root(id="switch-share"),
                orientation="horizontal",
            ),
            html_for="switch-share",
        ),
        field.label(
            field.root(
                field.content(
                    field.title("Enable notifications"),
                    field.description(
                        "Receive notifications when focus mode is enabled or disabled."
                    ),
                ),
                switch.root(id="switch-notifications", default_checked=True),
                orientation="horizontal",
            ),
            html_for="switch-notifications",
        ),
        class_name="w-full max-w-sm my-8",
    )
```


## Disabled

Pass the `disabled=True` prop directly to the `switch.root` component to deactivate user input. Pass the `data_disabled="true"` attribute to the `field.root` layout component for contextual styling.


```python
def switch_disabled() -> rx.Component:

    return field.root(
        switch.root(
            id="switch-disabled-unchecked",
            disabled=True,
        ),
        field.label(
            "Disabled",
            html_for="switch-disabled-unchecked",
        ),
        orientation="horizontal",
        data_disabled="true",
        class_name="w-fit ",
    )
```


## Invalid

Pass the `aria_invalid="true"` prop to the `switch.root` component to explicitly communicate an unfulfilled state. Pass the `data_invalid="true"` attribute to the `field.root` container layout to trigger error typography theme changes automatically.


```python
def switch_invalid() -> rx.Component:
    return field.root(
        field.content(
            field.label(
                "Accept terms and conditions",
                html_for="switch-terms",
            ),
            field.description("You must accept the terms and conditions to continue."),
        ),
        switch.root(
            id="switch-terms",
            aria_invalid="true",
        ),
        orientation="horizontal",
        data_invalid="true",
        class_name="max-w-sm",
    )
```


## Size

Use the `size` property on `switch.root` to scale the toggle boundaries down to `"sm"` or return to `"default"`. Stack components smoothly inside a unified layout using a `field.group` block.


```python
def switch_sizes() -> rx.Component:
    return field.group(
        field.root(
            switch.root(
                id="switch-size-sm",
                size="sm",
            ),
            field.label(
                "Small",
                html_for="switch-size-sm",
            ),
            orientation="horizontal",
        ),
        field.root(
            switch.root(
                id="switch-size-default",
                size="default",
            ),
            field.label(
                "Default",
                html_for="switch-size-default",
            ),
            orientation="horizontal",
        ),
        class_name="w-full max-w-[10rem]",
    )
```

