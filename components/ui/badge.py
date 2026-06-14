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
