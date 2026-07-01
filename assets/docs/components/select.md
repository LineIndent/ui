

# Select
Displays a list of options for the user to pick from—triggered by a button.

# Installation
Copy the following code into your app directory.

### CLI

```bash
buridan add component select
```

### Manual Installation

```python
"""Custom select component."""

from typing import Any, Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.core.foreach import foreach as foreach

from ..icons.hugeicon import hi
from ..icons.others import select_arrow
from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent
from .button import button

LiteralSelectSize = Literal["xs", "sm", "md", "lg", "xl"]
LiteralAlign = Literal["start", "center", "end"]
LiteralSide = Literal["bottom", "inline-end", "inline-start", "left", "right", "top"]
LiteralPosition = Literal["absolute", "fixed"]
LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    """Class names for select components."""

    TRIGGER = "flex w-fit items-center justify-between gap-1.5 rounded-lg border border-input bg-transparent py-2 pr-2 pl-2.5 text-sm whitespace-nowrap transition-colors outline-none select-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 data-placeholder:text-muted-foreground data-[size=default]:h-8 data-[size=sm]:h-7 data-[size=sm]:rounded-[min(var(--radius-md),10px)] *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-1.5 dark:bg-input/30 dark:hover:bg-input/50 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    VALUE = "flex-1 text-left cursor-default"
    ICON = "flex size-4 text-secondary-10 group-data-[disabled]/trigger:text-current"
    POPUP = "relative isolate z-50 max-h-(--available-height) w-(--anchor-width) min-w-36 origin-(--transform-origin) overflow-x-hidden overflow-y-auto rounded-lg bg-popover text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-[align-trigger=true]:animate-none data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95"
    ITEM = "focus:bg-accent focus:text-accent-foreground [&_svg:not([class*='text-'])]:text-muted-foreground relative flex w-full cursor-default items-center gap-2 rounded-sm py-1.5 px-2 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 *:[span]:last:flex *:[span]:last:items-center *:[span]:last:gap-2"
    ITEM_INDICATOR = ""
    ITEM_TEXT = "text-start"
    GROUP = "p-1"
    GROUP_LABEL = "text-muted-foreground px-2 py-1.5 text-xs"
    SEPARATOR = "bg-border pointer-events-none -mx-1 my-1 h-px"
    ARROW = "data-[side=bottom]:top-[-8px] data-[side=left]:right-[-13px] data-[side=left]:rotate-90 data-[side=right]:left-[-13px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-8px] data-[side=top]:rotate-180"
    POSITIONER = "outline-none"
    SCROLL_ARROW_UP = "top-0 z-10 flex w-full cursor-default items-center justify-center bg-popover py-1"
    SCROLL_ARROW_DOWN = "bottom-0 z-10 flex w-full cursor-default items-center justify-center bg-popover py-1"


class SelectBaseComponent(BaseUIComponent):
    """Base component for select components."""

    library = f"{PACKAGE_NAME}/select"

    @property
    def import_var(self):
        """Return the import variable for the select component."""
        return ImportVar(tag="Select", package_path="", install=False)


class SelectRoot(SelectBaseComponent):
    """Groups all parts of the select. Doesn't render its own HTML element."""

    tag = "Select.Root"

    # Identifies the field when a form is submitted.
    name: Var[str]

    # The uncontrolled value of the select when it's initially rendered.
    # To render a controlled select, use the `value` prop instead.
    default_value: Var[Any]

    # The value of the select
    value: Var[Any]

    # Callback fired when the value of the select changes. Use when controlled.
    on_value_change: EventHandler[passthrough_event_spec(str)]

    # Whether the select popup is initially open.
    # To render a controlled select popup, use the `open` prop instead.
    default_open: Var[bool]

    # Whether the select popup is currently open
    open: Var[bool]

    # Event handler called when the select popup is opened or closed
    on_open_change: EventHandler[passthrough_event_spec(bool)]

    # A ref to imperative actions.
    # When specified, the select will not be unmounted when closed.
    # Instead, the `unmount` function must be called to unmount the select manually.
    # Useful when the select's animation is controlled by an external library.
    actions_ref: Var[str]

    # Custom comparison logic used to determine if a select item value matches the current selected value.
    # Useful when item values are objects without matching referentially.
    # Defaults to `Object.is` comparison.
    is_item_equal_to_value: Var[Any]

    # When the item values are objects, this function converts the object value to a string representation for display in the trigger.
    # If the shape of the object is `{ value, label }`, the label will be used automatically without needing to specify this prop.
    item_to_string_label: Var[Any]

    # When the item values are objects, this function converts the object value to a string representation for form submission.
    # If the shape of the object is `{ value, label }`, the value will be used automatically without needing to specify this prop.
    item_to_string_value: Var[Any]

    # Data structure of the items rendered in the select popup.
    # When specified, `<Select.Value>` renders the label of the selected item instead of the raw value.
    items: Var[Any]

    # Determines if the select enters a modal state when open.
    # - True: user interaction is limited to the select: document page scroll is locked and pointer interactions on outside elements are disabled.
    # - False: user interaction with the rest of the document is allowed. Defaults to True.
    modal: Var[bool]

    # Whether multiple items can be selected. Defaults to False.
    multiple: Var[bool]

    # Event handler called after any animations complete when the select popup is opened or closed
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the user should be unable to choose a different option from the select popup. Defaults to False.
    read_only: Var[bool]

    # Whether the user must choose a value before submitting a form. Defaults to False.
    required: Var[bool]

    # A ref to access the hidden input element.
    input_ref: Var[Any]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the select root component."""
        props["data-slot"] = "select"
        return super().create(*children, **props)


class SelectTrigger(SelectBaseComponent):
    """A button that opens the select menu."""

    tag = "Select.Trigger"

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the select trigger component."""
        props["data-slot"] = "select-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class SelectValue(SelectBaseComponent):
    """Text label of the currently selected item."""

    tag = "Select.Value"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-value"
        cls.set_class_name(ClassNames.VALUE, props)
        return super().create(*children, **props)


class SelectBackdrop(SelectBaseComponent):
    """An overlay displayed beneath the menu popup."""

    tag = "Select.Backdrop"

    # The render prop
    render_: Var[Component]


class SelectPortal(SelectBaseComponent):
    """A portal element that moves the popup to a different part of the DOM.
    By default, the portal element is appended to <body>.
    """

    tag = "Select.Portal"

    # A parent element to render the portal element into.
    container: Var[str]


class SelectPositioner(SelectBaseComponent):
    """Positions the select menu popup."""

    tag = "Select.Positioner"

    # How to align the popup relative to the specified side. Defaults to "center".
    align: Var[LiteralAlign]

    # Additional offset along the alignment axis in pixels. Defaults to 0.
    align_offset: Var[int]

    # Which side of the anchor element to align the popup against. May automatically change to avoid collisions. Defaults to "bottom".
    side: Var[LiteralSide]

    # Minimum distance to maintain between the arrow and the edges of the popup.
    # Use it to prevent the arrow element from hanging out of the rounded corners of a popup. Defaults to 5.
    arrow_padding: Var[int]

    # Additional space to maintain from the edge of the collision boundary. Defaults to 5.
    collision_padding: Var[int | list[int]]

    # Whether to maintain the popup in the viewport after the anchor element was scrolled out of view. Defaults to False.
    sticky: Var[bool]

    # Determines which CSS position property to use. Defaults to "absolute".
    position_method: Var[LiteralPosition]

    # Whether the positioner overlaps the trigger so the selected item's text is aligned with the trigger's value text. This only applies to mouse input and is automatically disabled if there is not enough space. Defaults to False.
    align_item_with_trigger: Var[bool] = Var.create(False)

    # Whether the popup tracks any layout shift of its positioning anchor. Defaults to True.
    track_anchor: Var[bool]

    # Distance between the anchor and the popup in pixels. Defaults to 0.
    side_offset: Var[int]

    # Determines how to handle collisions when positioning the popup.
    collision_avoidance: Var[str]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-positioner"
        props.setdefault("side_offset", 4)
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class SelectPopup(SelectBaseComponent):
    """A container for the select items."""

    tag = "Select.Popup"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class SelectList(SelectBaseComponent):
    """A list component that wraps select items. Renders a <div> element."""

    tag = "Select.List"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the select list component.

        Returns:
            The component.
        """
        props["data-slot"] = "select-list"
        return super().create(*children, **props)


class SelectItem(SelectBaseComponent):
    """An individual option in the select menu."""

    tag = "Select.Item"

    # Overrides the text label to use on the trigger when this item is selected and when the item is matched during keyboard text navigation.
    label: Var[str]

    # A unique value that identifies this select item.
    value: Var[Any]

    # Whether the component should ignore user interaction.
    disabled: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class SelectItemText(SelectBaseComponent):
    """A text label of the select item."""

    tag = "Select.ItemText"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-item-text"
        cls.set_class_name(ClassNames.ITEM_TEXT, props)
        return super().create(*children, **props)


class SelectItemIndicator(SelectBaseComponent):
    tag = "Select.ItemIndicator"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "select-item-indicator"
        cls.set_class_name(ClassNames.ITEM_INDICATOR, props)

        if not children:
            children = (hi("Tick02Icon", class_name="size-4 text-secondary-10"),)

        return super().create(*children, **props)


class SelectGroup(SelectBaseComponent):
    """Groups related select items with the corresponding label."""

    tag = "Select.Group"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-group"
        cls.set_class_name(ClassNames.GROUP, props)
        return super().create(*children, **props)


class SelectGroupLabel(SelectBaseComponent):
    """An accessible label that is automatically associated with its parent group."""

    tag = "Select.GroupLabel"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-group-label"
        cls.set_class_name(ClassNames.GROUP_LABEL, props)
        return super().create(*children, **props)


class SelectSeparator(SelectBaseComponent):
    """A separator element accessible to screen readers."""

    tag = "Select.Separator"

    # The orientation of the separator.
    orientation: Var[LiteralOrientation] = Var.create("horizontal")

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-separator"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class SelectIcon(SelectBaseComponent):
    tag = "Select.Icon"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "select-icon"
        cls.set_class_name(ClassNames.ICON, props)

        if not children:
            children = (hi("ArrowDown01Icon", class_name="size-4"),)

        return super().create(*children, **props)


class SelectArrow(SelectBaseComponent):
    """Displays an element positioned against the select menu anchor."""

    tag = "Select.Arrow"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-arrow"
        cls.set_class_name(ClassNames.ARROW, props)
        return super().create(*children, **props)


class SelectScrollUpArrow(SelectBaseComponent):
    """An element that scrolls the select menu up when hovered."""

    tag = "Select.ScrollUpArrow"

    keep_mounted: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-scroll-up-arrow"
        cls.set_class_name(ClassNames.SCROLL_ARROW_UP, props)

        if "render_" not in props or props["render_"] is None:
            props["render_"] = hi("ArrowUp01Icon", class_name="size-6")

        return super().create(*children, **props)


class SelectScrollDownArrow(SelectBaseComponent):
    """An element that scrolls the select menu down when hovered."""

    tag = "Select.ScrollDownArrow"

    keep_mounted: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "select-scroll-down-arrow"
        cls.set_class_name(ClassNames.SCROLL_ARROW_DOWN, props)

        if "render_" not in props or props["render_"] is None:
            props["render_"] = hi("ArrowDown01Icon", class_name="size-6")

        return super().create(*children, **props)


class HighLevelSelect(SelectRoot):
    """High level wrapper for the Select component."""

    # The list of items to display in the select dropdown
    items: Var[list[str]]

    # The placeholder text to display when no item is selected
    placeholder: Var[str]

    # The size of the select component. Defaults to "md".
    size: Var[LiteralSelectSize]

    # Props for different component parts
    _trigger_props = {"placeholder", "size"}
    _items_props = {"items"}
    _positioner_props = {
        "align",
        "align_offset",
        "side",
        "arrow_padding",
        "collision_padding",
        "sticky",
        "position_method",
        "align_item_with_trigger",
        "track_anchor",
        "side_offset",
        "collision_avoidance",
    }
    _portal_props = {"container"}

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create a select component.

        Args:
            *children: Additional children to include in the select.
            **props: Additional properties to apply to the select component.

        Returns:
            The select component.
        """
        # Extract props for different parts
        trigger_props = {k: props.pop(k) for k in cls._trigger_props & props.keys()}
        items_props = {k: props.pop(k) for k in cls._items_props & props.keys()}
        positioner_props = {
            k: props.pop(k) for k in cls._positioner_props & props.keys()
        }
        portal_props = {k: props.pop(k) for k in cls._portal_props & props.keys()}

        # Get extracted values with defaults
        size = trigger_props.get("size", "sm")
        items = items_props.get("items", [])

        # Create the items children
        if isinstance(items, Var):
            items_children = foreach(
                items,
                lambda item: SelectItem.create(
                    render_=button(
                        SelectItemText.create(item),
                        SelectItemIndicator.create(
                            hi(
                                "Tick02Icon",
                                class_name="size-4",
                            ),
                        ),
                        variant="ghost",
                        size=size,
                        type="button",
                        class_name=ClassNames.ITEM,
                        disabled=props.get("disabled", False),
                    ),
                    value=item,
                    key=item,
                ),
            )
        else:
            items_children = [
                SelectItem.create(
                    render_=button(
                        SelectItemText.create(item),
                        SelectItemIndicator.create(
                            hi(
                                "Tick02Icon",
                                class_name="size-4",
                            ),
                        ),
                        variant="ghost",
                        size=size,
                        type="button",
                        class_name=ClassNames.ITEM,
                    ),
                    value=item,
                    key=item,
                )
                for item in items
            ]

        return SelectRoot.create(
            SelectTrigger.create(
                render_=button(
                    SelectValue.create(),
                    SelectIcon.create(
                        select_arrow(class_name="size-4 text-secondary-9")
                    ),
                    variant="outline",
                    size=size,
                    type="button",
                    class_name=ClassNames.TRIGGER,
                    disabled=props.get("disabled", False),
                ),
            ),
            SelectPortal.create(
                SelectPositioner.create(
                    SelectPopup.create(
                        items_children,
                        class_name=cn(
                            ClassNames.POPUP,
                            "",
                            "rounded-lg",
                        ),
                    ),
                    **positioner_props,
                ),
                **portal_props,
            ),
            *children,
            **props,
        )


class Select(ComponentNamespace):
    """Namespace for Select components."""

    root = staticmethod(SelectRoot.create)
    trigger = staticmethod(SelectTrigger.create)
    value = staticmethod(SelectValue.create)
    icon = staticmethod(SelectIcon.create)
    backdrop = staticmethod(SelectBackdrop.create)
    portal = staticmethod(SelectPortal.create)
    positioner = staticmethod(SelectPositioner.create)
    popup = staticmethod(SelectPopup.create)
    arrow = staticmethod(SelectArrow.create)
    scroll_up_arrow = staticmethod(SelectScrollUpArrow.create)
    scroll_down_arrow = staticmethod(SelectScrollDownArrow.create)
    list = staticmethod(SelectList.create)
    item = staticmethod(SelectItem.create)
    item_text = staticmethod(SelectItemText.create)
    item_indicator = staticmethod(SelectItemIndicator.create)
    group = staticmethod(SelectGroup.create)
    group_label = staticmethod(SelectGroupLabel.create)
    separator = staticmethod(SelectSeparator.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelSelect.create)


select = Select()
```


