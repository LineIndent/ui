

# Context Menu

Displays a menu of actions triggered by a right click.

# Installation

Copy the following code into your app directory.


> **Error: 'context_menu' not found in registry**


# Usage


> **Error: 'context_menu' not found in registry**


# Anatomy 

Use the following composition to build a `Context Menu` component.


```python
context_menu.root(
    context_menu.trigger(),
    context_menu.portal(
        context_menu.positioner(
            context_menu.popup(
                context_menu.item(),
                context_menu.separator(),
                context_menu.group(
                    context_menu.group_label(),
                    context_menu.item(),
                ),
                context_menu.checkbox_item(
                    context_menu.checkbox_item_indicator(),
                ),
                context_menu.radio_group(
                    context_menu.radio_item(
                        context_menu.radio_item_indicator(),
                    ),
                ),
                context_menu.sub(
                    context_menu.sub_trigger(),
                    context_menu.positioner(
                        context_menu.popup(),
                    ),
                ),
            ),
        ),
    ),
)
```


A Context Menu is built by composing a root trigger with an overlay surface.

```composition
context_menu.root
├── context_menu.trigger
└── context_menu.portal
    └── context_menu.positioner
        └── context_menu.popup
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   ├── context_menu.item
            │   └── context_menu.item
            ├── context_menu.separator
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   ├── context_menu.checkbox_item
            │   │   └── context_menu.checkbox_item_indicator
            │   └── context_menu.checkbox_item
            │       └── context_menu.checkbox_item_indicator
            ├── context_menu.separator
            ├── context_menu.group
            │   ├── context_menu.group_label
            │   └── context_menu.radio_group
            │       ├── context_menu.radio_item
            │       │   └── context_menu.radio_item_indicator
            │       └── context_menu.radio_item
            │           └── context_menu.radio_item_indicator
            └── context_menu.sub
                ├── context_menu.sub_trigger
                └── context_menu.positioner
                    └── context_menu.popup
                        └── context_menu.group
                            ├── context_menu.item
                            └── context_menu.item
```

# Examples

## Basic

A simple context menu with a few actions.


```python
def context_menu_basic() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-input border-dashed text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.item("Back"),
                        context_menu.item("Forward", disabled=True),
                        context_menu.item("Reload"),
                    ),
                ),
            ),
        ),
    )
```


## Submenu

Use `context_menu.sub` to nest secondary actions.


```python
def context_menu_submenu() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.item(
                            "Copy",
                            context_menu.shortcut("⌘C"),
                        ),
                        context_menu.item(
                            "Cut",
                            context_menu.shortcut("⌘X"),
                        ),
                    ),
                    context_menu.sub(
                        context_menu.sub_trigger("More Tools"),
                        context_menu.positioner(
                            context_menu.popup(
                                context_menu.group(
                                    context_menu.item("Save Page..."),
                                    context_menu.item("Create Shortcut..."),
                                    context_menu.item("Name Window..."),
                                ),
                                context_menu.separator(),
                                context_menu.group(
                                    context_menu.item("Developer Tools"),
                                ),
                                context_menu.separator(),
                                context_menu.group(
                                    context_menu.item("Delete", variant="destructive"),
                                ),
                                class_name="shadow-lg",
                            ),
                            side="right",
                        ),
                    ),
                ),
            ),
        ),
    )
```


## Shortcuts

Use `context_menu.shortcut` to show keyboard hints.


```python
def context_menu_shortcuts() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.item(
                            "Back",
                            context_menu.shortcut("⌘["),
                        ),
                        context_menu.item(
                            "Forward",
                            context_menu.shortcut("⌘]"),
                            disabled=True,
                        ),
                        context_menu.item(
                            "Reload",
                            context_menu.shortcut("⌘R"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.item(
                            "Save",
                            context_menu.shortcut("⌘S"),
                        ),
                        context_menu.item(
                            "Save As...",
                            context_menu.shortcut("⇧⌘S"),
                        ),
                    ),
                ),
            ),
        ),
    )
```


