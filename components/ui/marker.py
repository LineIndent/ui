"""Marker component — a flexible inline label with icon and content slots."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..utils.twmerge import cn

MarkerVariant = Literal["default", "separator", "border"]


class ClassNames:
    ROOT = (
        "group/marker relative flex min-h-4 w-full items-center gap-2 "
        "text-left text-sm text-muted-foreground"
    )

    VARIANTS: dict[str, str] = {
        "default": "",
        "separator": (
            "before:mr-1 before:h-px before:min-w-0 before:flex-1 before:bg-border "
            "after:ml-1 after:h-px after:min-w-0 after:flex-1 after:bg-border"
        ),
        "border": "border-b border-border pb-2",
    }

    ICON = "size-4 shrink-0"
    CONTENT = (
        "min-w-0 break-words "
        "group-data-[variant=separator]/marker:flex-none "
        "group-data-[variant=separator]/marker:text-center"
    )


def marker_root(
    *children,
    variant: MarkerVariant = "default",
    class_name: str = "",
    **props,
) -> rx.Component:
    """Root marker container."""
    return rx.el.div(
        *children,
        data_slot="marker",
        data_variant=variant,
        class_name=cn(
            ClassNames.ROOT,
            ClassNames.VARIANTS.get(variant, ""),
            class_name,
        ),
        **props,
    )


def marker_icon(*children, class_name: str = "", **props) -> rx.Component:
    """Icon slot — wraps any icon at a fixed size-4."""
    return rx.el.span(
        *children,
        data_slot="marker-icon",
        aria_hidden="true",
        class_name=cn(ClassNames.ICON, class_name),
        **props,
    )


def marker_content(*children, class_name: str = "", **props) -> rx.Component:
    """Content slot — handles text wrapping and separator alignment."""
    return rx.el.span(
        *children,
        data_slot="marker-content",
        class_name=cn(ClassNames.CONTENT, class_name),
        **props,
    )


class Marker(ComponentNamespace):
    """Marker namespace."""

    root = staticmethod(marker_root)
    icon = staticmethod(marker_icon)
    content = staticmethod(marker_content)

    class_names = ClassNames


marker = Marker()
