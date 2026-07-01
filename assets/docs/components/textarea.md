

# Textarea

Displays a form textarea or a component that looks like a textarea.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component textarea
```

### Manual Installation

```python
"""Custom Textarea component."""

from reflex.components.component import Component
from reflex_components_core.el import Textarea as TextareaComponent

from .component import CoreComponent


class ClassNames:
    """Class names for textarea components."""

    ROOT = "flex field-sizing-content min-h-16 min-w-xs rounded-lg border border-input bg-transparent px-2.5 py-2 text-base transition-colors outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:bg-input/50 disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 md:text-sm dark:bg-input/30 dark:disabled:bg-input/80 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40"


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
```


# Usage


```python
from components.ui.textarea import textarea
```


# Anatomy 
Use the following composition to build a `Textarea` component.


```python
textarea()
```


# Examples

## Basic Demo
A standard multiline text area for general text input.


```python
def textarea_basic_demo():
    return textarea(placeholder="Type your message here.")
```


## Field
Use `field.root`, `field.label`, and `field.description` together with a form control (such as textarea) to build a structured field with a label and helper text.


```python
def textarea_field():
    return field.root(
        field.label(
            "Message",
            html_for="textarea-message",
        ),
        field.description(
            "Enter your message below.",
        ),
        textarea(
            id="textarea-message",
            placeholder="Type your message here.",
        ),
    )
```


## Disabled
Use the `disabled` prop on textarea to disable user input. Apply `data-disabled` on `field.root` to propagate disabled styling to all field-related elements and ensure consistent visual state handling.


```python
def textarea_disabled():
    return field.root(
        field.label(
            "Message",
            html_for="textarea-disabled",
        ),
        textarea(
            id="textarea-disabled",
            placeholder="Type your message here.",
            disabled=True,
        ),
        **{"data-disabled": True},
    )
```


## Invalid
Apply `data-disabled` on Field to represent a disabled state and propagate styling, and apply data-invalid to represent validation errors.


```python
def textarea_invalid():
    return field.root(
        field.label(
            "Message",
            html_for="textarea-invalid",
        ),
        textarea(
            id="textarea-invalid",
            placeholder="Type your message here.",
            **{"aria-invalid": True},
        ),
        field.description(
            "Please enter a valid message.",
        ),
        **{"data-invalid": True},
    )
```

