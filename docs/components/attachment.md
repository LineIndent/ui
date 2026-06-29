---
title: "Attachment"
description: "Displays a file or image attachment with media, metadata, upload state, and actions."
order: 0
---

# Attachment

Displays a file or image attachment with media, metadata, upload state, and actions.

# Installation

Copy the following code into your app directory.

--INSTALL(attachment)--

# Usage

--USAGE(attachment)--

# Anatomy 

Use the following composition to build an `Attachment` component.

--ANATOMY(attachment)--

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

--DEMO(attachment_image_demo)--

## States

Set `state` to reflect the upload lifecycle. `uploading` and `processing` shimmer the title, and `error` switches to a destructive treatment.

--DEMO(attachment_states_demo)--


## Sizes

Use `size` to switch between `default`, `sm`, and `xs`.

--DEMO(attachment_sizes_demo)--

## Group

Wrap attachments in `attachment.group` to lay them out in a horizontally scrollable, snapping row with an edge fade.

--DEMO(attachment_group_demo)--

## Trigger

Add an `attachment.trigger` to make the whole card open a link or dialog. It fills the card behind the actions, so the actions stay clickable.

--DEMO(attachment_trigger_dialog_demo)--


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
