

# Message

Displays a message in a conversation, with optional avatar, header, footer, and alignment.

> **Note:** The Message component is a fully custom implementation with no external dependencies.

The `Message` component lays out a single message in a conversation. It handles the avatar, alignment, header, and footer around the message surface.

For AI apps, you can render reasoning steps, tool calls and assistant messages using the `Message` component.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component message
```

### Manual Installation

```python
"""Message component — chat bubble layout with avatar, content, header and footer slots."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..utils.twmerge import cn

MessageAlign = Literal["start", "end"]


class ClassNames:
    GROUP = "flex min-w-0 flex-col gap-2"

    ROOT = (
        "group/message relative flex w-full min-w-0 gap-2 text-sm "
        "data-[align=end]:flex-row-reverse"
    )

    AVATAR = (
        "flex w-fit min-w-8 shrink-0 items-center justify-center "
        "self-end overflow-hidden rounded-full bg-muted "
        "group-has-data-[slot=message-footer]/message:-translate-y-8"
    )

    CONTENT = (
        "flex w-full min-w-0 flex-col gap-2.5 break-words "
        "group-data-[align=end]/message:*:data-slot:self-end"
    )

    HEADER = (
        "flex max-w-full min-w-0 items-center px-3 text-xs font-medium "
        "text-muted-foreground "
        "group-has-data-[variant=ghost]/message:px-0"
    )

    FOOTER = (
        "flex max-w-full min-w-0 items-center px-3 text-xs font-medium "
        "text-muted-foreground "
        "group-has-data-[variant=ghost]/message:px-0 "
        "group-data-[align=end]/message:justify-end"
    )


def message_group(*children, class_name: str = "", **props) -> rx.Component:
    """Vertical stack of message rows."""
    return rx.el.div(
        *children,
        data_slot="message-group",
        class_name=cn(ClassNames.GROUP, class_name),
        **props,
    )


def message_root(
    *children,
    align: MessageAlign = "start",
    class_name: str = "",
    **props,
) -> rx.Component:
    """Single message row. Use align='end' for outgoing messages."""
    return rx.el.div(
        *children,
        data_slot="message",
        data_align=align,
        class_name=cn(ClassNames.ROOT, class_name),
        **props,
    )


def message_avatar(*children, class_name: str = "", **props) -> rx.Component:
    """Avatar slot — anchored to bottom of message, shifts up when footer is present."""
    return rx.el.div(
        *children,
        data_slot="message-avatar",
        class_name=cn(ClassNames.AVATAR, class_name),
        **props,
    )


def message_content(*children, class_name: str = "", **props) -> rx.Component:
    """Content area — holds bubbles, header, and footer."""
    return rx.el.div(
        *children,
        data_slot="message-content",
        class_name=cn(ClassNames.CONTENT, class_name),
        **props,
    )


def message_header(*children, class_name: str = "", **props) -> rx.Component:
    """Sender name or timestamp above the bubble."""
    return rx.el.div(
        *children,
        data_slot="message-header",
        class_name=cn(ClassNames.HEADER, class_name),
        **props,
    )


def message_footer(*children, class_name: str = "", **props) -> rx.Component:
    """Actions or reactions below the bubble."""
    return rx.el.div(
        *children,
        data_slot="message-footer",
        class_name=cn(ClassNames.FOOTER, class_name),
        **props,
    )


class Message(ComponentNamespace):
    """Message namespace."""

    group = staticmethod(message_group)
    root = staticmethod(message_root)
    avatar = staticmethod(message_avatar)
    content = staticmethod(message_content)
    header = staticmethod(message_header)
    footer = staticmethod(message_footer)

    class_names = ClassNames


message = Message()
```


# Usage


```python
from components.ui.message import Message
```


**Note:** `Message` owns the row layout—avatar, alignment, header, and footer.
Render the visible message surface inside it with
[`Bubble`](/docs/components/bubble). For the scroll container around a
conversation, use [`MessageScroller`](/docs/components/message-scroller).

# Anatomy 
Use the following composition to build a `Message` component.


```python
message.group(
    message.root(
        message.avatar(),
        message.content(
            message.header(),
            message.footer(),
        ),
    ),
)
```


# Examples

## Avatar

Use `message.avatar` to render an avatar next to the message. Set `align="end"` on the message to align the avatar to the end of the message.


```python
def message_with_avatar():
    return rx.el.div(
        message.root(
            message.avatar(
                avatar.root(
                    avatar.image(src="/avatars/03.png", alt="@avatar"),
                    avatar.fallback("R"),
                ),
            ),
            message.content(
                bubble.root(
                    bubble.content("The build failed during dependency installation."),
                    variant="muted",
                ),
            ),
        ),
        message.root(
            message.avatar(
                avatar.root(
                    avatar.image(src="/avatars/01.png", alt="@avatar"),
                    avatar.fallback("R"),
                ),
            ),
            message.content(
                bubble.root(
                    bubble.content("Can you share the exact error?"),
                ),
            ),
            align="end",
        ),
        message.root(
            message.avatar(
                avatar.root(
                    avatar.image(src="/avatars/03.png", alt="@avatar"),
                    avatar.fallback("R"),
                ),
            ),
            message.content(
                bubble.group(
                    bubble.root(
                        bubble.content("Here's the error from the logs"),
                        variant="muted",
                    ),
                    bubble.root(
                        bubble.content(
                            "Something went wrong with the build. The libraries are not "
                            "installed correctly. Try running the build again."
                        ),
                        variant="muted",
                    ),
                ),
            ),
        ),
        class_name="flex w-full max-w-sm flex-col gap-6 py-12",
    )
```


| align   | Description                                         |
| ------- | --------------------------------------------------- |
| `start` | Align the message to the start of the conversation. |
| `end`   | Align the message to the end of the conversation.   |

## Group

Use `message.group` to stack consecutive messages from the same sender. Render an empty `message.avatar` on the earlier messages to keep them aligned with the avatar on the last one.


```python
def message_with_group():
    return rx.el.div(
        message.group(
            message.root(
                message.avatar(),
                message.content(
                    bubble.root(
                        bubble.content("I checked the registry addresses."),
                        variant="muted",
                    ),
                ),
            ),
            message.root(
                message.avatar(
                    avatar.root(
                        avatar.image(src="/avatars/02.png", alt="@avatar"),
                        avatar.fallback("CN"),
                    ),
                ),
                message.content(
                    bubble.root(
                        bubble.content(
                            "The component and example JSON now live under the UI registry."
                        ),
                        variant="muted",
                    ),
                ),
            ),
        ),
        class_name="flex w-full max-w-sm flex-col gap-6 py-12",
    )
```


## Header and Footer

Use `message.header` for a sender name and `message.footer` for metadata such as a delivery or read status.


```python
def message_header_footer():
    return rx.el.div(
        message.root(
            message.content(
                message.header("Olivia"),
                bubble.root(
                    bubble.content("I already checked the logs."),
                    variant="muted",
                ),
            ),
        ),
        message.root(
            message.content(
                bubble.root(
                    bubble.content(
                        "Send the report to the team. Ping @lineindent if you need help."
                    ),
                ),
                message.footer(
                    rx.el.div(
                        "Read ",
                        rx.el.span("Yesterday", class_name="font-normal"),
                    ),
                ),
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


## Actions

Place message-level actions in `message.footer`, such as copy, retry, or feedback buttons.


```python
def message_with_actions():
    return rx.el.div(
        message.root(
            message.content(
                bubble.root(
                    bubble.content(
                        "The install failure is coming from the workspace package."
                    ),
                    variant="muted",
                ),
                message.footer(
                    button(
                        hi("Copy01Icon"),
                        variant="ghost",
                        size="sm",
                        aria_label="Copy",
                        title="Copy",
                    ),
                    button(
                        hi("ThumbsUpIcon"),
                        variant="ghost",
                        size="sm",
                        aria_label="Like",
                        title="Like",
                    ),
                    button(
                        hi("ThumbsDownIcon"),
                        variant="ghost",
                        size="sm",
                        aria_label="Dislike",
                        title="Dislike",
                    ),
                ),
            ),
        ),
        message.root(
            message.content(
                bubble.root(
                    bubble.content("Okay drop me a link. Taking a look..."),
                ),
                message.footer(
                    rx.el.span(
                        "Failed to send",
                        class_name="font-normal text-destructive",
                    ),
                    button(
                        hi("Refresh03Icon"),
                        variant="ghost",
                        size="sm",
                        title="Retry",
                        aria_label="Retry",
                    ),
                    class_name="gap-2",
                ),
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


## Attachment

Use the [`Attachment`](/docs/components/attachment) with the messages to displays a file or image attachment with media, metadata, upload state, and actions.


```python
def message_with_attachment():
    return rx.el.div(
        message.root(
            message.content(
                attachment.root(
                    attachment.media(
                        rx.el.img(
                            src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80",
                            alt="Workspace",
                        ),
                        variant="image",
                    ),
                    orientation="vertical",
                ),
                bubble.root(
                    bubble.content(
                        "Here's the image. Can you add it to the PDF? "
                        "Use it for the cover page."
                    ),
                ),
            ),
            align="end",
        ),
        message.root(
            message.content(
                bubble.root(
                    bubble.content(
                        "Done. Here's the PDF with the image added as the cover page."
                    ),
                    variant="muted",
                ),
                attachment.root(
                    attachment.media(
                        hi("File02Icon"),
                    ),
                    attachment.content(
                        attachment.title("sales-dashboard.pdf"),
                        attachment.description("PDF · 2.4 MB"),
                    ),
                    attachment.actions(
                        attachment.action(
                            hi("Download02Icon"),
                            title="Download",
                            aria_label="Download",
                        ),
                    ),
                ),
            ),
        ),
        message.root(
            message.content(
                bubble.root(
                    bubble.content("Thanks. Looks good."),
                ),
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


# Accessibility

`Message` is a presentational layout wrapper. Accessibility comes from the content you place inside it.

## Label icon-only actions

Action buttons in `message.footer` are usually icon-only, so give each one an `aria-label`.

```python
message.footer(
    button(
        hi("Refresh03Icon"),
        variant="ghost",
        size="sm",
        title="Retry",
        aria_label="Retry",
    ),
)
```

## Status updates

For in-progress messages, use a [`Marker`](/docs/components/marker) with `role="status"` so assistive tech announces the update as it appears.

```python
message.root(
    message.content(
        marker.root(
            marker.icon(spinner()),
            marker.content("Compacting conversation"),
            role="status",
        ),
    ),
)
```

# API Reference

## message.root

The message row wrapper.

| Prop        | Type               | Default   | Description                                       |
| ----------- | ------------------ | --------- | ------------------------------------------------- |
| `align`     | `"start" \| "end"` | `"start"` | The alignment of the message in the conversation. |
| `class_name` | `string`           | -         | Additional classes to apply to the row.           |

## message.group

Groups consecutive messages from the same sender.

| Prop        | Type     | Default | Description                                    |
| ----------- | -------- | ------- | ---------------------------------------------- |
| `class_name` | `string` | -       | Additional classes to apply to the group root. |

## message.avatar

The avatar slot, aligned to the bottom of the message. When the message has a `message.footer`, the avatar shifts up to stay aligned with the message surface instead of the footer.

| Prop        | Type     | Default | Description                                     |
| ----------- | -------- | ------- | ----------------------------------------------- |
| `class_name` | `string` | -       | Additional classes to apply to the avatar slot. |

### message.content

Wraps the header, message surface, and footer.

| Prop        | Type     | Default | Description                                      |
| ----------- | -------- | ------- | ------------------------------------------------ |
| `class_name` | `string` | -       | Additional classes to apply to the content slot. |

### message.header

Displays content above the message, such as a sender name. Stays aligned to the start regardless of `align`.

| Prop        | Type     | Default | Description                                |
| ----------- | -------- | ------- | ------------------------------------------ |
| `class_name` | `string` | -       | Additional classes to apply to the header. |

### message.footer

Displays content below the message, such as status or actions. Aligns to the message side.

| Prop        | Type     | Default | Description                                |
| ----------- | -------- | ------- | ------------------------------------------ |
| `class_name` | `string` | -       | Additional classes to apply to the footer. |
