

# Input Group

Add addons, buttons, and helper content to inputs.

# Installation

Copy the following code into your app directory.


> **Error: 'input_group' not found in registry**


# Usage


> **Error: 'input_group' not found in registry**


# Anatomy 
Use the following composition to build an `Input Group` component.


```python
input_group.root(
    input_group.input(placeholder="Search..."),
    input_group.addon(),
)
```


# Align

Use the `align` prop on `input_group.addon` to position the addon relative to the input.

>For proper focus management, **input_group.addon** should always be placed after **input_group.input** or **input_group.textarea** in the DOM. Use the **align** prop to visually position the addon.


## inline-start

Use `align="inline-start"` to position the addon at the start of the input. This is the default.


```python
def input_group_inline_start() -> rx.Component:
    return input_group.root(
        input_group.input(
            id="inline-start-input",
            placeholder="Search...",
        ),
        input_group.addon(
            hi("SearchIcon", class_name="text-muted-foreground"),
            align="inline-start",
        ),
        class_name="max-w-sm",
    )
```


## inline-end

Use `align="inline-end"` to position the addon at the end of the input.


```python
def input_group_inline_end() -> rx.Component:
    return input_group.root(
        input_group.input(
            id="inline-end-input",
            type="password",
            placeholder="Enter password",
        ),
        input_group.addon(
            hi("EyeOffIcon", class_name="text-muted-foreground"),
            align="inline-end",
        ),
        class_name="max-w-sm",
    )
```


## block-start

Use `align="block-start"` to position the addon above the input.


```python
def input_group_block_start() -> rx.Component:
    return rx.el.div(
        field.root(
            field.label("Input", html_for="block-start-input"),
            field.content(
                input_group.root(
                    input_group.input(
                        id="block-start-input",
                        placeholder="Enter your name",
                    ),
                    input_group.addon(
                        input_group.text("Full Name"),
                        align="block-start",
                    ),
                    class_name="h-auto",
                )
            ),
            field.description("Header positioned above the input."),
            orientation="vertical",
        ),
        field.root(
            field.label("Textarea", html_for="block-start-textarea"),
            field.content(
                input_group.root(
                    input_group.textarea(
                        id="block-start-textarea",
                        placeholder="console.log('Hello, world!');",
                        class_name="font-mono text-sm",
                    ),
                    input_group.addon(
                        hi("FileCodeIcon", class_name="text-muted-foreground"),
                        input_group.text("script.py", class_name="font-mono"),
                        input_group.button(
                            hi("CopyIcon"),
                            rx.el.span("Copy", class_name="sr-only"),
                            size="icon-xs",
                            class_name="ml-auto",
                        ),
                        align="block-start",
                    ),
                )
            ),
            field.description("Header positioned above the textarea."),
            orientation="vertical",
        ),
        class_name="flex flex-col gap-y-6 max-w-sm w-full",
    )
```


## block-end

Use `align="block-end"` to position the addon below the input.


```python
def input_group_block_end() -> rx.Component:
    return rx.el.div(
        field.root(
            field.label("Input", html_for="block-end-input"),
            field.content(
                input_group.root(
                    input_group.input(
                        id="block-end-input",
                        placeholder="Enter amount",
                    ),
                    input_group.addon(
                        input_group.text("USD"),
                        align="block-end",
                    ),
                    class_name="h-auto",
                )
            ),
            field.description("Footer positioned below the input."),
            orientation="vertical",
        ),
        field.root(
            field.label("Textarea", html_for="block-end-textarea"),
            field.content(
                input_group.root(
                    input_group.textarea(
                        id="block-end-textarea",
                        placeholder="Write a comment...",
                    ),
                    input_group.addon(
                        input_group.text("0/280"),
                        input_group.button(
                            "Post",
                            variant="default",
                            size="sm",
                            class_name="ml-auto",
                        ),
                        align="block-end",
                    ),
                )
            ),
            field.description("Footer positioned below the textarea."),
            orientation="vertical",
        ),
        class_name="flex flex-col gap-y-6 max-w-sm w-full",
    )
```


# Examples

## Icons

```python
def input_group_icons() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(placeholder="Search..."),
            input_group.addon(
                hi("Search01Icon", class_name="text-muted-foreground"),
                align="inline-start",
            ),
        ),
        input_group.root(
            input_group.input(type="email", placeholder="Enter your email"),
            input_group.addon(
                hi("Mail01Icon", class_name="text-muted-foreground"),
                align="inline-start",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Card number"),
            input_group.addon(
                hi("CreditCardIcon", class_name="text-muted-foreground"),
                align="inline-start",
            ),
            input_group.addon(
                hi("Tick02Icon", class_name="text-muted-foreground"),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Card number"),
            input_group.addon(
                hi("StarIcon", class_name="text-muted-foreground"),
                hi("InformationCircleIcon", class_name="text-muted-foreground"),
                align="inline-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-6",
    )
```


## Text

```python
def input_group_text() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.addon(
                input_group.text("$"),
                align="inline-start",
            ),
            input_group.input(placeholder="0.00"),
            input_group.addon(
                input_group.text("USD"),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.addon(
                input_group.text("https://"),
                align="inline-start",
            ),
            input_group.input(
                placeholder="example.com",
                class_name="!pl-0.5",
            ),
            input_group.addon(
                input_group.text(".com"),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Enter your username"),
            input_group.addon(
                input_group.text("@company.com"),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.textarea(placeholder="Enter your message"),
            input_group.addon(
                input_group.text(
                    "120 characters left",
                    class_name="text-xs text-muted-foreground",
                ),
                align="block-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-6",
    )
```


