from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var
from reflex_components_core.el import Div, Span

from ..utils.twmerge import cn
from .base_ui import PACKAGE_NAME, BaseUIComponent
from .component import CoreComponent


class ClassNames:
    ROOT = "group/avatar relative flex size-8 shrink-0 rounded-full select-none after:absolute after:inset-0 after:rounded-full after:border after:border-border after:mix-blend-darken data-[size=xl]:size-14 data-[size=lg]:size-10 data-[size=sm]:size-6 dark:after:mix-blend-lighten"
    IMAGE = "aspect-square size-full rounded-full object-cover"
    FALLBACK = "flex size-full items-center justify-center rounded-full bg-muted text-sm text-muted-foreground group-data-[size=sm]/avatar:text-xs"
    BADGE = "absolute right-0 bottom-0 z-10 inline-flex items-center justify-center rounded-full bg-primary text-primary-foreground bg-blend-color ring-2 ring-background select-none group-data-[size=sm]/avatar:size-2 group-data-[size=sm]/avatar:[&>svg]:hidden group-data-[size=default]/avatar:size-2.5 group-data-[size=default]/avatar:[&>svg]:size-2 group-data-[size=lg]/avatar:size-3 group-data-[size=lg]/avatar:[&>svg]:size-2"
    GROUP = "group/avatar-group flex -space-x-2 *:data-[slot=avatar]:ring-2 *:data-[slot=avatar]:ring-background"
    GROUP_COUNT = "relative flex size-8 shrink-0 items-center justify-center rounded-full bg-muted text-sm text-muted-foreground ring-2 ring-background group-has-data-[size=lg]/avatar-group:size-10 group-has-data-[size=sm]/avatar-group:size-6 [&>svg]:size-4 group-has-data-[size=lg]/avatar-group:[&>svg]:size-5 group-has-data-[size=sm]/avatar-group:[&>svg]:size-3"


class AvatarBaseComponent(BaseUIComponent):
    library = f"{PACKAGE_NAME}/avatar"

    @property
    def import_var(self):
        return ImportVar(tag="Avatar", package_path="", install=False)


class AvatarRoot(AvatarBaseComponent):
    tag = "Avatar.Root"
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        custom_classes = props.pop("class_name", "")
        size = props.pop("size", "default")
        props["data-slot"] = "avatar"
        props["data-size"] = size

        return super().create(
            *children, class_name=cn(ClassNames.ROOT, custom_classes), **props
        )


class AvatarImage(AvatarBaseComponent):
    tag = "Avatar.Image"
    src: Var[str]
    on_loading_status_change: EventHandler[passthrough_event_spec(str)]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        custom_classes = props.pop("class_name", "")
        props["data-slot"] = "avatar-image"

        return super().create(
            *children, class_name=cn(ClassNames.IMAGE, custom_classes), **props
        )


class AvatarFallback(AvatarBaseComponent):
    tag = "Avatar.Fallback"
    delay: Var[int]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        custom_classes = props.pop("class_name", "")
        props["data-slot"] = "avatar-fallback"

        return super().create(
            *children,
            class_name=cn(ClassNames.FALLBACK, custom_classes),
            **props,
        )


class AvatarBadge(Span, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> Span:
        custom_classes = props.pop("class_name", "")
        props["data-slot"] = "avatar-badge"

        return super().create(
            *children, class_name=cn(ClassNames.BADGE, custom_classes), **props
        )


class AvatarGroup(Div, CoreComponent):
    """The flex container wrapper for grouping multiple avatars."""

    @classmethod
    def create(cls, *children, **props) -> Div:
        custom_classes = props.pop("class_name", "")
        props["data-slot"] = "avatar-group"

        return super().create(
            *children, class_name=cn(ClassNames.GROUP, custom_classes), **props
        )


class AvatarGroupCount(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> Div:
        custom_classes = props.pop("class_name", "")
        props["data-slot"] = "avatar-group-count"

        return super().create(
            *children,
            class_name=cn(ClassNames.GROUP_COUNT, custom_classes),
            **props,
        )


class Avatar(ComponentNamespace):
    root = staticmethod(AvatarRoot.create)
    image = staticmethod(AvatarImage.create)
    fallback = staticmethod(AvatarFallback.create)
    badge = staticmethod(AvatarBadge.create)
    group = staticmethod(AvatarGroup.create)
    group_count = staticmethod(AvatarGroupCount.create)
    class_names = ClassNames


avatar = Avatar()
