from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..icons.hugeicon import hi
from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    ROOT = (
        "peer relative flex size-4 shrink-0 items-center justify-center rounded-[4px] "
        "border border-input transition-colors outline-none "
        "group-has-disabled/field:opacity-50 after:absolute after:-inset-x-3 after:-inset-y-2 "
        "focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 "
        "disabled:cursor-not-allowed disabled:opacity-50 "
        "aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 "
        "aria-invalid:aria-checked:border-primary dark:bg-input/30 "
        "dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 "
        "data-checked:border-primary data-checked:bg-primary data-checked:text-primary-foreground "
        "dark:data-checked:bg-primary"
    )
    INDICATOR = (
        "grid place-content-center text-current transition-none [&>svg]:size-3.5"
    )


class CheckboxBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/checkbox"

    @property
    def import_var(self):
        return ImportVar(tag="Checkbox", package_path="", install=False)


class CheckboxRoot(CheckboxBaseComponent):
    tag = "Checkbox.Root"

    default_checked: Var[bool]
    checked: Var[bool]
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]
    indeterminate: Var[bool]
    disabled: Var[bool]
    required: Var[bool]
    name: Var[str]
    value: Var[str]
    native_button: Var[bool]
    parent: Var[bool]
    read_only: Var[bool]
    render_: Component

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "checkbox"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CheckboxIndicator(CheckboxBaseComponent):
    tag = "Checkbox.Indicator"

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        if len(children) == 0:
            children = (hi("Tick02Icon"),)
        props["data-slot"] = "checkbox-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class Checkbox(ComponentNamespace):
    root = staticmethod(CheckboxRoot.create)
    indicator = staticmethod(CheckboxIndicator.create)
    class_names = ClassNames


checkbox = Checkbox()
