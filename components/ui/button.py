from typing import Literal

from reflex.vars.base import Var
from reflex_components_core.el import Button as BaseButton

from ..utils.twmerge import cn
from .component import CoreComponent

LiteralButtonVariant = Literal[
    "default",
    "destructive",
    "outline",
    "secondary",
    "ghost",
    "link",
]
LiteralButtonSize = Literal[
    "default",
    "xs",
    "sm",
    "lg",
    "icon",
    "icon-xs",
    "icon-sm",
    "icon-lg",
]

DEFAULT_CLASS_NAME = (
    "group/button inline-flex shrink-0 items-center justify-center "
    "rounded-lg border border-transparent bg-clip-padding "
    "text-sm font-medium whitespace-nowrap transition-all outline-none select-none "
    "focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 "
    "active:not-aria-[haspopup]:translate-y-px "
    "disabled:pointer-events-none disabled:opacity-50 "
    "aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 "
    "dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 "
    "[&_svg]:pointer-events-none [&_svg]:shrink-0 "
    "[&_svg:not([class*='size-'])]:size-4"
)

BUTTON_VARIANTS = {
    "variant": {
        "default": ("bg-primary text-primary-foreground hover:bg-primary/80"),
        "outline": (
            "border-border bg-background hover:bg-muted hover:text-foreground "
            "aria-expanded:bg-muted aria-expanded:text-foreground "
            "dark:border-input dark:bg-input/30 dark:hover:bg-input/50"
        ),
        "secondary": (
            "bg-secondary text-secondary-foreground "
            "hover:bg-[color-mix(in_oklch,var(--secondary),var(--foreground)_5%)] "
            "aria-expanded:bg-secondary aria-expanded:text-secondary-foreground"
        ),
        "ghost": (
            "hover:bg-muted hover:text-foreground "
            "aria-expanded:bg-muted aria-expanded:text-foreground "
            "dark:hover:bg-muted/50"
        ),
        "destructive": (
            "bg-destructive/10 text-destructive hover:bg-destructive/20 "
            "focus-visible:border-destructive/40 focus-visible:ring-destructive/20 "
            "dark:bg-destructive/20 dark:hover:bg-destructive/30 "
            "dark:focus-visible:ring-destructive/40"
        ),
        "link": "text-primary underline-offset-4 hover:underline",
    },
    "size": {
        "default": (
            "h-8 gap-1.5 px-2.5 "
            "has-data-[icon=inline-end]:pr-2 "
            "has-data-[icon=inline-start]:pl-2"
        ),
        "xs": (
            "h-6 gap-1 rounded-[min(var(--radius-md),10px)] px-2 text-xs "
            "in-data-[slot=button-group]:rounded-lg "
            "has-data-[icon=inline-end]:pr-1.5 has-data-[icon=inline-start]:pl-1.5 "
            "[&_svg:not([class*='size-'])]:size-3"
        ),
        "sm": (
            "h-7 gap-1 rounded-[min(var(--radius-md),12px)] px-2.5 text-[0.8rem] "
            "in-data-[slot=button-group]:rounded-lg "
            "has-data-[icon=inline-end]:pr-1.5 has-data-[icon=inline-start]:pl-1.5 "
            "[&_svg:not([class*='size-'])]:size-3.5"
        ),
        "lg": (
            "h-9 gap-1.5 px-2.5 "
            "has-data-[icon=inline-end]:pr-2 "
            "has-data-[icon=inline-start]:pl-2"
        ),
        "icon": "size-8",
        "icon-xs": (
            "size-6 rounded-[min(var(--radius-md),10px)] "
            "in-data-[slot=button-group]:rounded-lg "
            "[&_svg:not([class*='size-'])]:size-3"
        ),
        "icon-sm": (
            "size-7 rounded-[min(var(--radius-md),12px)] "
            "in-data-[slot=button-group]:rounded-lg"
        ),
        "icon-lg": "size-9",
    },
}


class Button(BaseButton, CoreComponent):
    variant: Var[LiteralButtonVariant]
    size: Var[LiteralButtonSize]

    @classmethod
    def create(cls, *children, **props) -> BaseButton:
        variant = props.pop("variant", "default")
        size = props.pop("size", "default")
        custom_classes = props.pop("class_name", "")

        return super().create(
            *children,
            data_slot="button",
            class_name=cn(
                DEFAULT_CLASS_NAME,
                BUTTON_VARIANTS["variant"].get(variant, ""),
                BUTTON_VARIANTS["size"].get(size, ""),
                custom_classes,
            ),
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [*super()._exclude_props(), "size", "variant"]


def button_variants(variant: str = "default", size: str = "default") -> Var:
    return cn(
        DEFAULT_CLASS_NAME,
        BUTTON_VARIANTS["variant"].get(variant, ""),
        BUTTON_VARIANTS["size"].get(size, ""),
    )


button = Button.create