## Groups

Group related actions and separate them with dividers.


```python
def context_menu_groups() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.group_label("File"),
                        context_menu.item(
                            "New File",
                            context_menu.shortcut("⌘N"),
                        ),
                        context_menu.item(
                            "Open File",
                            context_menu.shortcut("⌘O"),
                        ),
                        context_menu.item(
                            "Save",
                            context_menu.shortcut("⌘S"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.group_label("Edit"),
                        context_menu.item(
                            "Undo",
                            context_menu.shortcut("⌘Z"),
                        ),
                        context_menu.item(
                            "Redo",
                            context_menu.shortcut("⇧⌘Z"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.item(
                            "Cut",
                            context_menu.shortcut("⌘X"),
                        ),
                        context_menu.item(
                            "Copy",
                            context_menu.shortcut("⌘C"),
                        ),
                        context_menu.item(
                            "Paste",
                            context_menu.shortcut("⌘V"),
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.item(
                            "Delete",
                            context_menu.shortcut("⌫"),
                            variant="destructive",
                        ),
                    ),
                ),
            ),
        ),
    )
```


## Checkboxes

Use `context_menu.checkbox_item` for toggles.


```python
def context_menu_checkboxes() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            "Show Bookmarks Bar",
                            default_checked=True,
                        ),
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            "Show Full URLs",
                        ),
                        context_menu.checkbox_item(
                            context_menu.checkbox_item_indicator(
                                hi("Tick02Icon", class_name="size-4")
                            ),
                            "Show Developer Tools",
                            default_checked=True,
                        ),
                    ),
                ),
            ),
        ),
    )
```


## Radio

Use `context_menu.radio_item` for exclusive choices.


```python
def context_menu_radio() -> rx.Component:
    return context_menu.root(
        context_menu.trigger(
            rx.el.span(
                "Right click here",
                class_name="hidden pointer-fine:inline-block",
            ),
            rx.el.span(
                "Long press here",
                class_name="hidden pointer-coarse:inline-block",
            ),
            class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
        ),
        context_menu.portal(
            context_menu.positioner(
                context_menu.popup(
                    context_menu.group(
                        context_menu.group_label("People"),
                        context_menu.radio_group(
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "Pedro Duarte",
                                value="pedro",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "Colm Tuite",
                                value="colm",
                            ),
                            value=selected_user.value,
                            on_value_change=selected_user.set_value,
                        ),
                    ),
                    context_menu.separator(),
                    context_menu.group(
                        context_menu.group_label("Theme"),
                        context_menu.radio_group(
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "Light",
                                value="light",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "Dark",
                                value="dark",
                            ),
                            context_menu.radio_item(
                                context_menu.radio_item_indicator(
                                    hi("CheckIcon", class_name="size-4")
                                ),
                                "System",
                                value="system",
                            ),
                            value=selected_theme.value,
                            on_value_change=selected_theme.set_value,
                        ),
                    ),
                ),
            ),
        ),
    )
```



## Sides

Control submenu placement with side and align props.


```python
def context_menu_sides() -> rx.Component:
    return rx.el.div(
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (top)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (top)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="top",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (right)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (right)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="right",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (bottom)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (bottom)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="bottom",
                ),
            ),
        ),
        context_menu.root(
            context_menu.trigger(
                rx.el.span(
                    "Right click (left)",
                    class_name="hidden pointer-fine:inline-block",
                ),
                rx.el.span(
                    "Long press (left)",
                    class_name="hidden pointer-coarse:inline-block",
                ),
                class_name="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed border-input text-sm",
            ),
            context_menu.portal(
                context_menu.positioner(
                    context_menu.popup(
                        context_menu.group(
                            context_menu.item("Back"),
                            context_menu.item("Forward"),
                            context_menu.item("Reload"),
                        ),
                    ),
                    side="left",
                ),
            ),
        ),
        class_name="grid w-full max-w-sm grid-cols-2 gap-4",
    )
```

