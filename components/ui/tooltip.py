"""Tooltip component from base-ui components."""

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


# Constants for default class names
class ClassNames:
    """Class names for tooltip components."""

    TRIGGER = "inline-flex items-center justify-center"
    POPUP = "z-50 inline-flex w-fit max-w-xs origin-(--transform-origin) items-center gap-1.5 rounded-radius bg-foreground px-3 py-1.5 text-xs text-background has-data-[slot=kbd]:pr-1.5 data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 **:data-[slot=kbd]:relative **:data-[slot=kbd]:isolate **:data-[slot=kbd]:z-50 **:data-[slot=kbd]:rounded-sm data-[state=delayed-open]:animate-in data-[state=delayed-open]:fade-in-0 data-[state=delayed-open]:zoom-in-95 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95"
    ARROW = "data-[side=bottom]:top-[-7.5px] data-[side=left]:right-[-12.5px] data-[side=left]:rotate-90 data-[side=right]:left-[-12.5px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-7.5px] data-[side=top]:rotate-180"


class TooltipBaseComponent(BaseUIComponent):
    """Base component for tooltip components."""

    library = f"{PACKAGE_NAME}/tooltip"

    @property
    def import_var(self):
        """Return the import variable for the tooltip component."""
        return ImportVar(tag="Tooltip", package_path="", install=False)


class TooltipRoot(TooltipBaseComponent):
    """Root component for a tooltip."""

    tag = "Tooltip.Root"

    # Whether the tooltip is currently open.
    open: Var[bool]

    # Whether the tooltip is initially open. To render a controlled tooltip, use the open prop instead. Defaults to False.
    default_open: Var[bool]

    # Event handler called when the tooltip is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Event handler called after any animations complete when the tooltip is opened or closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    # Determines which axis the tooltip should track the cursor on. Defaults to "None".
    track_cursor_axis: Var[LiteralTrackCursorAxis]

    # Whether the tooltip is disabled. Defaults to False.
    disabled: Var[bool]

    # How long to wait before opening the tooltip. Specified in milliseconds. Defaults to 600.
    delay: Var[int]

    # How long to wait before closing the tooltip. Specified in milliseconds. Defaults to 0.
    close_delay: Var[int]

    # Whether the tooltip contents can be hovered without closing the tooltip. Defaults to True.
    hoverable: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tooltip root component."""
        props["data-slot"] = "tooltip"
        return super().create(*children, **props)


class TooltipProvider(TooltipBaseComponent):
    """Provider component for tooltips."""

    tag = "Tooltip.Provider"

    # How long to wait before opening a tooltip. Specified in milliseconds.
    delay: Var[int]

    # How long to wait before closing a tooltip. Specified in milliseconds.
    close_delay: Var[int]

    # Another tooltip will open instantly if the previous tooltip is closed within this timeout. Specified in milliseconds. Defaults to 400.
    timeout: Var[int]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tooltip provider component."""
        props["data-slot"] = "tooltip-provider"
        return super().create(*children, **props)


class TooltipTrigger(TooltipBaseComponent):
    """Trigger element for the tooltip."""

    tag = "Tooltip.Trigger"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tooltip trigger component."""
        props["data-slot"] = "tooltip-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class TooltipPortal(TooltipBaseComponent):
    """Portal that moves the tooltip to a different part of the DOM."""

    tag = "Tooltip.Portal"

    # A parent element to render the portal element into.
    container: Var[str]

    # Whether to keep the portal mounted in the DOM while the popup is hidden. Defaults to False.
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tooltip portal component."""
        props["data-slot"] = "tooltip-portal"
        return super().create(*children, **props)


