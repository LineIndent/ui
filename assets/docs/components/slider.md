

# Slider

An input where the user selects a value from within a given range.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component slider
```

### Manual Installation

```python
"""Custom Slider component."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]

on_value_event_spec = (
    passthrough_event_spec(int),
    passthrough_event_spec(float),
    passthrough_event_spec(list[int | float]),
    passthrough_event_spec(list[int]),
    passthrough_event_spec(list[float]),
)


class ClassNames:
    """Class names for slider components."""

    VALUE = "text-sm text-primary-11 font-medium"

    ROOT = (
        "flex max-w-64 w-full touch-none items-center select-none "
        "data-[orientation=vertical]:h-64 data-[orientation=vertical]:w-auto "
        "data-[orientation=vertical]:flex-col"
    )

    CONTROL = (
        "flex items-center justify-center w-full "
        "data-[orientation=vertical]:flex-col "
        "data-[orientation=vertical]:h-full"
    )

    TRACK = (
        "h-1 w-full rounded-radius bg-secondary select-none "
        "data-[orientation=vertical]:h-full "
        "data-[orientation=vertical]:w-1"
    )

    INDICATOR = (
        "absolute h-full rounded-radius bg-primary select-none "
        "data-[orientation=vertical]:w-full "
        "data-[orientation=vertical]:h-auto"
    )

    THUMB = (
        "size-3 rounded-radius bg-white outline-[1px] outline-black "
        "select-none box-shadow:[0_0_0_1px_rgba(0,0,0,1),0_1px_2px_rgba(0,0,0,.04)] "
        "data-[dragging]:h-5 transition-[height,scale] hover:h-4.5"
    )


class SliderBaseComponent(BaseUIComponent):
    """Base component for slider components."""

    library = f"{PACKAGE_NAME}/slider"

    @property
    def import_var(self):
        """Return the import variable for the slider component."""
        return ImportVar(tag="Slider", package_path="", install=False)


class SliderRoot(SliderBaseComponent):
    """Groups all parts of the slider. Renders a div element."""

    tag = "Slider.Root"

    # Identifies the field when a form is submitted.
    name: Var[str]

    # The uncontrolled value of the slider when it's initially rendered. To render a controlled slider, use the value prop instead.
    default_value: Var[int | float | list[int | float]]

    # The value of the slider. For ranged sliders, provide an array with two values.
    value: Var[int | float | list[int | float]]

    # Callback function that is fired when the slider's value changed.
    on_value_change: EventHandler[on_value_event_spec]

    # Callback function that is fired when the pointerup is triggered.
    on_value_committed: EventHandler[on_value_event_spec]

    # Locale information for formatting.
    locale: Var[str]

    # The granularity with which the slider can step through values. (A "discrete" slider.) The min prop serves as the origin for the valid values. We recommend (max - min) to be evenly divisible by the step. Defaults to 1.
    step: Var[float | int]

    # The granularity with which the slider can step through values when using Page Up/Page Down or Shift + Arrow Up/Arrow Down. Defaults to 10.
    large_step: Var[float | int]

    # The minimum steps between values in a range slider. Defaults to 0.
    min_steps_between_values: Var[float | int]

    # The minimum allowed value of the slider. Should not be equal to max. Defaults to 0.
    min: Var[float | int]

    # The maximum allowed value of the slider. Should not be equal to min. Defaults to 100.
    max: Var[float | int]

    # Options to format the input value.
    format: Var[dict]

    # Whether the slider is disabled.
    disabled: Var[bool]

    # The component orientation. Defaults to "horizontal".
    orientation: Var[LiteralOrientation]

    # A ref to access the hidden input element.
    input_ref: Var[str]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the slider root component."""
        props["data-slot"] = "slider"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class SliderValue(SliderBaseComponent):
    """Displays the current value of the slider as text. Renders an output element."""

    tag = "Slider.Value"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the slider value component."""
        props["data-slot"] = "slider-value"
        cls.set_class_name(ClassNames.VALUE, props)
        return super().create(*children, **props)


class SliderControl(SliderBaseComponent):
    """The clickable, interactive part of the slider. Renders a div element."""

    tag = "Slider.Control"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the slider control component."""
        props["data-slot"] = "slider-control"
        cls.set_class_name(ClassNames.CONTROL, props)
        return super().create(*children, **props)


