"""Custom avatar component."""

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    """Class names for avatar components."""

    ROOT = "shrink-0 inline-flex size-8 items-center justify-center overflow-hidden rounded-full align-middle text-base font-medium select-none"
    IMAGE = "size-full object-cover shrink-0"
    FALLBACK = "flex size-full items-center justify-center text-sm bg-muted"


class AvatarBaseComponent(BaseUIComponent):
    """Base component for avatar components."""

    library = f"{PACKAGE_NAME}/avatar"

    @property
    def import_var(self):
        """Return the import variable for the avatar component."""
        return ImportVar(tag="Avatar", package_path="", install=False)


class AvatarRoot(AvatarBaseComponent):
    """Displays a user's profile picture, initials, or fallback icon."""

    tag = "Avatar.Root"

    # The component to render
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the avatar root component."""
        props["data-slot"] = "avatar"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class AvatarImage(AvatarBaseComponent):
    """The image to be displayed in the avatar."""

    tag = "Avatar.Image"

    # The image source URL
    src: Var[str]

    # Callback when loading status changes
    on_loading_status_change: EventHandler[passthrough_event_spec(str)]

    # The component to render
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the avatar image component."""
        props["data-slot"] = "avatar-image"
        cls.set_class_name(ClassNames.IMAGE, props)
        return super().create(*children, **props)


class AvatarFallback(AvatarBaseComponent):
    """Rendered when the image fails to load or when no image is provided."""

    tag = "Avatar.Fallback"

    # How long to wait before showing the fallback. Specified in milliseconds
    delay: Var[int]

    # The component to render
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the avatar fallback component."""
        props["data-slot"] = "avatar-fallback"
        cls.set_class_name(ClassNames.FALLBACK, props)
        return super().create(*children, **props)


class HighLevelAvatar(AvatarRoot):
    """High level wrapper for the Avatar component."""

    # The image source URL
    src: Var[str]

    # Image props
    _image_props = {"src", "on_loading_status_change", "render_"}

    # Fallback props
    _fallback_props = {"delay"}

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the avatar component."""
        # Extract props for each subcomponent
        image_props = {k: props.pop(k) for k in cls._image_props & props.keys()}
        fallback_props = {k: props.pop(k) for k in cls._fallback_props & props.keys()}

        fallback_content = props.pop("fallback", "")

        return AvatarRoot.create(
            AvatarImage.create(**image_props),
            AvatarFallback.create(fallback_content, **fallback_props),
            *children,
            **props,
        )


class Avatar(ComponentNamespace):
    """Namespace for Avatar components."""

    root = staticmethod(AvatarRoot.create)
    image = staticmethod(AvatarImage.create)
    fallback = staticmethod(AvatarFallback.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelAvatar.create)


avatar = Avatar()
