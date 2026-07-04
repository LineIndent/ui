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
