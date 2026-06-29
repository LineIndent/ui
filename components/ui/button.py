from typing import Literal

from reflex.vars.base import Var
from reflex_components_core.core import cond
from reflex_components_core.el import Button as BaseButton

from ..icons.others import spinner
from .component import CoreComponent

LiteralButtonVariant = Literal[
    "primary", "destructive", "outline", "secondary", "ghost", "link", "dark"
]
LiteralButtonSize = Literal[
    "default", "xs", "sm", "lg", "icon", "icon-xs", "icon-sm", "icon-lg"
]

DEFAULT_CLASS_NAME = (
    "font-theme inline-flex items-center justify-center gap-2 whitespace-nowrap "
    "rounded-radius text-sm font-medium transition-all "
    "disabled:pointer-events-none disabled:opacity-50 outline-none "
    "[&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 "
    "[&_svg]:shrink-0 shrink-0"
)

BUTTON_VARIANTS = {
    "variant": {
        "default": "bg-primary text-primary-foreground hover:bg-primary/90",
        "destructive": (
            "bg-destructive/10 text-destructive hover:bg-destructive/20 "
            "focus-visible:border-destructive/40 focus-visible:ring-destructive/20 "
            "dark:bg-destructive/20 dark:hover:bg-destructive/30"
        ),
        "outline": (
            "border border-input bg-background shadow-xs text-foreground "
            "hover:bg-accent hover:text-accent-foreground "
            "dark:bg-input/30 dark:hover:bg-input/50"
        ),
        "secondary": "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        "ghost": "hover:bg-accent hover:text-accent-foreground dark:hover:bg-muted/50",
        "link": "text-primary underline-offset-4 hover:underline",
    },
    "size": {
        "default": "h-8 gap-1.5 px-2.5 has-[>svg]:px-2.5",
        "xs": "h-6 rounded-[min(calc(var(--radius) * 0.8),10px)] gap-1 px-2 text-xs",
        "sm": "h-7 rounded-[min(calc(var(--radius) * 0.8),12px)] gap-1 px-2.5 text-[0.8rem]",
        "lg": "h-9 gap-1.5 px-2.5",
        "icon": "size-8",
        "icon-xs": "size-6 rounded-[min(calc(var(--radius) * 0.8),10px)]",
        "icon-sm": "size-7 rounded-[min(calc(var(--radius) * 0.8),12px)]",
        "icon-lg": "size-9",
    },
}


class Button(BaseButton, CoreComponent):
    """A custom button component."""

    # Button variant. Defaults to "primary".
    variant: Var[LiteralButtonVariant]

    # Button size. Defaults to "md".
    size: Var[LiteralButtonSize]

    # The loading state of the button
    loading: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseButton:
        """Create the button component."""
        variant = props.pop("variant", "default")
        cls.validate_variant(variant)

        size = props.pop("size", "default")
        cls.validate_size(size)

        loading = props.pop("loading", False)
        disabled = props.pop("disabled", False)

        button_classes = f"{DEFAULT_CLASS_NAME} {BUTTON_VARIANTS['variant'][variant]} {BUTTON_VARIANTS['size'][size]}"

        cls.set_class_name(button_classes, props)

        children_list = list(children)

        if isinstance(loading, Var):
            props["disabled"] = cond(loading, True, disabled)
            children_list.insert(0, cond(loading, spinner()))
        else:
            props["disabled"] = True if loading else disabled
            children_list.insert(0, spinner()) if loading else None

        return super().create(*children_list, **props)

    @staticmethod
    def validate_variant(variant: LiteralButtonVariant):
        """Validate the button variant."""
        if variant not in BUTTON_VARIANTS["variant"]:
            available_variants = ", ".join(BUTTON_VARIANTS["variant"].keys())
            message = (
                f"Invalid variant: {variant}. Available variants: {available_variants}"
            )
            raise ValueError(message)

    @staticmethod
    def validate_size(size: LiteralButtonSize):
        """Validate the button size."""
        if size not in BUTTON_VARIANTS["size"]:
            available_sizes = ", ".join(BUTTON_VARIANTS["size"].keys())
            message = f"Invalid size: {size}. Available sizes: {available_sizes}"
            raise ValueError(message)

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "size",
            "variant",
            "loading",
        ]


button = Button.create
