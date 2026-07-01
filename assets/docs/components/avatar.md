

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
```


# Usage


```python
from components.ui.avatar import Avatar
```


# Anatomy 
Use the following composition to build an `Avatar` component.


```python
avatar.root(
    avatar.image(),
    avatar.fallback(),
)
```


# Examples

## Basic

A basic avatar component with an image and a fallback.


```python
def avatar_basic() -> rx.Component:
    return avatar.root(
        avatar.image(
            src="https://github.com/LineIndent.png",
            custom_attrs={"alt": "@lineindent"},
        ),
        avatar.fallback("AH"),
    )
```


## Badge

Use the `avatar.badge` component to add a badge to the avatar. The badge is positioned at the bottom right of the avatar.


```python
def avatar_with_badge() -> rx.Component:
    return avatar.root(
        avatar.image(
            src="https://avatars.githubusercontent.com/u/84860195?v=4",
            custom_attrs={"alt": "@LineIndent"},
        ),
        avatar.fallback("AH"),
        avatar.badge(
            class_name="bg-green-600 dark:bg-green-800",
        ),
    )
```


Use the `class_Name` prop to add custom styles to the badge such as custom colors, sizes, etc.

```reflex
avatar.badge(class_name="bg-green-600 dark:bg-green-800")
```

## Badge with Icon

You can also use an icon inside `avatar.badge`.


```python
def avatar_badge_icon() -> rx.Component:
    return avatar.root(
        avatar.image(
            src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
            custom_attrs={"alt": "Reflex Dev"},
        ),
        avatar.fallback("RD"),
        avatar.badge(
            hi("PlusSignIcon"),
        ),
    )
```


## Avatar Group

Use the `avatar.group` component to add a group of avatars.


```python
def avatar_as_group() -> rx.Component:
    return avatar.group(
        avatar.root(
            avatar.image(
                src="/avatars/01.png",
                custom_attrs={"alt": "@avatar-1"},
            ),
            avatar.fallback("RD"),
        ),
        avatar.root(
            avatar.image(
                src="/avatars/02.png",
                custom_attrs={"alt": "@avatar-2"},
            ),
            avatar.fallback("LI"),
        ),
        avatar.root(
            avatar.fallback("AH"),
        ),
        class_name="grayscale",
    )
```


## Avatar Group Count

Use `avatar.group_count` to add a count to the group.


```python
def avatar_with_group_count() -> rx.Component:
    return avatar.group(
        avatar.root(
            avatar.fallback("AH"),
        ),
        avatar.root(
            avatar.image(
                src="/avatars/01.png",
                custom_attrs={"alt": "@avatar-1"},
            ),
            avatar.fallback("RD"),
        ),
        avatar.root(
            avatar.image(
                src="/avatars/02.png",
                custom_attrs={"alt": "@avatar-2"},
            ),
            avatar.fallback("LI"),
        ),
        avatar.group_count("+3"),
        class_name="grayscale",
    )
```


## Avatar Group with Icon

You can also use an icon inside `avatar.group_count`.


```python
def avatar_group_count_icon() -> rx.Component:
    return avatar.group(
        avatar.root(
            avatar.fallback("AH"),
        ),
        avatar.root(
            avatar.image(
                src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
                custom_attrs={"alt": "@reflex-dev"},
            ),
            avatar.fallback("CN"),
        ),
        avatar.root(
            avatar.image(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                custom_attrs={"alt": "LineIndent"},
            ),
            avatar.fallback("LI"),
        ),
        avatar.group_count(
            hi("PlusSignIcon"),
        ),
        class_name="grayscale",
    )
```


## Sizes

Use the `size` prop to change the size of the avatar.


```python
def avatar_sizes() -> rx.Component:
    return rx.el.div(
        avatar.root(
            avatar.image(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                custom_attrs={"alt": "@LineIndent"},
            ),
            avatar.fallback("LI"),
            size="sm",
        ),
        avatar.root(
            avatar.image(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                custom_attrs={"alt": "@LineIndent"},
            ),
            avatar.fallback("LI"),
        ),
        avatar.root(
            avatar.image(
                src="https://avatars.githubusercontent.com/u/84860195?v=4",
                custom_attrs={"alt": "@LineIndent"},
            ),
            avatar.fallback("LI"),
            size="lg",
        ),
        class_name="flex flex-wrap items-center gap-2",
    )
```


## Dropdown

You can use the `Avatar` component as a trigger for a dropdown menu.


```python
def avatar_dropdown_menu() -> rx.Component:
    return menu.root(
        menu.trigger(
            render_=button(
                avatar.root(
                    avatar.image(
                        src="https://github.com/LineIndent.png",
                        custom_attrs={"alt": "lineindent"},
                    ),
                    avatar.fallback("LI"),
                ),
                variant="ghost",
                size="icon",
                class_name="rounded-full",
            )
        ),
        menu.portal(
            menu.positioner(
                menu.popup(
                    menu.group(
                        menu.item("Profile"),
                        menu.item("Billing"),
                        menu.item("Settings"),
                    ),
                    class_name="w-32",
                ),
            )
        ),
    )
```


# API Reference

## avatar.root

The `avatar.root` component is the root component that wraps the avatar image and fallback.

| Prop        | Type                        | Default     |
| ----------- | --------------------------- | ----------- |
| `size`      | `"default" \| "sm" \| "lg"` | `"default"` |
| `class_name` | `string`                    | -           |

## avatar.image

The `avatar.image` component displays the avatar image. It accepts all Base UI Avatar Image props.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `src`       | `string` | -       |
| `alt`       | `string` | -       |
| `class_name` | `string` | -       |

## avatar.fallback

The `avatar.fallback` component displays a fallback when the image fails to load. It accepts all Base UI Avatar Fallback props.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## avatar.badge

The `avatar.badge` component displays a badge indicator on the avatar, typically positioned at the bottom right.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## avatar.group

The `avatar.group` component displays a group of avatars with overlapping styling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## avatar.group_count

The `avatar.group_count` component displays a count indicator in an avatar group, typically showing the number of additional avatars.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |
