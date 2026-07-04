from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.el import Div

from .base_ui import PACKAGE_NAME, BaseUIComponent
from .component import CoreComponent


class ClassNames:
    BACKDROP = "fixed inset-0 z-50 bg-black/10 duration-100 supports-backdrop-filter:backdrop-blur-xs data-open:animate-in data-closed:animate-out data-closed:fade-out-0 data-open:fade-in-0"
    POPUP = "fixed left-[50%] top-[50%] z-50 grid w-full max-w-[calc(100%-2rem)] translate-x-[-50%] translate-y-[-50%] gap-4 rounded-xl bg-popover p-4 text-sm text-popover-foreground ring-1 ring-foreground/10 duration-100 outline-hidden sm:max-w-sm data-open:animate-in data-closed:animate-out data-closed:fade-out-0 data-open:fade-in-0 data-closed:zoom-out-95 data-open:zoom-in-95"
    HEADER = "flex flex-col gap-2"
    TITLE = "cn-font-heading text-base leading-none font-medium text-foreground"
    DESCRIPTION = "text-sm text-muted-foreground"
    FOOTER = "-mx-4 -mb-4 flex flex-col-reverse gap-2 rounded-b-xl border-t border-foreground/10 bg-muted/50 p-4 sm:flex-row sm:justify-end"
    TRIGGER = ""
    CLOSE = "!absolute !top-2 !right-2 rounded-xs opacity-70 transition-opacity hover:opacity-100 focus:outline-hidden text-muted-foreground"


class DialogBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/dialog"

    @property
    def import_var(self):
        return ImportVar(tag="Dialog", package_path="", install=False)


class DialogRoot(DialogBaseComponent):
    tag = "Dialog.Root"

    default_open: Var[bool]
    open: Var[bool]
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]
    dismissible: Var[bool]
    modal: Var[bool | Literal["trap-focus"]]
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "dialog"
        return super().create(*children, **props)


class DialogTrigger(DialogBaseComponent):
    tag = "Dialog.Trigger"

    native_button: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "dialog-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class DialogPortal(DialogBaseComponent):
    tag = "Dialog.Portal"

    container: Var[str]
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "dialog-portal"
        return super().create(*children, **props)


class DialogBackdrop(DialogBaseComponent):
    tag = "Dialog.Backdrop"

    force_render: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "dialog-overlay"
        cls.set_class_name(ClassNames.BACKDROP, props)
        return super().create(*children, **props)


class DialogPopup(DialogBaseComponent):
    tag = "Dialog.Popup"

    initial_focus: Var[str]
    final_focus: Var[str]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "dialog-content"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class DialogTitle(DialogBaseComponent):
    tag = "Dialog.Title"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "dialog-title"
        cls.set_class_name(ClassNames.TITLE, props)
        return super().create(*children, **props)


class DialogDescription(DialogBaseComponent):
    tag = "Dialog.Description"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "dialog-description"
        cls.set_class_name(ClassNames.DESCRIPTION, props)
        return super().create(*children, **props)


class DialogClose(DialogBaseComponent):
    tag = "Dialog.Close"

    native_button: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "dialog-close"
        cls.set_class_name(ClassNames.CLOSE, props)
        return super().create(*children, **props)


class DialogHeader(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> Div:
        props["data-slot"] = "dialog-header"
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class DialogFooter(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> Div:
        props["data-slot"] = "dialog-footer"
        cls.set_class_name(ClassNames.FOOTER, props)
        return super().create(*children, **props)


class Dialog(ComponentNamespace):
    root = staticmethod(DialogRoot.create)
    trigger = staticmethod(DialogTrigger.create)
    portal = staticmethod(DialogPortal.create)
    backdrop = staticmethod(DialogBackdrop.create)
    popup = staticmethod(DialogPopup.create)
    title = staticmethod(DialogTitle.create)
    description = staticmethod(DialogDescription.create)
    close = staticmethod(DialogClose.create)
    header = staticmethod(DialogHeader.create)
    footer = staticmethod(DialogFooter.create)
    class_names = ClassNames


dialog = Dialog()
