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
