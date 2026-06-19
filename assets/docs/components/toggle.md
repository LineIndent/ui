

# Toggle

A two-state button that can be either on or off.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component toggle
```

### Manual Installation

```python
"""Custom toggle component."""

from reflex.components.component import Component
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    """Class names for toggle components."""

    ROOT = "group/toggle p-1 inline-flex items-center justify-center gap-1 rounded-radius border border-input text-sm font-medium whitespace-nowrap transition-all hover:bg-muted hover:text-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 aria-pressed:bg-muted data-[state=on]:bg-muted dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"

    ICON_VARIANT_CLASSES = {
        "fill": "data-[pressed]:[&_svg]:fill-primary",
        "stroke": "data-[pressed]:[&_svg]:text-primary",
        None: "",
    }


class ToggleBaseComponent(BaseUIComponent):
    """Base component for toggle components."""

    library = f"{PACKAGE_NAME}/toggle"

    @property
    def import_var(self):
        """Return the import variable for the toggle component."""
        return ImportVar(tag="Toggle", package_path="", install=False)


class Toggle(ToggleBaseComponent):
    """A two-state button that can be on or off. Renders a <button> element."""

    tag = "Toggle"

    # A unique string that identifies the toggle when used inside a toggle group.
    value: Var[str]

    # Whether the toggle button is currently pressed. This is the uncontrolled counterpart of pressed. Defaults to False.
    default_pressed: Var[bool]

    # Whether the toggle button is currently pressed. This is the controlled counterpart of default_pressed.
    pressed: Var[bool]

    # Callback fired when the pressed state is changed.
    on_pressed_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    #
    icon_variant: Var[str | None]  # "fill" | "stroke" | None

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the toggle component."""
        props["data-slot"] = "toggle"
        cls.set_class_name(
            cn(
                ClassNames.ROOT,
                ClassNames.ICON_VARIANT_CLASSES.get(props.get("icon_variant")),
            ),
            props,
        )
        return super().create(*children, **props)


toggle = Toggle.create
```


# Usage


```python
from components.ui.toggle import toggle
```


# Anatomy 
Use the following composition to build a `Toggle`


```python
toggle()
```



# Examples

## Icon Toggle Variants
Use `toggle()` for a pressable on/off control. Control icon behavior with `icon_variant="fill"` to fill icons on press, or omit it and style manually using `data-[pressed] selectors` (e.g. text-* or fill-*).


```python
def toggle_general():
    return rx.el.div(
        toggle(
            hi(
                "Bookmark02Icon",
                class_name="size-4",
            ),
            "Bookmark",
            icon_variant="fill",
        ),
        toggle(
            hi("TextUnderlineIcon", class_name="size-4"),
            "Underline",
        ),
        class_name="flex flex-row gap-x-2 items-center justify-center",
    )
```


## Pressed State
Use `default_pressed=True` to set the default pressed state of a toggle.


```python
def toggle_pressed_state():
    return toggle(hi("TextItalicIcon", class_name="size-4"), default_pressed=True)
```


## Disabled
Set `disabled=True` to disable a toggle.


```python
def toggle_disabled():
    return toggle(hi("TextUnderlineIcon", class_name="size-4"), disabled=True)
```

