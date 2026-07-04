from typing import Literal

from reflex.components.component import ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.el import Div

from .base_ui import BaseUIComponent
from .component import CoreComponent
from .separator import SeparatorComponent


class ClassNames:
    BASE_GROUP = "flex w-fit items-stretch *:focus-visible:relative *:focus-visible:z-10 has-[>[data-slot=button-group]]:gap-2 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-lg [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1"
    HORIZONTAL = "*:data-slot:rounded-r-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-r-lg! [&>[data-slot]~[data-slot]]:rounded-l-none [&>[data-slot]~[data-slot]]:border-l-0"
    VERTICAL = "flex-col *:data-slot:rounded-b-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-b-lg! [&>[data-slot]~[data-slot]]:rounded-t-none [&>[data-slot]~[data-slot]]:border-t-0"
    TEXT = "flex items-center gap-2 rounded-lg border bg-muted px-2.5 text-sm font-medium [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4"
    SEPARATOR = "relative self-stretch bg-input data-horizontal:mx-px data-horizontal:w-auto data-vertical:my-px data-vertical:h-auto"


class ButtonGroupRoot(Div, CoreComponent):
    orientation: Var[Literal["horizontal", "vertical"]]

    @classmethod
    def create(cls, *children, **props) -> Div:
        props["data-slot"] = "button-group"
        orientation = props.get("orientation", "horizontal")

        variant_class = (
            ClassNames.HORIZONTAL
            if orientation == "horizontal"
            else ClassNames.VERTICAL
        )
        combined_class = f"{ClassNames.BASE_GROUP} {variant_class}"

        cls.set_class_name(combined_class, props)

        props["role"] = "group"
        props["data-orientation"] = orientation

        return super().create(*children, **props)


class ButtonGroupText(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> Div:
        props["data-slot"] = "button-group-text"
        cls.set_class_name(ClassNames.TEXT, props)
        return super().create(*children, **props)


class ButtonGroupSeparator(SeparatorComponent):
    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "button-group-separator"

        if "orientation" not in props:
            props["orientation"] = "vertical"

        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class ButtonGroup(ComponentNamespace):
    root = staticmethod(ButtonGroupRoot.create)
    text = staticmethod(ButtonGroupText.create)
    separator = staticmethod(ButtonGroupSeparator.create)


button_group = ButtonGroup()
