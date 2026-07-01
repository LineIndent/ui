

# Breadcrumb

Displays the path to the current resource using a hierarchy of links.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component breadcrumb
```

### Manual Installation

```python
import reflex as rx

from ..icons.hugeicon import hi
from ..utils.twmerge import cn


class Breadcrumb:
    @classmethod
    def root(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["aria-label"] = "breadcrumb"

        props["data-slot"] = "breadcrumb"

        return rx.el.nav(
            *children,
            class_name=cn(custom_classes),
            **props,
        )

    @classmethod
    def list(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-list"

        base_classes = (
            "flex flex-wrap items-center gap-1.5 text-sm wrap-break-word "
            "text-muted-foreground"
        )

        return rx.el.ol(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def item(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-item"

        base_classes = "inline-flex items-center gap-1"

        return rx.el.li(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def link(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-link"

        props.setdefault("href", "#")

        base_classes = "transition-colors hover:text-foreground no-underline"

        return rx.el.a(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def page(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-page"

        props["role"] = "link"

        props["aria-disabled"] = "true"

        props["aria-current"] = "page"

        base_classes = "font-normal text-foreground"

        return rx.el.span(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def separator(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-separator"

        props["role"] = "presentation"

        props["aria-hidden"] = "true"

        base_classes = "[&>svg]:size-3.5"

        if not children:
            children = (hi("ArrowRight01Icon"),)

        return rx.el.li(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def ellipsis(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-ellipsis"

        props["role"] = "presentation"

        props["aria-hidden"] = "true"

        base_classes = "flex size-5 items-center justify-center [&>svg]:size-4"

        if not children:
            children = (
                rx.icon(tag="ellipsis"),
                rx.el.span("More", class_name="sr-only"),
            )

        return rx.el.span(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )


breadcrumb = Breadcrumb
```



# Anatomy 
Use the following composition to build a `Breadcrumb` component.


```python
breadcrumb(
    breadcrumb_list(
        breadcrumb_item(
            breadcrumb_link(),
        ),
        breadcrumb_separator(),
        breadcrumb_item(
            breadcrumb_page(),
        ),
    ),
)
```


# Examples

## Basic 
A basic breadcrumb with a home link and a components link.


```python
def breadcrumb_basic() -> rx.Component:
    return breadcrumb.root(
        breadcrumb.list(
            breadcrumb.item(
                breadcrumb.link("Home", href="#"),
            ),
            breadcrumb.separator(),
            breadcrumb.item(
                breadcrumb.link("Components", href="#"),
            ),
            breadcrumb.separator(),
            breadcrumb.item(
                breadcrumb.page("Breadcrumb"),
            ),
        )
    )
```


## Custom Separator
Use a custom component as `children` for `breadcrumb.separator` to create a custom separator.


```python
def breadcrumb_custom_separator() -> rx.Component:
    return breadcrumb.root(
        breadcrumb.list(
            breadcrumb.item(
                breadcrumb.link("Home", href="#"),
            ),
            breadcrumb.separator(hi("LinerIcon")),
            breadcrumb.item(
                breadcrumb.link("Components", href="#"),
            ),
            breadcrumb.separator(hi("LinerIcon")),
            breadcrumb.item(
                breadcrumb.page("Breadcrumb"),
            ),
        )
    )
```


## Dropdown

You can compose `breadcrumb.item` with a `menu.root` to create a dropdown in the breadcrumb.


```python
def breadcrumb_dropdown_demo() -> rx.Component:
    return breadcrumb.root(
        breadcrumb.list(
            breadcrumb.item(
                breadcrumb.link("Home", href="#"),
            ),
            breadcrumb.separator(hi("LinerIcon")),
            breadcrumb.item(
                menu.root(
                    menu.trigger(
                        render_=rx.el.button(
                            "Components",
                            hi(
                                "ArrowDown01Icon",
                                custom_attrs={"data-icon": "inline-end"},
                                class_name="size-4",
                            ),
                            class_name="flex flex-row items-center gap-x-2",
                        )
                    ),
                    menu.portal(
                        menu.positioner(
                            menu.popup(
                                menu.group(
                                    menu.item("Documentation"),
                                    menu.item("Themes"),
                                    menu.item("GitHub"),
                                ),
                                align="start",
                            )
                        ),
                    ),
                ),
            ),
            breadcrumb.separator(hi("LinerIcon")),
            breadcrumb.item(
                breadcrumb.page("Breadcrumb"),
            ),
        )
    )
```


## Collapsed 

We provide a `breadcrumb.ellipsis` component to show a collapsed state when the breadcrumb is too long.


```python
def breadcrumb_ellipsis() -> rx.Component:
    return breadcrumb.root(
        breadcrumb.list(
            breadcrumb.item(
                breadcrumb.link("Home", href="#"),
            ),
            breadcrumb.separator(),
            breadcrumb.item(
                breadcrumb.ellipsis(),
            ),
            breadcrumb.separator(),
            breadcrumb.item(
                breadcrumb.link("Components", href="#"),
            ),
            breadcrumb.separator(),
            breadcrumb.item(
                breadcrumb.page("Breadcrumb"),
            ),
        )
    )
```


# API Reference

## breadcrumb.root

The `breadcrumb.root` component is the root navigation element that wraps all breadcrumb components.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## breadcrumb.list

The `breadcrumb.list` component displays the ordered list of breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## breadcrumb.item

The `breadcrumb.item` component wraps individual breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## breadcrumb.link

The `breadcrumb.link` component displays a clickable link in the breadcrumb.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## breadcrumb.page

The `breadcrumb.page` component displays the current page in the breadcrumb (non-clickable).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## breadcrumb.separator

The `breadcrumb.separator` component displays a separator between breadcrumb items. You can pass custom children to override the default separator icon.

| Prop        | Type              | Default |
| ----------- | ----------------- | ------- |
| `children`  | `rx.Component` | -       |
| `class_name` | `string`          | -       |

## breadcrumb.ellipsis

The `breadcrumb.ellipsis` component displays an ellipsis indicator for collapsed breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |
