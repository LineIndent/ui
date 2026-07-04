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
        "h-1 w-full rounded-lg bg-secondary select-none "
        "data-[orientation=vertical]:h-full "
        "data-[orientation=vertical]:w-1"
    )

    INDICATOR = (
        "absolute h-full rounded-lg bg-primary select-none "
        "data-[orientation=vertical]:w-full "
        "data-[orientation=vertical]:h-auto"
    )

    THUMB = (
        "size-3 rounded-lg bg-white outline-[1px] outline-black "
        "select-none box-shadow:[0_0_0_1px_rgba(0,0,0,1),0_1px_2px_rgba(0,0,0,.04)] "
        "data-[dragging]:h-5 transition-[height,scale] hover:h-4.5"
    )


class SliderBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/slider"

    @property
    def import_var(self):
        return ImportVar(tag="Slider", package_path="", install=False)


class SliderRoot(SliderBaseComponent):
    tag = "Slider.Root"

    name: Var[str]

    default_value: Var[int | float | list[int | float]]

    value: Var[int | float | list[int | float]]

    on_value_change: EventHandler[on_value_event_spec]

    on_value_committed: EventHandler[on_value_event_spec]

    locale: Var[str]

    step: Var[float | int]

    large_step: Var[float | int]

    min_steps_between_values: Var[float | int]

    min: Var[float | int]

    max: Var[float | int]

    format: Var[dict]

    disabled: Var[bool]

    orientation: Var[LiteralOrientation]

    input_ref: Var[str]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "slider"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class SliderValue(SliderBaseComponent):
    tag = "Slider.Value"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "slider-value"
        cls.set_class_name(ClassNames.VALUE, props)
        return super().create(*children, **props)


class SliderControl(SliderBaseComponent):
    tag = "Slider.Control"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "slider-control"
        cls.set_class_name(ClassNames.CONTROL, props)
        return super().create(*children, **props)


class SliderTrack(SliderBaseComponent):
    tag = "Slider.Track"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "slider-track"
        cls.set_class_name(ClassNames.TRACK, props)
        return super().create(*children, **props)


class SliderIndicator(SliderBaseComponent):
    tag = "Slider.Indicator"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "slider-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class SliderThumb(SliderBaseComponent):
    tag = "Slider.Thumb"

    get_aria_label: Var[str]

    get_aria_value_text: Var[str]

    disabled: Var[bool]

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "slider-thumb"
        cls.set_class_name(ClassNames.THUMB, props)
        return super().create(*children, **props)


class Slider(ComponentNamespace):
    root = staticmethod(SliderRoot.create)
    value = staticmethod(SliderValue.create)
    control = staticmethod(SliderControl.create)
    track = staticmethod(SliderTrack.create)
    indicator = staticmethod(SliderIndicator.create)
    thumb = staticmethod(SliderThumb.create)
    class_names = ClassNames


slider = Slider()
