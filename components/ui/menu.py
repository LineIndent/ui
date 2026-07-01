from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..icons.hugeicon import hi
from .base_ui import PACKAGE_NAME, BaseUIComponent

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
    TRIGGER = ""
    PORTAL = ""
    POSITIONER = "isolate z-50 outline-none"
    POPUP = (
        "z-50 max-h-[var(--available-height)] w-[var(--anchor-width)] min-w-32 "
        "origin-[var(--transform-origin)] overflow-x-hidden overflow-y-auto "
        "rounded-lg bg-popover p-1 text-popover-foreground shadow-md "
        "ring-1 ring-foreground/10 duration-100 outline-none "
        "data-[side=bottom]:slide-in-from-top-2 "
        "data-[side=left]:slide-in-from-right-2 "
        "data-[side=right]:slide-in-from-left-2 "
        "data-[side=top]:slide-in-from-bottom-2 "
        "data-[open]:animate-in data-[open]:fade-in-0 data-[open]:zoom-in-95 "
        "data-[closed]:animate-out data-[closed]:fade-out-0 data-[closed]:zoom-out-95"
    )
    ITEM = (
        "group/menu-item relative flex cursor-default items-center gap-1.5 "
        "rounded-lg px-1.5 py-1 text-sm outline-hidden select-none "
        "focus:bg-accent focus:text-accent-foreground "
        "not-data-[variant=destructive]:focus:**:text-accent-foreground "
        "data-inset:pl-7 "
        "data-[variant=destructive]:text-destructive "
        "data-[variant=destructive]:focus:bg-destructive/10 "
        "data-[variant=destructive]:focus:text-destructive "
        "dark:data-[variant=destructive]:focus:bg-destructive/20 "
        "data-disabled:pointer-events-none data-disabled:opacity-50 "
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 "
        "[&_svg:not([class*='size-'])]:size-4"
    )
    SEPARATOR = "-mx-1 my-1 h-px bg-border"
    POSITIONER_SUB = "isolate z-50 outline-none"
    POPUP_SUB = (
        "z-50 w-auto min-w-24 origin-(--transform-origin) overflow-x-hidden "
        "overflow-y-auto rounded-lg bg-popover p-1 text-popover-foreground "
        "shadow-lg ring-1 ring-foreground/10 duration-100 "
        "data-[side=bottom]:slide-in-from-top-2 "
        "data-[side=left]:slide-in-from-right-2 "
        "data-[side=right]:slide-in-from-left-2 "
        "data-[side=top]:slide-in-from-bottom-2 "
        "data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 "
        "data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95"
    )
    GROUP_LABEL = (
        "px-1.5 py-1 text-xs font-medium text-muted-foreground data-inset:pl-7"
    )
    SUBMENU_TRIGGER = (
        "flex cursor-default items-center justify-between gap-1.5 rounded-lg px-1.5 py-1 "
        "text-sm outline-hidden select-none "
        "focus:bg-accent focus:text-accent-foreground "
        "not-data-[variant=destructive]:focus:**:text-accent-foreground "
        "data-inset:pl-7 "
        "data-popup-open:bg-accent data-popup-open:text-accent-foreground "
        "data-open:bg-accent data-open:text-accent-foreground "
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 "
        "[&_svg:not([class*='size-'])]:size-4"
    )

    RADIO_ITEM = (
        "relative flex cursor-default items-center gap-2 rounded-sm "
        "py-1 pr-8 pl-1.5 text-sm outline-hidden select-none "
        "data-disabled:pointer-events-none data-disabled:opacity-50 "
        "focus:bg-accent focus:text-accent-foreground "
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 "
        "[&_svg:not([class*='size-'])]:size-4"
    )
    RADIO_ITEM_INDICATOR = (
        "pointer-events-none absolute right-2 flex items-center justify-center"
    )
    CHECKBOX_ITEM = (
        "relative flex cursor-default items-center gap-1.5 rounded-md "
        "py-1 pr-8 pl-1.5 text-sm outline-hidden select-none "
        "data-disabled:pointer-events-none data-disabled:opacity-50 "
        "focus:bg-accent focus:text-accent-foreground "
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 "
        "[&_svg:not([class*='size-'])]:size-4"
    )
    CHECKBOX_ITEM_INDICATOR = (
        "pointer-events-none absolute right-2 flex items-center justify-center"
    )
    ARROW = (
        "data-[side=bottom]:top-[-8px] data-[side=left]:right-[-13px] "
        "data-[side=left]:rotate-90 data-[side=right]:left-[-13px] "
        "data-[side=right]:-rotate-90 data-[side=top]:bottom-[-8px] "
        "data-[side=top]:rotate-180"
    )
    GROUP = ""
    RADIO_GROUP = ""
    ITEM_TEXT = "text-start"
    ITEM_INDICATOR = "text-current"


