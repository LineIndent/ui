

# Toggle Group

A set of two-state buttons that can be toggled on or off.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component toggle_group
```

### Manual Installation

```python
# from typing import Literal

# from reflex.components.component import Component
# from reflex.event import EventHandler, passthrough_event_spec
# from reflex.utils.imports import ImportVar
# from reflex.vars.base import Var

# from .base_ui import PACKAGE_NAME, BaseUIComponent

# LiteralOrientation = Literal["horizontal", "vertical"]


# class ClassNames:
#     ROOT = ""


# class ToggleGroupBaseComponent(BaseUIComponent):
#     library = f"{PACKAGE_NAME}/toggle-group"

#     @property
#     def import_var(self):
#         return ImportVar(tag="ToggleGroup", package_path="", install=False)


# class ToggleGroupRoot(ToggleGroupBaseComponent):
#     tag = "ToggleGroup"

#     default_value: Var[list[str | int]]

#     value: Var[list[str | int]]

#     on_value_change: EventHandler[passthrough_event_spec(list[str | int], dict)]

#     multiple: Var[bool]

#     disabled: Var[bool]

#     loop: Var[bool]

#     orientation: Var[LiteralOrientation]

#     render_: Var[Component]

#     @classmethod
#     def create(cls, *children, **props) -> BaseUIComponent:
#         props["data-slot"] = "toggle-group"
#         cls.set_class_name(ClassNames.ROOT, props)
#         return super().create(*children, **props)


# toggle_group = ToggleGroupRoot.create


# from typing import Literal

# from reflex.components.component import Component, ComponentNamespace
# from reflex.event import EventHandler, passthrough_event_spec
# from reflex.utils.imports import ImportVar
# from reflex.vars.base import Var

# from ..utils.twmerge import cn
# from .base_ui import PACKAGE_NAME, BaseUIComponent

# LiteralOrientation = Literal["horizontal", "vertical"]
# LiteralToggleVariant = Literal["default", "outline"]
# LiteralToggleSize = Literal["default", "sm", "lg"]


# class ClassNames:
#     ROOT = (
#         "group/toggle-group flex w-fit flex-row items-center gap-(--gap) rounded-lg "
#         "data-[size=sm]:rounded-[min(var(--radius-md),10px)] "
#         "data-[orientation=vertical]:flex-col data-[orientation=vertical]:items-stretch"
#     )

#     # Same variant/size classes as toggle.py, but gated on the ROOT's data
#     # attributes rather than computed per-item — this is what lets each
#     # item inherit variant/size from the group without needing JS context.
#     ITEM_VARIANTS = {
#         "default": "group-data-[variant=default]/toggle-group:bg-transparent",
#         "outline": (
#             "group-data-[variant=outline]/toggle-group:border "
#             "group-data-[variant=outline]/toggle-group:border-input "
#             "group-data-[variant=outline]/toggle-group:bg-transparent "
#             "group-data-[variant=outline]/toggle-group:hover:bg-muted"
#         ),
#     }

#     ITEM_SIZES = {
#         "default": (
#             "group-data-[size=default]/toggle-group:h-8 "
#             "group-data-[size=default]/toggle-group:min-w-8 "
#             "group-data-[size=default]/toggle-group:px-2.5"
#         ),
#         "sm": (
#             "group-data-[size=sm]/toggle-group:h-7 "
#             "group-data-[size=sm]/toggle-group:min-w-7 "
#             "group-data-[size=sm]/toggle-group:rounded-[min(var(--radius-md),10px)] "
#             "group-data-[size=sm]/toggle-group:px-2.5 "
#             "group-data-[size=sm]/toggle-group:text-[0.8rem] "
#             "group-data-[size=sm]/toggle-group:[&_svg:not([class*='size-'])]:size-3.5"
#         ),
#         "lg": (
#             "group-data-[size=lg]/toggle-group:h-9 "
#             "group-data-[size=lg]/toggle-group:min-w-9 "
#             "group-data-[size=lg]/toggle-group:px-2.5"
#         ),
#     }

