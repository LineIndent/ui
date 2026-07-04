

# Dialog

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component dialog
```

### Manual Installation

```python
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
```


# Usage


```python
from components.ui.dialog import Dialog
```


# Anatomy 
Use the following composition to build a `Dialog` component.


```python
dialog.root(
    dialog.trigger(),
    dialog.portal(
        dialog.backdrop(),
        dialog.popup(
            dialog.title(),
            dialog.description(),
            dialog.close(),
        ),
    ),
)
```


# Examples

## Custom Close Button

Replace the default close control with your own button. Make sure to pass in `dialog.class_names.CLOSE` to the rendered  component to ensure proper positioning.


```python
def dialog_close_button() -> rx.Component:
    return dialog.root(
        dialog.trigger(render_=button("Share", variant="outline")),
        dialog.portal(
            dialog.backdrop(),
            dialog.popup(
                dialog.header(
                    dialog.title("Share link"),
                    dialog.description(
                        "Anyone who has this link will be able to view this."
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label("Link", html_for="link", class_name="sr-only"),
                        input(
                            id="link",
                            default_value="https://ui.buridan.com/docs/getting-started/installation",
                            read_only=True,
                        ),
                        class_name="grid flex-1 gap-2",
                    ),
                    class_name="flex items-center gap-2",
                ),
                dialog.footer(
                    dialog.close(render_=button("Close", type="button")),
                    class_name="sm:justify-start",
                ),
                dialog.close(
                    render_=button(
                        hi("Cancel01Icon", class_name="size-4"),
                        variant="ghost",
                        size="icon-sm",
                        class_name=dialog.class_names.CLOSE,
                    )
                ),
                class_name="sm:max-w-md",
            ),
        ),
    )
```


## No Close Button

To omit the top-right close cross icon from your dialog layout, simply exclude the `dialog.close()` sub-component containing the icon button from your composition tree.


```python
def dialog_no_close_button() -> rx.Component:
    return dialog.root(
        dialog.trigger(render_=button("No Close Button", variant="outline")),
        dialog.portal(
            dialog.backdrop(),
            dialog.popup(
                dialog.header(
                    dialog.title("No Close Button"),
                    dialog.description(
                        "This dialog doesn't have a close button in the top-right corner."
                    ),
                ),
            ),
        ),
    )
```


## Sticky Footer

Keep actions visible while the content scrolls.


```python
def dialog_sticky_footer() -> rx.Component:
    return dialog.root(
        dialog.trigger(render_=button("Sticky Footer", variant="outline")),
        dialog.portal(
            dialog.backdrop(),
            dialog.popup(
                dialog.header(
                    dialog.title("Sticky Footer"),
                    dialog.description(
                        "This dialog has a sticky footer that stays visible while the content scrolls."
                    ),
                ),
                rx.el.div(
                    *[
                        rx.el.p(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do "
                            "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
                            "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                            "reprehenderit in voluptate velit esse cillum dolore eu fugiat "
                            "nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
                            "sunt in culpa qui officia deserunt mollit anim id est laborum.",
                            class_name="mb-4 leading-normal",
                        )
                        for _ in range(10)
                    ],
                    class_name="-mx-4 no-scrollbar max-h-[50vh] overflow-y-auto px-4",
                ),
                dialog.footer(
                    dialog.close(render_=button("Close", variant="outline")),
                ),
                dialog.close(
                    render_=button(
                        hi("Cancel01Icon", class_name="size-4"),
                        variant="ghost",
                        size="icon-sm",
                        class_name=dialog.class_names.CLOSE,
                    )
                ),
            ),
        ),
    )
```

