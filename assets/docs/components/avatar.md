

# Avatar

Displays a user's profile picture, initials, or fallback icon.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component avatar
```

### Manual Installation

```python
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
```


# Usage


> **Error processing usage for avatar: module, class, method, function, traceback, frame, or code object was expected, got Avatar**


# Anatomy 
Use the following composition to build a `Avatar`


```python
avatar.root(
    avatar.image(),
    avatar.fallback(),
)
```



# Examples

Below are examples demonstrating how the component can be used.

## General

Displays a basic avatar with either a user image or a fallback placeholder.


```python
def avatar_general():
    return rx.box(
        avatar(
            src="https://avatars.githubusercontent.com/u/84860195?v=4",
            alt="@LineIndent",
            fallback="CN",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/198465274?s=200&v=4",
            alt="@buridan-ui",
            fallback="BUI",
            class_name="rounded-lg",
        ),
        rx.box(
            avatar(
                src="",
                alt="@buridan-ui",
                fallback="BU",
            ),
            avatar(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                alt="@buridan-ui",
                fallback="BUI",
            ),
            avatar(
                src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
                alt="@reflex",
                fallback="RE",
            ),
            class_name=(
                "flex -space-x-2 "
                "*:data-[slot=avatar]:ring-2 *:data-[slot=avatar]:ring-[var(--background)] "
                "*:data-[slot=avatar]:grayscale"
            ),
        ),
        class_name="flex flex-row flex-wrap items-center gap-12 p-8",
    )
```


## Sizes

Demonstrates how to scale the avatar component using Tailwind utility classes.


```python
def avatar_sizes():
    """Example showing different avatar sizes"""
    return rx.box(
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-6",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-8",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-10",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-12",
        ),
        avatar(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            alt="@reflex",
            fallback="RE",
            class_name="size-16",
        ),
        class_name="flex items-center gap-4 p-8",
    )
```


## With Badge

Shows how to combine an avatar with status or notification badges for added context.


```python
def avatar_with_badge():
    """Example showing avatar with status badge"""
    return rx.box(
        rx.box(
            avatar(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                alt="@LineIndent",
                fallback="CN",
                class_name="size-12",
            ),
            rx.box(
                class_name=(
                    "absolute bottom-0 right-0 size-3 rounded-full "
                    "bg-green-500 border-2 border-[var(--background)]"
                ),
            ),
            class_name="relative inline-block",
        ),
        class_name="p-8",
    )
```

