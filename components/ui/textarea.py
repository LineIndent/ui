"""Custom Textarea component."""

from reflex.components.component import Component
from reflex_components_core.el import Textarea as TextareaComponent

from .component import CoreComponent


class ClassNames:
    """Class names for textarea components."""

    ROOT = "flex field-sizing-content min-h-16 min-w-xs rounded-radius border border-input bg-transparent px-2.5 py-2 text-base transition-colors outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:bg-input/50 disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 md:text-sm dark:bg-input/30 dark:disabled:bg-input/80 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40"

    # ROOT = (
    #     "placeholder:text-muted-foreground "
    #     "selection:bg-primary selection:text-primary-foreground "
    #     "dark:bg-input/30 border-input "
    #     "min-h-20 rounded-radius border bg-transparent px-3 py-2 text-base shadow-xs "
    #     "transition-[color,box-shadow] outline-none resize-none "
    #     "disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 "
    #     "md:text-sm "
    #     "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
    #     "aria-invalid:ring-[var(--destructive)]/20 dark:aria-invalid:ring-[var(--destructive)]/40 "
    #     "aria-invalid:border-[var(--destructive)]"
    # )


class Textarea(TextareaComponent, CoreComponent):
    """Root component for Textarea."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the textarea component."""
        props.setdefault(
            "custom_attrs",
            {
                "autoComplete": "off",
                "autoCapitalize": "none",
                "autoCorrect": "off",
                "spellCheck": "false",
            },
        )
        props["data-slot"] = "textarea"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


textarea = Textarea.create
