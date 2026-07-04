from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.el import Div

from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralAlign = Literal["start", "center", "end"]
LiteralSide = Literal["bottom", "inline-end", "inline-start", "left", "right", "top"]
LiteralPosition = Literal["absolute", "fixed"]


class ClassNames:
    ROOT = ""
    TRIGGER = ""
    BACKDROP = ""
    PORTAL = ""
    POSITIONER = ""
    POPUP = "z-50 flex w-72 origin-(--transform-origin) flex-col gap-2.5 rounded-lg bg-popover p-2.5 text-sm text-popover-foreground shadow-md ring-1 ring-foreground/10 outline-hidden duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95"
    ARROW = "data-[side=bottom]:top-[-8px] data-[side=left]:right-[-13px] data-[side=left]:rotate-90 data-[side=right]:left-[-13px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-8px] data-[side=top]:rotate-180"
    HEADER = "flex flex-col gap-0.5 text-sm"
    TITLE = "font-medium"
    DESCRIPTION = "text-muted-foreground"
    CLOSE = ""


class PopoverBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/popover"

    @property
    def import_var(self):
        return ImportVar(tag="Popover", package_path="", install=False)


class PopoverRoot(PopoverBaseComponent):
    tag = "Popover.Root"

    default_open: Var[bool]

    open: Var[bool]

    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    modal: Var[bool | Literal["trap-focus"]]

    open_on_hover: Var[bool]

    delay: Var[int]

    close_delay: Var[int]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover"
        return super().create(*children, **props)


class PopoverTrigger(PopoverBaseComponent):
    tag = "Popover.Trigger"

    native_button: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class PopoverBackdrop(PopoverBaseComponent):
    tag = "Popover.Backdrop"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover-backdrop"
        cls.set_class_name(ClassNames.BACKDROP, props)
        return super().create(*children, **props)


class PopoverPortal(PopoverBaseComponent):
    tag = "Popover.Portal"

    container: Var[str]

    keep_mounted: Var[bool]


class PopoverPositioner(PopoverBaseComponent):
    tag = "Popover.Positioner"

    align: Var[LiteralAlign]

    align_offset: Var[int]

    side: Var[LiteralSide]

    side_offset: Var[int]

    arrow_padding: Var[int]

    anchor: Var[str]

    collision_boundary: Var[str]

    collision_padding: Var[int | list[int]]

    sticky: Var[bool]

    position_method: Var[LiteralPosition]

    track_anchor: Var[bool]

    collision_avoidance: Var[str]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover-positioner"
        props.setdefault("side_offset", 4)
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class PopoverPopup(PopoverBaseComponent):
    tag = "Popover.Popup"

    initial_focus: Var[str]

    final_focus: Var[str]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class PopoverArrow(PopoverBaseComponent):
    tag = "Popover.Arrow"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover-arrow"
        cls.set_class_name(ClassNames.ARROW, props)
        return super().create(*children, **props)


class PopoverHeader(Div):
    @classmethod
    def create(cls, *children, **props):
        props.setdefault("data-slot", "popover-header")
        props["class_name"] = cn(ClassNames.HEADER, props.get("class_name", ""))
        return super().create(*children, **props)


class PopoverTitle(PopoverBaseComponent):
    tag = "Popover.Title"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover-title"
        cls.set_class_name(ClassNames.TITLE, props)
        return super().create(*children, **props)


class PopoverDescription(PopoverBaseComponent):
    tag = "Popover.Description"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover-description"
        cls.set_class_name(ClassNames.DESCRIPTION, props)
        return super().create(*children, **props)


class PopoverClose(PopoverBaseComponent):
    tag = "Popover.Close"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "popover-close"
        cls.set_class_name(ClassNames.CLOSE, props)
        return super().create(*children, **props)


class Popover(ComponentNamespace):
    root = staticmethod(PopoverRoot.create)
    trigger = staticmethod(PopoverTrigger.create)
    backdrop = staticmethod(PopoverBackdrop.create)
    portal = staticmethod(PopoverPortal.create)
    positioner = staticmethod(PopoverPositioner.create)
    popup = staticmethod(PopoverPopup.create)
    arrow = staticmethod(PopoverArrow.create)
    header = staticmethod(PopoverHeader.create)
    title = staticmethod(PopoverTitle.create)
    description = staticmethod(PopoverDescription.create)
    close = staticmethod(PopoverClose.create)
    class_names = ClassNames


popover = Popover()
