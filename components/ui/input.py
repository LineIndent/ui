from reflex.components.component import ComponentNamespace
from reflex_components_core.el import Input

INPUT = (
    "file:text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] "
    "selection:bg-[var(--primary)] selection:text-[var(--primary-foreground)] "
    "dark:bg-[var(--input)]/30 border-[var(--input)] "
    "h-9 w-full min-w-0 rounded-radius border bg-transparent px-3 py-1 text-base shadow-xs "
    "transition-[color,box-shadow] outline-none "
    "file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium "
    "disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 "
    "md:text-sm "
    "focus-visible:border-[var(--ring)] focus-visible:ring-[var(--ring)]/50 focus-visible:ring-[3px] "
    "aria-invalid:ring-[var(--destructive)]/20 dark:aria-invalid:ring-[var(--destructive)]/40 "
    "aria-invalid:border-[var(--destructive)]"
)


class InputComponent(Input):
    """Styled input component that extends rx.el.input."""

    @classmethod
    def create(cls, *children, **props):
        """Create the input component with default styling."""
        # Get existing class_name or empty string
        existing_class = props.get("class_name", "")

        # Merge base classes with any custom classes
        props["class_name"] = f"{INPUT} {existing_class}".strip()

        # Set data slot
        props["data_slot"] = "input"

        # Set default type if not provided
        if "type" not in props:
            props["type"] = "text"

        return super().create(*children, **props)


class Input(ComponentNamespace):
    """Namespace for Input component."""

    __call__ = staticmethod(InputComponent.create)


input = Input()
