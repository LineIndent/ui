

# Context Menu

Displays a menu of actions triggered by a right click.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component context_menu
```

### Manual Installation

```python
"""Custom context menu component."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.core.foreach import foreach

from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent
from .button import button

LiteralOpenChangeReason = Literal[
    "arrowKey",
    "escapeKey",
    "select",
    "hover",
    "click",
    "focus",
    "dismiss",
    "typeahead",
    "tab",
]
LiteralMenuOrientation = Literal["vertical", "horizontal"]
LiteralSide = Literal["top", "right", "bottom", "left"]
LiteralAlign = Literal["start", "center", "end"]
LiteralPositionMethod = Literal["absolute", "fixed"]
LiteralCollisionAvoidance = Literal["flip", "shift", "auto"]
LiteralMenuSize = Literal["xs", "sm", "md", "lg", "xl"]


class ClassNames:
    """Class names for context menu components."""

    TRIGGER = ""
    PORTAL = ""
    BACKDROP = "fixed inset-0"
    POPUP = "z-50 max-h-(--radix-context-menu-content-available-height) min-w-[8rem] origin-(--radix-context-menu-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-md border border-input p-1 shadow-md bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2"
    ITEM = "relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 [&_svg:not([class*='text-'])]:text-muted-foreground"
    ITEM_INDICATOR = "text-current"
    ITEM_TEXT = "text-start"
    SEPARATOR = "bg-border -mx-1 my-1 h-px"
    ARROW = "data-[side=bottom]:top-[-8px] data-[side=left]:right-[-13px] data-[side=left]:rotate-90 data-[side=right]:left-[-13px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-8px] data-[side=top]:rotate-180"
    POSITIONER = "outline-none"
    GROUP = ""
    GROUP_LABEL = "text-foreground px-2 py-1.5 text-sm font-medium"
    RADIO_GROUP = ""
    RADIO_ITEM = "relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    RADIO_ITEM_INDICATOR = (
        "absolute left-2 flex size-3.5 items-center justify-center pointer-events-none"
    )
    CHECKBOX_ITEM = "relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    CHECKBOX_ITEM_INDICATOR = (
        "absolute left-2 flex size-3.5 items-center justify-center pointer-events-none"
    )
    SUBMENU_TRIGGER = "relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 [&_svg:not([class*='text-'])]:text-muted-foreground"


class ContextMenuBaseComponent(BaseUIComponent):
    """Base component for context menu components."""

    library = f"{PACKAGE_NAME}/context-menu"

    @property
    def import_var(self):
        """Return the import variable for the context menu component."""
        return ImportVar(tag="ContextMenu", package_path="", install=False)


class ContextMenuRoot(ContextMenuBaseComponent):
    """Groups all parts of the context menu. Doesn't render its own HTML element."""

    tag = "ContextMenu.Root"

    # Whether the context menu is initially open. To render a controlled context menu, use the open prop instead. Defaults to False.
    default_open: Var[bool]

    # Whether the context menu is currently open.
    open: Var[bool]

    # Event handler called when the context menu is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    # A ref to imperative actions. When specified, the context menu will not be unmounted when closed. Instead, the unmount function must be called to unmount the context menu manually. Useful when the context menu's animation is controlled by an external library.
    actions_ref: Var[str]

    # When in a submenu, determines whether pressing the Escape key closes the entire menu, or only the current child menu. Defaults to True.
    close_parent_on_esc: Var[bool]

    # Event handler called after any animations complete when the context menu is closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether keyboard navigation should loop around when reaching the end of the items. Defaults to True.
    loop: Var[bool]

    # The visual orientation of the menu. Controls whether roving focus uses up/down or left/right arrow keys. Defaults to "vertical".
    orientation: Var[LiteralMenuOrientation]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu root component."""
        props["data-slot"] = "context-menu"
        return super().create(*children, **props)


class ContextMenuTrigger(ContextMenuBaseComponent):
    """An area that opens the context menu on right click or long press. Renders a <div> element."""

    tag = "ContextMenu.Trigger"

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu trigger component."""
        props["data-slot"] = "context-menu-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class ContextMenuPortal(ContextMenuBaseComponent):
    """A portal element that moves the popup to a different part of the DOM. By default, the portal element is appended to <body>."""

    tag = "ContextMenu.Portal"

    # A parent element to render the portal element into. Defaults to document.body.
    container: Var[str]

    # Whether to keep the portal mounted in the DOM while the popup is hidden. Defaults to False.
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu portal component."""
        props["data-slot"] = "context-menu-portal"
        cls.set_class_name(ClassNames.PORTAL, props)
        return super().create(*children, **props)


class ContextMenuBackdrop(ContextMenuBaseComponent):
    """A backdrop element that covers the entire viewport when the context menu is open. Renders a <div> element."""

    tag = "ContextMenu.Backdrop"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu backdrop component."""
        props["data-slot"] = "context-menu-backdrop"
        cls.set_class_name(ClassNames.BACKDROP, props)
        return super().create(*children, **props)