#     ITEM_BASE = (
#         "group-data-toggle-group-item/toggle-group:inline-flex items-center justify-center gap-1 "
#         "text-sm font-medium whitespace-nowrap transition-all outline-none "
#         "hover:bg-muted hover:text-foreground "
#         "focus:z-10 focus-visible:z-10 "
#         "focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 "
#         "disabled:pointer-events-none disabled:opacity-50 "
#         "aria-invalid:border-destructive aria-invalid:ring-destructive/20 "
#         "aria-pressed:bg-muted data-[state=on]:bg-muted "
#         "dark:aria-invalid:ring-destructive/40 "
#         "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 "
#         "shrink-0 "
#         # segmented/connected mode when the group's spacing is 0
#         "group-data-[spacing=0]/toggle-group:rounded-none "
#         "group-data-[spacing=0]/toggle-group:px-2 "
#         "group-data-horizontal/toggle-group:group-data-[spacing=0]/toggle-group:first:rounded-l-lg "
#         "group-data-horizontal/toggle-group:group-data-[spacing=0]/toggle-group:last:rounded-r-lg "
#         "group-data-vertical/toggle-group:group-data-[spacing=0]/toggle-group:first:rounded-t-lg "
#         "group-data-vertical/toggle-group:group-data-[spacing=0]/toggle-group:last:rounded-b-lg "
#         "group-data-horizontal/toggle-group:group-data-[spacing=0]/toggle-group:group-data-[variant=outline]/toggle-group:border-l-0 "
#         "group-data-horizontal/toggle-group:group-data-[spacing=0]/toggle-group:group-data-[variant=outline]/toggle-group:first:border-l "
#         "group-data-vertical/toggle-group:group-data-[spacing=0]/toggle-group:group-data-[variant=outline]/toggle-group:border-t-0 "
#         "group-data-vertical/toggle-group:group-data-[spacing=0]/toggle-group:group-data-[variant=outline]/toggle-group:first:border-t"
#     )


# class ToggleGroupBaseComponent(BaseUIComponent):
#     library = f"{PACKAGE_NAME}/toggle-group"

#     @property
#     def import_var(self):
#         return ImportVar(tag="ToggleGroup", package_path="", install=False)


# class ToggleGroupRoot(ToggleGroupBaseComponent):
#     tag = "ToggleGroup"

#     default_value: Var[list[str | int]]
#     value: Var[list[str | int]]
#     on_value_change: EventHandler[passthrough_event_spec(list[str | int], dict)]
#     multiple: Var[bool]
#     disabled: Var[bool]
#     loop: Var[bool]
#     orientation: Var[LiteralOrientation]
#     render_: Var[Component]

#     @classmethod
#     def create(cls, *children, **props) -> BaseUIComponent:
#         variant = props.pop("variant", "default")
#         size = props.pop("size", "default")
#         spacing = props.pop("spacing", 2)

#         props["data-slot"] = "toggle-group"
#         props["data-variant"] = variant
#         props["data-size"] = size
#         props["data-spacing"] = spacing
#         props["style"] = {"--gap": spacing, **props.get("style", {})}

#         cls.set_class_name(ClassNames.ROOT, props)
#         return super().create(*children, **props)


# class ToggleGroupItem(BaseUIComponent):
#     tag = "Toggle"
#     library = f"{PACKAGE_NAME}/toggle"

#     @property
#     def import_var(self):
#         return ImportVar(tag="Toggle", package_path="", install=False)

#     value: Var[str]
#     disabled: Var[bool]
#     render_: Var[Component]

#     @classmethod
#     def create(cls, *children, **props) -> BaseUIComponent:
#         # variant/size are optional per-item overrides; if omitted the
#         # group-data selectors above inherit from the parent Root's
#         # data-variant/data-size automatically.
#         variant = props.pop("variant", None)
#         size = props.pop("size", None)

#         props["data-slot"] = "toggle-group-item"
#         if variant:
#             props["data-variant"] = variant
#         if size:
#             props["data-size"] = size

