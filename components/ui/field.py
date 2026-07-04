from typing import Literal

from reflex.components.component import ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.el import elements

from components.ui.separator import separator

LiteralOrientation = Literal["vertical", "horizontal", "responsive"]
LiteralLegendVariant = Literal["legend", "label"]


class ClassNames:
    FIELD_SET = "flex flex-col gap-4 has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3"

    FIELD_LEGEND = "mb-1.5 font-medium data-[variant=label]:text-sm data-[variant=legend]:text-base"

    FIELD_GROUP = "group/field-group @container/field-group flex flex-col gap-5 data-[slot=checkbox-group]:gap-3 *:data-[slot=field-group]:gap-4"

    FIELD_ROOT_BASE = (
        "group/field flex w-full gap-2 data-[invalid=true]:text-destructive"
    )

    FIELD_ROOT_ORIENTATIONS = {
        "vertical": "flex-col *:w-full [&>.sr-only]:w-auto",
        "horizontal": "flex-row items-center has-[>[data-slot=field-content]]:items-start *:data-[slot=field-label]:flex-auto has-[>[data-slot=field-content]]:[&>[data-slot=checkbox]]:mt-[2.5px]",
        "responsive": "flex-col *:w-full @md/field-group:flex-row @md/field-group:items-center @md/field-group:*:w-auto @md/field-group:has-[>[data-slot=field-content]]:items-start @md/field-group:*:data-[slot=field-label]:flex-auto [&>.sr-only]:w-auto @md/field-group:has-[>[data-slot=field-content]]:[&>[data-slot=checkbox]]:mt-px",
    }

    FIELD_CONTENT = "group/field-content flex flex-1 flex-col gap-0.5 leading-snug"

    FIELD_LABEL = "group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-data-checked:border-primary/30 has-data-checked:bg-primary/5 has-[>[data-slot=field]]:rounded-lg has-[>[data-slot=field]]:border border-input *:data-[slot=field]:p-2.5 dark:has-data-checked:border-primary/20 dark:has-data-checked:bg-primary/10 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col"

    FIELD_TITLE = "flex w-fit items-center gap-2 text-sm font-medium group-data-[disabled=true]/field:opacity-50"

    FIELD_DESCRIPTION = "text-left text-sm leading-normal font-normal text-muted-foreground group-has-data-horizontal/field:text-balance [[data-variant=legend]+&]:-mt-1.5 last:mt-0 nth-last-2:-mt-1 [&>a]:underline [&>a]:underline-offset-4 [&>a:hover]:text-primary"

    FIELD_SEPARATOR = (
        "relative -my-2 h-5 text-sm group-data-[variant=outline]/field-group:-mb-2"
    )

    FIELD_ERROR = "text-sm font-normal text-destructive"


class FieldSet(elements.Fieldset):
    @classmethod
    def create(cls, *children, **props) -> elements.Fieldset:
        props["data-slot"] = "field-set"
        props["class_name"] = (
            f"{ClassNames.FIELD_SET} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldLegend(elements.Legend):
    variant: Var[LiteralLegendVariant]

    @classmethod
    def create(cls, *children, **props) -> elements.Legend:
        props["data-slot"] = "field-legend"
        variant = props.pop("variant", "legend")
        props["data-variant"] = variant
        props["class_name"] = (
            f"{ClassNames.FIELD_LEGEND} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldGroup(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["data-slot"] = "field-group"
        props["class_name"] = (
            f"{ClassNames.FIELD_GROUP} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldRoot(elements.Div):
    orientation: Var[LiteralOrientation]

    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["role"] = "group"
        props["data-slot"] = "field"

        orientation = props.pop("orientation", "vertical")
        props["data-orientation"] = orientation

        orientation_styles = ClassNames.FIELD_ROOT_ORIENTATIONS.get(orientation, "")

        props["class_name"] = (
            f"{ClassNames.FIELD_ROOT_BASE} {orientation_styles} {props.get('class_name', '')}".strip()
        )

        return super().create(*children, **props)


class FieldContent(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["data-slot"] = "field-content"
        props["class_name"] = (
            f"{ClassNames.FIELD_CONTENT} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldLabel(elements.Label):
    @classmethod
    def create(cls, *children, **props) -> elements.Label:
        props["data-slot"] = "field-label"
        props["class_name"] = (
            f"{ClassNames.FIELD_LABEL} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldTitle(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["data-slot"] = "field-label"
        props["class_name"] = (
            f"{ClassNames.FIELD_TITLE} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldDescription(elements.P):
    @classmethod
    def create(cls, *children, **props) -> elements.P:
        props["data-slot"] = "field-description"
        props["class_name"] = (
            f"{ClassNames.FIELD_DESCRIPTION} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldSeparator(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["data-slot"] = "field-separator"
        props["data-content"] = "true" if children else "false"
        props["class_name"] = (
            f"{ClassNames.FIELD_SEPARATOR} {props.get('class_name', '')}".strip()
        )

        inner_elements = [separator(class_name="absolute inset-0 top-1/2")]
        if children:
            inner_elements.append(
                elements.Span(
                    *children,
                    data_slot="field-separator-content",
                    class_name="relative mx-auto block w-fit bg-background px-2 text-muted-foreground",
                )
            )
        return super().create(*inner_elements, **props)


class FieldError(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["role"] = "alert"
        props["data-slot"] = "field-error"
        props["class_name"] = (
            f"{ClassNames.FIELD_ERROR} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class Field(ComponentNamespace):
    set = staticmethod(FieldSet.create)
    legend = staticmethod(FieldLegend.create)
    group = staticmethod(FieldGroup.create)
    root = staticmethod(FieldRoot.create)
    content = staticmethod(FieldContent.create)
    label = staticmethod(FieldLabel.create)
    title = staticmethod(FieldTitle.create)
    description = staticmethod(FieldDescription.create)
    separator = staticmethod(FieldSeparator.create)
    error = staticmethod(FieldError.create)
    class_names = ClassNames


field = Field()
