---
title: Bubble
description: Displays conversational content in a message bubble. Supports variants, alignment, grouping, reactions, and collapsible content.
order: 0 
---

# Bubble

Displays conversational content in a message bubble. Supports variants, alignment, grouping, reactions, and collapsible content.

The `Bubble` component displays framed conversational content. Use it for chat text, short structured output, quoted replies, suggestions, and reactions.

For full-featured chat interfaces, use the [`Message`](/docs/components/message) component. `Bubble` is intentionally scoped to the bubble surface. Place avatars, names, timestamps, metadata, and message-level actions in [`Message`](/docs/components/message).

# Installation

Copy the following code into your app directory.

--INSTALL(bubble)--

# Usage

--USAGE(bubble)--

# Anatomy
Use the following composition to build a `Bubble` component.

--ANATOMY(bubble)--

# Features

- Seven visual variants, from a strong primary bubble to unframed ghost content
- Start and end alignment for sender and receiver bubbles
- Reactions that anchor to the bubble edge with configurable side and alignment
- Bubbles size to their content, up to 80% of the container width
- Polymorphic content via `render` for link and button bubbles
- Customizable styling through the `class_name` prop on every part

# Examples

## Variants

Use `variant` to change the visual treatment of the bubble.

--DEMO(bubble_with_variants)--


| Variant       | Description                                            |
| ------------- | ------------------------------------------------------ |
| `default`     | A strong primary bubble, usually for the current user. |
| `secondary`   | The standard neutral bubble for conversation content.  |
| `muted`       | A lower-emphasis bubble for quiet supporting content.  |
| `tinted`      | A subtle primary-tinted bubble.                        |
| `outline`     | A bordered bubble for secondary or rich content.       |
| `ghost`       | Unframed content for assistant text or rich content.   |
| `destructive` | A destructive bubble for error or failed actions.      |

A bubble sizes to its content, up to 80% of the container width. The `ghost` variant removes the max-width so assistant text and rich content can span the full row.

## Alignment

Use `align` on `bubble.root` to align the bubble to the start or end of the conversation.

--DEMO(bubble_alignment_demo)--

| align   | Description                                        |
| ------- | -------------------------------------------------- |
| `start` | Align the bubble to the start of the conversation. |
| `end`   | Align the bubble to the end of the conversation.   |

**Note:** When building chat interfaces, you probably want to use alignment on the `Message` component itself, not the `Bubble` component. You can use the `role` prop on the `message.root` component to automatically align the bubble to the start or end of the conversation.

## Bubble Group

Use `bubble.group` to group consecutive bubbles from the same sender. Note the `align` prop should be set on the `bubble.root` component itself, not the `bubble.group` component.

```composition
bubble.group
├── bubble.root
│   └── bubble.content
└── bubble.root
    └── bubble.content
```

--DEMO(bubble_group_demo)--

## Links and Buttons

You can turn a bubble into a link or button by using the passing the interactive elements directly into the `bubble.content` slot. The `bubble.content` accepts `*children` so simply placing a button or link will render that component. 

--DEMO(bubble_link_button_demo)--

## Reactions

Use `bubble.reactions` for bubble reactions. You can use it to display reactions or quick action buttons. Use `side` and `align` to position the row — `side="top"` anchors it to the upper edge. Reactions overlap the bubble edge, so leave vertical space between rows — the examples below use a larger `gap` for this reason.

--DEMO(bubble_reactions_demo)--


## Show More / Collapsible

Long bubble content can be composed with [`Collapsible`](/docs/components/collapsible) to allow for a show more or show less interaction. Use the `collapsible.trigger` component to trigger the collapsible content.

--DEMO(bubble_collapsible_demo)--

## Tooltip

Wrap a bubble in a [`Tooltip`](/docs/components/tooltip) to reveal metadata on hover, such as when a message was read.

--DEMO(bubble_tooltip_demo)--

## Popover

Pair a bubble with a [`Popover`](/docs/components/popover) to surface more information on demand, such as the full error message for a failed action.

--DEMO(bubble_popover_demo)--

# Accessibility

`bubble.root` renders the presentational message surface. Keep conversation-level semantics on the surrounding container and follow the guidelines below.

## Labeling Reactions

Reactions render as a row of emoji. A screen reader reads each glyph with no context, and counters like `+8` are announced as "plus eight". Group the row as a single image with a descriptive `aria_label` so it announces once. `role="img"` also hides the individual emoji from assistive tech, so no `aria_hidden` is needed.

```python
bubble.reactions(
    rx.el.span("👍"),
    rx.el.span("🔥"),
    rx.el.span("+8"),
    role="img",
    aria_label="Reactions: thumbs up, fire, and 8 more"
)
```

When reactions are interactive, render buttons instead and give icon-only buttons an `aria_label`.

```python
bubble.reactions(
    button(
        ...,
        aria_label="Thumbs up",
        variant="secondary",
        size="sm"
    )
)
```

## Interactive Bubbles

When a bubble is clickable, render it as a real `<button>` or `<a>`. `bubble.-*` content accept `*children` so simply passing in the interactive component will get rendered. `bubble.content` ships a visible focus ring for interactive elements, and the accessible name comes from the bubble text. No extra label is needed.

```python
bubble.root(
    bubble.content(
        "I forgot my password",
        rx.el.button(type="button", on_click=on_reply)
    ),
    variant="muted",
    align="end"
)
```

## Meaning Beyond Color

Bubble variants signal role and tone with color. Pair them with text, alignment, or icons so meaning is not conveyed by color alone. For a `destructive` bubble, keep the error context in the message text rather than relying on the color treatment.

# API Reference

## bubble.root

The root bubble wrapper.

| Prop        | Type                                                                                       | Default     | Description                                      |
| ----------- | ------------------------------------------------------------------------------------------ | ----------- | ------------------------------------------------ |
| `variant`   | `"default" \| "secondary" \| "muted" \| "tinted" \| "outline" \| "ghost" \| "destructive"` | `"default"` | The bubble visual treatment.                     |
| `align`     | `"start" \| "end"`                                                                         | `"start"`   | The inline alignment of the bubble.              |
| `class_name` | `string`                                                                                   | -           | Additional classes to apply to the root element. |

## bubble.content

The bubble content wrapper.

| Prop        | Type                       | Default | Description                                               |
| ----------- | -------------------------- | ------- | --------------------------------------------------------- |
| `*children`    | `rx.Component` | -       | Render the content as a different element such as a link. |
| `class_name` | `string`                   | -       | Additional classes to apply to the content element.       |

## bubble.reactions

Displays overlapped reactions for a bubble.

| Prop        | Type                | Default    | Description                                      |
| ----------- | ------------------- | ---------- | ------------------------------------------------ |
| `side`      | `"top" \| "bottom"` | `"bottom"` | The side of the bubble to anchor the reactions.  |
| `align`     | `"start" \| "end"`  | `"end"`    | The inline alignment of the reactions.           |
| `class_name` | `string`            | -          | Additional classes to apply to the reaction row. |

## bubble.group

Groups consecutive bubbles from the same sender.

| Prop        | Type     | Default | Description                                    |
| ----------- | -------- | ------- | ---------------------------------------------- |
| `class_name` | `string` | -       | Additional classes to apply to the group root. |
