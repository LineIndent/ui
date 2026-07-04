---
title: "Field"
description: "Combine labels, controls, and help text to compose accessible form fields and grouped inputs."
order: 0
---

# Field

Combine labels, controls, and help text to compose accessible form fields and grouped inputs.

# Installation

Copy the following code into your app directory.

--INSTALL(field)--

# Usage

--USAGE(field)--

# Composition

## field.root

A single control with label, helper text, and validation.

```python
field.root
├── field.label
├── Input / Textarea / switch.root / select.root
├── field.description
└── field.error
```

## field.group

Related fields in one group. Use `field.separator` between sections when needed.

```python
field.group
├── field.root
│   ├── field.label
│   ├── Input / Textarea / switch.root / select.root
│   ├── field.description
│   └── field.error
├── field.separator
└── field.root
    ├── field.label
    └── Input / Textarea / switch.root / select.root
```

## field.set

Semantic grouping with a legend and description, usually containing a `field.group`.

```python
field.set
├── field.legend
├── field.description
└── field.group
    ├── field.root
    │   ├── field.label
    │   ├── Input / Textarea / switch.root / select.root
    │   ├── field.description
    │   └── field.error
    └── field.root
        ├── field.label
        └── Input / Textarea / switch.root / select.root
```

# Anatomy 
Use the following composition to build a `Field` component.

--ANATOMY(field)--


- `field.root` is the core wrapper for a single field.

- `field.content` is a flex column that groups label and description. Not required if you have no description.

- Wrap related fields with `field.group`, and use `field.set` with `field.legend` for semantic grouping.

# Examples

## General

--DEMO(field_demo)--

# Responsive Layout

- **Vertical fields**: Default orientation stacks label, control, and helper text—ideal for mobile-first layouts.  

- **Horizontal fields**: Set `orientation="horizontal"` on `field.root` to align the label and control side-by-side. Pair with `field.content` to keep descriptions aligned.  

- **Responsive fields**: Set `orientation="responsive"` for automatic column layouts inside container-aware parents.

# Validation and Errors

- Add `data_invalid="true"` to `field.root` to switch the entire block into an error state.

- Add `aria_invalid="true"` on the input itself for assistive technologies.

- Render `field.error` immediately after the control or inside `field.content` to keep error messages aligned with the field.

```python
field.root(
    field.label("Email", html_for="email"),
    input(id="email", type="email", aria_invalid="true"),
    field.error("Enter a valid email address."),
    data_invalid="true",
)
```

# API Reference

## field.set

Container that renders a semantic `fieldset` with spacing presets.

| Prop | Type | Default |
| --- | --- | --- |
| `class_name` | `str` | |

```python
field.set_(
    field.legend("Delivery"),
    field.group(),
)
```

## field.legend

Legend element for a `field.set_`. Switch to the `"label"` variant to align with standard label sizing.

| Prop | Type | Default |
| --- | --- | --- |
| `variant` | `"legend" | "label"` | `"legend"` |
| `class_name` | `str` |  |

```python
field.legend("Notification Preferences", variant="label")
```

The `field.legend` has two variants: `legend` and `label`. The `label` variant applies standard input label sizing and alignment, which is useful if you are stacking nested fieldsets.

## field.group

Layout wrapper that stacks `field.root` components and enables container queries for responsive orientations.

| Prop | Type | Default |
| --- | --- | --- |
| `class_name` | `str` |  |

```python
field.group(
    field.root(),
    field.root(),
    class_name="@container/field-group flex flex-col gap-6",
)
```

## field.root

The core wrapper for a single field. Provides orientation control, invalid state styling, and spacing configurations.

| Prop | Type | Default |
| --- | --- | --- |
| `orientation` | `"vertical" | "horizontal" | "responsive"` | `"vertical"` |
| `class_name` | `str` |  |
| `data_invalid` | `str` |  |

```python
field.root(
    field.label("Remember me", html_for="remember"),
    switch.root(id="remember"),
    orientation="horizontal",
)
```

## field.content

Flex column that groups control and descriptions when the label sits beside the control. Not required if you have no layout description block.

| Prop | Type | Default |
| --- | --- | --- |
| `class_name` | `str` |  |

```python
field.root(
    checkbox.root(id="notifications"),
    field.content(
        field.label("Notifications", html_for="notifications"),
        field.description("Email, SMS, and push options."),
    ),
)
```

## field.label

Label styled for both direct inputs and nested `field` child items.

| Prop | Type | Default |
| --- | --- | --- |
| `html_for` | `str` |  |
| `class_name` | `str` |  |

```python
field.label("Email", html_for="email")
```

## field.title

Renders a standalone title with matching label typography properties inside a `field.content` node block.

| Prop | Type | Default |
| --- | --- | --- |
| `class_name` | `str` |  |

```python
field.content(
    field.title("Enable Touch ID"),
    field.description("Unlock your device faster."),
)
```

## field.description

Helper text slot that automatically line-balances lengthy strings cleanly when utilized inside horizontal configurations.

| Prop | Type | Default |
| --- | --- | --- |
| `class_name` | `str` |  |

```python
field.description("We never share your email with anyone.")
```

## field.separator

Visual divider rule used to separate sections or categories inside a wrapping `field.group` component. Accepts optional inline children contents.

| Prop | Type | Default |
| --- | --- | --- |
| `class_name` | `str` |  |

```python
field.separator("Or continue with")
```

## field.error

Accessible error notification typography container block configured automatically with standard application state layout variables (`role="alert"`).

| Prop | Type | Default |
| --- | --- | --- |
| `class_name` | `str` |  |

```python
field.error("Invalid passcode combination provided.")
```
