

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
"""Checkbox component from base-ui components."""

from reflex.components.component import ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.el import Label

from ..icons.hugeicon import hi
from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    """Class names for the checkbox component."""

    # ROOT = "flex size-4 items-center justify-center rounded-[4px] data-[checked]:bg-primary data-[unchecked]:border data-[unchecked]:border-input data-[disabled]:cursor-not-allowed data-[disabled]:border data-[disabled]:border-input/50 data-[disabled]:bg-secondary hover:bg-secondary transition-colors cursor-default"
    ROOT = (
        "flex size-4 items-center justify-center rounded-[4px] "
        "border border-input "
        "data-[checked]:border-primary "
        "data-[checked]:bg-primary "
        "hover:bg-secondary transition-colors "
        "data-[disabled]:cursor-not-allowed "
        "data-[disabled]:border-input/50 "
        "data-[disabled]:bg-secondary "
        "shrink-0 "
        "cursor-default"
    )
    INDICATOR = "flex text-primary-foreground data-[unchecked]:hidden data-[disabled]:text-foreground/50"
    LABEL = "text-sm text-foreground font-medium flex items-center gap-2"
    CONTAINER = "flex flex-row items-center gap-2"


class CheckboxBaseComponent(BaseUIComponent):
    """Base component for checkbox components."""

    library = f"{PACKAGE_NAME}/checkbox"

    @property
    def import_var(self):
        """Return the import variable for the checkbox component."""
        return ImportVar(tag="Checkbox", package_path="", install=False)


class CheckboxRoot(CheckboxBaseComponent):
    """The root checkbox component."""

    tag = "Checkbox.Root"

    # Whether the checkbox is initially ticked. To render a controlled checkbox, use the checked prop instead. Defaults to False.
    default_checked: Var[bool]

    # Whether the checkbox is currently ticked. To render an uncontrolled checkbox, use the default_checked prop instead.
    checked: Var[bool]

    # Event handler called when the checkbox is ticked or unticked.
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Whether the checkbox is in a mixed state: neither ticked, nor unticked. Defaults to False.
    indeterminate: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the checkbox is required. Defaults to False.
    required: Var[bool]

    # Identifies the field when a form is submitted.
    name: Var[str]

    # The value of the selected checkbox.
    value: Var[str]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # Whether the checkbox controls a group of child checkboxes. Must be used in a Checkbox Group. Defaults to False.
    parent: Var[bool]

    # Whether the user should be unable to tick or untick the checkbox. Defaults to False.
    read_only: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the checkbox root component."""
        props["data-slot"] = "checkbox"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CheckboxIndicator(CheckboxBaseComponent):
    """The indicator that shows whether the checkbox is checked."""

    tag = "Checkbox.Indicator"

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the checkbox indicator component."""
        if len(children) == 0:
            children = (hi("Tick02Icon", size=14),)
        props["data-slot"] = "checkbox-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class HighLevelCheckbox(CheckboxRoot):
    """High level wrapper for the Checkbox component."""

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create a high level checkbox component.

        Args:
            *children: The content of the checkbox.
            **props: Additional properties to apply to the checkbox component.

        Returns:
            The checkbox component and its indicator.
        """
        class_name = props.pop("class_name", "")
        if label := props.pop("label", None):
            return Label.create(  # pyright: ignore[reportReturnType]
                CheckboxRoot.create(
                    CheckboxIndicator.create(),
                    *children,
                    **props,
                ),
                label,
                class_name=cn(ClassNames.LABEL, class_name),
            )
        return CheckboxRoot.create(
            CheckboxIndicator.create(),
            *children,
            **props,
            class_name=class_name,
        )


class Checkbox(ComponentNamespace):
    """Namespace for Checkbox components."""

    root = staticmethod(CheckboxRoot.create)
    indicator = staticmethod(CheckboxIndicator.create)
    high_level = staticmethod(HighLevelCheckbox.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelCheckbox.create)


checkbox = Checkbox()
```


# Usage


> **Error processing usage for checkbox: module, class, method, function, traceback, frame, or code object was expected, got Checkbox**


# Anatomy 
Use the following composition to build a `Checkbox`


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
            checkbox(id="terms-checkbox-basic"),
            field.label(
                "Accept terms and conditions",
                html_for="terms-checkbox-basic",
            ),
            orientation="horizontal",
        ),
        class_name="mx-auto w-56",
    )
```


## Description

Use `field.description` for helper text.


```python
def checkbox_description() -> rx.Component:
    return rx.el.div(
        field.root(
            checkbox(
                id="terms-checkbox-desc",
                name="terms-checkbox-desc",
                default_checked=True,
            ),
            rx.el.div(
                field.label(
                    "Accept terms and conditions",
                    html_for="terms-checkbox-desc",
                ),
                field.description(
                    "By clicking this checkbox, you agree to the terms and conditions."
                ),
                class_name="flex flex-col",
            ),
            orientation="horizontal",
        ),
        class_name="mx-auto w-72",
    )
```


## Disabled

Use the `disabled` prop to prevent interaction and add the `data-disabled` attribute to the component for disabled styles.


```python
def checkbox_disabled() -> rx.Component:
    return rx.el.div(
        field.root(
            checkbox(
                id="toggle-checkbox-disabled",
                name="toggle-checkbox-disabled",
                disabled=True,
            ),
            field.label(
                "Enable notifications",
                html_for="toggle-checkbox-disabled",
            ),
            orientation="horizontal",
            disabled=True,
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
                checkbox(id="hard-disks", default_checked=True),
                field.label(
                    "Hard disks", html_for="hard-disks", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox(id="ext-disks", default_checked=True),
                field.label(
                    "External disks", html_for="ext-disks", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox(id="cds-dvds"),
                field.label(
                    "CDs, DVDs, and iPods",
                    html_for="cds-dvds",
                    class_name="font-normal",
                ),
                orientation="horizontal",
            ),
            field.root(
                checkbox(id="servers"),
                field.label(
                    "Connected servers", html_for="servers", class_name="font-normal"
                ),
                orientation="horizontal",
            ),
            class_name="flex flex-col w-full",
        ),
    )
```

