

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

from .component import CoreComponent

LiteralBadgeVariant = Literal["default", "secondary", "destructive", "outline"]

DEFAULT_BASE_CLASSES = (
    "inline-flex items-center justify-center rounded-radius border px-2 py-0.5 text-xs font-medium "
    "w-fit whitespace-nowrap shrink-0 [&>svg]:size-3 gap-1 [&>svg]:pointer-events-none "
    "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
    "aria-invalid:ring-[var(--destructive)]/20 dark:aria-invalid:ring-[var(--destructive)]/40 "
    "aria-invalid:border-[var(--destructive)] transition-[color,box-shadow] overflow-hidden"
)

BADGE_VARIANTS = {
    "default": (
        "border-transparent bg-[var(--primary)] text-[var(--primary-foreground)] "
        "[a&]:hover:bg-[var(--primary)]/90"
    ),
    "secondary": (
        "border-transparent bg-[var(--secondary)] text-[var(--secondary-foreground)] "
        "[a&]:hover:bg-[var(--secondary)]/90"
    ),
    "destructive": (
        "border-transparent bg-[var(--destructive)] text-white "
        "[a&]:hover:bg-[var(--destructive)]/90 "
        "focus-visible:ring-[var(--destructive)]/20 dark:focus-visible:ring-[var(--destructive)]/40 "
        "dark:bg-[var(--destructive)]/60"
    ),
    "outline": (
        "text-[var(--foreground)] border-[var(--input)] "
        "[a&]:hover:bg-[var(--accent)] [a&]:hover:text-[var(--accent-foreground)]"
    ),
}


def get_badge_classes(variant: LiteralBadgeVariant) -> str:
    """Get the complete badge class string.

    Args:
        variant: The badge variant to apply

    Returns:
        The complete class string for the badge
    """
    variant_classes = BADGE_VARIANTS[variant]
    return f"{DEFAULT_BASE_CLASSES} {variant_classes}"


class Badge(Span, CoreComponent):
    """A badge component that displays a label."""

    # Badge variant
    variant: Var[LiteralBadgeVariant]

    @classmethod
    def create(cls, *children, **props) -> Span:
        """Create the badge component.

        Args:
            *children: The badge content
            **props: Component properties including variant

        Returns:
            A configured Span component
        """
        variant = props.pop("variant", "default")

        cls.set_class_name(get_badge_classes(variant), props)

        # Add data-slot attribute
        props.setdefault("data_slot", "badge")

        return super().create(*children, **props)

    def _exclude_props(self) -> list[str]:
        """Exclude component-specific props from being passed to the DOM.

        Returns:
            List of prop names to exclude
        """
        return [*super()._exclude_props(), "variant"]


badge = Badge.create
```


# Usage


```python
from components.ui.badge import badge
```


# Anatomy 
Use the following composition to build a `Badge`


```python
badge()
```



# Examples


## Default

Displays a standard badge using the default variant, ideal for basic labeling.


```python
def badge_default():
    return rx.box(
        rx.box(
            badge("Badge"),
            badge("Secondary", variant="secondary"),
            badge("Destructive", variant="destructive"),
            badge("Outline", variant="outline"),
            class_name="flex w-full flex-wrap gap-2",
        ),
        rx.box(
            badge(
                rx.icon(tag="badge-check"),
                "Verified",
                variant="secondary",
                class_name="bg-blue-500 text-white dark:bg-blue-600",
            ),
            badge(
                "8",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "99",
                variant="destructive",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            badge(
                "20+",
                variant="outline",
                class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
            ),
            class_name="flex w-full flex-wrap gap-2",
        ),
        class_name="flex flex-col items-center gap-2 p-8",
    )
```


## With Icons

Demonstrates how to include icons inside badges for visual context or emphasis.


```python
def badge_with_icons():
    return rx.box(
        badge(
            rx.icon(tag="check"),
            "Success",
            variant="secondary",
            class_name="bg-green-500 text-white dark:bg-green-600",
        ),
        badge(
            rx.icon(tag="x"),
            "Error",
            variant="destructive",
        ),
        badge(
            rx.icon(tag="triangle-alert"),
            "Warning",
            variant="secondary",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        badge(
            rx.icon(tag="info"),
            "Info",
            variant="secondary",
            class_name="bg-blue-500 text-white dark:bg-blue-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )
```


## Status

Showcases how badges can represent different statuses, like success or error, using color.


```python
def badge_status():
    return rx.box(
        badge("New", variant="default"),
        badge("Popular", variant="secondary"),
        badge("Sale", variant="destructive"),
        badge("Draft", variant="outline"),
        badge(
            rx.icon(tag="star"),
            "Featured",
            class_name="bg-yellow-500 text-white dark:bg-yellow-600",
        ),
        class_name="flex flex-wrap gap-2 p-8",
    )
```


## Notification Count

Illustrates how to use badges for showing counts, such as unread notifications or messages.


```python
def badge_notification_count():
    return rx.box(
        badge(
            "1",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "5",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "10",
            variant="secondary",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        badge(
            "99+",
            variant="destructive",
            class_name="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums",
        ),
        class_name="flex items-center gap-2 p-8",
    )
```

