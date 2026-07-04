from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    ROOT = (
        "group/tabs flex gap-2 data-[orientation=horizontal]:flex-col "
        "data-[orientation=vertical]:flex-row data-[orientation=vertical]:gap-4"
    )

    LIST = (
        "group/tabs-list relative inline-flex w-fit items-center justify-center rounded-lg p-[3px] "
        "text-muted-foreground bg-muted "
        "group-data-[orientation=horizontal]/tabs:h-8 group-data-[orientation=vertical]/tabs:h-fit "
        "group-data-[orientation=vertical]/tabs:flex-col group-data-[orientation=vertical]/tabs:p-1 group-data-[orientation=vertical]/tabs:gap-1 "
        "data-[variant=line]:rounded-none data-[variant=line]:bg-transparent data-[variant=line]:gap-1"
    )

    TAB = (
        "relative inline-flex h-[calc(100%-1px)] flex-1 items-center justify-center gap-1.5 "
        "rounded-md border border-transparent px-1.5 py-0.5 text-sm font-medium whitespace-nowrap "
        "text-foreground/60 transition-all hover:text-foreground "
        "focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1 "
        "disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none "
        "dark:text-muted-foreground dark:hover:text-foreground "
        "group-data-[orientation=vertical]/tabs:w-full group-data-[orientation=vertical]/tabs:justify-start "
        "data-[active]:text-foreground "
        "group-data-[variant=default]/tabs-list:data-[active]:bg-background "
        "dark:group-data-[variant=default]/tabs-list:data-[active]:border-input "
        "dark:group-data-[variant=default]/tabs-list:data-[active]:bg-input/30 "
        "group-data-[variant=default]/tabs-list:data-[active]:shadow-sm "
        "group-data-[variant=line]/tabs-list:data-[active]:bg-transparent "
        "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
    )

    INDICATOR = (
        "absolute z-[0] transition-all duration-200 ease-in-out "
        "group-data-[variant=default]/tabs-list:rounded-lg "
        "group-data-[variant=default]/tabs-list:bg-background "
        "group-data-[variant=default]/tabs-list:shadow-sm "
        "dark:group-data-[variant=default]/tabs-list:border dark:group-data-[variant=default]/tabs-list:border-input "
        "dark:group-data-[variant=default]/tabs-list:bg-input/30 "
        "group-data-[variant=line]/tabs-list:bg-foreground "
        "group-data-[variant=line]/tabs-list:!h-[2px] "
        "group-data-[variant=line]/tabs-list:!top-[auto] "
        "group-data-[variant=line]/tabs-list:!bottom-0 "
        "[left:var(--active-tab-left)] [top:var(--active-tab-top)] "
        "[width:var(--active-tab-width)] [height:var(--active-tab-height)]"
    )

    PANEL = "flex-1 text-sm outline-none flex flex-col gap-2"


class TabsBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/tabs"

    @property
    def import_var(self):
        return ImportVar(tag="Tabs", package_path="", install=False)


class TabsRoot(TabsBaseComponent):
    tag = "Tabs.Root"
    default_value: Var[str | int]
    value: Var[str | int]
    on_value_change: EventHandler[passthrough_event_spec(str | dict)]
    orientation: Var[LiteralOrientation]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class TabsList(TabsBaseComponent):
    tag = "Tabs.List"
    activate_on_focus: Var[bool]
    loop: Var[bool]
    variant: Var[Literal["default", "line"]]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs-list"
        if "variant" in props:
            props["data-variant"] = props.pop("variant")
        else:
            props["data-variant"] = "default"

        cls.set_class_name(ClassNames.LIST, props)
        return super().create(*children, **props)


class TabsTab(TabsBaseComponent):
    tag = "Tabs.Tab"
    value: Var[str | int]
    native_button: Var[bool]
    disabled: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs-trigger"
        cls.set_class_name(ClassNames.TAB, props)
        return super().create(*children, **props)


class TabsIndicator(TabsBaseComponent):
    tag = "Tabs.Indicator"
    render_before_hydration: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class TabsPanel(TabsBaseComponent):
    tag = "Tabs.Panel"
    value: Var[str | int]
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "tabs-content"
        cls.set_class_name(ClassNames.PANEL, props)
        return super().create(*children, **props)


class Tabs(ComponentNamespace):
    root = __call__ = staticmethod(TabsRoot.create)
    list = staticmethod(TabsList.create)
    tab = staticmethod(TabsTab.create)
    panel = staticmethod(TabsPanel.create)
    indicator = staticmethod(TabsIndicator.create)
    class_names = ClassNames


tabs = Tabs()
