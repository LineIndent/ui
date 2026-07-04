

# Menu

Displays a menu to the user — such as a set of actions or functions — triggered by a button.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component menu
```

### Manual Installation

```python
from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.el import Span

from ..icons.hugeicon import hi
from .base_ui import PACKAGE_NAME, BaseUIComponent
from .component import CoreComponent

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
    SHORTCUT = (
        "ml-auto text-xs tracking-widest text-muted-foreground "
        "group-focus/menu-item:text-accent-foreground"
    )


class MenuBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/menu"

    @property
    def import_var(self):

        return ImportVar(tag="Menu", package_path="", install=False)


class MenuRoot(MenuBaseComponent):
    tag = "Menu.Root"

    default_open: Var[bool]

    open: Var[bool]

    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    close_parent_on_esc: Var[bool]

    modal: Var[bool]

    disabled: Var[bool]

    open_on_hover: Var[bool]

    delay: Var[int]

    close_delay: Var[int]

    loop: Var[bool]

    orientation: Var[LiteralMenuOrientation]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu"
        return super().create(*children, **props)


class MenuTrigger(MenuBaseComponent):
    tag = "Menu.Trigger"

    native_button: Var[bool]

    disabled: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class MenuPortal(MenuBaseComponent):
    tag = "Menu.Portal"

    container: Var[str]

    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-portal"
        cls.set_class_name(ClassNames.PORTAL, props)
        return super().create(*children, **props)


class MenuPositioner(MenuBaseComponent):
    tag = "Menu.Positioner"

    collision_avoidance: Var[bool | LiteralCollisionAvoidance]

    align: Var[LiteralAlign]

    align_offset: Var[int]

    side: Var[LiteralSide]

    side_offset: Var[int]

    arrow_padding: Var[int]

    collision_padding: Var[int]

    collision_boundary: Var[str]

    sticky: Var[bool]

    track_anchor: Var[bool]

    position_method: Var[LiteralPositionMethod]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-positioner"
        props.setdefault("side_offset", 4)
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class MenuPopup(MenuBaseComponent):
    tag = "Menu.Popup"

    final_focus: Var[str]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(
            *children,
            **props,
        )


class MenuArrow(MenuBaseComponent):
    tag = "Menu.Arrow"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-arrow"
        cls.set_class_name(ClassNames.ARROW, props)
        return super().create(*children, **props)


class MenuItem(MenuBaseComponent):
    tag = "Menu.Item"

    label: Var[str]

    close_on_click: Var[bool]

    native_button: Var[bool]

    disabled: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class MenuSubMenuRoot(MenuBaseComponent):
    tag = "Menu.SubmenuRoot"

    default_open: Var[bool]

    open: Var[bool]

    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    close_parent_on_esc: Var[bool]

    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    disabled: Var[bool]

    open_on_hover: Var[bool]

    delay: Var[int]

    close_delay: Var[int]

    loop: Var[bool]

    orientation: Var[LiteralMenuOrientation]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-submenu-root"
        cls.set_class_name(ClassNames.ITEM_TEXT, props)
        return super().create(*children, **props)


class MenuSubMenuTrigger(MenuBaseComponent):
    tag = "Menu.SubmenuTrigger"

    label: Var[str]

    native_button: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-submenu-trigger"
        cls.set_class_name(ClassNames.SUBMENU_TRIGGER, props)
        return super().create(
            *children,
            hi("ArrowRight01Icon"),
            **props,
        )


class MenuGroup(MenuBaseComponent):
    tag = "Menu.Group"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-group"
        cls.set_class_name(ClassNames.GROUP, props)
        return super().create(*children, **props)


class MenuGroupLabel(MenuBaseComponent):
    tag = "Menu.GroupLabel"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-group-label"
        cls.set_class_name(ClassNames.GROUP_LABEL, props)
        return super().create(*children, **props)


class MenuShortcut(Span, CoreComponent):
    """Visual inline keystroke reminder flags for parent drop actions."""

    @classmethod
    def create(cls, *children, **props) -> Span:
        props["data-slot"] = "menu-shortcut"
        cls.set_class_name(ClassNames.SHORTCUT, props)
        return super().create(*children, **props)


class MenuRadioGroup(MenuBaseComponent):
    tag = "Menu.RadioGroup"

    default_value: Var[str | int]

    value: Var[str | int]

    on_value_change: EventHandler[passthrough_event_spec(str | int, dict)]

    disabled: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-radio-group"
        cls.set_class_name(ClassNames.RADIO_GROUP, props)
        return super().create(*children, **props)


