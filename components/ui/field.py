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