class TooltipPositioner(TooltipBaseComponent):
    """Positions the tooltip relative to the trigger."""

    tag = "Tooltip.Positioner"

    # How to align the popup relative to the specified side. Defaults to "center".
    align: Var[LiteralAlign]

    # Additional offset along the alignment axis in pixels. Defaults to 0.
    align_offset: Var[int]

    # Which side of the anchor element to align the popup against. May automatically change to avoid collisions. Defaults to "top".
    side: Var[LiteralSide]

    # Distance between the anchor and the popup in pixels. Defaults to 0.
    side_offset: Var[int]

    # Minimum distance to maintain between the arrow and the edges of the popup. Use it to prevent the arrow element from hanging out of the rounded corners of a popup. Defaults to 5.
    arrow_padding: Var[int]

    # An element to position the popup against. By default, the popup will be positioned against the trigger.
    anchor: Var[str]

    # An element or a rectangle that delimits the area that the popup is confined to. Defaults to "clipping-ancestors".
    collision_boundary: Var[str]

    # Additional space to maintain from the edge of the collision boundary. Defaults to 5.
    collision_padding: Var[int]

    # Whether to maintain the popup in the viewport after the anchor element was scrolled out of view. Defaults to False.
    sticky: Var[bool]

    # Determines which CSS position property to use. Defaults to "absolute".
    position_method: Var[LiteralPositionMethod]

    # Indicates whether the tooltip should track the anchor's position
    track_anchor: Var[bool]

    # Determines how to handle collisions when positioning the popup.
    collision_avoidance: Var[str | dict[str, str]]

    # Render prop for the positioner
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tooltip positioner component."""
        props["data-slot"] = "tooltip-positioner"
        return super().create(*children, **props)


class TooltipPopup(TooltipBaseComponent):
    """Container for the tooltip content."""

    tag = "Tooltip.Popup"

    # Render prop for the popup
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tooltip popup component."""
        props["data-slot"] = "tooltip-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class TooltipArrow(TooltipBaseComponent):
    """Arrow element for the tooltip."""

    tag = "Tooltip.Arrow"

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the tooltip arrow component."""
        props["data-slot"] = "tooltip-arrow"
        cls.set_class_name(ClassNames.ARROW, props)

        if not children:
            return super().create(arrow_svg(), **props)

        return super().create(*children, **props)


class HighLevelTooltip(TooltipRoot):
    """High level wrapper for the Tooltip component."""

    # Content to display in the tooltip
    content: Var[str] | Component

    # Props for different component parts
    _root_props = {
        "open",
        "default_open",
        "on_open_change",
        "on_open_change_complete",
        "track_cursor_axis",
        "disabled",
        "delay",
        "close_delay",
        "hoverable",
    }
    _portal_props = {
        "container",
        "keep_mounted",
    }
    _positioner_props = {
        "align",
        "align_offset",
        "side",
        "side_offset",
        "arrow_padding",
        "anchor",
        "collision_boundary",
        "collision_padding",
        "sticky",
        "position_method",
        "track_anchor",
        "collision_avoidance",
        "class_name",
    }

    @classmethod
    def create(
        cls,
        trigger: Component,
        content: str | Component | None = None,
        **props,
    ) -> BaseUIComponent:
        """Create a high level tooltip component.

        Args:
            trigger: The component that triggers the tooltip.
            content: The content to display in the tooltip.
            **props: Additional properties to apply to the tooltip component.

        Returns:
            The tooltip component with all necessary subcomponents.
        """
        # Extract content from props if provided there
        if content is None and "content" in props:
            content = props.pop("content")

        # Extract props for different parts
        root_props = {k: props.pop(k) for k in cls._root_props & props.keys()}
        portal_props = {k: props.pop(k) for k in cls._portal_props & props.keys()}
        positioner_props = {
            k: props.pop(k) for k in cls._positioner_props & props.keys()
        }

        # Set default values
        positioner_props.setdefault("side_offset", 8)
        root_props.setdefault("delay", 0)
        root_props.setdefault("close_delay", 0)

        return TooltipRoot.create(
            TooltipTrigger.create(
                render_=trigger,
            ),
            TooltipPortal.create(
                TooltipPositioner.create(
                    TooltipPopup.create(
                        TooltipArrow.create(arrow_svg()),
                        content,
                    ),
                    **positioner_props,
                ),
                **portal_props,
            ),
            **root_props,
        )


class Tooltip(ComponentNamespace):
    """Namespace for Tooltip components."""

    provider = staticmethod(TooltipProvider.create)
    root = staticmethod(TooltipRoot.create)
    trigger = staticmethod(TooltipTrigger.create)
    portal = staticmethod(TooltipPortal.create)
    positioner = staticmethod(TooltipPositioner.create)
    popup = staticmethod(TooltipPopup.create)
    arrow = staticmethod(TooltipArrow.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelTooltip.create)


tooltip = Tooltip()
