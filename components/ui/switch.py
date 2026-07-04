from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralSwitchSize = Literal["default", "sm"]


class ClassNames:
    ROOT = (
        "peer group/switch relative inline-flex shrink-0 items-center rounded-full "
        "border border-transparent transition-all outline-none "
        "after:absolute after:-inset-x-3 after:-inset-y-2 "
        "focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 "
        "aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 "
        "data-[size=default]:h-[18.4px] data-[size=default]:w-[32px] "
        "data-[size=sm]:h-[14px] data-[size=sm]:w-[24px] "
        "dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 "
        "data-checked:bg-primary data-unchecked:bg-input dark:data-unchecked:bg-input/80 "
        "data-disabled:cursor-not-allowed data-disabled:opacity-50"
    )

    THUMB = (
        "pointer-events-none block rounded-full bg-background ring-0 transition-transform "
        "group-data-[size=default]/switch:size-4 group-data-[size=sm]/switch:size-3 "
        "group-data-[size=default]/switch:data-checked:translate-x-[calc(100%-2px)] "
        "group-data-[size=sm]/switch:data-checked:translate-x-[calc(100%-2px)] "
        "dark:data-checked:bg-primary-foreground "
        "group-data-[size=default]/switch:data-unchecked:translate-x-0 "
        "group-data-[size=sm]/switch:data-unchecked:translate-x-0 "
        "dark:data-unchecked:bg-foreground"
    )


class SwitchBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/switch"

    @property
    def import_var(self):
        return ImportVar(tag="Switch", package_path="", install=False)


class SwitchRoot(SwitchBaseComponent):
    tag = "Switch.Root"

    name: Var[str]
    default_checked: Var[bool]
    checked: Var[bool]
    on_checked_change: EventHandler[passthrough_event_spec(bool)]
    native_button: Var[bool]
    disabled: Var[bool]
    read_only: Var[bool]
    required: Var[bool]
    input_ref: Var[str]
    size: Var[LiteralSwitchSize]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "switch"

        # Pull or default size prop and put it in data attribute
        size = props.pop("size", "default")
        props["data-size"] = size

        cls.set_class_name(ClassNames.ROOT, props)

        # If no explicit thumb/child is given, auto-inject it like Shadcn does!
        if not children:
            children = (SwitchThumb.create(),)

        return super().create(*children, **props)


class SwitchThumb(SwitchBaseComponent):
    tag = "Switch.Thumb"
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "switch-thumb"
        cls.set_class_name(ClassNames.THUMB, props)
        return super().create(*children, **props)


class Switch(ComponentNamespace):
    root = staticmethod(SwitchRoot.create)
    thumb = staticmethod(SwitchThumb.create)
    class_names = ClassNames


switch = Switch()