class ContextMenuPositioner(ContextMenuBaseComponent):
    """Positions the context menu popup against the trigger. Renders a <div> element."""

    tag = "ContextMenu.Positioner"

    # Determines how to handle collisions when positioning the popup.
    collision_avoidance: Var[LiteralCollisionAvoidance]

    # How to align the popup relative to the specified side. Defaults to "center".
    align: Var[LiteralAlign]

    # Additional offset along the alignment axis in pixels. Defaults to 0.
    align_offset: Var[int]

    # Which side of the anchor element to align the popup against. May automatically change to avoid collisions. Defaults to "bottom".
    side: Var[LiteralSide]

    # Distance between the anchor and the popup in pixels. Defaults to 0.
    side_offset: Var[int]

    # Minimum distance to maintain between the arrow and the edges of the popup. Defaults to 5.
    arrow_padding: Var[int]

    # Additional space to maintain from the edge of the collision boundary. Defaults to 5.
    collision_padding: Var[int]

    # An element or a rectangle that delimits the area that the popup is confined to. Defaults to "clipping-ancestors".
    collision_boundary: Var[str]

    # Whether to maintain the popup in the viewport after the anchor element was scrolled out of view. Defaults to False.
    sticky: Var[bool]

    # Whether the popup tracks any layout shift of its positioning anchor. Defaults to True.
    track_anchor: Var[bool]

    # Determines which CSS position property to use. Defaults to "absolute".
    position_method: Var[LiteralPositionMethod]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu positioner component."""
        props["data-slot"] = "context-menu-positioner"
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class ContextMenuPopup(ContextMenuBaseComponent):
    """A container for the context menu items. Renders a <div> element."""

    tag = "ContextMenu.Popup"

    # Determines the element to focus when the context menu is closed. By default, focus returns to the trigger.
    final_focus: Var[str]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu popup component."""
        props["data-slot"] = "context-menu-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class ContextMenuArrow(ContextMenuBaseComponent):
    """Displays an element positioned against the context menu anchor. Renders a <div> element."""

    tag = "ContextMenu.Arrow"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu arrow component."""
        props["data-slot"] = "context-menu-arrow"
        cls.set_class_name(ClassNames.ARROW, props)
        return super().create(*children, **props)


class ContextMenuItem(ContextMenuBaseComponent):
    """An individual interactive item in the context menu. Renders a <div> element."""

    tag = "ContextMenu.Item"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]

    # Whether to close the context menu when the item is clicked. Defaults to True.
    close_on_click: Var[bool]

    # Whether the component renders a native button element when replacing it via the render prop. Set to true if the rendered element is a native button. Defaults to False.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu item component."""
        props["data-slot"] = "context-menu-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class ContextMenuSeparator(ContextMenuBaseComponent):
    """A separator element accessible to screen readers. Renders a <div> element."""

    tag = "ContextMenu.Separator"

    # The orientation of the separator. Defaults to "horizontal".
    orientation: Var[LiteralMenuOrientation]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu separator component."""
        props["data-slot"] = "context-menu-separator"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class ContextMenuGroup(ContextMenuBaseComponent):
    """Groups related context menu items with the corresponding label. Renders a <div> element."""

    tag = "ContextMenu.Group"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu group component."""
        props["data-slot"] = "context-menu-group"
        cls.set_class_name(ClassNames.GROUP, props)
        return super().create(*children, **props)


