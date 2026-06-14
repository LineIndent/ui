# Buridan UI Component Patterns

Follow these patterns to ensure consistency with the Buridan UI architecture.

## 1. Imports
Components are added to the local project in `components/ui/`.
```python
from components.ui.button import button
from components.ui.input import input
from components.icons.hugeicon import hi
```

## 2. Layout Decorator
Wrap pages with `layout_decorator` for consistent navigation and headers.
```python
from app.templates.layout import layout_decorator

@layout_decorator(
    title="My Page",
    description="Page description here."
)
def my_page():
    return rx.el.div(...)
```

## 3. ClientStateVar
Use `ClientStateVar` for fast, client-side UI state.
```python
from reflex.experimental import ClientStateVar

# Define
my_state = ClientStateVar.create("my_state_name", "default_value")

# Use
rx.button("Toggle", on_click=my_state.set_value("new_value"))
rx.cond(my_state.value == "new_value", ...)
```

## 4. Tailwind Merging
Use the `cn` utility for conditional classes.
```python
from components.utils.twmerge import cn

def my_comp(class_name: str = ""):
    return rx.el.div(
        class_name=cn("default-classes", class_name)
    )
```