class MenuBaseComponent(BaseUIComponent):
    """Base component for menu components."""

    library = f"{PACKAGE_NAME}/menu"

    @property
    def import_var(self):
        """Return the import variable for the menu component."""
        return ImportVar(tag="Menu", package_path="", install=False)


class MenuRoot(MenuBaseComponent):
    """Groups all parts of the menu. Doesn't render its own HTML element."""

    tag = "Menu.Root"

    # Whether the menu is initially open. To render a controlled menu, use the open prop instead. Defaults to False.
    default_open: Var[bool]

    # Whether the menu is currently open.
    open: Var[bool]

    # Event handler called when the menu is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Event handler called after any animations complete when the menu is closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    # When in a submenu, determines whether pressing the Escape key closes the entire menu, or only the current child menu. Defaults to True.
    close_parent_on_esc: Var[bool]

    # Determines if the menu enters a modal state when open. Defaults to True.
    # - True: user interaction is limited to the menu: document page scroll is locked and and pointer interactions on outside elements are disabled.
    # - False: user interaction with the rest of the document is allowed.
    modal: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the menu should also open when the trigger is hovered.
    open_on_hover: Var[bool]

    # How long to wait before the menu may be opened on hover. Specified in milliseconds. Requires the open_on_hover prop. Defaults to 100.
    delay: Var[int]

    # How long to wait before closing the menu that was opened on hover. Specified in milliseconds. Requires the open_on_hover prop. Defaults to 0.
    close_delay: Var[int]

    # Whether to loop keyboard focus back to the first item when the end of the list is reached while using the arrow keys. Defaults to True.
    loop: Var[bool]

    # The visual orientation of the menu. Controls whether roving focus uses up/down or left/right arrow keys. Defaults to 'vertical'.
    orientation: Var[LiteralMenuOrientation]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu root component."""
        props["data-slot"] = "menu"
        return super().create(*children, **props)


class MenuTrigger(MenuBaseComponent):
    """A button that opens the menu. Renders a <button> element."""

    tag = "Menu.Trigger"

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu trigger component."""
        props["data-slot"] = "menu-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class MenuPortal(MenuBaseComponent):
    """A portal element that moves the popup to a different part of the DOM. By default, the portal element is appended to <body>."""

    tag = "Menu.Portal"

    # A parent element to render the portal element into.
    container: Var[str]

    # Whether to keep the portal mounted in the DOM while the popup is hidden. Defaults to False.
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu portal component."""
        props["data-slot"] = "menu-portal"
        cls.set_class_name(ClassNames.PORTAL, props)
        return super().create(*children, **props)


class MenuPositioner(MenuBaseComponent):
    """Positions the menu popup against the trigger. Renders a <div> element."""

    tag = "Menu.Positioner"

    # Determines how to handle collisions when positioning the popup.
    collision_avoidance: Var[bool | LiteralCollisionAvoidance]

    # How to align the popup relative to the specified side. Defaults to "center".
    align: Var[LiteralAlign]

    # Additional offset along the alignment axis in pixels. Defaults to 0.
    align_offset: Var[int]

    # Which side of the anchor element to align the popup against. May automatically change to avoid collisions. Defaults to "bottom".
    side: Var[LiteralSide]

    # Distance between the anchor and the popup in pixels. Defaults to 0.
    side_offset: Var[int]

    # Minimum distance to maintain between the arrow and the edges of the popup. Use it to prevent the arrow element from hanging out of the rounded corners of a popup. Defaults to 5.
    arrow_padding: Var[int]

    # Additional space to maintain from the edge of the collision boundary. Defaults to 5.
    collision_padding: Var[int]

    # An element or a rectangle that delimits the area that the popup is confined to. Defaults to the "clipping-ancestors".
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
        """Create the menu positioner component."""
        props["data-slot"] = "menu-positioner"
        props.setdefault("side_offset", 4)
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class MenuPopup(MenuBaseComponent):
    """A container for the menu items. Renders a <div> element."""

    tag = "Menu.Popup"

    # Determines the element to focus when the menu is closed. By default, focus returns to the trigger.
    final_focus: Var[str]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu popup component."""
        props["data-slot"] = "menu-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(
            *children,
            **props,
        )


