

# Textarea

Custom Textarea component.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component textarea
```

### Manual Installation

```python
from typing import Optional, Union

import reflex as rx
from reflex_components_core.el import Input as ElInput
from reflex_components_core.el import Textarea as ElTextarea


# --- 1. The Factory System (Standardizes the style and data_slot) ---
class ComponentFactory:
    def __init__(self, base_component_class, base_classes: str):
        self.base_class = base_component_class
        self.base_classes = base_classes

    def __call__(self, **props):
        # Merge your base styling with any custom class_name provided
        custom_classes = props.get("class_name", "")
        props["class_name"] = f"{self.base_classes} {custom_classes}".strip()

        # Mandatory for the CSS grid to find these components
        props["data_slot"] = "input"

        return self.base_class.create(**props)


# --- 2. Defining the Factories with your EXACT original styling ---
Input = ComponentFactory(
    ElInput,
    "flex-1 bg-transparent border-0 outline-none text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] px-2 py-2 text-sm",
)

Textarea = ComponentFactory(
    ElTextarea,
    "flex-1 bg-transparent border-0 outline-none resize-none text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] placeholder:text-sm px-3 py-3 text-sm",
)


# --- 3. The Components using the new system ---
def input_with_addons(
    *children,
    placeholder: str = "",
    prefix: Optional[Union[str, rx.Component]] = None,
    suffix: Optional[Union[str, rx.Component]] = None,
    input_type: str = "text",
    class_name: str = "",
    **props,
):
    children = list(children)
    if prefix:
        if isinstance(prefix, str):
            prefix = rx.el.p(
                prefix,
                class_name="text-[var(--muted-foreground)] text-sm font-medium pl-2 select-none pointer-events-none",
            )
        children.insert(0, prefix)

    children.append(Input(type=input_type, placeholder=placeholder, **props))

    if suffix:
        if isinstance(suffix, str):
            suffix = rx.el.p(
                suffix,
                class_name="text-[var(--muted-foreground)] text-sm font-medium pr-2 select-none pointer-events-none",
            )
        children.append(suffix)

    return rx.el.div(
        *children,
        class_name=f"flex items-center w-full h-9 bg-transparent border border-[var(--input)] dark:bg-[var(--input)]/30 rounded-[var(--radius)] shadow-xs focus-within:border-[var(--ring)] focus-within:ring-[var(--ring)]/50 focus-within:ring-[3px] transition-[color,box-shadow] {class_name}",
    )


def textarea_with_footer(
    placeholder: str = "",
    footer_text: Optional[str] = None,
    class_name: str = "",
    **props,
):
    children = [Textarea(placeholder=placeholder, **props)]
    if footer_text:
        children.append(
            rx.el.p(
                footer_text,
                class_name="text-[var(--muted-foreground)] text-xs px-3 pb-3 pt-0 select-none pointer-events-none",
            )
        )

    return rx.el.div(
        *children,
        class_name=f"flex flex-col w-full bg-transparent border border-[var(--input)] dark:bg-[var(--input)]/30 rounded-[var(--radius)] shadow-xs focus-within:border-[var(--ring)] focus-within:ring-[var(--ring)]/50 focus-within:ring-[3px] transition-[color,box-shadow] {class_name}",
    )
```


# Usage


> **Error processing usage for textarea: module, class, method, function, traceback, frame, or code object was expected, got ComponentFactory**


# Anatomy 
Use the following composition to build a `Textarea`


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

