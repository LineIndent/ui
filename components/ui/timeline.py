"""Custom Timeline component."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..utils.twmerge import cn

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    ROOT = "group/timeline flex data-[orientation=horizontal]:w-full data-[orientation=horizontal]:flex-row data-[orientation=vertical]:flex-col"
    ITEM = "group/timeline-item relative flex flex-1 flex-col gap-0.5 group-data-[orientation=vertical]/timeline:ms-8 group-data-[orientation=horizontal]/timeline:mt-8 group-data-[orientation=horizontal]/timeline:not-last:pe-8 group-data-[orientation=vertical]/timeline:not-last:pb-6 has-[+[data-completed]]:**:data-[slot=timeline-separator]:bg-primary"
    HEADER = ""
    TITLE = "font-medium text-sm"
    CONTENT = "text-muted-foreground text-sm"
    DATE = "mb-1 block font-medium text-muted-foreground text-xs group-data-[orientation=vertical]/timeline:max-sm:h-4"
    INDICATOR = "group-data-[orientation=horizontal]/timeline:-top-6 group-data-[orientation=horizontal]/timeline:-translate-y-1/2 group-data-[orientation=vertical]/timeline:-left-6 group-data-[orientation=vertical]/timeline:-translate-x-1/2 absolute size-4 rounded-full border-2 border-primary/20 group-data-[orientation=vertical]/timeline:top-0 group-data-[orientation=horizontal]/timeline:left-0 group-data-completed/timeline-item:border-primary"
    SEPARATOR = "group-data-[orientation=horizontal]/timeline:-top-6 group-data-[orientation=horizontal]/timeline:-translate-y-1/2 group-data-[orientation=vertical]/timeline:-left-6 group-data-[orientation=vertical]/timeline:-translate-x-1/2 absolute self-start bg-primary/10 group-last/timeline-item:hidden group-data-[orientation=horizontal]/timeline:h-0.5 group-data-[orientation=vertical]/timeline:h-[calc(100%-1rem-0.25rem)] group-data-[orientation=horizontal]/timeline:w-[calc(100%-1rem-0.25rem)] group-data-[orientation=vertical]/timeline:w-0.5 group-data-[orientation=horizontal]/timeline:translate-x-4.5 group-data-[orientation=vertical]/timeline:translate-y-4.5"


def timeline_root(
    *children,
    orientation: LiteralOrientation = "vertical",
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.ROOT, class_name),
        data_slot="timeline",
        data_orientation=orientation,
        **props,
    )


def timeline_item(
    *children,
    step: int,
    active_step: int,
    class_name: str = "",
    **props,
) -> rx.Component:
    completed = step <= active_step

    return rx.el.div(
        *children,
        class_name=cn(ClassNames.ITEM, class_name),
        data_slot="timeline-item",
        data_completed="" if completed else None,
        **props,
    )


def timeline_header(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.HEADER, class_name),
        data_slot="timeline-header",
        **props,
    )


def timeline_title(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.h3(
        *children,
        class_name=cn(ClassNames.TITLE, class_name),
        data_slot="timeline-title",
        **props,
    )


def timeline_content(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.CONTENT, class_name),
        data_slot="timeline-content",
        **props,
    )


def timeline_date(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.time(
        *children,
        class_name=cn(ClassNames.DATE, class_name),
        data_slot="timeline-date",
        **props,
    )


def timeline_indicator(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.INDICATOR, class_name),
        data_slot="timeline-indicator",
        aria_hidden=True,
        **props,
    )


def timeline_separator(
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        class_name=cn(ClassNames.SEPARATOR, class_name),
        data_slot="timeline-separator",
        aria_hidden=True,
        **props,
    )


class Timeline(ComponentNamespace):
    """Namespace for Timeline components."""

    root = staticmethod(timeline_root)
    item = staticmethod(timeline_item)
    header = staticmethod(timeline_header)
    title = staticmethod(timeline_title)
    content = staticmethod(timeline_content)
    date = staticmethod(timeline_date)
    indicator = staticmethod(timeline_indicator)
    separator = staticmethod(timeline_separator)
    __call__ = staticmethod(timeline_root)


timeline = Timeline()