## Button

```python
def input_group_button() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(
                placeholder="https://ui.buridan.dev/",
                read_only=True,
            ),
            input_group.addon(
                input_group.button(
                    rx.cond(
                        _input_copy.value,
                        hi("Tick02Icon"),
                        hi("Copy01Icon"),
                    ),
                    aria_label="Copy",
                    title="Copy",
                    size="icon-xs",
                    on_click=[
                        _input_copy.set_value(True),
                        rx.set_clipboard("https://ui.buridan.dev/"),
                    ],
                    on_mouse_down=rx.call_function(
                        _input_copy.set_value(False)
                    ).debounce(1500),
                ),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.addon(
                input_group.button(
                    hi("InformationCircleIcon"),
                    variant="secondary",
                    size="icon-xs",
                ),
                align="inline-start",
            ),
            input_group.addon(
                "https://",
                class_name="pl-1.5 text-muted-foreground",
                align="inline-start",
            ),
            input_group.input(id="input-secure-19"),
            input_group.addon(
                input_group.button(
                    hi(
                        "StarIcon",
                        class_name=rx.cond(
                            _input_star.value,
                            "text-blue-600 fill-blue-600",
                            "",
                        ),
                    ),
                    size="icon-xs",
                    on_click=_input_star.set_value(~_input_star.value),
                ),
                align="inline-end",
            ),
            class_name="[--radius:9999px]",
        ),
        input_group.root(
            input_group.input(placeholder="Type to search..."),
            input_group.addon(
                input_group.button(
                    "Search",
                    variant="secondary",
                ),
                align="inline-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-6",
    )
```


## Spinner

```python
def input_group_spinner() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(placeholder="Searching..."),
            input_group.addon(
                spinner(),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Processing..."),
            input_group.addon(
                spinner(),
                align="inline-start",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Saving changes..."),
            input_group.addon(
                input_group.text("Saving..."),
                spinner(),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Refreshing data..."),
            input_group.addon(
                spinner(),
                align="inline-start",
            ),
            input_group.addon(
                input_group.text(
                    "Please wait...",
                    class_name="text-muted-foreground",
                ),
                align="inline-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-4",
    )
```


## Dropdown

```python
def input_group_dropdown() -> rx.Component:
    return rx.el.div(
        input_group.root(
            input_group.input(placeholder="Enter file name"),
            input_group.addon(
                menu.root(
                    menu.trigger(
                        render_=input_group.button(
                            hi("MoreHorizontal"),
                            variant="ghost",
                            aria_label="More",
                            size="icon-xs",
                        )
                    ),
                    menu.portal(
                        menu.positioner(
                            menu.popup(
                                menu.group(
                                    menu.item("Settings"),
                                    menu.item("Copy path"),
                                    menu.item("Open location"),
                                )
                            ),
                            align="end",
                        )
                    ),
                ),
                align="inline-end",
            ),
        ),
        input_group.root(
            input_group.input(placeholder="Enter search query"),
            input_group.addon(
                menu.root(
                    menu.trigger(
                        render_=input_group.button(
                            "Search In... ",
                            hi("ChevronDownIcon", class_name="size-3 ml-1 inline"),
                            variant="ghost",
                            class_name="!pr-1.5 text-xs",
                        )
                    ),
                    menu.portal(
                        menu.positioner(
                            menu.popup(
                                menu.group(
                                    menu.item("Documentation"),
                                    menu.item("Blog Posts"),
                                    menu.item("Changelog"),
                                )
                            ),
                            align="end",
                        )
                    ),
                ),
                align="inline-end",
            ),
        ),
        class_name="grid w-full max-w-sm gap-4",
    )
```


# API Reference

## input_group.root

The main component that wraps inputs and addons.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` |         |


## input_group.addon

Displays icons, text, buttons, or other content alongside inputs.

>For proper focus navigation, the `input_group.addon` component should be placed after the input. Set the `align` prop to position the addon.

| Prop        | Type                                                             | Default          |
| ----------- | ---------------------------------------------------------------- | ---------------- |
| `align`     | `"inline-start" \| "inline-end" \| "block-start" \| "block-end"` | `"inline-start"` |
| `class_name` | `string`                                                         |                  |


>For **input_group.input**, use the **inline-start** or **inline-end** alignment. For **input_group.textarea**, use the **block-start** or **block-end** alignment.

The `input_group.addon` component can have multiple `input_group.button` components and icons.

## input_group.button

Displays buttons within input groups. See the [Button](/docs/components/button) docs for more information. 

| Prop        | Type                                                                          | Default   |
| ----------- | ----------------------------------------------------------------------------- | --------- |
| `size`      | `"xs" \| "icon-xs" \| "sm" \| "icon-sm"`                                      | `"xs"`    |
| `variant`   | `"default" \| "destructive" \| "outline" \| "secondary" \| "ghost" \| "link"` | `"ghost"` |
| `class_name` | `string`                                                                      |           |

## input_group.input

Replacement for `input()` when building input groups. This component has the input group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` |         |

All other props are passed through to the underlying `Input()` component.

## input_group.textarea

Replacement for `textarea()` when building input groups. This component has the textarea group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` |         |

All other props are passed through to the underlying `textarea()` component.
