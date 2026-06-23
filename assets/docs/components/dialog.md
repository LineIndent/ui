

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
"""Custom dialog component."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.el import Div

from ..icons.hugeicon import hi
from .base_ui import PACKAGE_NAME, BaseUIComponent
from .button import button


class ClassNames:
    """Class names for dialog components."""

    BACKDROP = "data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50"
    POPUP = "w-full bg-background data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 fixed top-[50%] left-[50%] z-50 grid w-full translate-x-[-50%] translate-y-[-50%] gap-4 rounded-lg border border-input p-6 shadow-lg duration-200"
    TITLE = "text-lg leading-none font-medium text-foreground"
    DESCRIPTION = "text-muted-foreground text-sm"
    HEADER = "flex flex-col"
    CONTENT = "flex flex-col"
    TRIGGER = ""
    CLOSE = "text-foreground"


class DialogBaseComponent(BaseUIComponent):
    """Base component for dialog components."""

    library = f"{PACKAGE_NAME}/dialog"

    @property
    def import_var(self):
        """Return the import variable for the dialog component."""
        return ImportVar(tag="Dialog", package_path="", install=False)


class DialogRoot(DialogBaseComponent):
    """Groups all parts of the dialog. Doesn't render its own HTML element."""

    tag = "Dialog.Root"

    # Whether the dialog is initially open. To render a controlled dialog, use the open prop instead.
    default_open: Var[bool]

    # Whether the dialog is currently open.
    open: Var[bool]

    # Event handler called when the dialog is opened or closed
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Determines whether the dialog should close on outside clicks. Defaults to True.
    dismissible: Var[bool]

    # Determines if the dialog enters a modal state when open.
    # - True: user interaction is limited to just the dialog: focus is trapped, document page scroll is locked, and pointer interactions on outside elements are disabled.
    # - False: user interaction with the rest of the document is allowed.
    # - 'trap-focus': focus is trapped inside the dialog, but document page scroll is not locked and pointer interactions outside of it remain enabled.
    modal: Var[bool | Literal["trap-focus"]]

    # Event handler called after any animations complete when the dialog is opened or closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog root component."""
        props["data-slot"] = "dialog"
        return super().create(*children, **props)


class DialogTrigger(DialogBaseComponent):
    """A button that opens the dialog. Renders a <button> element."""

    tag = "Dialog.Trigger"

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog trigger component."""
        props["data-slot"] = "dialog-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class DialogPortal(DialogBaseComponent):
    """A portal element that moves the popup to a different part of the DOM. By default, the portal element is appended to <body>."""

    tag = "Dialog.Portal"

    # A parent element to render the portal element into.
    container: Var[str]

    # Whether to keep the portal mounted in the DOM while the popup is hidden. Defaults to False.
    keep_mounted: Var[bool]


class DialogBackdrop(DialogBaseComponent):
    """An overlay displayed beneath the popup. Renders a <div> element."""

    tag = "Dialog.Backdrop"

    # Whether the backdrop is forced to render even when nested. Defaults to False.
    force_render: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog backdrop component."""
        props["data-slot"] = "dialog-backdrop"
        cls.set_class_name(ClassNames.BACKDROP, props)
        return super().create(*children, **props)


class DialogPopup(DialogBaseComponent):
    """A container for the dialog contents. Renders a <div> element."""

    tag = "Dialog.Popup"

    # Determines the element to focus when the dialog is opened. By default, the first focusable element is focused.
    initial_focus: Var[str]

    # Determines the element to focus when the dialog is closed. By default, focus returns to the trigger.
    final_focus: Var[str]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog popup component."""
        props["data-slot"] = "dialog-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class DialogTitle(DialogBaseComponent):
    """A heading that labels the dialog. Renders an <h2> element."""

    tag = "Dialog.Title"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog title component."""
        props["data-slot"] = "dialog-title"
        cls.set_class_name(ClassNames.TITLE, props)
        return super().create(*children, **props)


class DialogDescription(DialogBaseComponent):
    """A paragraph with additional information about the dialog. Renders a <p> element.."""

    tag = "Dialog.Description"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog description component."""
        props["data-slot"] = "dialog-description"
        cls.set_class_name(ClassNames.DESCRIPTION, props)
        return super().create(*children, **props)


class DialogClose(DialogBaseComponent):
    """A paragraph with additional information about the dialog. Renders a <p> element."""

    tag = "Dialog.Close"

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog close component."""
        props["data-slot"] = "dialog-close"
        cls.set_class_name(ClassNames.CLOSE, props)
        return super().create(*children, **props)


