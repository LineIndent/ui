import reflex as rx

from components.ui.slider import slider


def slider_demo():
    return rx.el.div(
        slider.root(
            slider.control(slider.track(slider.indicator(), slider.thumb())),
            default_value=20,
        ),
        class_name="w-full max-w-md flex justify-center",
    )