# Usage

```python
from components.ui.select import select
```


# Anatomy 
Use the following composition to build a `Select` component.

```python
select.root(
    select.trigger(
        select.value(),
        select.icon(),
    ),
    select.portal(
        select.positioner(
            select.popup(
                select.group(
                    select.group_label(),
                    select.item(
                        select.item_text(),
                        select.item_indicator(),
                    ),
                ),
                select.separator(),
            ),
        ),
    ),
)
```


# Examples

## Align Item
Use `align_item_with_trigger` on `select.positioner()` to control whether the selected item aligns with the trigger. When true (default), the popup positions so the selected item appears over the trigger. When false, the popup aligns to the trigger edge.


```python
def select_align_with_items():

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p("Align Item", class_name="font-medium text-foreground"),
                rx.el.p(
                    "Toggle to align the item with the trigger.",
                    class_name="text-muted-foreground",
                ),
                class_name="flex flex-col gap-y-2 text-sm",
            ),
            switch.root(
                switch.thumb(),
                on_checked_change=align_with_item_trigger.set_value(
                    ~align_with_item_trigger.value
                ),
            ),
            class_name="flex flex-row items-start justify-between w-full",
        ),
        select.root(
            select.trigger(
                select.value(),
                select.icon(hi("ArrowDown01Icon", classs_name="size-4")),
                class_name="w-full flex items-center justify-between group",
            ),
            select.portal(
                select.positioner(
                    select.popup(
                        select.group(
                            select.group_label("Fruit"),
                            *[
                                select.item(
                                    select.item_text(fruit.capitalize()),
                                    select.item_indicator(
                                        hi("Tick02Icon", class_name="size-4")
                                    ),
                                    value=fruit,
                                    class_name="w-full !max-w-sm flex flex-row items-center justify-between",
                                )
                                for fruit in items
                            ],
                        ),
                    ),
                    side_offset=4,
                    align_item_with_trigger=align_with_item_trigger.value,
                ),
            ),
            name="example_select",
            default_value="blueberry",
        ),
        class_name="flex flex-col gap-y-4 max-w-sm",
    )
```


