"""Bubble component — chat message bubble with variants, content, and reactions slots."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..utils.twmerge import cn

BubbleVariant = Literal[
    "default", "secondary", "muted", "tinted", "outline", "ghost", "destructive"
]
BubbleAlign = Literal["start", "end"]
BubbleSide = Literal["top", "bottom"]


class ClassNames:
    GROUP = "flex min-w-0 flex-col gap-2"

    VARIANTS: dict[str, str] = {
        "default": (
            "*:data-[slot=bubble-content]:bg-primary "
            "*:data-[slot=bubble-content]:text-primary-foreground"
        ),
        "secondary": (
            "*:data-[slot=bubble-content]:bg-secondary "
            "*:data-[slot=bubble-content]:text-secondary-foreground"
        ),
        "muted": ("*:data-[slot=bubble-content]:bg-muted"),
        "tinted": (
            "*:data-[slot=bubble-content]:bg-[oklch(from_var(--primary)_0.93_calc(c*0.4)_h)] "
            "*:data-[slot=bubble-content]:text-foreground "
            "dark:*:data-[slot=bubble-content]:bg-[oklch(from_var(--primary)_0.3_calc(c*0.4)_h)]"
        ),
        "outline": (
            "*:data-[slot=bubble-content]:border-border "
            "*:data-[slot=bubble-content]:bg-background"
        ),
        "ghost": (
            "border-none "
            "*:data-[slot=bubble-content]:rounded-none "
            "*:data-[slot=bubble-content]:bg-transparent "
            "*:data-[slot=bubble-content]:p-0"
        ),
        "destructive": (
            "*:data-[slot=bubble-content]:bg-destructive/10 "
            "*:data-[slot=bubble-content]:text-destructive "
            "dark:*:data-[slot=bubble-content]:bg-destructive/20"
        ),
    }

    ROOT = (
        "group/bubble relative flex w-fit max-w-[80%] min-w-0 flex-col gap-1 "
        "group-data-[align=end]/message:self-end "
        "data-[align=end]:self-end "
        "data-[variant=ghost]:max-w-full"
    )

    CONTENT = (
        "w-fit max-w-full min-w-0 overflow-hidden rounded-3xl border border-transparent "
        "px-3 py-2.5 text-sm leading-relaxed break-words "
        "group-data-[align=end]/bubble:self-end"
    )

    REACTIONS_BASE = (
        "absolute z-10 flex w-fit shrink-0 items-center justify-center gap-1 "
        "rounded-full bg-muted px-1.5 py-0.5 text-sm ring-3 ring-card has-[button]:p-0"
    )

    REACTIONS_SIDE: dict[str, str] = {
        "top": "top-0 -translate-y-3/4",
        "bottom": "bottom-0 translate-y-3/4",
    }

    REACTIONS_ALIGN: dict[str, str] = {
        "start": "left-3",
        "end": "right-3",
    }


def bubble_group(*children, class_name: str = "", **props) -> rx.Component:
    """Vertical stack of bubbles."""
    return rx.el.div(
        *children,
        data_slot="bubble-group",
        class_name=cn(ClassNames.GROUP, class_name),
        **props,
    )


def bubble_root(
    *children,
    variant: BubbleVariant = "default",
    align: BubbleAlign = "start",
    class_name: str = "",
    **props,
) -> rx.Component:
    """
    Bubble root container.

    Variants: default, secondary, muted, tinted, outline, ghost, destructive
    Align:    start (incoming), end (outgoing)
    """
    return rx.el.div(
        *children,
        data_slot="bubble",
        data_variant=variant,
        data_align=align,
        class_name=cn(
            ClassNames.ROOT,
            ClassNames.VARIANTS.get(variant, ""),
            class_name,
        ),
        **props,
    )


def bubble_content(*children, class_name: str = "", **props) -> rx.Component:
    """The bubble content pill — rounded, padded, colored by the parent variant."""
    return rx.el.div(
        *children,
        data_slot="bubble-content",
        class_name=cn(ClassNames.CONTENT, class_name),
        **props,
    )


def bubble_reactions(
    *children,
    side: BubbleSide = "bottom",
    align: BubbleAlign = "end",
    class_name: str = "",
    **props,
) -> rx.Component:
    """
    Emoji reactions overlay — positioned relative to the bubble.

    Side:  top | bottom (default: bottom)
    Align: start | end  (default: end)
    """
    return rx.el.div(
        *children,
        data_slot="bubble-reactions",
        data_align=align,
        data_side=side,
        class_name=cn(
            ClassNames.REACTIONS_BASE,
            ClassNames.REACTIONS_SIDE.get(side, ""),
            ClassNames.REACTIONS_ALIGN.get(align, ""),
            class_name,
        ),
        **props,
    )


class Bubble(ComponentNamespace):
    """Bubble namespace."""

    group = staticmethod(bubble_group)
    root = staticmethod(bubble_root)
    content = staticmethod(bubble_content)
    reactions = staticmethod(bubble_reactions)

    class_names = ClassNames


bubble = Bubble()
