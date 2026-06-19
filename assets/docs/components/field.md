

# Field

Combine labels, controls, and help text to compose accessible form fields and grouped inputs.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component field
```

### Manual Installation

```python
"""Custom field component."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["vertical", "horizontal"]


class ClassNames:
    ROOT = (
        "group/field flex w-full gap-2 data-[invalid=true]:text-destructive "
        "data-[orientation=vertical]:flex-col "
        "data-[orientation=horizontal]:flex-row data-[orientation=horizontal]:items-start "
        "data-[orientation=horizontal]:[&>[data-slot=checkbox]]:mt-[0.125rem]"
    )

    LABEL = (
        "peer/field-label flex w-fit gap-2 leading-snug text-sm font-medium "
        "data-[orientation=horizontal]:flex-auto "
        "group-data-[disabled=true]/field:opacity-50"
    )

    CONTROL = "w-full"

    DESCRIPTION = (
        "text-sm leading-normal text-muted-foreground "
        "group-has-data-horizontal/field:text-balance"
    )

    ITEM = "flex flex-col gap-0.5"

    ERROR = "text-sm font-normal text-destructive"

    VALIDITY = "hidden"


class FieldBaseComponent(BaseUIComponent):
    """Base component for field components."""

    library = f"{PACKAGE_NAME}/field"

    @property
    def import_var(self):
        """Return import variable."""
        return ImportVar(tag="Field", package_path="", install=False)


class FieldRoot(FieldBaseComponent):
    """Groups all field parts."""

    tag = "Field.Root"

    orientation: Var[LiteralOrientation]

    invalid: Var[bool]

    disabled: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "field"

        orientation = props.pop("orientation", None)
        if orientation:
            props["data-orientation"] = orientation

        disabled = props.pop("disabled", False)
        if disabled:
            props["data-disabled"] = "true"

        cls.set_class_name(ClassNames.ROOT, props)

        return super().create(*children, **props)


class FieldLabel(FieldBaseComponent):
    """Field label."""

    tag = "Field.Label"

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "field-label"
        cls.set_class_name(ClassNames.LABEL, props)

        return super().create(
            *children,
            **props,
        )


class FieldControl(FieldBaseComponent):
    """Field control."""

    tag = "Field.Control"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "field-control"
        cls.set_class_name(ClassNames.CONTROL, props)

        return super().create(
            *children,
            **props,
        )


class FieldDescription(FieldBaseComponent):
    """Field description."""

    tag = "Field.Description"

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "field-description"
        cls.set_class_name(ClassNames.DESCRIPTION, props)

        return super().create(
            *children,
            **props,
        )


class FieldItem(FieldBaseComponent):
    """Field item."""

    tag = "Field.Item"

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "field-item"
        cls.set_class_name(ClassNames.ITEM, props)

        return super().create(
            *children,
            **props,
        )


class FieldError(FieldBaseComponent):
    """Field error."""

    tag = "Field.Error"

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "field-error"
        cls.set_class_name(ClassNames.ERROR, props)

        return super().create(
            *children,
            **props,
        )


class FieldValidity(FieldBaseComponent):
    """Field validity state."""

    tag = "Field.Validity"

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "field-validity"
        cls.set_class_name(ClassNames.VALIDITY, props)

        return super().create(
            *children,
            **props,
        )


class Field(ComponentNamespace):
    """Field namespace."""

    root = staticmethod(FieldRoot.create)
    label = staticmethod(FieldLabel.create)
    control = staticmethod(FieldControl.create)
    description = staticmethod(FieldDescription.create)
    item = staticmethod(FieldItem.create)
    error = staticmethod(FieldError.create)
    validity = staticmethod(FieldValidity.create)

    class_names = ClassNames


field = Field()
```


# Usage


```python
from components.ui.field import Field
```


# Anatomy 
Use the following composition to build an `Field`


```python
field.root(
    field.label(),
    field.control(),
    field.description(),
    field.item(),
    field.error(),
    field.validity(),
)
```


# Examples

## General


```python
def field_demo() -> rx.Component:
    return rx.el.div(
        rx.el.form(
            rx.el.div(
                rx.el.fieldset(
                    rx.el.legend("Payment Method", class_name="font-medium mb-1"),
                    rx.el.p(
                        "All transactions are secure and encrypted",
                        class_name="text-sm text-muted-foreground mb-4",
                    ),
                    rx.el.div(
                        field.root(
                            field.label("Name on Card", html_for="name"),
                            field.control(
                                render_=input(
                                    id="name",
                                    placeholder="Evil Rabbit",
                                    class_name="!w-full",
                                ),
                                class_name="w-full",
                            ),
                            orientation="vertical",
                        ),
                        field.root(
                            field.label("Card Number", html_for="card"),
                            field.control(
                                render_=rx.el.div(
                                    input(
                                        id="card",
                                        placeholder="1234 5678 9012 3456",
                                        class_name="!w-full",
                                    ),
                                    class_name="w-full flex-1",
                                ),
                                class_name="w-full",
                            ),
                            field.description("Enter your 16-digit card number"),
                            orientation="vertical",
                        ),
                        class_name="flex flex-col w-full gap-y-2",
                    ),
                ),
                rx.el.fieldset(
                    rx.el.legend("Billing Address", class_name="font-medium mb-2"),
                    rx.el.p(
                        "The billing address associated with your payment method",
                        class_name="text-sm text-muted-foreground mb-3",
                    ),
                    field.root(
                        field.control(render_=checkbox()),
                        field.label(
                            "Same as shipping address",
                            html_for="shipping",
                            class_name="text-sm",
                        ),
                        orientation="horizontal",
                    ),
                ),
                field.root(
                    field.label("Comments", html_for="comments"),
                    field.control(
                        render_=textarea(
                            id="comments",
                            placeholder="Add any additional comments",
                            class_name="resize-none",
                        )
                    ),
                    orientation="vertical",
                ),
                field.root(
                    rx.el.div(
                        button("Submit", type="submit"),
                        button("Cancel", variant="outline", type="button"),
                        class_name="flex flex-row gap-x-4",
                    ),
                    orientation="horizontal",
                ),
                class_name="w-full flex flex-col gap-y-4",
            ),
            class_name="w-full flex",
        ),
        class_name="w-full max-w-md py-4",
    )
```