class MenuArrow(MenuBaseComponent):
    """Displays an element positioned against the menu anchor. Renders a <div> element."""

    tag = "Menu.Arrow"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu arrow component."""
        props["data-slot"] = "menu-arrow"
        cls.set_class_name(ClassNames.ARROW, props)
        return super().create(*children, **props)


class MenuItem(MenuBaseComponent):
    """An individual interactive item in the menu. Renders a <div> element."""

    tag = "Menu.Item"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]

    # Whether to close the menu when the item is clicked. Defaults to True.
    close_on_click: Var[bool]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to False.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu item component."""
        props["data-slot"] = "menu-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class MenuSubMenuRoot(MenuBaseComponent):
    """Groups all parts of a submenu. Doesn't render its own HTML element."""

    tag = "Menu.SubmenuRoot"

    # Whether the menu is initially open. To render a controlled menu, use the open prop instead. Defaults to False.
    default_open: Var[bool]

    # Whether the menu is currently open.
    open: Var[bool]

    # Event handler called when the menu is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    # When in a submenu, determines whether pressing the Escape key closes the entire menu, or only the current child menu. Defaults to True.
    close_parent_on_esc: Var[bool]

    # Event handler called after any animations complete when the menu is closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the menu should also open when the trigger is hovered. Defaults to True.
    open_on_hover: Var[bool]

    # How long to wait before the menu may be opened on hover. Specified in milliseconds. Requires the open_on_hover prop. Defaults to 100.
    delay: Var[int]

    # How long to wait before closing the menu that was opened on hover. Specified in milliseconds. Requires the open_on_hover prop. Defaults to 0.
    close_delay: Var[int]

    # Whether to loop keyboard focus back to the first item when the end of the list is reached while using the arrow keys. Defaults to True.
    loop: Var[bool]

    # The visual orientation of the menu. Controls whether roving focus uses up/down or left/right arrow keys. Defaults to 'vertical'.
    orientation: Var[LiteralMenuOrientation]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu submenu root component."""
        props["data-slot"] = "menu-submenu-root"
        cls.set_class_name(ClassNames.ITEM_TEXT, props)
        return super().create(*children, **props)


class MenuSubMenuTrigger(MenuBaseComponent):
    """A menu item that opens a submenu."""

    tag = "Menu.SubmenuTrigger"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to False.
    native_button: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu submenu trigger component."""
        props["data-slot"] = "menu-submenu-trigger"
        cls.set_class_name(ClassNames.SUBMENU_TRIGGER, props)

        # Automatically add the chevron if it's a submenu trigger
        # We append it to the children tuple
        return super().create(
            *children,
            hi("ArrowRight01Icon"),
            **props,
        )


class MenuGroup(MenuBaseComponent):
    """Groups related menu items with the corresponding label. Renders a <div> element."""

    tag = "Menu.Group"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu group component."""
        props["data-slot"] = "menu-group"
        cls.set_class_name(ClassNames.GROUP, props)
        return super().create(*children, **props)


class MenuGroupLabel(MenuBaseComponent):
    """An accessible label that is automatically associated with its parent group. Renders a <div> element."""

    tag = "Menu.GroupLabel"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu group label component."""
        props["data-slot"] = "menu-group-label"
        cls.set_class_name(ClassNames.GROUP_LABEL, props)
        return super().create(*children, **props)


