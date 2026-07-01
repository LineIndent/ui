

# Badge

Displays a badge or a component that looks like a badge.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component badge
```

### Manual Installation

```python
from typing import Literal

from reflex.vars.base import Var
from reflex_components_core.el import Span

from ..utils.twmerge import cn
from .component import CoreComponent

LiteralBadgeVariant = Literal[
    "default", "secondary", "destructive", "outline", "ghost", "link"
]

DEFAULT_BASE_CLASSES = (
    "group/badge inline-flex h-5 w-fit shrink-0 items-center justify-center gap-1 overflow-hidden "
    "rounded-4xl border border-transparent px-2 py-0.5 text-xs font-medium whitespace-nowrap "
    "transition-all focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 "
    "has-data-[icon=inline-end]:pr-1.5 has-data-[icon=inline-start]:pl-1.5 aria-invalid:border-destructive "
    "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 [&>svg]:pointer-events-none [&>svg]:size-3!"
)

BADGE_VARIANTS = {
    "default": "bg-primary text-primary-foreground [a]:hover:bg-primary/80",
    "secondary": "bg-secondary text-secondary-foreground [a]:hover:bg-secondary/80",
    "destructive": (
        "bg-destructive/10 text-destructive focus-visible:ring-destructive/20 "
        "dark:bg-destructive/20 dark:focus-visible:ring-destructive/40 [a]:hover:bg-destructive/20"
    ),
    "outline": "border-border text-foreground [a]:hover:bg-muted [a]:hover:text-muted-foreground",
    "ghost": "hover:bg-muted hover:text-muted-foreground dark:hover:bg-muted/50",
    "link": "text-primary underline-offset-4 hover:underline",
}


def badge_variants(variant: str = "default") -> Var:
    return cn(
        DEFAULT_BASE_CLASSES,
        BADGE_VARIANTS.get(variant, BADGE_VARIANTS["default"]),
    )


class Badge(Span, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> Span:
        custom_classes = props.pop("class_name", "")
        variant = props.pop("variant", "default")
        props["data-slot"] = "badge"
        props["data-variant"] = variant

        return super().create(
            *children,
            class_name=cn(badge_variants(variant), custom_classes),
            **props,
        )


badge = Badge.create
```


# Usage


```python
from components.ui.badge import badge
```


# Anatomy 
Use the following composition to build a `Badge` component.


```python
badge()
```


# Examples

## Variants

Use the `variant` prop to change the variant of the badge.


```python
def badge_with_variants() -> rx.Component:
    return rx.el.div(
        badge("Default"),
        badge("Secondary", variant="secondary"),
        badge("Destructive", variant="destructive"),
        badge("Outline", variant="outline"),
        badge("Ghost", variant="ghost"),
        class_name="flex flex-wrap gap-2",
    )
```


## With Icons

You can render an icon inside the badge. Use `data-icon="inline-start"` to render the icon on the left and `data-icon="inline-end"` to render the icon on the right.


```python
def badge_with_icon() -> rx.Component:
    return rx.el.div(
        badge(
            hi("CheckmarkBadge01Icon", custom_attrs={"data-icon": "inline-start"}),
            "Verified",
            variant="secondary",
        ),
        badge(
            "Bookmark",
            hi("Bookmark02Icon", custom_attrs={"data-icon": "inline-end"}),
            variant="outline",
        ),
        class_name="flex flex-wrap gap-2",
    )
```


## With Spinner

You can render a spinner inside the badge. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` prop to the spinner.


```python
def badge_with_spinner() -> rx.Component:
    return rx.el.div(
        badge(
            spinner(custom_attrs={"data-icon": "inline-start"}),
            "Deleting",
            variant="destructive",
        ),
        badge(
            "Generating",
            spinner(custom_attrs={"data-icon": "inline-end"}),
            variant="secondary",
        ),
        class_name="flex flex-wrap gap-2",
    )
```


## Link

You can pass in `rx.el.a` to turn a badge into a link. The `badge` component accepts `*children` so any interactive element can be passed to it. 


```python
def badge_as_link() -> rx.Component:
    return badge(
        rx.el.a(
            "Open Link",
            hi("ArrowUpRightIcon", custom_attrs={"data-icon": "inline-end"}),
            href="#link",
            class_name="inline-flex items-center gap-1 text-inherit no-underline",
        ),
    )
```


## Custom Colors

You can customize the colors of a badge by adding custom classes such as `bg-green-50 dark:bg-green-800` to the `badge` component.


```python
def badge_custom_colors() -> rx.Component:
    return rx.el.div(
        badge(
            "Blue",
            class_name="bg-blue-50 text-blue-700 dark:bg-blue-950 dark:text-blue-300",
        ),
        badge(
            "Green",
            class_name="bg-green-50 text-green-700 dark:bg-green-950 dark:text-green-300",
        ),
        badge(
            "Sky",
            class_name="bg-sky-50 text-sky-700 dark:bg-sky-950 dark:text-sky-300",
        ),
        badge(
            "Purple",
            class_name="bg-purple-50 text-purple-700 dark:bg-purple-950 dark:text-purple-300",
        ),
        badge(
            "Red",
            class_name="bg-red-50 text-red-700 dark:bg-red-950 dark:text-red-300",
        ),
        class_name="flex flex-wrap gap-2",
    )
```



# API Reference

## badge

The `badge` component displays a badge or a component that looks like a badge.

| Prop        | Type                                                                          | Default     |
| ----------- | ----------------------------------------------------------------------------- | ----------- |
| `variant`   | `"default" \| "secondary" \| "destructive" \| "outline" \| "ghost" \| "link"` | `"default"` |
| `class_name` | `string`                                                                      | -           |
