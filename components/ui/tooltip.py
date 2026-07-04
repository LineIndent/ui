from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..icons.others import arrow_svg
from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralSide = Literal["top", "right", "bottom", "left", "inline-end", "inline-start"]
LiteralAlign = Literal["start", "center", "end"]
LiteralPositionMethod = Literal["absolute", "fixed"]
LiteralTrackCursorAxis = Literal["none", "bottom", "x", "y"]


class ClassNames:
    TRIGGER = "inline-flex items-center justify-center"
    POPUP = "z-50 inline-flex w-fit max-w-xs origin-(--transform-origin) items-center gap-1.5 rounded-lg bg-foreground px-3 py-1.5 text-xs text-background has-data-[slot=kbd]:pr-1.5 data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 **:data-[slot=kbd]:relative **:data-[slot=kbd]:isolate **:data-[slot=kbd]:z-50 **:data-[slot=kbd]:rounded-sm data-[state=delayed-open]:animate-in data-[state=delayed-open]:fade-in-0 data-[state=delayed-open]:zoom-in-95 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95"
    ARROW = "data-[side=bottom]:top-[-7.5px] data-[side=left]:right-[-12.5px] data-[side=left]:rotate-90 data-[side=right]:left-[-12.5px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-7.5px] data-[side=top]:rotate-180"


class TooltipBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/tooltip"

    @property
    def import_var(self):
        return ImportVar(tag="Tooltip", package_path="", install=False)


class TooltipRoot(TooltipBaseComponent):
    tag = "Tooltip.Root"

    open: Var[bool]

    default_open: Var[bool]

    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    track_cursor_axis: Var[LiteralTrackCursorAxis]

    disabled: Var[bool]

    delay: Var[int]

    close_delay: Var[int]

    hoverable: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tooltip"
        return super().create(*children, **props)


class TooltipProvider(TooltipBaseComponent):
    tag = "Tooltip.Provider"

    delay: Var[int]

    close_delay: Var[int]

    timeout: Var[int]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tooltip-provider"
        return super().create(*children, **props)


class TooltipTrigger(TooltipBaseComponent):
    tag = "Tooltip.Trigger"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tooltip-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class TooltipPortal(TooltipBaseComponent):
    tag = "Tooltip.Portal"

    container: Var[str]

    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tooltip portal component."""
        props["data-slot"] = "tooltip-portal"
        return super().create(*children, **props)


class TooltipPositioner(TooltipBaseComponent):
    tag = "Tooltip.Positioner"

    align: Var[LiteralAlign]

    align_offset: Var[int]

    side: Var[LiteralSide]

    side_offset: Var[int]

    arrow_padding: Var[int]

    anchor: Var[str]

    collision_boundary: Var[str]

    collision_padding: Var[int]

    sticky: Var[bool]

    position_method: Var[LiteralPositionMethod]

    track_anchor: Var[bool]

    collision_avoidance: Var[str | dict[str, str]]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tooltip-positioner"
        return super().create(*children, **props)


class TooltipPopup(TooltipBaseComponent):
    tag = "Tooltip.Popup"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data_slot"] = "tooltip-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class TooltipArrow(TooltipBaseComponent):
    tag = "Tooltip.Arrow"

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tooltip-arrow"
        cls.set_class_name(ClassNames.ARROW, props)

        if not children:
            return super().create(arrow_svg(), **props)

        return super().create(*children, **props)


class Tooltip(ComponentNamespace):
    provider = staticmethod(TooltipProvider.create)
    root = staticmethod(TooltipRoot.create)
    trigger = staticmethod(TooltipTrigger.create)
    portal = staticmethod(TooltipPortal.create)
    positioner = staticmethod(TooltipPositioner.create)
    popup = staticmethod(TooltipPopup.create)
    arrow = staticmethod(TooltipArrow.create)
    class_names = ClassNames


tooltip = Tooltip()