## Groups
Use `select.group` to organize items into sections, `select.group_label` to label each section, and `select.separator` to visually divide groups.


```python
def select_groups():
    fruits = [
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]

    vegetables = [
        {"label": "Carrot", "value": "carrot"},
        {"label": "Broccoli", "value": "broccoli"},
        {"label": "Spinach", "value": "spinach"},
    ]

    return select.root(
        select.trigger(
            select.value(),
            select.icon(
                # hi("ArrowDown01Icon", classs_name="size-4"),
            ),
            class_name="w-full max-w-48 flex items-center justify-between",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.group(
                        select.group_label("Fruits"),
                        *[
                            select.item(
                                select.item_text(item["label"]),
                                select.item_indicator(
                                    # hi("Tick02Icon", class_name="size-4")
                                ),
                                value=item["value"],
                                class_name="flex flex-row items-center justify-between",
                            )
                            for item in fruits
                        ],
                    ),
                    select.separator(),
                    select.group(
                        select.group_label("Vegetables"),
                        *[
                            select.item(
                                select.item_text(item["label"]),
                                select.item_indicator(
                                    # hi("Tick02Icon", class_name="size-4")
                                ),
                                value=item["value"],
                                class_name="flex flex-row items-center justify-between",
                            )
                            for item in vegetables
                        ],
                    ),
                ),
            ),
        ),
        items=[*fruits, *vegetables],
        name="select_groups",
        default_value="banana",
    )
```