class SliderTrack(SliderBaseComponent):
    """Contains the slider indicator and represents the entire range of the slider. Renders a div element."""

    tag = "Slider.Track"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the slider track component."""
        props["data-slot"] = "slider-track"
        cls.set_class_name(ClassNames.TRACK, props)
        return super().create(*children, **props)


class SliderIndicator(SliderBaseComponent):
    """Visualizes the current value of the slider. Renders a div element."""

    tag = "Slider.Indicator"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the slider indicator component."""
        props["data-slot"] = "slider-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class SliderThumb(SliderBaseComponent):
    """The draggable part of the slider at the tip of the indicator. Renders a div element."""

    tag = "Slider.Thumb"

    # Accepts a function which returns a string value that provides a user-friendly name for the input associated with the thumb.
    get_aria_label: Var[str]

    # Accepts a function which returns a string value that provides a user-friendly name for the current value of the slider. This is important for screen reader users.
    get_aria_value_text: Var[str]

    # Whether the thumb should ignore user interaction.
    disabled: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the slider thumb component."""
        props["data-slot"] = "slider-thumb"
        cls.set_class_name(ClassNames.THUMB, props)
        return super().create(*children, **props)


class HighLevelSlider(SliderRoot):
    """High-level wrapper for the Slider component."""

    @classmethod
    def create(cls, **props) -> BaseUIComponent:
        """Create a complete slider component.

        Args:
            **props: Additional properties to apply to the slider component.

        Returns:
            The slider component.
        """
        return SliderRoot.create(
            SliderControl.create(
                SliderTrack.create(
                    SliderIndicator.create(),
                    SliderThumb.create(),
                ),
            ),
            **props,
        )


class Slider(ComponentNamespace):
    """Namespace for Slider components."""

    root = staticmethod(SliderRoot.create)
    value = staticmethod(SliderValue.create)
    control = staticmethod(SliderControl.create)
    track = staticmethod(SliderTrack.create)
    indicator = staticmethod(SliderIndicator.create)
    thumb = staticmethod(SliderThumb.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelSlider.create)


slider = Slider()
```


# Usage


```python
from components.ui.slider import slider
```


# Anatomy 
Use the following composition to build a `Slider`


```python
slider.root(
    slider.control(
        slider.track(
            slider.indicator(),
            slider.thumb(),
        ),
    ),
)
```



# Examples

## Basic
A basic low-level slider demo.

```python
def slider_demo():
    return rx.el.div(
        slider.root(
            slider.control(slider.track(slider.indicator(), slider.thumb())),
            default_value=20,
        ),
        class_name="w-full max-w-md flex justify-center",
    )
```


## Range
Use an array with two values for a range slider.

```python
def slider_range():
    return rx.el.div(
        slider.root(
            slider.control(
                slider.track(
                    slider.indicator(),
                    slider.thumb(),
                    slider.thumb(),
                ),
            ),
            default_value=[25, 50],
            max=100,
            step=5,
        ),
        class_name="w-full max-w-xs mx-auto flex justify-center",
    )
```


## Vertical
Use `orientation="vertical"` for a vertical slider.

```python
def slider_vertical():
    return rx.el.div(
        slider.root(
            slider.control(
                slider.track(slider.indicator(), slider.thumb()),
            ),
            default_value=[50],
            max=100,
            step=1,
            orientation="vertical",
            class_name="h-40",
        ),
        slider.root(
            slider.control(
                slider.track(slider.indicator(), slider.thumb()),
            ),
            default_value=[25],
            max=100,
            step=1,
            orientation="vertical",
            class_name="h-40",
        ),
        class_name="h-full mx-auto flex w-full max-w-xs items-center justify-center gap-6",
    )
```

