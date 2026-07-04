# from typing import Literal

# from reflex.components.component import Component
# from reflex.event import EventHandler, passthrough_event_spec
# from reflex.utils.imports import ImportVar
# from reflex.vars.base import Var

# from ..utils.twmerge import cn
# from .base_ui import PACKAGE_NAME, BaseUIComponent

# Stroke = Literal["fill", "stroke"]


# class ClassNames:
#     ROOT = "group/toggle p-1 inline-flex items-center justify-center gap-1 rounded-lg border border-input text-sm font-medium whitespace-nowrap transition-all hover:bg-muted hover:text-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 aria-pressed:bg-muted data-[state=on]:bg-muted dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"

#     ICON_VARIANT_CLASSES = {
#         "fill": "data-[pressed]:[&_svg]:fill-primary",
#         "stroke": "data-[pressed]:[&_svg]:text-primary",
#         None: "",
#     }


# class ToggleBaseComponent(BaseUIComponent):
#     library = f"{PACKAGE_NAME}/toggle"

#     @property
#     def import_var(self):
#         return ImportVar(tag="Toggle", package_path="", install=False)


# class Toggle(ToggleBaseComponent):
#     tag = "Toggle"

#     value: Var[str]

#     default_pressed: Var[bool]

#     pressed: Var[bool]

#     on_pressed_change: EventHandler[passthrough_event_spec(bool, dict)]

#     native_button: Var[bool]

#     disabled: Var[bool]

#     icon_variant: Var[Stroke | None]

#     render_: Var[Component]

#     @classmethod
#     def create(cls, *children, **props) -> BaseUIComponent:
#         props["data-slot"] = "toggle"
#         cls.set_class_name(
#             cn(
#                 ClassNames.ROOT,
#                 ClassNames.ICON_VARIANT_CLASSES.get(props.get("icon_variant")),
#             ),
#             props,
#         )
#         return super().create(*children, **props)


# toggle = Toggle.create

from typing import Literal

from reflex.components.component import Component
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent

Stroke = Literal["fill", "stroke"]
LiteralToggleVariant = Literal["default", "outline"]
LiteralToggleSize = Literal["default", "sm", "lg"]


class ClassNames:
    ROOT = (
        "group/toggle inline-flex items-center justify-center gap-1 rounded-lg "
        "text-sm font-medium whitespace-nowrap transition-all outline-none "
        "hover:bg-muted hover:text-foreground "
        "focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 "
        "disabled:pointer-events-none disabled:opacity-50 "
        "aria-invalid:border-destructive aria-invalid:ring-destructive/20 "
        "aria-pressed:bg-muted data-[state=on]:bg-muted "
        "dark:aria-invalid:ring-destructive/40 "
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    )

    VARIANTS = {
        "default": "bg-transparent",
        "outline": "border border-input bg-transparent hover:bg-muted",
    }

    SIZES = {
        "default": (
            "h-8 min-w-8 px-2.5 "
            "has-data-[icon=inline-end]:pr-2 has-data-[icon=inline-start]:pl-2"
        ),
        "sm": (
            "h-7 min-w-7 rounded-[min(var(--radius-md),12px)] px-2.5 text-[0.8rem] "
            "has-data-[icon=inline-end]:pr-1.5 has-data-[icon=inline-start]:pl-1.5 "
            "[&_svg:not([class*='size-'])]:size-3.5"
        ),
        "lg": (
            "h-9 min-w-9 px-2.5 "
            "has-data-[icon=inline-end]:pr-2 has-data-[icon=inline-start]:pl-2"
        ),
    }

    ICON_VARIANT_CLASSES = {
        "fill": "data-[pressed]:[&_svg]:fill-primary",
        "stroke": "data-[pressed]:[&_svg]:text-primary",
        None: "",
    }


class ToggleBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/toggle"

    @property
    def import_var(self):
        return ImportVar(tag="Toggle", package_path="", install=False)


class Toggle(ToggleBaseComponent):
    tag = "Toggle"

    value: Var[str]
    default_pressed: Var[bool]
    pressed: Var[bool]
    on_pressed_change: EventHandler[passthrough_event_spec(bool, dict)]
    native_button: Var[bool]
    disabled: Var[bool]
    icon_variant: Var[Stroke | None]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        variant = props.pop("variant", "default")
        size = props.pop("size", "default")
        data_slot = props.pop("data_slot", "toggle")

        props["data-slot"] = data_slot
        cls.set_class_name(
            cn(
                ClassNames.ROOT,
                ClassNames.VARIANTS.get(variant, ""),
                ClassNames.SIZES.get(size, ""),
                ClassNames.ICON_VARIANT_CLASSES.get(props.get("icon_variant")),
            ),
            props,
        )
        return super().create(*children, **props)

    def _exclude_props(self) -> list[str]:
        return [*super()._exclude_props(), "variant", "size"]


toggle = Toggle.create
