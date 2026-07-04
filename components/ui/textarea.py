from reflex_components_core.el import Textarea

from .component import CoreComponent


class ClassNames:
    ROOT = (
        "flex field-sizing-content min-h-16 w-full rounded-lg border border-input bg-transparent "
        "px-2.5 py-2 text-base transition-colors outline-none placeholder:text-muted-foreground "
        "focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:cursor-not-allowed "
        "disabled:bg-input/50 disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 "
        "aria-invalid:ring-destructive/20 md:text-sm dark:bg-input/30 dark:disabled:bg-input/80 "
        "dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40"
    )


class TextAreaComponent(Textarea, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> Textarea:
        props.setdefault(
            "custom_attrs",
            {
                "autoComplete": "off",
                "autoCapitalize": "none",
                "autoCorrect": "off",
                "spellCheck": "false",
            },
        )
        props.setdefault("data_slot", "textarea")
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


textarea = TextAreaComponent.create