#         cls.set_class_name(
#             cn(
#                 ClassNames.ITEM_BASE,
#                 ClassNames.ITEM_VARIANTS.get(variant, ""),
#                 ClassNames.ITEM_SIZES.get(size, ""),
#             ),
#             props,
#         )
#         return super().create(*children, **props)


# class ToggleGroup(ComponentNamespace):
#     root = __call__ = staticmethod(ToggleGroupRoot.create)
#     item = staticmethod(ToggleGroupItem.create)
#     class_names = ClassNames


# toggle_group = ToggleGroup()


from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]
LiteralToggleVariant = Literal["default", "outline"]
LiteralToggleSize = Literal["default", "sm", "lg"]


class ClassNames:
    ROOT = (
        "group/toggle-group flex w-fit flex-row items-center rounded-lg "
        "data-[size=sm]:rounded-[min(var(--radius-md),10px)] "
        "data-[orientation=vertical]:flex-col data-[orientation=vertical]:items-stretch"
    )

    ITEM_VARIANTS = {
        "default": "group-data-[variant=default]/toggle-group:bg-transparent",
        "outline": (
            "group-data-[variant=outline]/toggle-group:border "
            "group-data-[variant=outline]/toggle-group:border-input "
            "group-data-[variant=outline]/toggle-group:bg-transparent "
            "group-data-[variant=outline]/toggle-group:hover:bg-muted"
        ),
    }

    ITEM_SIZES = {
        "default": (
            "group-data-[size=default]/toggle-group:h-8 "
            "group-data-[size=default]/toggle-group:min-w-8 "
            "group-data-[size=default]/toggle-group:px-2.5"
        ),
        "sm": (
            "group-data-[size=sm]/toggle-group:h-7 "
            "group-data-[size=sm]/toggle-group:min-w-7 "
            "group-data-[size=sm]/toggle-group:rounded-[min(var(--radius-md),10px)] "
            "group-data-[size=sm]/toggle-group:px-2.5 "
            "group-data-[size=sm]/toggle-group:text-[0.8rem] "
            "group-data-[size=sm]/toggle-group:[&_svg:not([class*='size-'])]:size-3.5"
        ),
        "lg": (
            "group-data-[size=lg]/toggle-group:h-9 "
            "group-data-[size=lg]/toggle-group:min-w-9 "
            "group-data-[size=lg]/toggle-group:px-2.5"
        ),
    }

    ITEM_BASE = (
        "inline-flex shrink-0 items-center justify-center gap-1 rounded-lg "
        "text-sm font-medium whitespace-nowrap transition-all outline-none "
        "hover:bg-muted hover:text-foreground "
        "focus:z-10 focus-visible:z-10 "
        "focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 "
        "disabled:pointer-events-none disabled:opacity-50 "
        "aria-invalid:border-destructive aria-invalid:ring-destructive/20 "
        "aria-pressed:bg-muted data-[state=on]:bg-muted "
        "dark:aria-invalid:ring-destructive/40 "
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 "
        "group-data-[spacing=0]/toggle-group:rounded-none "
        "group-data-[spacing=0]/toggle-group:px-2 "
        "group-data-[orientation=horizontal]/toggle-group:group-data-[spacing=0]/toggle-group:first:rounded-l-lg "
        "group-data-[orientation=horizontal]/toggle-group:group-data-[spacing=0]/toggle-group:last:rounded-r-lg "
        "group-data-[orientation=vertical]/toggle-group:group-data-[spacing=0]/toggle-group:first:rounded-t-lg "
        "group-data-[orientation=vertical]/toggle-group:group-data-[spacing=0]/toggle-group:last:rounded-b-lg "
        "group-data-[orientation=horizontal]/toggle-group:group-data-[spacing=0]/toggle-group:group-data-[variant=outline]/toggle-group:border-l-0 "
        "group-data-[orientation=horizontal]/toggle-group:group-data-[spacing=0]/toggle-group:group-data-[variant=outline]/toggle-group:first:border-l "
        "group-data-[orientation=vertical]/toggle-group:group-data-[spacing=0]/toggle-group:group-data-[variant=outline]/toggle-group:border-t-0 "
        "group-data-[orientation=vertical]/toggle-group:group-data-[spacing=0]/toggle-group:group-data-[variant=outline]/toggle-group:first:border-t"
    )


class ToggleGroupBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/toggle-group"

    @property
    def import_var(self):
        return ImportVar(tag="ToggleGroup", package_path="", install=False)


class ToggleGroupRoot(ToggleGroupBaseComponent):
    tag = "ToggleGroup"
    default_value: Var[list[str | int]]
    value: Var[list[str | int]]
    on_value_change: EventHandler[passthrough_event_spec(list[str | int], dict)]
    multiple: Var[bool]
    disabled: Var[bool]
    loop: Var[bool]
    orientation: Var[LiteralOrientation]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        variant = props.pop("variant", "default")
        size = props.pop("size", "default")
        spacing = props.pop("spacing", 2)
        orientation = props.get("orientation", "horizontal")

        props["data-slot"] = "toggle-group"
        props["data-variant"] = variant
        props["data-size"] = size
        props["data-spacing"] = spacing
        props["data-orientation"] = orientation
        props["style"] = {"gap": f"{spacing * 0.25}rem", **props.get("style", {})}

        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class ToggleGroupItem(BaseUIComponent):
    tag = "Toggle"
    library = f"{PACKAGE_NAME}/toggle"

    @property
    def import_var(self):
        return ImportVar(tag="Toggle", package_path="", install=False)

    value: Var[str]
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        variant = props.pop("variant", None)
        size = props.pop("size", None)

        props["data-slot"] = "toggle-group-item"
        if variant:
            props["data-variant"] = variant
        if size:
            props["data-size"] = size

        variant_classes = (
            ClassNames.ITEM_VARIANTS.get(variant)
            if variant
            else " ".join(ClassNames.ITEM_VARIANTS.values())
        )
        size_classes = (
            ClassNames.ITEM_SIZES.get(size)
            if size
            else " ".join(ClassNames.ITEM_SIZES.values())
        )

        cls.set_class_name(
            cn(
                ClassNames.ITEM_BASE,
                variant_classes,
                size_classes,
            ),
            props,
        )
        return super().create(*children, **props)


class ToggleGroup(ComponentNamespace):
    root = __call__ = staticmethod(ToggleGroupRoot.create)
    item = staticmethod(ToggleGroupItem.create)
    class_names = ClassNames


toggle_group = ToggleGroup()
```


# Usage


```python
from components.ui.toggle_group import toggle_group
```


# Anatomy 
Use the following composition to build a `Toggle Group` component.


```python
toggle_group(
    toggle_group.item("Option 1", value="1"),
    toggle_group.item("Option 2", value="2"),
)
```


# Examples

## Outline

Use `variant="outline"` for an outline style.


```python
def toggle_group_outline() -> rx.Component:
    return toggle_group.root(
        toggle_group.item(
            "All",
            value="all",
            aria_label="Toggle all",
        ),
        toggle_group.item(
            "Missed",
            value="missed",
            aria_label="Toggle missed",
        ),
        variant="outline",
        default_value=["all"],
    )
```


## Sizes

Use the `size` prop to change the size of the toggle group.


```python
def toggle_group_sizes() -> rx.Component:
    return rx.el.div(
        toggle_group.root(
            toggle_group.item("Top", value="top", aria_label="Toggle top"),
            toggle_group.item("Bottom", value="bottom", aria_label="Toggle bottom"),
            toggle_group.item("Left", value="left", aria_label="Toggle left"),
            toggle_group.item("Right", value="right", aria_label="Toggle right"),
            size="sm",
            variant="outline",
            default_value=["top"],
        ),
        toggle_group.root(
            toggle_group.item("Top", value="top", aria_label="Toggle top"),
            toggle_group.item("Bottom", value="bottom", aria_label="Toggle bottom"),
            toggle_group.item("Left", value="left", aria_label="Toggle left"),
            toggle_group.item("Right", value="right", aria_label="Toggle right"),
            variant="outline",
            default_value=["top"],
        ),
        class_name="flex flex-col gap-4",
    )
```


## Spacing

Use `spacing` to add spacing between toggle group items.


```python
def toggle_group_spacing() -> rx.Component:
    return toggle_group.root(
        toggle_group.item("Top", value="top", aria_label="Toggle top"),
        toggle_group.item("Bottom", value="bottom", aria_label="Toggle bottom"),
        toggle_group.item("Left", value="left", aria_label="Toggle left"),
        toggle_group.item("Right", value="right", aria_label="Toggle right"),
        size="sm",
        variant="outline",
        spacing=4,
        default_value=["top"],
    )
```


## Vertical

Use `orientation="vertical"` for vertical toggle groups.


```python
def toggle_group_vertical() -> rx.Component:
    return toggle_group.root(
        toggle_group.item(
            rx.icon(tag="bold"),
            value="bold",
            aria_label="Toggle bold",
        ),
        toggle_group.item(
            rx.icon(tag="italic"),
            value="italic",
            aria_label="Toggle italic",
        ),
        toggle_group.item(
            rx.icon(tag="underline"),
            value="underline",
            aria_label="Toggle underline",
        ),
        multiple=True,
        orientation="vertical",
        spacing=1,
        default_value=["bold", "italic"],
    )
```


## Disabled


```python
def toggle_group_disabled() -> rx.Component:
    return toggle_group.root(
        toggle_group.item(
            hi("TextBoldIcon"),
            value="bold",
            aria_label="Toggle bold",
        ),
        toggle_group.item(
            hi("TextItalicIcon"),
            value="italic",
            aria_label="Toggle italic",
        ),
        toggle_group.item(
            hi("TextUnderlineIcon"),
            value="strikethrough",
            aria_label="Toggle strikethrough",
        ),
        disabled=True,
    )
```


## Custom

A custom toggle group example.


```python
def toggle_group_custom() -> rx.Component:

    return field.set(
        field.root(
            field.label("Font Weight"),
            toggle_group.root(
                toggle_group.item(
                    rx.el.span("Aa", class_name="text-2xl leading-none font-light"),
                    rx.el.span("Light", class_name="text-xs text-muted-foreground"),
                    value="light",
                    aria_label="Light",
                    class_name="flex !size-16 flex-col items-center justify-center rounded-xl",
                ),
                toggle_group.item(
                    rx.el.span("Aa", class_name="text-2xl leading-none font-normal"),
                    rx.el.span("Normal", class_name="text-xs text-muted-foreground"),
                    value="normal",
                    aria_label="Normal",
                    class_name="flex !size-16 flex-col items-center justify-center rounded-xl",
                ),
                toggle_group.item(
                    rx.el.span("Aa", class_name="text-2xl leading-none font-medium"),
                    rx.el.span("Medium", class_name="text-xs text-muted-foreground"),
                    value="medium",
                    aria_label="Medium",
                    class_name="flex !size-16 flex-col items-center justify-center rounded-xl",
                ),
                toggle_group.item(
                    rx.el.span("Aa", class_name="text-2xl leading-none font-bold"),
                    rx.el.span("Bold", class_name="text-xs text-muted-foreground"),
                    value="bold",
                    aria_label="Bold",
                    class_name="flex !size-16 flex-col items-center justify-center rounded-xl",
                ),
                on_value_change=font_weight.set_value,
                variant="outline",
                spacing=2,
                size="lg",
            ),
            field.description(
                "Use ",
                rx.el.code(
                    f"font-{font_weight.value}",
                    class_name="rounded-md bg-muted px-1 py-0.5 font-mono",
                ),
                " to set the font weight.",
            ),
        )
    )
```


>The default spacing is **2** so toggle groups render with space between items by default. Use **spacing={0}** for connected items.