class ContextMenuGroupLabel(ContextMenuBaseComponent):
    """An accessible label that is automatically associated with its parent group. Renders a <div> element."""

    tag = "ContextMenu.GroupLabel"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu group label component."""
        props["data-slot"] = "context-menu-group-label"
        cls.set_class_name(ClassNames.GROUP_LABEL, props)
        return super().create(*children, **props)


class ContextMenuRadioGroup(ContextMenuBaseComponent):
    """Groups related radio items. Renders a <div> element."""

    tag = "ContextMenu.RadioGroup"

    # The uncontrolled value of the radio item that should be initially selected. To render a controlled radio group, use the value prop instead.
    default_value: Var[str | int]

    # The controlled value of the radio group.
    value: Var[str | int]

    # Event handler called when the value changes.
    on_value_change: EventHandler[passthrough_event_spec(str | int, dict)]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu radio group component."""
        props["data-slot"] = "context-menu-radio-group"
        cls.set_class_name(ClassNames.RADIO_GROUP, props)
        return super().create(*children, **props)


class ContextMenuRadioItem(ContextMenuBaseComponent):
    """A context menu item that works like a radio button in a given group. Renders a <div> element."""

    tag = "ContextMenu.RadioItem"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]

    value: Var[str | int]

    # Whether to close the context menu when the item is clicked. Defaults to False.
    close_on_click: Var[bool]

    # Whether the component renders a native button element when replacing it via the render prop. Set to true if the rendered element is a native button. Defaults to False.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu radio item component."""
        props["data-slot"] = "context-menu-radio-item"
        cls.set_class_name(ClassNames.RADIO_ITEM, props)
        return super().create(*children, **props)


class ContextMenuRadioItemIndicator(ContextMenuBaseComponent):
    """Indicates whether the radio item is selected. Renders a <div> element."""

    tag = "ContextMenu.RadioItemIndicator"

    # Whether to keep the indicator mounted in the DOM when the radio item is not checked. Defaults to False.
    keep_mounted: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu radio item indicator component."""
        props["data-slot"] = "context-menu-radio-item-indicator"
        cls.set_class_name(ClassNames.RADIO_ITEM_INDICATOR, props)
        return super().create(*children, **props)


class ContextMenuCheckboxItem(ContextMenuBaseComponent):
    """A context menu item that toggles a setting on or off. Renders a <div> element."""

    tag = "ContextMenu.CheckboxItem"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]

    # Whether the checkbox item is initially checked. To render a controlled checkbox item, use the checked prop instead. Defaults to False.
    default_checked: Var[bool]

    # Whether the checkbox item is currently checked. To render an uncontrolled checkbox item, use the default_checked prop instead.
    checked: Var[bool]

    # Event handler called when the checkbox item is ticked or unticked.
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Whether to close the context menu when the item is clicked. Defaults to False.
    close_on_click: Var[bool]

    # Whether the component renders a native button element when replacing it via the render prop. Set to true if the rendered element is a native button. Defaults to False.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu checkbox item component."""
        props["data-slot"] = "context-menu-checkbox-item"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM, props)
        return super().create(*children, **props)


class ContextMenuCheckboxItemIndicator(ContextMenuBaseComponent):
    """Indicates whether the checkbox item is ticked. Renders a <div> element."""

    tag = "ContextMenu.CheckboxItemIndicator"

    # Whether to keep the indicator mounted in the DOM when the checkbox item is not checked. Defaults to False.
    keep_mounted: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu checkbox item indicator component."""
        props["data-slot"] = "context-menu-checkbox-item-indicator"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM_INDICATOR, props)
        return super().create(*children, **props)


class ContextMenuSubmenuRoot(ContextMenuBaseComponent):
    """Groups all parts of a submenu. Doesn't render its own HTML element."""

    tag = "ContextMenu.SubmenuRoot"

    # Whether the submenu is initially open. To render a controlled submenu, use the open prop instead. Defaults to False.
    default_open: Var[bool]

    # Whether the submenu is currently open.
    open: Var[bool]

    # Event handler called when the submenu is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    # When in a submenu, determines whether pressing the Escape key closes the entire menu, or only the current child menu. Defaults to True.
    close_parent_on_esc: Var[bool]

    # Event handler called after any animations complete when the submenu is closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the submenu should also open when the trigger is hovered. Defaults to True.
    open_on_hover: Var[bool]

    # How long to wait before the submenu may be opened on hover. Specified in milliseconds. Requires the open_on_hover prop. Defaults to 100.
    delay: Var[int]

    # How long to wait before closing the submenu that was opened on hover. Specified in milliseconds. Requires the open_on_hover prop. Defaults to 0.
    close_delay: Var[int]

    # Whether to loop keyboard focus back to the first item when the end of the list is reached while using the arrow keys. Defaults to True.
    loop: Var[bool]

    # The visual orientation of the submenu. Controls whether roving focus uses up/down or left/right arrow keys. Defaults to "vertical".
    orientation: Var[LiteralMenuOrientation]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu submenu root component."""
        props["data-slot"] = "context-menu-submenu-root"
        return super().create(*children, **props)


class ContextMenuSubmenuTrigger(ContextMenuBaseComponent):
    """A context menu item that opens a submenu."""

    tag = "ContextMenu.SubmenuTrigger"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]

    # Whether the component renders a native button element when replacing it via the render prop. Set to true if the rendered element is a native button. Defaults to False.
    native_button: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu submenu trigger component."""
        props["data-slot"] = "context-menu-submenu-trigger"
        cls.set_class_name(ClassNames.SUBMENU_TRIGGER, props)
        return super().create(*children, **props)