class MenuRadioGroup(MenuBaseComponent):
    """Groups related radio items. Renders a <div> element."""

    tag = "Menu.RadioGroup"

    # The uncontrolled value of the radio item that should be initially selected. To render a controlled radio group, use the value prop instead.
    default_value: Var[str | int]

    # The controlled value of the radio item that should be currently selected. To render an uncontrolled radio group, use the defaultValue prop instead.
    value: Var[str | int]

    # Function called when the selected value changes.
    on_value_change: EventHandler[passthrough_event_spec(str | int, dict)]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu radio group component."""
        props["data-slot"] = "menu-radio-group"
        cls.set_class_name(ClassNames.RADIO_GROUP, props)
        return super().create(*children, **props)


class MenuRadioItem(MenuBaseComponent):
    """A menu item that works like a radio button in a given group. Renders a <div> element."""

    tag = "Menu.RadioItem"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]

    # Value of the radio item. This is the value that will be set in the MenuRadioGroup when the item is selected.
    value: Var[str | int]

    # Whether to close the menu when the item is clicked. Defaults to False.
    close_on_click: Var[bool]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to False.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu radio item component."""
        props["data-slot"] = "menu-radio-item"
        cls.set_class_name(ClassNames.RADIO_ITEM, props)
        return super().create(*children, **props)


class MenuRadioItemIndicator(MenuBaseComponent):
    """Indicates whether the radio item is selected. Renders a <div> element."""

    tag = "Menu.RadioItemIndicator"

    # Whether to keep the HTML element in the DOM when the radio item is inactive. Defaults to False.
    keep_mounted: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu radio item indicator component."""
        props["data-slot"] = "menu-radio-item-indicator"
        cls.set_class_name(ClassNames.RADIO_ITEM_INDICATOR, props)
        return super().create(*children, **props)


class MenuCheckboxItem(MenuBaseComponent):
    """A menu item that toggles a setting on or off. Renders a <div> element."""

    tag = "Menu.CheckboxItem"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]

    # Whether the checkbox item is initially ticked. To render a controlled checkbox item, use the checked prop instead. Defaults to False.
    default_checked: Var[bool]

    # Whether the checkbox item is ticked. To render an uncontrolled checkbox item, use the default_checked prop instead.
    checked: Var[bool]

    # Event handler called when the checkbox item is ticked or unticked.
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Whether to close the menu when the item is clicked. Defaults to False.
    close_on_click: Var[bool]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to False.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu checkbox item component."""
        props["data-slot"] = "menu-checkbox-item"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM, props)
        return super().create(*children, **props)


class MenuCheckboxItemIndicator(MenuBaseComponent):
    """Indicates whether the checkbox item is ticked. Renders a <div> element."""

    tag = "Menu.CheckboxItemIndicator"

    # Whether to keep the HTML element in the DOM when the checkbox item is not checked. Defaults to False.
    keep_mounted: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu checkbox item indicator component."""
        props["data-slot"] = "menu-checkbox-item-indicator"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM_INDICATOR, props)
        return super().create(*children, hi("Tick02Icon"), **props)


class MenuSeparator(MenuBaseComponent):
    """A separator element accessible to screen readers. Renders a <div> element."""

    tag = "Menu.Separator"

    # The orientation of the separator. Defaults to 'horizontal'.
    orientation: Var[LiteralMenuOrientation]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the menu separator component."""
        props["data-slot"] = "menu-separator"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class Menu(ComponentNamespace):
    """Namespace for Menu components."""

    root = staticmethod(MenuRoot.create)
    trigger = staticmethod(MenuTrigger.create)
    portal = staticmethod(MenuPortal.create)
    positioner = staticmethod(MenuPositioner.create)
    popup = staticmethod(MenuPopup.create)
    arrow = staticmethod(MenuArrow.create)
    item = staticmethod(MenuItem.create)
    separator = staticmethod(MenuSeparator.create)
    group = staticmethod(MenuGroup.create)
    group_label = staticmethod(MenuGroupLabel.create)
    radio_group = staticmethod(MenuRadioGroup.create)
    radio_item = staticmethod(MenuRadioItem.create)
    radio_item_indicator = staticmethod(MenuRadioItemIndicator.create)
    checkbox_item = staticmethod(MenuCheckboxItem.create)
    checkbox_item_indicator = staticmethod(MenuCheckboxItemIndicator.create)
    submenu_root = staticmethod(MenuSubMenuRoot.create)
    submenu_trigger = staticmethod(MenuSubMenuTrigger.create)
    class_names = ClassNames


menu = Menu()
