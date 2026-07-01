from typing import Any, Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex.vars.object import ObjectVar
from reflex_components_core.core.foreach import foreach
from reflex_components_core.el import Div

from ..icons.hugeicon import hi, icon
from .base_ui import PACKAGE_NAME, BaseUIComponent
from .button import button

LiteralOrientation = Literal["horizontal", "vertical"]

ITEMS_TYPE = list[dict[str, str | Component]]


class ClassNames:
    """Class names for accordion components."""

    ROOT = "flex w-full flex-col divide-y divide-input"
    ITEM = "not-last:border-b"
    HEADER = ""
    TRIGGER = "group/accordion-trigger relative flex flex-1 items-start justify-between rounded-lg border border-transparent py-2.5 text-left text-sm font-medium transition-all outline-none hover:underline focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 focus-visible:after:border-ring disabled:pointer-events-none disabled:opacity-50 **:data-[slot=accordion-trigger-icon]:ml-auto **:data-[slot=accordion-trigger-icon]:size-4 **:data-[slot=accordion-trigger-icon]:text-muted-foreground"
    PANEL = "h-[var(--accordion-panel-height)] overflow-hidden transition-[height] ease-out data-[ending-style]:h-0 data-[starting-style]:h-0"
    PANEL_DIV = ""
    TRIGGER_ICON = "size-4 shrink-0 transition-all ease-out group-data-[panel-open]:scale-110 group-data-[panel-open]:rotate-45"


class AccordionBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/accordion"

    @property
    def import_var(self):
        """Return the import variable for the accordion component."""
        return ImportVar(tag="Accordion", package_path="", install=False)


class AccordionRoot(AccordionBaseComponent):
    """Groups all parts of the accordion."""

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
        """Create the accordion root component."""
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
        """Create the accordion item component."""
        props["data-slot"] = "accordion-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class AccordionHeader(AccordionBaseComponent):
    tag = "Accordion.Header"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the accordion header component."""
        props["data-slot"] = "accordion-header"
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class AccordionTrigger(AccordionBaseComponent):
    tag = "Accordion.Trigger"

    title: Var[str]

    native_button: Var[bool]

    render_: Var[Component] | None = None

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "accordion-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)

        if "render_" not in props or props["render_"] is None:
            if "title" not in props:
                if len(children) == 1 and isinstance(children[0], str):
                    props["title"] = children[0]
                elif children:
                    raise TypeError(
                        "AccordionTrigger expects a single string child "
                        "when used without a `title` prop."
                    )
                else:
                    raise ValueError("AccordionTrigger requires a `title`.")

            props["render_"] = button(
                props["title"],
                hi(
                    "Add01Icon",
                    class_name=(
                        "text-muted-foreground size-4 transition-transform duration-50 ease-in-out "
                        "group-aria-[expanded=true]:rotate-45"
                    ),
                ),
                variant="ghost",
                class_name=(
                    "w-full flex items-center justify-between group py-2 "
                    "font-medium !text-sm hover:bg-transparent !px-0"
                ),
            )

        return super().create(*children, **props)


class AccordionPanel(AccordionBaseComponent):
    tag = "Accordion.Panel"

    hidden_until_found: Var[bool]

    keep_mounted: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the accordion panel component."""
        props["data-slot"] = "accordion-panel"
        cls.set_class_name(ClassNames.PANEL, props)
        return super().create(*children, **props)


class Accordion(ComponentNamespace):
    root = staticmethod(AccordionRoot.create)
    item = staticmethod(AccordionItem.create)
    header = staticmethod(AccordionHeader.create)
    trigger = staticmethod(AccordionTrigger.create)
    panel = staticmethod(AccordionPanel.create)
    class_names = ClassNames


accordion = Accordion()