class HighLevelContextMenu(ContextMenuRoot):
    """High level wrapper for the ContextMenu component."""

    # The trigger component to use for the context menu
    trigger: Var[Component | None]

    # The list of items to display in the context menu - can be strings or tuples of (label, on_click_handler)
    items: Var[list[str | tuple[str, EventHandler]]]

    # The size of the context menu. Defaults to "md".
    size: Var[LiteralMenuSize]

    # Props for different component parts
    _item_props = {"close_on_click"}
    _positioner_props = {
        "align",
        "align_offset",
        "side",
        "arrow_padding",
        "collision_padding",
        "sticky",
        "position_method",
        "track_anchor",
        "side_offset",
        "collision_avoidance",
        "collision_boundary",
    }
    _portal_props = {"container", "keep_mounted"}

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create a context menu component.

        Args:
            *children: Additional children to include in the context menu.
            **props: Additional properties to apply to the context menu component.

        Returns:
            The context menu component.
        """
        # Extract props for different parts
        item_props = {k: props.pop(k) for k in cls._item_props & props.keys()}
        positioner_props = {
            k: props.pop(k) for k in cls._positioner_props & props.keys()
        }
        portal_props = {k: props.pop(k) for k in cls._portal_props & props.keys()}

        trigger = props.pop("trigger", None)
        items = props.pop("items", [])
        size = props.pop("size", "md")

        def create_context_menu_item(
            item: str | tuple[str, EventHandler],
        ) -> BaseUIComponent:
            if isinstance(item, tuple):
                label, on_click_handler = item
                return ContextMenuItem.create(
                    render_=button(
                        label,
                        variant="ghost",
                        class_name=ClassNames.ITEM,
                        disabled=props.get("disabled", False),
                        on_click=on_click_handler,
                        size=size,
                        type="button",
                    ),
                    key=label,
                    **item_props,
                )
            return ContextMenuItem.create(
                render_=button(
                    item,
                    variant="ghost",
                    class_name=ClassNames.ITEM,
                    disabled=props.get("disabled", False),
                    size=size,
                    type="button",
                ),
                key=item,
                **item_props,
            )

        if isinstance(items, Var):
            items_children = foreach(items, create_context_menu_item)
        else:
            items_children = [create_context_menu_item(item) for item in items]

        return ContextMenuRoot.create(
            (
                ContextMenuTrigger.create(
                    render_=trigger,
                )
                if trigger
                else None
            ),
            ContextMenuPortal.create(
                ContextMenuPositioner.create(
                    ContextMenuPopup.create(
                        items_children,
                        *children,
                        class_name=cn(
                            ClassNames.POPUP,
                            "",
                            # f"rounded-[calc(var(--radius-ui-{size})+0.25rem)]",
                        ),
                    ),
                    **positioner_props,
                ),
                **portal_props,
            ),
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "trigger",
            "items",
            "size",
        ]


class ContextMenu(ComponentNamespace):
    """Namespace for ContextMenu components."""

    root = staticmethod(ContextMenuRoot.create)
    trigger = staticmethod(ContextMenuTrigger.create)
    portal = staticmethod(ContextMenuPortal.create)
    backdrop = staticmethod(ContextMenuBackdrop.create)
    positioner = staticmethod(ContextMenuPositioner.create)
    popup = staticmethod(ContextMenuPopup.create)
    arrow = staticmethod(ContextMenuArrow.create)
    item = staticmethod(ContextMenuItem.create)
    separator = staticmethod(ContextMenuSeparator.create)
    group = staticmethod(ContextMenuGroup.create)
    group_label = staticmethod(ContextMenuGroupLabel.create)
    radio_group = staticmethod(ContextMenuRadioGroup.create)
    radio_item = staticmethod(ContextMenuRadioItem.create)
    radio_item_indicator = staticmethod(ContextMenuRadioItemIndicator.create)
    checkbox_item = staticmethod(ContextMenuCheckboxItem.create)
    checkbox_item_indicator = staticmethod(ContextMenuCheckboxItemIndicator.create)
    submenu_root = staticmethod(ContextMenuSubmenuRoot.create)
    submenu_trigger = staticmethod(ContextMenuSubmenuTrigger.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelContextMenu.create)


context_menu = ContextMenu()
```


# Usage


```python
from components.ui.context_menu import context_menu
```


# Anatomy 
Use the following composition to build a `Context Menu` component.


```python
context_menu.root(
    context_menu.trigger(),
    context_menu.portal(
        context_menu.positioner(
            context_menu.popup(
                context_menu.item(),
                context_menu.separator(),
                context_menu.group(
                    context_menu.group_label(),
                    context_menu.item(),
                ),
                context_menu.checkbox_item(
                    context_menu.checkbox_item_indicator(),
                ),
                context_menu.radio_group(
                    context_menu.radio_item(
                        context_menu.radio_item_indicator(),
                    ),
                ),
                context_menu.submenu_root(
                    context_menu.submenu_trigger(),
                    context_menu.portal(
                        context_menu.positioner(
                            context_menu.popup(),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
```



# Examples


## Low Level Demo

Uses the low-level context_menu API for full control over state and structure.


```python
def context_menu_low_level_demo():
    return context_menu.root(
        context_menu.trigger(
            "Right click here",
            class_name="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.item(
                        rx.flex(
                            "Back",
                            rx.text(
                                "⌘[",
                                class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                            ),
                            class_name="w-full justify-between items-center",
                        ),
                        class_name="pl-8",
                    ),
                    context_menu.item(
                        rx.flex(
                            "Forward",
                            rx.text(
                                "⌘]",
                                class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                            ),
                            class_name="w-full justify-between items-center",
                        ),
                        disabled=True,
                        class_name="pl-8",
                    ),
                    context_menu.item(
                        rx.flex(
                            "Reload",
                            rx.text(
                                "⌘R",
                                class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                            ),
                            class_name="w-full justify-between items-center",
                        ),
                        class_name="pl-8",
                    ),
                    context_menu.submenu_root(
                        context_menu.submenu_trigger(
                            rx.flex(
                                "More Tools",
                                rx.icon(
                                    "chevron-right",
                                    class_name="ml-auto text-xs tracking-widest text-muted-foreground",
                                ),
                                class_name="w-full justify-between items-center",
                            ),
                            class_name="pl-8",
                        ),
                        context_menu.portal(
                            context_menu.positioner(
                                context_menu.popup(
                                    context_menu.item("Save Page..."),
                                    context_menu.item("Create Shortcut..."),
                                    context_menu.item("Name Window..."),
                                    context_menu.separator(),
                                    context_menu.item("Developer Tools"),
                                    context_menu.separator(),
                                    context_menu.item(
                                        "Delete",
                                        class_name="text-destructive focus:bg-destructive/10 dark:focus:bg-destructive/20 focus:text-destructive data-[variant=destructive]:*:[svg]:!text-destructive",
                                    ),
                                    class_name="w-44",
                                ),
                            ),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.checkbox_item(
                        context_menu.checkbox_item_indicator(
                            rx.icon(tag="check", class_name="size-4"),
                        ),
                        "Show Bookmarks",
                    ),
                    context_menu.checkbox_item(
                        context_menu.checkbox_item_indicator(
                            rx.icon(tag="check", class_name="size-4"),
                        ),
                        "Show Full URLs",
                    ),
                    context_menu.separator(),
                    context_menu.radio_group(
                        context_menu.group(
                            context_menu.group_label(
                                "People",
                                class_name="pl-8",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    rx.icon(
                                        tag="circle", class_name="size-2 fill-current"
                                    ),
                                ),
                                "Pedro Duarte",
                                value="pedro",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    rx.icon(
                                        tag="circle", class_name="size-2 fill-current"
                                    ),
                                ),
                                "Colm Tuite",
                                value="colm",
                            ),
                        ),
                        value="pedro",
                    ),
                    class_name="w-52",
                ),
            ),
        ),
    )
```

