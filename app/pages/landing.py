import reflex as rx

from app.examples.components import (
    card_five,
    card_four,
    card_fourteen,
    card_nine,
    card_nineteen,
    card_one,
    card_seven,
    card_seventeen,
    card_six,
    card_sixteen,
    card_ten,
    card_thirteen,
    card_three,
)
from app.templates.layout import layout_decorator
from components.icons.hugeicon import hi
from components.ui.button import button


@layout_decorator(
    title="The UI Library for Reflex Developers",
    description="Buridan UI gives you composable, themeable components designed for Reflex. Extend, override, and ship without fighting the framework.",
    ctas=[
        rx.el.a(
            button("Build Your Own", hi("ArrowRight02Icon", class_name="size-4")),
            href="/create",
        )
    ],
)
def landing_page():

    landing_desktop = rx.el.div(
        card_five(),
        card_four(),
        card_fourteen(),
        card_nine(),
        card_nineteen(),
        card_one(),
        card_seven(),
        card_seventeen(),
        card_six(),
        card_sixteen(),
        card_ten(),
        card_thirteen(),
        card_three(),
        class_name=" ".join(
            [
                # -> main layout style
                "max-w-[96rem]",
                "mx-auto",
                "columns-[320px]",
                "px-7",
                "gap-6",
                "space-y-6",
                # -> access inner card children to modify CSS tokens
                "[&>*]:p-5",
                "[&>*]:shadow-md",
                "[&>*]:rounded-[2rem]",
                "[&>div>div]:gap-y-4",
                "[&_button]:!rounded-[2rem]",
                "[&_input]:!rounded-[2rem] [&_div]:!rounded-[2rem]",
                # -> create masking fade-away at the bottom of the component
                "sm:mask-[linear-gradient(to_bottom,black_65%,transparent_100%)]",
                "sm:mask-size-[100%_100%]",
                "sm:mask-repeat-no-repeat",
            ]
        ),
    )

    landing_mobile = rx.el.div(
        rx.color_mode_cond(
            rx.el.image(
                src="/landing_preview.webp",
                class_name="w-[1450px] max-w-none",
            ),
            rx.el.image(
                src="/landing_preview_dark.webp",
                class_name="w-[1450px] max-w-none",
            ),
        ),
        class_name="overflow-hidden w-full flex justify-center",
    )

    return rx.el.div(
        rx.el.div(landing_mobile, class_name="flex sm:hidden w-full"),
        rx.el.div(landing_desktop, class_name="hidden sm:block w-full"),
    )
