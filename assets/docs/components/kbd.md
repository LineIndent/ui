

# Kbd

Used to display textual user input from keyboard.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component kbd
```

### Manual Installation

```python
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
```



# Anatomy 
Use the following composition to build a `Kbd`


```python
kbd()
# or
kbd_group(
    kbd(),
    kbd(),
)
```


# Examples

## Default
A basic example showing a single styled keyboard key.


```python
def kbd_default():
    """
    Example matching the shadcn KbdDemo component.
    Shows keyboard shortcuts with modifier keys.
    """
    return rx.box(
        # Mac modifier keys
        kbd_group(
            kbd("⌘"),
            kbd("⇧"),
            kbd("⌥"),
            kbd("⌃"),
        ),
        # Keyboard shortcut combination
        kbd_group(
            kbd("Ctrl"),
            rx.el.span("+"),
            kbd("B"),
        ),
        class_name="flex flex-col items-center gap-4 p-8",
    )
```


## Common Shortcuts
Displays familiar keyboard shortcuts like copy or paste.


```python
def kbd_common_shortcuts():
    """Common keyboard shortcuts"""
    return rx.box(
        rx.box(
            rx.text("Save:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("S"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Copy:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("C"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Paste:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("V"),
            ),
            class_name="flex items-center",
        ),
        rx.box(
            rx.text("Undo:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("Z"),
            ),
            class_name="flex items-center",
        ),
        class_name="flex flex-col gap-3 p-8",
    )
```


## Special Keys
Shows styling for special keys such as Enter, Tab, or Esc.


```python
def kbd_special_keys():
    """Special key examples"""
    return rx.box(
        kbd("Enter"),
        kbd("Esc"),
        kbd("Tab"),
        kbd("Space"),
        kbd("←"),
        kbd("→"),
        kbd("↑"),
        kbd("↓"),
        kbd("Delete"),
        kbd("Backspace"),
        class_name="flex flex-wrap gap-2 p-8",
    )
```


## Complex Shortcuts
Demonstrates multi-key combinations for advanced shortcuts.


```python
def kbd_complex_shortcuts():
    """Complex multi-key shortcuts"""
    return rx.box(
        # Three modifier keys
        rx.box(
            rx.text("Screenshot:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("Ctrl"),
                rx.el.span("+"),
                kbd("Shift"),
                rx.el.span("+"),
                kbd("S"),
            ),
            class_name="flex items-center mb-3",
        ),
        # Mac command
        rx.box(
            rx.text("Quit:", class_name="text-sm font-medium mr-2"),
            kbd_group(
                kbd("⌘"),
                rx.el.span("+"),
                kbd("Q"),
            ),
            class_name="flex items-center mb-3",
        ),
        # Function key
        rx.box(
            rx.text("Full Screen:", class_name="text-sm font-medium mr-2"),
            kbd("F11"),
            class_name="flex items-center",
        ),
        class_name="p-8",
    )
```


## With Icons
Displays keyboard shortcuts paired with icons for clarity.


```python
def kbd_with_icons():
    """Kbd with icons"""
    return rx.box(
        kbd_group(
            kbd(
                rx.icon(tag="command", size=12),
            ),
            rx.el.span("+"),
            kbd("K"),
        ),
        kbd_group(
            kbd(
                rx.icon(tag="arrow-left", size=12),
            ),
            kbd(
                rx.icon(tag="arrow-right", size=12),
            ),
        ),
        class_name="flex flex-col items-center gap-4 p-8",
    )
```