class MenuRadioItem(MenuBaseComponent):
    tag = "Menu.RadioItem"

    label: Var[str]

    value: Var[str | int]

    close_on_click: Var[bool]

    native_button: Var[bool]

    disabled: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-radio-item"
        cls.set_class_name(ClassNames.RADIO_ITEM, props)
        return super().create(*children, **props)


class MenuRadioItemIndicator(MenuBaseComponent):
    tag = "Menu.RadioItemIndicator"

    keep_mounted: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-radio-item-indicator"
        cls.set_class_name(ClassNames.RADIO_ITEM_INDICATOR, props)
        return super().create(*children, hi("Tick02Icon"), **props)


class MenuCheckboxItem(MenuBaseComponent):
    tag = "Menu.CheckboxItem"

    label: Var[str]

    default_checked: Var[bool]

    checked: Var[bool]

    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]

    close_on_click: Var[bool]

    native_button: Var[bool]

    disabled: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-checkbox-item"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM, props)
        return super().create(*children, **props)


class MenuCheckboxItemIndicator(MenuBaseComponent):
    tag = "Menu.CheckboxItemIndicator"

    keep_mounted: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-checkbox-item-indicator"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM_INDICATOR, props)
        return super().create(*children, hi("Tick02Icon"), **props)


class MenuSeparator(MenuBaseComponent):
    tag = "Menu.Separator"

    orientation: Var[LiteralMenuOrientation]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "menu-separator"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class Menu(ComponentNamespace):
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
    shortcut = staticmethod(MenuShortcut.create)
    class_names = ClassNames


menu = Menu()
```


# Usage


```python
from components.ui.menu import Menu
```


# Anatomy 
Use the following composition to build a `Menu` component.


```python
menu.root(
    menu.trigger(),
    menu.portal(
        menu.positioner(
            menu.popup(
                menu.item(),
                menu.separator(),
                menu.group(
                    menu.group_label(),
                    menu.item(),
                ),
                menu.checkbox_item(
                    menu.checkbox_item_indicator(),
                ),
                menu.radio_group(
                    menu.radio_item(
                        menu.radio_item_indicator(),
                    ),
                ),
                menu.submenu_root(
                    menu.submenu_trigger(),
                    menu.portal(
                        menu.positioner(
                            menu.popup(),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
```


# Example

## Basic

A basic dropdown menu with labels and separators.


```python
def menu_basic():
    return menu.root(
        menu.trigger(render_=button("Open", variant="outline")),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("My Account"),
                        menu.item("Profile"),
                        menu.item("Billing"),
                        menu.item("Settings"),
                    ),
                    menu.separator(),
                    menu.group(
                        menu.item("Team"),
                        menu.submenu_root(
                            menu.submenu_trigger("Invite users"),
                            menu.portal(
                                menu.positioner(
                                    menu.popup(
                                        menu.item("Email"),
                                        menu.item("Message"),
                                        menu.separator(),
                                        menu.item("More..."),
                                    ),
                                    side="right",
                                    align="start",
                                    align_offset=-3,
                                    side_offset=0,
                                ),
                            ),
                        ),
                        menu.item("New Team"),
                    ),
                    menu.separator(),
                    menu.group(
                        menu.item("GitHub"),
                        menu.item("Support"),
                        menu.item("API", disabled=True),
                    ),
                    menu.separator(),
                    menu.group(menu.item("Log out")),
                    class_name="w-40",
                ),
                align="start",
            ),
        ),
    )
```


## Submenu

Use `menu.submenu_root` to nest secondary actions.


```python
def menu_submenu():
    return menu.root(
        menu.trigger(render_=button("Open", variant="outline")),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.item("Team"),
                        menu.submenu_root(
                            menu.submenu_trigger("Invite users"),
                            menu.portal(
                                menu.positioner(
                                    menu.popup(
                                        menu.item("Email"),
                                        menu.item("Message"),
                                        menu.submenu_root(
                                            menu.submenu_trigger("More options"),
                                            menu.portal(
                                                menu.positioner(
                                                    menu.popup(
                                                        menu.item("Calendly"),
                                                        menu.item("Slack"),
                                                        menu.separator(),
                                                        menu.item("Webhook"),
                                                    ),
                                                    side="right",
                                                    align="start",
                                                ),
                                            ),
                                        ),
                                        menu.separator(),
                                        menu.item("Advanced..."),
                                    ),
                                    side="right",
                                    align="start",
                                ),
                            ),
                        ),
                        menu.item("New Team"),
                    ),
                ),
                align="start",
            ),
        ),
    )
```


## Shortcuts

Add `menu.shortcut` to show keyboard hints.


```python
def menu_shortcuts() -> rx.Component:
    return menu.root(
        menu.trigger(
            render_=button("Open", variant="outline"),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("My Account"),
                        menu.item("Profile", menu.shortcut("⇧⌘P")),
                        menu.item("Billing", menu.shortcut("⌘B")),
                        menu.item("Settings", menu.shortcut("⌘S")),
                    ),
                    menu.separator(),
                    menu.item("Log out", menu.shortcut("⇧⌘Q")),
                ),
            ),
        ),
    )
```


## Icons

Combine icons with labels for quick scanning.


```python
def menu_icons() -> rx.Component:
    return menu.root(
        menu.trigger(
            render_=button("Open", variant="outline"),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.item(hi("UserIcon"), "Profile"),
                    menu.item(hi("CreditCardIcon"), "Billing"),
                    menu.item(hi("Setting07Icon"), "Settings"),
                    menu.separator(),
                    menu.item(
                        hi("LogoutSquare01Icon"), "Log out", variant="destructive"
                    ),
                ),
            ),
        ),
    )
```


## Checkboxes

Use `menu.checkbox_item` for toggles. 


```python
def menu_checkboxes():
    return menu.root(
        menu.trigger(render_=button("Open", variant="outline")),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("Appearance"),
                        menu.checkbox_item(
                            "Status Bar",
                            menu.checkbox_item_indicator(),
                            default_checked=show_status_bar.value,
                            on_checked_change=show_status_bar.set_value(
                                ~show_status_bar.value
                            ),
                        ),
                        menu.checkbox_item(
                            "Activity Bar",
                            disabled=True,
                        ),
                        menu.checkbox_item(
                            "Panel",
                            menu.checkbox_item_indicator(),
                            default_checked=show_panel.value,
                            on_checked_change=show_panel.set_value,
                        ),
                    ),
                    class_name="w-40",
                ),
            ),
        ),
    )
```


## Checkboxes Icons

Add icons to checkbox items.


```python
def menu_checkboxes_icons() -> rx.Component:
    return menu.root(
        email_notif,
        sms_notif,
        push_notif,
        menu.trigger(
            render_=button("Notifications", variant="outline"),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("Notification Preferences"),
                        menu.checkbox_item(
                            hi("Mail01Icon"),
                            "Email notifications",
                            menu.checkbox_item_indicator(),
                            default_checked=email_notif.value,
                            on_checked_change=email_notif.set_value,
                        ),
                        menu.checkbox_item(
                            hi("Message01Icon"),
                            "SMS notifications",
                            menu.checkbox_item_indicator(),
                            default_checked=sms_notif.value,
                            on_checked_change=sms_notif.set_value,
                        ),
                        menu.checkbox_item(
                            hi("Notification01Icon"),
                            "Push notifications",
                            menu.checkbox_item_indicator(),
                            default_checked=push_notif.value,
                            on_checked_change=push_notif.set_value,
                        ),
                    ),
                    class_name="w-48",
                ),
            ),
        ),
    )
```


## Radio Group

Use `menu.radio_group` for exclusive choices.


```python
def menu_radio_group() -> rx.Component:
    return menu.root(
        panel_position,
        menu.trigger(
            render_=button("Open", variant="outline"),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.group_label("Panel Position"),
                        menu.radio_group(
                            menu.radio_item(
                                "Top",
                                menu.radio_item_indicator(),
                                value="top",
                            ),
                            menu.radio_item(
                                "Bottom",
                                menu.radio_item_indicator(),
                                value="bottom",
                            ),
                            menu.radio_item(
                                "Right",
                                menu.radio_item_indicator(),
                                value="right",
                            ),
                            value=panel_position.value,
                            on_value_change=panel_position.set_value,
                        ),
                    ),
                    class_name="w-32",
                ),
            ),
        ),
    )
```


## Avatar 

An account switcher dropdown triggered by an avatar.


```python
def menu_avatar() -> rx.Component:
    return menu.root(
        menu.trigger(
            render_=button(
                avatar.root(
                    avatar.image(src="https://github.com/shadcn.png", alt="shadcn"),
                    avatar.fallback("LR"),
                ),
                variant="ghost",
                size="icon",
                class_name="rounded-full",
            ),
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.item(hi("UserIcon"), "Account"),
                        menu.item(hi("CreditCardIcon"), "Billing"),
                        menu.item(hi("Notification01Icon"), "Notifications"),
                    ),
                    menu.separator(),
                    menu.item(
                        hi("LogoutSquare01Icon"),
                        "Sign Out",
                    ),
                ),
                align="end",
            ),
        ),
    )
```

