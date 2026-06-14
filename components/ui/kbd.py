import reflex as rx


def kbd(*children, class_name: str = "", **props):
    """
    Keyboard key component matching shadcn/ui styling.
    Uses CSS variables from your theme for colors.

    Args:
        *children: Key content (text, symbols, icons)
        class_name: Additional classes
        **props: Additional props for the kbd element
    """
    base_classes = (
        "bg-[var(--muted)] text-[var(--muted-foreground)] "
        "pointer-events-none inline-flex h-5 w-fit min-w-5 items-center justify-center gap-1 "
        "rounded-sm px-1 font-sans text-xs font-medium select-none "
        "[&_svg:not([class*='size-'])]:size-3 "
        "[[data-slot=tooltip-content]_&]:bg-[var(--background)]/20 "
        "[[data-slot=tooltip-content]_&]:text-[var(--background)] "
        "dark:[[data-slot=tooltip-content]_&]:bg-[var(--background)]/10"
    )

    return rx.el.kbd(
        *children,
        data_slot="kbd",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def kbd_group(*children, class_name: str = "", **props):
    """
    Group multiple kbd elements together with spacing.

    Args:
        *children: Multiple kbd elements
        class_name: Additional classes
        **props: Additional props for the group element
    """
    base_classes = "inline-flex items-center gap-1"

    return rx.el.kbd(
        *children,
        data_slot="kbd-group",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )
