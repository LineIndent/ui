---
title: "Card"
description: "Displays a card with header, content, and footer."
order: 0
---

# Card

Displays a card with header, content, and footer.

# Installation

Copy the following code into your app directory.

--INSTALL(card)--

# Usage

--USAGE(card)--

# Anatomy 
Use the following composition to build a `Card` component.

--ANATOMY(card)--

# Examples

## Size

Use the `size="sm"` prop to set the size of the card to small. The small size variant uses smaller spacing.

--DEMO(card_small)--

## Spacing

In addition to the `size` prop, you can use the `--card-spacing` CSS variable to control the spacing between sections and the inset of card parts.

--DEMO(card_spacing)--

Use negative margins with `-mx-(--card-spacing)` to make content go edge to edge while keeping it aligned with the card inset. When the edge-to-edge content sits above a footer, use `-mb-(--card-spacing)` on `card.content` to remove the section gap.

--DEMO(card_edge_to_edge)--


## Image

Add an image before the card header to create a card with an image.

--DEMO(card_image)--


# API Reference

## card.root

The `card.root` component is the root container for card content.

| Prop        | Type                | Default     |
| ----------- | ------------------- | ----------- |
| `size`      | `"default" \| "sm"` | `"default"` |
| `class_name` | `string`            | -           |

## card.header

The `card.header` component is used for a title, description, and optional action.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.title

The `card.title` component is used for the card title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.description

The `card.description` component is used for helper text under the title.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.action

The `card.action` component places content in the top-right of the header (for example, a button or a badge).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.content

The `card.content` component is used for the main card body.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |

## card.footer

The `card.footer` component is used for actions and secondary content at the bottom of the card.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `class_name` | `string` | -       |
