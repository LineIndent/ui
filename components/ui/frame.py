"""Custom Frame component."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..utils.twmerge import cn

LiteralVariant = Literal["default", "inverse", "ghost"]
LiteralSpacing = Literal["xs", "sm", "default", "lg"]


class ClassNames:
    ROOT = "relative flex flex-col bg-muted/50 gap-0.75 p-0.75 rounded-xl"
    ROOT_VARIANT_DEFAULT = "border border-border bg-clip-padding"
    ROOT_VARIANT_INVERSE = "border border-border bg-background bg-clip-padding"
    ROOT_VARIANT_GHOST = ""
    PANEL = "relative grow overflow-hidden rounded-xl border border-border bg-card bg-clip-padding shadow-xs p-(--frame-panel-p)"
    HEADER = "flex flex-col px-(--frame-panel-header-px) py-(--frame-panel-header-py)"
    TITLE = "text-sm font-semibold"
    DESCRIPTION = "text-muted-foreground text-sm"
    FOOTER = (
        "flex flex-col gap-1 px-(--frame-panel-footer-px) py-(--frame-panel-footer-py)"
    )


VARIANT_CLASSES: dict[str, str] = {
    "default": ClassNames.ROOT_VARIANT_DEFAULT,
    "inverse": ClassNames.ROOT_VARIANT_INVERSE,
    "ghost": ClassNames.ROOT_VARIANT_GHOST,
}

SPACING_CLASSES: dict[str, str] = {
    "xs": "[--frame-panel-p:--spacing(2)] [--frame-panel-header-px:--spacing(2)] [--frame-panel-header-py:--spacing(1)] [--frame-panel-footer-px:--spacing(2)] [--frame-panel-footer-py:--spacing(1)]",
    "sm": "[--frame-panel-p:--spacing(3)] [--frame-panel-header-px:--spacing(3)] [--frame-panel-header-py:--spacing(2)] [--frame-panel-footer-px:--spacing(3)] [--frame-panel-footer-py:--spacing(2)]",
    "default": "[--frame-panel-p:--spacing(4)] [--frame-panel-header-px:--spacing(4)] [--frame-panel-header-py:--spacing(3)] [--frame-panel-footer-px:--spacing(4)] [--frame-panel-footer-py:--spacing(3)]",
    "lg": "[--frame-panel-p:--spacing(5)] [--frame-panel-header-px:--spacing(5)] [--frame-panel-header-py:--spacing(4)] [--frame-panel-footer-px:--spacing(5)] [--frame-panel-footer-py:--spacing(4)]",
}


def frame_root(
    *children,
    variant: LiteralVariant = "default",
    spacing: LiteralSpacing = "default",
    stacked: bool = False,
    dense: bool = False,
    class_name: str = "",
    **props,
) -> rx.Component:
    stacked_class = (
        "gap-0 *:has-[+[data-slot=frame-panel]]:rounded-b-none *:[[data-slot=frame-panel]+[data-slot=frame-panel]]:rounded-t-none *:[[data-slot=frame-panel]+[data-slot=frame-panel]]:border-t-0"
        if stacked
        else ""
    )

    dense_class = (
        "p-0 gap-0 [&_[data-slot=frame-panel]]:-mx-px [&_[data-slot=frame-panel]]:before:hidden [&_[data-slot=frame-panel]:last-child]:-mb-px"
        if dense
        else ""
    )

    return rx.el.div(
        *children,
        class_name=cn(
            ClassNames.ROOT,
            VARIANT_CLASSES.get(variant, ""),
            SPACING_CLASSES.get(spacing, ""),
            stacked_class,
            dense_class,
            class_name,
        ),
        data_slot="frame",
        data_spacing=spacing,
        **props,
    )


def frame_panel(*children, class_name: str = "", **props) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.PANEL, class_name),
        data_slot="frame-panel",
        **props,
    )


def frame_header(*children, class_name: str = "", **props) -> rx.Component:
    return rx.el.header(
        *children,
        class_name=cn(ClassNames.HEADER, class_name),
        data_slot="frame-panel-header",
        **props,
    )


def frame_title(*children, class_name: str = "", **props) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.TITLE, class_name),
        data_slot="frame-panel-title",
        **props,
    )


def frame_description(*children, class_name: str = "", **props) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.DESCRIPTION, class_name),
        data_slot="frame-panel-description",
        **props,
    )


def frame_footer(*children, class_name: str = "", **props) -> rx.Component:
    return rx.el.footer(
        *children,
        class_name=cn(ClassNames.FOOTER, class_name),
        data_slot="frame-panel-footer",
        **props,
    )


class Frame(ComponentNamespace):
    """Namespace for Frame components."""

    root = staticmethod(frame_root)
    panel = staticmethod(frame_panel)
    header = staticmethod(frame_header)
    title = staticmethod(frame_title)
    description = staticmethod(frame_description)
    footer = staticmethod(frame_footer)
    __call__ = staticmethod(frame_root)


frame = Frame()
