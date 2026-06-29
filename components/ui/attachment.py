"""Attachment component — file and image attachment previews for chat UI."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..ui.button import button
from ..utils.twmerge import cn

AttachmentOrientation = Literal["horizontal", "vertical"]
AttachmentSize = Literal["default", "sm", "xs"]
AttachmentState = Literal["idle", "uploading", "processing", "error", "done"]
AttachmentMediaVariant = Literal["icon", "image"]


class ClassNames:
    ROOT_BASE = (
        "group/attachment relative flex w-full max-w-full min-w-0 shrink-0 flex-wrap "
        "rounded-2xl border border-input bg-card text-card-foreground transition-colors "
        "focus-within:ring-1 focus-within:ring-ring/30 "
        "has-[>a,>button]:hover:bg-muted/50 "
        "data-[state=error]:border-destructive/30 "
        "data-[state=idle]:border-dashed"
    )

    SIZES: dict[str, str] = {
        "default": (
            "gap-2 text-sm "
            "has-data-[slot=attachment-content]:px-2.5 "
            "has-data-[slot=attachment-content]:py-2 "
            "has-data-[slot=attachment-media]:p-2"
        ),
        "sm": (
            "gap-2.5 text-xs "
            "has-data-[slot=attachment-content]:px-2 "
            "has-data-[slot=attachment-content]:py-1.5 "
            "has-data-[slot=attachment-media]:p-1.5"
        ),
        "xs": (
            "gap-1.5 rounded-xl text-xs "
            "has-data-[slot=attachment-content]:px-1.5 "
            "has-data-[slot=attachment-content]:py-1 "
            "has-data-[slot=attachment-media]:p-1"
        ),
    }

    ORIENTATIONS: dict[str, str] = {
        "horizontal": "min-w-40 items-center",
        "vertical": "w-24 flex-col has-data-[slot=attachment-content]:w-30",
    }

    MEDIA_BASE = (
        "relative flex aspect-square w-10 shrink-0 items-center justify-center "
        "overflow-hidden rounded-lg bg-muted text-foreground "
        "group-data-[orientation=vertical]/attachment:w-full "
        "group-data-[size=sm]/attachment:w-8 "
        "group-data-[size=xs]/attachment:w-7 "
        "group-data-[size=xs]/attachment:rounded-md "
        "group-data-[state=error]/attachment:bg-destructive/10 "
        "group-data-[state=error]/attachment:text-destructive "
        "[&_svg]:pointer-events-none "
        "[&_svg:not([class*='size-'])]:size-4 "
        "group-data-[orientation=vertical]/attachment:[&_svg:not([class*='size-'])]:size-6 "
        "group-data-[size=xs]/attachment:[&_svg:not([class*='size-'])]:size-3.5"
    )

    MEDIA_VARIANTS: dict[str, str] = {
        "icon": "",
        "image": (
            "opacity-60 "
            "group-data-[state=done]/attachment:opacity-100 "
            "group-data-[state=idle]/attachment:opacity-100 "
            "*:[img]:aspect-square *:[img]:w-full *:[img]:object-cover"
        ),
    }

    CONTENT = (
        "max-w-full min-w-0 flex-1 leading-tight "
        "group-data-[orientation=vertical]/attachment:px-1"
    )

    TITLE = (
        "block max-w-full min-w-0 truncate font-medium "
        "group-data-[state=processing]/attachment:shimmer "
        "group-data-[state=uploading]/attachment:shimmer"
    )

    DESCRIPTION = (
        "mt-0.5 block min-w-0 max-w-full truncate text-xs text-muted-foreground "
        "group-data-[state=error]/attachment:text-destructive/80"
    )

    ACTIONS = (
        "relative z-20 flex shrink-0 items-center "
        "group-data-[orientation=vertical]/attachment:absolute "
        "group-data-[orientation=vertical]/attachment:top-3 "
        "group-data-[orientation=vertical]/attachment:right-3 "
        "group-data-[orientation=vertical]/attachment:gap-1"
    )

    TRIGGER = "absolute inset-0 z-10 outline-none"

    GROUP = (
        "flex scroll-fade-x min-w-0 snap-x snap-mandatory scroll-px-1 scrollbar-none gap-3 "
        "overflow-x-auto overscroll-x-contain py-1 "
        "*:data-[slot=attachment]:flex-none "
        "*:data-[slot=attachment]:snap-start"
    )


def attachment_root(
    *children,
    orientation: AttachmentOrientation = "horizontal",
    size: AttachmentSize = "default",
    state: AttachmentState = "done",
    class_name: str = "",
    **props,
) -> rx.Component:
    """
    Root attachment container.

    orientation: horizontal (default) | vertical
    size:        default | sm | xs
    state:       idle | uploading | processing | error | done (default)
    """
    return rx.el.div(
        *children,
        data_slot="attachment",
        data_state=state,
        data_size=size,
        data_orientation=orientation,
        class_name=cn(
            ClassNames.ROOT_BASE,
            ClassNames.SIZES.get(size, ""),
            ClassNames.ORIENTATIONS.get(orientation, ""),
            class_name,
        ),
        **props,
    )


def attachment_media(
    *children,
    variant: AttachmentMediaVariant = "icon",
    class_name: str = "",
    **props,
) -> rx.Component:
    """Icon or image preview slot."""
    return rx.el.div(
        *children,
        data_slot="attachment-media",
        data_variant=variant,
        class_name=cn(
            ClassNames.MEDIA_BASE,
            ClassNames.MEDIA_VARIANTS.get(variant, ""),
            class_name,
        ),
        **props,
    )


def attachment_content(*children, class_name: str = "", **props) -> rx.Component:
    """Text content area — holds title and description."""
    return rx.el.div(
        *children,
        data_slot="attachment-content",
        class_name=cn(ClassNames.CONTENT, class_name),
        **props,
    )


def attachment_title(*children, class_name: str = "", **props) -> rx.Component:
    """Filename or attachment title. Shimmers during uploading/processing."""
    return rx.el.span(
        *children,
        data_slot="attachment-title",
        class_name=cn(ClassNames.TITLE, class_name),
        **props,
    )


def attachment_description(*children, class_name: str = "", **props) -> rx.Component:
    """File type, size, or other metadata."""
    return rx.el.span(
        *children,
        data_slot="attachment-description",
        class_name=cn(ClassNames.DESCRIPTION, class_name),
        **props,
    )


def attachment_actions(*children, class_name: str = "", **props) -> rx.Component:
    """
    Row of action buttons.
    In vertical orientation, absolutely positioned top-right.
    """
    return rx.el.div(
        *children,
        data_slot="attachment-actions",
        class_name=cn(ClassNames.ACTIONS, class_name),
        **props,
    )


def attachment_action(*children, class_name: str = "", **props) -> rx.Component:
    """Individual action button."""
    props.setdefault("variant", "ghost")
    props.setdefault("size", "icon-xs")
    return button(
        *children,
        data_slot="attachment-action",
        class_name=cn(class_name),
        **props,
    )


def attachment_trigger(
    *children, link: bool = False, class_name: str = "", **props
) -> rx.Component:

    component_fn = rx.el.a if link else rx.el.button

    props.setdefault("data_slot", "attachment-trigger")
    props.setdefault("class_name", cn(ClassNames.TRIGGER, class_name))

    if not link:
        props.setdefault("type", "button")

    return component_fn(*children, **props)


def attachment_group(*children, class_name: str = "", **props) -> rx.Component:
    """
    Horizontal scrolling row of attachments.
    Snaps to each attachment on scroll.
    """
    return rx.el.div(
        *children,
        data_slot="attachment-group",
        class_name=cn(ClassNames.GROUP, class_name),
        **props,
    )


class Attachment(ComponentNamespace):
    """Attachment namespace."""

    root = staticmethod(attachment_root)
    media = staticmethod(attachment_media)
    content = staticmethod(attachment_content)
    title = staticmethod(attachment_title)
    description = staticmethod(attachment_description)
    actions = staticmethod(attachment_actions)
    action = staticmethod(attachment_action)
    trigger = staticmethod(attachment_trigger)
    group = staticmethod(attachment_group)

    class_names = ClassNames


attachment = Attachment()