## Scrollable
Use `select.scroll_up_arrow` and `select.scroll_down_arrow` to provide navigation controls for scrolling through long lists of select items within the dropdown.


```python
def select_with_scroll_arrows():
    north_america = [
        {"label": "Eastern Standard Time", "value": "est"},
        {"label": "Central Standard Time", "value": "cst"},
        {"label": "Mountain Standard Time", "value": "mst"},
        {"label": "Pacific Standard Time", "value": "pst"},
        {"label": "Alaska Standard Time", "value": "akst"},
        {"label": "Hawaii Standard Time", "value": "hst"},
    ]

    europe_africa = [
        {"label": "Greenwich Mean Time", "value": "gmt"},
        {"label": "Central European Time", "value": "cet"},
        {"label": "Eastern European Time", "value": "eet"},
        {"label": "Central Africa Time", "value": "cat"},
        {"label": "East Africa Time", "value": "eat"},
    ]

    asia = [
        {"label": "Moscow Time", "value": "msk"},
        {"label": "India Standard Time", "value": "ist"},
        {"label": "China Standard Time", "value": "cst_china"},
        {"label": "Japan Standard Time", "value": "jst"},
    ]

    return select.root(
        select.trigger(
            select.value(),
            select.icon(),
            class_name="w-full max-w-64 flex items-center justify-between",
        ),
        select.portal(
            select.positioner(
                select.popup(
                    select.scroll_up_arrow(),
                    select.list(
                        select.group(
                            select.group_label("North America"),
                            *[
                                select.item(
                                    select.item_text(i["label"]),
                                    select.item_indicator(),
                                    value=i["value"],
                                )
                                for i in north_america
                            ],
                        ),
                        select.group(
                            select.group_label("Europe & Africa"),
                            *[
                                select.item(
                                    select.item_text(i["label"]),
                                    select.item_indicator(),
                                    value=i["value"],
                                )
                                for i in europe_africa
                            ],
                        ),
                        select.group(
                            select.group_label("Asia"),
                            *[
                                select.item(
                                    select.item_text(i["label"]),
                                    select.item_indicator(),
                                    value=i["value"],
                                )
                                for i in asia
                            ],
                        ),
                        class_name="max-h-64 overflow-y-auto",
                    ),
                    select.scroll_down_arrow(),
                ),
            ),
        ),
        items=[
            {"label": "Select timezone", "value": None},
            *north_america,
            *europe_africa,
            *asia,
        ],
        name="timezone_select",
        default_value="est",
    )
```

