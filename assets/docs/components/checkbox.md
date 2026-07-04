

# Checkbox

A control that allows the user to toggle between checked and not checked.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component checkbox
```

### Manual Installation

```python
from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..icons.hugeicon import hi
from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    ROOT = (
        "peer relative flex size-4 shrink-0 items-center justify-center rounded-[4px] "
        "border border-input transition-colors outline-none "
        "group-has-disabled/field:opacity-50 after:absolute after:-inset-x-3 after:-inset-y-2 "
        "focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 "
        "disabled:cursor-not-allowed disabled:opacity-50 "
        "aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 "
        "aria-invalid:aria-checked:border-primary dark:bg-input/30 "
        "dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 "
        "data-checked:border-primary data-checked:bg-primary data-checked:text-primary-foreground "
        "dark:data-checked:bg-primary"
    )
    INDICATOR = (
        "grid place-content-center text-current transition-none [&>svg]:size-3.5"
    )


class CheckboxBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/checkbox"

    @property
    def import_var(self):
        return ImportVar(tag="Checkbox", package_path="", install=False)


class CheckboxRoot(CheckboxBaseComponent):
    tag = "Checkbox.Root"

    default_checked: Var[bool]
    checked: Var[bool]
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]
    indeterminate: Var[bool]
    disabled: Var[bool]
    required: Var[bool]
    name: Var[str]
    value: Var[str]
    native_button: Var[bool]
    parent: Var[bool]
    read_only: Var[bool]
    render_: Component

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "checkbox"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CheckboxIndicator(CheckboxBaseComponent):
    tag = "Checkbox.Indicator"

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        if len(children) == 0:
            children = (hi("Tick02Icon"),)
        props["data-slot"] = "checkbox-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class Checkbox(ComponentNamespace):
    root = staticmethod(CheckboxRoot.create)
    indicator = staticmethod(CheckboxIndicator.create)
    class_names = ClassNames


checkbox = Checkbox()
```


# Usage


```python
from components.ui.checkbox import Checkbox
```


# Anatomy 
Use the following composition to build a `Checkbox` component.


```python
checkbox.root(
    checkbox.indicator(),
)
```


# Examples

## Basic

Pair the checkbox with `field.root` and `field.label` for proper layout and labeling.


```python
def checkbox_basic():
    return rx.el.div(
        field.root(
            checkbox.root(
                checkbox.indicator(),
                id="terms-checkbox-basic",
            ),
            field.label(
                "Accept terms and conditions",
                html_for="terms-checkbox-basic",
            ),
            orientation="horizontal",
        ),
        class_name="mx-auto max-w-sm",
    )
```


## Description

Use `field.description` for helper text.


```python
def checkbox_description() -> rx.Component:
    return field.group(
        field.root(
            checkbox.root(
                checkbox.indicator(),
                id="terms-checkbox-desc",
                name="terms-checkbox-desc",
                default_checked=True,
            ),
            field.content(
                field.label(
                    "Accept terms and conditions",
                    html_for="terms-checkbox-desc",
                ),
                field.description(
                    "By clicking this checkbox, you agree to the terms and conditions."
                ),
            ),
            orientation="horizontal",
        ),
        class_name="mx-auto w-72",
    )
```


## Disabled

Use the `disabled` prop to prevent interaction and add the `data_disabled=True` attribute to the component for disabled styles.


```python
def checkbox_disabled() -> rx.Component:
    return rx.el.div(
        field.root(
            checkbox.root(
                checkbox.indicator(),
                id="toggle-checkbox-disabled",
                name="toggle-checkbox-disabled",
                disabled=True,
            ),
            field.label(
                "Enable notifications",
                html_for="toggle-checkbox-disabled",
            ),
            orientation="horizontal",
            data_disabled=True,
        ),
        class_name="mx-auto w-56",
    )
```


## Group

Use multiple fields to create a checkbox list.


```python
def checkbox_group() -> rx.Component:
    return rx.el.fieldset(
        rx.el.legend(
            "Show these items on the desktop:",
            class_name="mb-1.5 font-medium text-sm text-foreground",
        ),
        rx.el.p(
            "Select the items you want to show on the desktop.",
            class_name="mb-4 text-sm text-muted-foreground",
        ),
        rx.el.div(
            field.root(
                checkbox.root(
                    checkbox.indicator(),
                    id="hard-disks",
                    default_checked=True,
                ),
                field.label(
                    "Hard disks", html_for="hard-disks", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox.root(
                    checkbox.indicator(),
                    id="ext-disks",
                    default_checked=True,
                ),
                field.label(
                    "External disks", html_for="ext-disks", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox.root(
                    checkbox.indicator(),
                    id="cds-dvds",
                ),
                field.label(
                    "CDs, DVDs, and iPods",
                    html_for="cds-dvds",
                    class_name="font-normal",
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox.root(
                    checkbox.indicator(),
                    id="servers",
                ),
                field.label(
                    "Connected servers", html_for="servers", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            class_name="flex flex-col w-full",
        ),
    )
```