class HighLevelDialog(DialogRoot):
    """High level dialog component."""

    # Dialog props
    trigger: Var[Component | None]
    content: Var[str | Component | None]
    title: Var[str | Component | None]
    description: Var[str | Component | None]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the dialog component."""
        trigger = props.pop("trigger", None)
        content = props.pop("content", None)
        title = props.pop("title", None)
        description = props.pop("description", None)
        class_name = props.pop("class_name", "")

        return DialogRoot.create(
            DialogTrigger.create(render_=trigger) if trigger is not None else None,
            DialogPortal.create(
                DialogBackdrop.create(class_name="backdrop-blur-[5px]"),
                DialogPopup.create(
                    Div.create(
                        Div.create(
                            DialogTitle.create(title) if title is not None else None,
                            DialogClose.create(
                                render_=button(
                                    hi("Cancel01Icon"),
                                    variant="ghost",
                                    size="icon-sm",
                                    class_name=ClassNames.CLOSE,
                                ),
                            ),
                            class_name="flex flex-row justify-between items-baseline gap-1",
                        ),
                        (
                            DialogDescription.create(description)
                            if description is not None
                            else None
                        ),
                        data_slot="dialog-header",
                        class_name=ClassNames.HEADER,
                    ),
                    Div.create(
                        content,
                        data_slot="dialog-content",
                        class_name=ClassNames.CONTENT,
                    ),
                    *children,
                    class_name=class_name,
                ),
            ),
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "trigger",
            "content",
            "title",
            "description",
        ]


class Dialog(ComponentNamespace):
    """Namespace for Dialog components."""

    root = staticmethod(DialogRoot.create)
    trigger = staticmethod(DialogTrigger.create)
    portal = staticmethod(DialogPortal.create)
    backdrop = staticmethod(DialogBackdrop.create)
    popup = staticmethod(DialogPopup.create)
    title = staticmethod(DialogTitle.create)
    description = staticmethod(DialogDescription.create)
    close = staticmethod(DialogClose.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelDialog.create)


dialog = Dialog()
```


# Usage


```python
from components.ui.dialog import dialog
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


## High Level

Uses the simplified dialog() API with trigger, title, description, and content props for quick implementation.


```python
def dialog_high_level():
    return dialog(
        trigger=button("Open Dialog", variant="outline"),
        title="Are you absolutely sure?",
        description="This action cannot be undone. This will permanently delete your account and remove your data from our servers.",
        content=rx.flex(
            button("Cancel", variant="outline", class_name="flex-1"),
            button("Continue", class_name="flex-1"),
            class_name="flex gap-2 w-full",
        ),
        class_name="!w-full max-w-md",
    )
```


## Low Level

Uses the low-level dialog.root(), dialog.trigger(), dialog.portal() etc. for full control over structure and styling


```python
def dialog_low_level():
    return dialog.root(
        dialog.trigger(render_=button("Open Dialog")),
        dialog.portal(
            dialog.backdrop(class_name="backdrop-blur-[5px]"),
            dialog.popup(
                rx.el.div(
                    rx.el.div(
                        dialog.title("Edit Profile"),
                        dialog.close(
                            render_=button(
                                rx.icon("x", class_name="size-4"),
                                variant="ghost",
                                size="icon-sm",
                                class_name="text-secondary-11",
                            ),
                        ),
                        class_name="flex justify-between items-baseline gap-1",
                    ),
                    dialog.description(
                        "Make changes to your profile here. Click save when you're done."
                    ),
                    class_name="flex flex-col gap-2",
                ),
                # Content section
                rx.el.div(
                    rx.el.div(
                        rx.el.p("Name", class_name="text-sm font-medium mb-2"),
                        input(placeholder="Enter your name"),
                    ),
                    rx.el.div(
                        rx.el.p("Email", class_name="text-sm font-medium mb-2"),
                        input(placeholder="Enter your email", type="email"),
                    ),
                    rx.el.div(
                        dialog.close(
                            render_=button(
                                "Cancel", variant="outline", class_name="flex-1"
                            ),
                        ),
                        button("Save Changes", class_name="flex-1"),
                        class_name="flex gap-2 w-full",
                    ),
                    class_name="flex flex-col gap-4",
                ),
                class_name="!w-full max-w-lg",
            ),
        ),
    )
```

