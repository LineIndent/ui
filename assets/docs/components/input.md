

# Input

A text input component for forms and user data entry with built-in styling and accessibility features.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component input
```

### Manual Installation

```python
from reflex.components.component import ComponentNamespace
from reflex_components_core.el import Input as BaseInput

from ..utils.twmerge import cn
from .component import CoreComponent


class ClassNames:
    INPUT = (
        "w-full file:text-foreground placeholder:text-muted-foreground "
        "selection:bg-primary selection:text-primary-foreground "
        "dark:bg-input/30 border-input "
        "h-8 w-full min-w-0 rounded-lg border bg-transparent px-3 py-1 text-base "
        "transition-[color,box-shadow] outline-none "
        "file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium "
        "disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 "
        "md:text-sm "
        "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] "
        "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 "
        "aria-invalid:border-destructive"
    )


class InputComponent(BaseInput, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> BaseInput:

        existing_class = props.get("class_name", "")

        props["class_name"] = cn(ClassNames.INPUT, existing_class)

        props.setdefault("data_slot", "input")

        if "type" not in props:
            props["type"] = "text"

        return super().create(*children, **props)


class Input(ComponentNamespace):
    __call__ = staticmethod(InputComponent.create)
    class_name = ClassNames


input = Input()
```


# Usage


```python
from components.ui.input import input
```


# Anatomy 
Use the following composition to build an `Input` component.


```python
input()
```



# Examples

## Basic Demo
A simple text input demonstrating the default appearance and behavior.


```python
def input_basic_demo():
    return rx.el.div(
        rx.text("Text Input", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Enter your name",
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Email
An input field optimized for email address entry.


```python
def input_email():
    return rx.el.div(
        rx.el.p("Email Input", class_name="text-sm font-medium mb-2"),
        input(
            type="email",
            placeholder="name@example.com",
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Password
An input field that hides characters for secure password entry.


```python
def input_password():
    return rx.el.div(
        rx.el.p("Password Input", class_name="text-sm font-medium mb-2"),
        input(
            type="password",
            placeholder="Enter your password",
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Disabled
An example of an input field in a disabled state.


```python
def input_disabled():
    return rx.el.div(
        rx.el.p("Disabled Input", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Disabled input",
            disabled=True,
        ),
        class_name="w-full max-w-md p-8",
    )
```


## File Input
An input field for selecting and uploading files.


```python
def input_file_input():
    return rx.el.div(
        rx.el.p("File Input", class_name="text-sm font-medium mb-2"),
        input(
            type="file",
        ),
        class_name="w-full max-w-md p-8",
    )
```


## Custom Input
An input field with a custom width and styling.


```python
def input_custom_input():
    return rx.el.div(
        rx.el.p("Custom Width", class_name="text-sm font-medium mb-2"),
        input(
            type="text",
            placeholder="Max width 300px",
            class_name="max-w-[300px]",
        ),
        class_name="w-full max-w-md p-8",
    )
```

