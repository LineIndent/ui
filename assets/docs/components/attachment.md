

# Attachment

Displays a file or image attachment with media, metadata, upload state, and actions.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component attachment
```

### Manual Installation

```python
"""Attachment component — file and image attachment previews for chat UI."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..ui.button import button
from ..utils.twmerge import cn

AttachmentOrientation = Literal["horizontal", "vertical"]
AttachmentSize = Literal["default", "sm", "xs"]
AttachmentState = Literal["idle", "uploading", "processing", "error", "done"]
AttachmentMediaVariant = Literal["icon", "image"]


class ClassNames:
    ROOT_BASE = (
        "group/attachment relative flex w-full max-w-full min-w-0 shrink-0 flex-wrap "
        "rounded-2xl border border-input bg-card text-card-foreground transition-colors "
        "focus-within:ring-1 focus-within:ring-ring/30 "
        "has-[>a,>button]:hover:bg-muted/50 "
        "data-[state=error]:border-destructive/30 "
        "data-[state=idle]:border-dashed"
    )

    SIZES: dict[str, str] = {
        "default": (
            "gap-2 text-sm "
            "has-data-[slot=attachment-content]:px-2.5 "
            "has-data-[slot=attachment-content]:py-2 "
            "has-data-[slot=attachment-media]:p-2"
        ),
        "sm": (
            "gap-2.5 text-xs "
            "has-data-[slot=attachment-content]:px-2 "
            "has-data-[slot=attachment-content]:py-1.5 "
            "has-data-[slot=attachment-media]:p-1.5"
        ),
        "xs": (
            "gap-1.5 rounded-xl text-xs "
            "has-data-[slot=attachment-content]:px-1.5 "
            "has-data-[slot=attachment-content]:py-1 "
            "has-data-[slot=attachment-media]:p-1"
        ),
    }

    ORIENTATIONS: dict[str, str] = {
        "horizontal": "min-w-40 items-center",
        "vertical": "w-24 flex-col has-data-[slot=attachment-content]:w-30",
    }

    MEDIA_BASE = (
        "relative flex aspect-square w-10 shrink-0 items-center justify-center "
        "overflow-hidden rounded-lg bg-muted text-foreground "
        "group-data-[orientation=vertical]/attachment:w-full "
        "group-data-[size=sm]/attachment:w-8 "
        "group-data-[size=xs]/attachment:w-7 "
        "group-data-[size=xs]/attachment:rounded-md "
        "group-data-[state=error]/attachment:bg-destructive/10 "
        "group-data-[state=error]/attachment:text-destructive "
        "[&_svg]:pointer-events-none "
        "[&_svg:not([class*='size-'])]:size-4 "
        "group-data-[orientation=vertical]/attachment:[&_svg:not([class*='size-'])]:size-6 "
        "group-data-[size=xs]/attachment:[&_svg:not([class*='size-'])]:size-3.5"
    )

    MEDIA_VARIANTS: dict[str, str] = {
        "icon": "",
        "image": (
            "opacity-60 "
            "group-data-[state=done]/attachment:opacity-100 "
            "group-data-[state=idle]/attachment:opacity-100 "
            "*:[img]:aspect-square *:[img]:w-full *:[img]:object-cover"
        ),
    }

    CONTENT = (
        "max-w-full min-w-0 flex-1 leading-tight "
        "group-data-[orientation=vertical]/attachment:px-1"
    )

    TITLE = (
        "block max-w-full min-w-0 truncate font-medium "
        "group-data-[state=processing]/attachment:shimmer "
        "group-data-[state=uploading]/attachment:shimmer"
    )

    DESCRIPTION = (
        "mt-0.5 block min-w-0 max-w-full truncate text-xs text-muted-foreground "
        "group-data-[state=error]/attachment:text-destructive/80"
    )

    ACTIONS = (
        "relative z-20 flex shrink-0 items-center "
        "group-data-[orientation=vertical]/attachment:absolute "
        "group-data-[orientation=vertical]/attachment:top-3 "
        "group-data-[orientation=vertical]/attachment:right-3 "
        "group-data-[orientation=vertical]/attachment:gap-1"
    )

    TRIGGER = "absolute inset-0 z-10 outline-none"

    GROUP = (
        "flex scroll-fade-x min-w-0 snap-x snap-mandatory scroll-px-1 scrollbar-none gap-3 "
        "overflow-x-auto overscroll-x-contain py-1 "
        "*:data-[slot=attachment]:flex-none "
        "*:data-[slot=attachment]:snap-start"
    )


def attachment_root(
    *children,
    orientation: AttachmentOrientation = "horizontal",
    size: AttachmentSize = "default",
    state: AttachmentState = "done",
    class_name: str = "",
    **props,
) -> rx.Component:
    """
    Root attachment container.

    orientation: horizontal (default) | vertical
    size:        default | sm | xs
    state:       idle | uploading | processing | error | done (default)
    """
    return rx.el.div(
        *children,
        data_slot="attachment",
        data_state=state,
        data_size=size,
        data_orientation=orientation,
        class_name=cn(
            ClassNames.ROOT_BASE,
            ClassNames.SIZES.get(size, ""),
            ClassNames.ORIENTATIONS.get(orientation, ""),
            class_name,
        ),
        **props,
    )


def attachment_media(
    *children,
    variant: AttachmentMediaVariant = "icon",
    class_name: str = "",
    **props,
) -> rx.Component:
    """Icon or image preview slot."""
    return rx.el.div(
        *children,
        data_slot="attachment-media",
        data_variant=variant,
        class_name=cn(
            ClassNames.MEDIA_BASE,
            ClassNames.MEDIA_VARIANTS.get(variant, ""),
            class_name,
        ),
        **props,
    )


def attachment_content(*children, class_name: str = "", **props) -> rx.Component:
    """Text content area — holds title and description."""
    return rx.el.div(
        *children,
        data_slot="attachment-content",
        class_name=cn(ClassNames.CONTENT, class_name),
        **props,
    )


def attachment_title(*children, class_name: str = "", **props) -> rx.Component:
    """Filename or attachment title. Shimmers during uploading/processing."""
    return rx.el.span(
        *children,
        data_slot="attachment-title",
        class_name=cn(ClassNames.TITLE, class_name),
        **props,
    )


def attachment_description(*children, class_name: str = "", **props) -> rx.Component:
    """File type, size, or other metadata."""
    return rx.el.span(
        *children,
        data_slot="attachment-description",
        class_name=cn(ClassNames.DESCRIPTION, class_name),
        **props,
    )


def attachment_actions(*children, class_name: str = "", **props) -> rx.Component:
    """
    Row of action buttons.
    In vertical orientation, absolutely positioned top-right.
    """
    return rx.el.div(
        *children,
        data_slot="attachment-actions",
        class_name=cn(ClassNames.ACTIONS, class_name),
        **props,
    )


def attachment_action(*children, class_name: str = "", **props) -> rx.Component:
    """Individual action button."""
    props.setdefault("variant", "ghost")
    props.setdefault("size", "icon-xs")
    return button(
        *children,
        data_slot="attachment-action",
        class_name=cn(class_name),
        **props,
    )


def attachment_trigger(
    *children, link: bool = False, class_name: str = "", **props
) -> rx.Component:

    component_fn = rx.el.a if link else rx.el.button

    props.setdefault("data_slot", "attachment-trigger")
    props.setdefault("class_name", cn(ClassNames.TRIGGER, class_name))

    if not link:
        props.setdefault("type", "button")

    return component_fn(*children, **props)


def attachment_group(*children, class_name: str = "", **props) -> rx.Component:
    """
    Horizontal scrolling row of attachments.
    Snaps to each attachment on scroll.
    """
    return rx.el.div(
        *children,
        data_slot="attachment-group",
        class_name=cn(ClassNames.GROUP, class_name),
        **props,
    )


class Attachment(ComponentNamespace):
    """Attachment namespace."""

    root = staticmethod(attachment_root)
    media = staticmethod(attachment_media)
    content = staticmethod(attachment_content)
    title = staticmethod(attachment_title)
    description = staticmethod(attachment_description)
    actions = staticmethod(attachment_actions)
    action = staticmethod(attachment_action)
    trigger = staticmethod(attachment_trigger)
    group = staticmethod(attachment_group)

    class_names = ClassNames


attachment = Attachment()
```


# Usage


```python
from components.ui.attachment import Attachment
```


# Anatomy 

Use the following composition to build an `Attachment` component.


```python
attachment.root(
    attachment.media(),
    attachment.content(
        attachment.title(),
        attachment.description(),
    ),
    attachment.actions(
        attachment.action()
    ),
)
```


# Features

- Icon and image media through `attachment.media`
- Upload states: `idle`, `uploading`, `processing`, `error`, and `done` with built-in styling and a shimmer while in progress
- Three sizes and horizontal or vertical orientation
- A full-card `attachment.trigger` that opens a link or dialog while the actions stay independently clickable
- Scrollable, snapping `attachment.group` with an edge fade
- Customizable styling through the `class_name` prop on every part

# Examples

## Image

Set `variant="image"` on `attachment.media` and render an `rx.el.img()` inside it. Use `orientation="vertical"` to stack the media above the content.


```python
def attachment_image_demo():
    return rx.el.div(
        attachment.group(
            rx.foreach(
                images,
                lambda image: attachment.root(
                    attachment.trigger(
                        link=True,
                        href=image["src"],
                        target="_blank",
                        rel="noreferrer",
                        aria_label=f"Open {image['name']}",
                    ),
                    attachment.media(
                        rx.el.img(src=image["src"], alt=image["alt"]),
                        variant="image",
                    ),
                    attachment.content(
                        attachment.title(image["name"]),
                        attachment.description(image["meta"]),
                    ),
                    attachment.actions(
                        attachment.action(
                            hi("Cancel01Icon"),
                            aria_label=f"Remove {image['name']}",
                        )
                    ),
                    orientation="vertical",
                ),
            ),
            class_name="w-full",
        ),
        class_name="mx-auto w-full max-w-sm py-12",
    )
```


## States

Set `state` to reflect the upload lifecycle. `uploading` and `processing` shimmer the title, and `error` switches to a destructive treatment.


```python
def attachment_states_demo():
    return rx.el.div(
        attachment.root(
            attachment.media(hi("Clock01Icon")),
            attachment.content(
                attachment.title("selected-file.pdf"),
                attachment.description("Ready to upload"),
            ),
            attachment.actions(
                attachment.action(
                    hi("Cancel01Icon"), aria_label="Remove selected-file.pdf"
                )
            ),
            state="idle",
        ),
        attachment.root(
            attachment.media(spinner()),
            attachment.content(
                attachment.title(
                    "design-system.zip",
                    class_name="shimmer",
                ),
                attachment.description("Uploading · 64%"),
            ),
            attachment.actions(
                attachment.action(hi("Cancel01Icon"), aria_label="Cancel upload")
            ),
            state="uploading",
        ),
        attachment.root(
            attachment.media(hi("File02Icon")),
            attachment.content(
                attachment.title("market-research.pdf"),
                attachment.description("Processing document"),
            ),
            attachment.actions(
                attachment.action(
                    hi("Cancel01Icon"), aria_label="Remove market-research.pdf"
                )
            ),
            state="processing",
        ),
        attachment.root(
            attachment.media(hi("FileExclamationPointIcon")),
            attachment.content(
                attachment.title("financial-model.xlsx"),
                attachment.description("Upload failed. Try again."),
            ),
            attachment.actions(
                attachment.action(hi("RefreshIcon"), aria_label="Retry upload"),
                attachment.action(
                    hi("Cancel01Icon"), aria_label="Remove financial-model.xlsx"
                ),
            ),
            state="error",
        ),
        attachment.root(
            attachment.media(hi("Tick02Icon")),
            attachment.content(
                attachment.title("uploaded-report.pdf"),
                attachment.description("Uploaded · 1.8 MB"),
            ),
            attachment.actions(
                attachment.action(
                    hi("Cancel01Icon"), aria_label="Remove uploaded-report.pdf"
                )
            ),
            state="done",
        ),
        class_name="w-full mx-auto max-w-sm py-12 flex flex-col gap-y-4",
    )
```



## Sizes

Use `size` to switch between `default`, `sm`, and `xs`.


```python
def attachment_sizes_demo():
    return rx.el.div(
        attachment.root(
            attachment.media(hi("File02Icon")),
            attachment.content(
                attachment.title("Default attachment"),
                attachment.description("PDF · 2.4 MB"),
            ),
            size="default",
        ),
        attachment.root(
            attachment.media(hi("File02Icon")),
            attachment.content(
                attachment.title("Small attachment"),
                attachment.description("PDF · 2.4 MB"),
            ),
            size="sm",
        ),
        attachment.root(
            attachment.media(hi("File02Icon")),
            attachment.content(
                attachment.title("Extra small attachment"),
            ),
            size="xs",
        ),
        class_name="mx-auto w-full max-w-sm py-12 flex flex-col gap-y-4",
    )
```


## Group

Wrap attachments in `attachment.group` to lay them out in a horizontally scrollable, snapping row with an edge fade.


```python
def attachment_group_demo():
    return rx.el.div(
        attachment.group(
            rx.foreach(
                items,
                lambda item: attachment.root(
                    rx.cond(
                        item["type"] == "image",
                        attachment.media(
                            rx.el.img(src=item["src"], alt=item["name"]),
                            variant="image",
                        ),
                        attachment.media(hi("File02Icon")),
                    ),
                    attachment.content(
                        attachment.title(item["name"]),
                        attachment.description(item["meta"]),
                    ),
                    attachment.actions(
                        attachment.action(
                            hi("Cancel01Icon"), aria_label=f"Remove {item['name']}"
                        )
                    ),
                    class_name="w-64",
                ),
            ),
            class_name="full",
        ),
        class_name="mx-auto w-full max-w-sm py-12",
    )
```


## Trigger

Add an `attachment.trigger` to make the whole card open a link or dialog. It fills the card behind the actions, so the actions stay clickable.


```python
def attachment_trigger_dialog_demo():
    return rx.el.div(
        dialog.root(
            attachment.root(
                attachment.media(hi("File01Icon")),
                attachment.content(
                    attachment.title("research-summary.pdf"),
                    attachment.description("Open preview dialog"),
                ),
                attachment.actions(
                    attachment.action(hi("Copy01Icon"), aria_label="Copy link"),
                    attachment.action(
                        hi("Cancel01Icon"), aria_label="Remove research-summary.pdf"
                    ),
                ),
                dialog.trigger(attachment.trigger(link=False)),
                class_name="w-full",
            ),
            dialog.portal(
                dialog.backdrop(class_name="backdrop-blur-[3px]"),
                dialog.popup(
                    dialog.title("research-summary.pdf"),
                    dialog.description(
                        "The attachment trigger fills the card and opens the dialog, "
                        "while the actions stay independently clickable above it."
                    ),
                    class_name="max-w-md rounded-2xl",
                ),
            ),
        ),
        class_name="mx-auto w-full max-w-sm py-12",
    )
```



# Accessibility

`attachment.action` renders a `Button`, and `attachment.trigger` renders either a real `rx.el.button()` or a `rx.el.a()` if the `link` prop is set to `True`. Follow the guidance below so both are operable and announced.

## Label icon-only actions

`attachment.action` is usually icon-only, so give each one an `aria-label` describing the action and its target.

```python
attachment.action(
    hi("Cancel01Icon"), aria_label="Remove market-research.pdf"
)
```

## Label the trigger

`attachment.trigger` overlays the entire attachment with a clickable surface.

Use `aria_label` to describe what activating the attachment does. This is required when the trigger has no visible text.

### Link trigger (opens a URL)

```python
attachment.trigger(
    link=True,
    href=url,
    target="_blank",
    rel="noreferrer",
    aria_label="Open workspace.png",
)
```

### Button trigger (interactive action)

```python
attachment.trigger(
    on_click=handle_open,
    aria_label="Open attachment preview",
)
```


The trigger sits behind the actions in the stacking order, so an `attachment.action` and the `attachment.trigger` never trap each other — both remain separately focusable and clickable.

## Keyboard scrolling

An `attachment.group` scrolls horizontally. When its attachments are interactive: a trigger or actions, keyboard users reach off-screen items by tabbing to them. For a row of presentational attachments, make the group itself focusable and scrollable by adding `tabIndex={0}`, `role="group"`, and an `aria-label`.

## Meaning beyond color

The `error` state uses a destructive color. Keep the failure reason in `attachment.description` so the state is not conveyed by color alone.

# API Reference

## attachment.root

The root attachment container.

| Prop          | Type                                                         | Default        | Description                                       |
| ------------- | ------------------------------------------------------------ | -------------- | ------------------------------------------------- |
| `state`       | `"idle" \| "uploading" \| "processing" \| "error" \| "done"` | `"done"`       | The upload state. Drives styling and the shimmer. |
| `size`        | `"default" \| "sm" \| "xs"`                                  | `"default"`    | The attachment size.                              |
| `orientation` | `"horizontal" \| "vertical"`                                 | `"horizontal"` | Lay the media beside or above the content.        |
| `class_name`   | `string`                                                     | -              | Additional classes to apply to the root element.  |

## attachment.media

The media slot for an icon or image preview.

| Prop        | Type                | Default  | Description                                    |
| ----------- | ------------------- | -------- | ---------------------------------------------- |
| `variant`   | `"icon" \| "image"` | `"icon"` | Whether the media holds an icon or an `<img>`. |
| `class_name` | `string`            | -        | Additional classes to apply to the media slot. |

## attachment.content

Wraps the title and description.

| Prop        | Type     | Default | Description                                      |
| ----------- | -------- | ------- | ------------------------------------------------ |
| `class_name` | `string` | -       | Additional classes to apply to the content slot. |

## attachment.title

The attachment name. Shimmers while the attachment is `uploading` or `processing`.

| Prop        | Type     | Default | Description                               |
| ----------- | -------- | ------- | ----------------------------------------- |
| `class_name` | `string` | -       | Additional classes to apply to the title. |

## attachment.description

Secondary metadata such as the file type, size, or upload status.

| Prop        | Type     | Default | Description                                     |
| ----------- | -------- | ------- | ----------------------------------------------- |
| `class_name` | `string` | -       | Additional classes to apply to the description. |

## attachment.actions

A container for one or more actions, aligned to the end of the attachment.

| Prop        | Type     | Default | Description                                 |
| ----------- | -------- | ------- | ------------------------------------------- |
| `class_name` | `string` | -       | Additional classes to apply to the actions. |

## attachment.action

An action button. Renders a [`Button`](/docs/components/button) and accepts all of its props.

| Prop       | Type                                  | Default     | Description                              |
| ---------- | ------------------------------------- | ----------- | ---------------------------------------- |
| `size`     | `Button["size"]`                      | `"icon-xs"` | The button size.                         |
| `class_name` | `string` | -       | Additional classes to apply to the actions. |

## attachment.trigger

A full-card overlay that activates the attachment. Renders a `rx.el.button` by default or a `rx.el.a` when `link=True`.

| Prop         | Type                  | Default | Description                                                                   |
| ------------ | --------------------- | ------- | ----------------------------------------------------------------------------- |
| `link`       | `bool`         | `False`  | If set, renders an anchor (`rx.el.a`) instead of a button.                        |
| `aria_label` | `str \| None`         | `None`  | Accessibility label for screen readers. Required when no visible text exists. |
| `class_name` | `str`                 | `""`    | Additional CSS classes applied to the trigger.                                |


## attachment.group

Lays out attachments in a horizontally scrollable, snapping row.

| Prop        | Type     | Default | Description                               |
| ----------- | -------- | ------- | ----------------------------------------- |
| `class_name` | `string` | -       | Additional classes to apply to the group. |
