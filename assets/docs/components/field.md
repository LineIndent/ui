

# Field

Combine labels, controls, and help text to compose accessible form fields and grouped inputs.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component field
```

### Manual Installation

```python
from typing import Literal

from reflex.components.component import ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.el import elements

from components.ui.separator import separator

LiteralOrientation = Literal["vertical", "horizontal", "responsive"]
LiteralLegendVariant = Literal["legend", "label"]


class ClassNames:
    FIELD_SET = "flex flex-col gap-4 has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3"

    FIELD_LEGEND = "mb-1.5 font-medium data-[variant=label]:text-sm data-[variant=legend]:text-base"

    FIELD_GROUP = "group/field-group @container/field-group flex flex-col gap-5 data-[slot=checkbox-group]:gap-3 *:data-[slot=field-group]:gap-4"

    FIELD_ROOT_BASE = (
        "group/field flex w-full gap-2 data-[invalid=true]:text-destructive"
    )

    FIELD_ROOT_ORIENTATIONS = {
        "vertical": "flex-col *:w-full [&>.sr-only]:w-auto",
        "horizontal": "flex-row items-center has-[>[data-slot=field-content]]:items-start *:data-[slot=field-label]:flex-auto has-[>[data-slot=field-content]]:[&>[data-slot=checkbox]]:mt-[2.5px]",
        "responsive": "flex-col *:w-full @md/field-group:flex-row @md/field-group:items-center @md/field-group:*:w-auto @md/field-group:has-[>[data-slot=field-content]]:items-start @md/field-group:*:data-[slot=field-label]:flex-auto [&>.sr-only]:w-auto @md/field-group:has-[>[data-slot=field-content]]:[&>[data-slot=checkbox]]:mt-px",
    }

    FIELD_CONTENT = "group/field-content flex flex-1 flex-col gap-0.5 leading-snug"

    FIELD_LABEL = "group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50 has-data-checked:border-primary/30 has-data-checked:bg-primary/5 has-[>[data-slot=field]]:rounded-lg has-[>[data-slot=field]]:border border-input *:data-[slot=field]:p-2.5 dark:has-data-checked:border-primary/20 dark:has-data-checked:bg-primary/10 has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col"

    FIELD_TITLE = "flex w-fit items-center gap-2 text-sm font-medium group-data-[disabled=true]/field:opacity-50"

    FIELD_DESCRIPTION = "text-left text-sm leading-normal font-normal text-muted-foreground group-has-data-horizontal/field:text-balance [[data-variant=legend]+&]:-mt-1.5 last:mt-0 nth-last-2:-mt-1 [&>a]:underline [&>a]:underline-offset-4 [&>a:hover]:text-primary"

    FIELD_SEPARATOR = (
        "relative -my-2 h-5 text-sm group-data-[variant=outline]/field-group:-mb-2"
    )

    FIELD_ERROR = "text-sm font-normal text-destructive"


class FieldSet(elements.Fieldset):
    @classmethod
    def create(cls, *children, **props) -> elements.Fieldset:
        props["data-slot"] = "field-set"
        props["class_name"] = (
            f"{ClassNames.FIELD_SET} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldLegend(elements.Legend):
    variant: Var[LiteralLegendVariant]

    @classmethod
    def create(cls, *children, **props) -> elements.Legend:
        props["data-slot"] = "field-legend"
        variant = props.pop("variant", "legend")
        props["data-variant"] = variant
        props["class_name"] = (
            f"{ClassNames.FIELD_LEGEND} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldGroup(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["data-slot"] = "field-group"
        props["class_name"] = (
            f"{ClassNames.FIELD_GROUP} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldRoot(elements.Div):
    orientation: Var[LiteralOrientation]

    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["role"] = "group"
        props["data-slot"] = "field"

        orientation = props.pop("orientation", "vertical")
        props["data-orientation"] = orientation

        orientation_styles = ClassNames.FIELD_ROOT_ORIENTATIONS.get(orientation, "")

        props["class_name"] = (
            f"{ClassNames.FIELD_ROOT_BASE} {orientation_styles} {props.get('class_name', '')}".strip()
        )

        return super().create(*children, **props)


class FieldContent(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["data-slot"] = "field-content"
        props["class_name"] = (
            f"{ClassNames.FIELD_CONTENT} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldLabel(elements.Label):
    @classmethod
    def create(cls, *children, **props) -> elements.Label:
        props["data-slot"] = "field-label"
        props["class_name"] = (
            f"{ClassNames.FIELD_LABEL} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldTitle(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["data-slot"] = "field-label"
        props["class_name"] = (
            f"{ClassNames.FIELD_TITLE} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldDescription(elements.P):
    @classmethod
    def create(cls, *children, **props) -> elements.P:
        props["data-slot"] = "field-description"
        props["class_name"] = (
            f"{ClassNames.FIELD_DESCRIPTION} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class FieldSeparator(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["data-slot"] = "field-separator"
        props["data-content"] = "true" if children else "false"
        props["class_name"] = (
            f"{ClassNames.FIELD_SEPARATOR} {props.get('class_name', '')}".strip()
        )

        inner_elements = [separator(class_name="absolute inset-0 top-1/2")]
        if children:
            inner_elements.append(
                elements.Span(
                    *children,
                    data_slot="field-separator-content",
                    class_name="relative mx-auto block w-fit bg-background px-2 text-muted-foreground",
                )
            )
        return super().create(*inner_elements, **props)


class FieldError(elements.Div):
    @classmethod
    def create(cls, *children, **props) -> elements.Div:
        props["role"] = "alert"
        props["data-slot"] = "field-error"
        props["class_name"] = (
            f"{ClassNames.FIELD_ERROR} {props.get('class_name', '')}".strip()
        )
        return super().create(*children, **props)


class Field(ComponentNamespace):
    set = staticmethod(FieldSet.create)
    legend = staticmethod(FieldLegend.create)
    group = staticmethod(FieldGroup.create)
    root = staticmethod(FieldRoot.create)
    content = staticmethod(FieldContent.create)
    label = staticmethod(FieldLabel.create)
    title = staticmethod(FieldTitle.create)
    description = staticmethod(FieldDescription.create)
    separator = staticmethod(FieldSeparator.create)
    error = staticmethod(FieldError.create)
    class_names = ClassNames


field = Field()
```


# Usage


```python
from components.ui.field import Field
```


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


```python
field.root(
    field.content(
        field.label(),
        field.title(),
        field.description(),
    ),
    field.error(),
)
```



- `field.root` is the core wrapper for a single field.

- `field.content` is a flex column that groups label and description. Not required if you have no description.

- Wrap related fields with `field.group`, and use `field.set` with `field.legend` for semantic grouping.

# Examples

## General


```python
def field_demo() -> rx.Component:
    return rx.el.div(
        rx.el.form(
            field.group(
                field.set(
                    field.legend("Payment Method"),
                    field.description("All transactions are secure and encrypted"),
                    field.group(
                        field.root(
                            field.label("Name on Card", html_for="checkout-card-name"),
                            input(
                                id="checkout-card-name",
                                placeholder="Evil Rabbit",
                                required=True,
                            ),
                        ),
                        field.root(
                            field.label("Card Number", html_for="checkout-card-number"),
                            input(
                                id="checkout-card-number",
                                placeholder="1234 5678 9012 3456",
                                required=True,
                            ),
                            field.description("Enter your 16-digit card number"),
                        ),
                        rx.el.div(
                            field.root(
                                field.label("Month", html_for="checkout-exp-month"),
                                select.root(
                                    select.trigger(
                                        select.value(),
                                        select.icon(),
                                        id="checkout-exp-month",
                                    ),
                                    select.portal(
                                        select.positioner(
                                            select.popup(
                                                select.group(
                                                    *[
                                                        select.item(
                                                            select.item_text(
                                                                item["label"]
                                                            ),
                                                            select.item_indicator(),
                                                            value=item["value"],
                                                        )
                                                        for item in months
                                                    ]
                                                )
                                            )
                                        )
                                    ),
                                    items=months,
                                    default_value="MM",
                                ),
                            ),
                            field.root(
                                field.label("Year", html_for="checkout-exp-year"),
                                select.root(
                                    select.trigger(
                                        select.value(),
                                        select.icon(),
                                        id="checkout-exp-year",
                                    ),
                                    select.portal(
                                        select.positioner(
                                            select.popup(
                                                select.group(
                                                    *[
                                                        select.item(
                                                            select.item_text(
                                                                item["label"]
                                                            ),
                                                            select.item_indicator(),
                                                            value=item["value"],
                                                        )
                                                        for item in years
                                                    ]
                                                )
                                            )
                                        )
                                    ),
                                    items=years,
                                    default_value="YYYY",
                                ),
                            ),
                            field.root(
                                field.label("CVV", html_for="checkout-cvv"),
                                input(
                                    id="checkout-cvv",
                                    placeholder="123",
                                    required=True,
                                ),
                            ),
                            class_name="grid grid-cols-3 gap-4",
                        ),
                    ),
                ),
                field.separator(),
                field.set(
                    field.legend("Billing Address"),
                    field.description(
                        "The billing address associated with your payment method"
                    ),
                    field.group(
                        field.root(
                            checkbox.root(
                                checkbox.indicator(),
                                id="checkout-same-as-shipping",
                                default_checked=True,
                            ),
                            field.label(
                                "Same as shipping address",
                                html_for="checkout-same-as-shipping",
                                class_name="font-normal",
                            ),
                            orientation="horizontal",
                        )
                    ),
                ),
                field.set(
                    field.group(
                        field.root(
                            field.label("Comments", html_for="checkout-comments"),
                            textarea(
                                id="checkout-comments",
                                placeholder="Add any additional comments",
                                class_name="resize-none",
                            ),
                        )
                    )
                ),
                field.root(
                    button("Submit", type="submit"),
                    button("Cancel", variant="outline", type="button"),
                    orientation="horizontal",
                ),
            )
        ),
        class_name="w-full max-w-md my-10",
    )
```


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
