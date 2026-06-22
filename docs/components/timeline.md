---
title: "Timeline"
description: "A visual representation of events in chronological order."
order: 23
---

# Timeline

A visual representation of events in chronological order.

# Installation

Copy the following code into your app directory.

--INSTALL(timeline)--

# Usage

--USAGE(timeline)--

# Anatomy

--ANATOMY(timeline)--

# Examples

## Basic Timeline

--DEMO(timeline_basic)--

## Left-Aligned Dates

Set the `data-[]` CSS prop to `-left-32` to align dates to the left.

--DEMO(timeline_left_aligned_dates)--

# API Reference 

## timeline.root

| Prop          | Type                         |      Default | Description                                                        |
| ------------- | ---------------------------- | -----------: | ------------------------------------------------------------------ |
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` | Controls whether timeline items render vertically or horizontally. |
| `class_name`  | `str`                        |         `""` | Additional classes applied to the root container.                  |
| `**props`     | `Any`                        |            — | Additional props forwarded to the underlying `div`.                |

## timeline.item

| Prop          | Type  | Default | Description                                             |
| ------------- | ----- | ------: | ------------------------------------------------------- |
| `step`        | `int` |       — | Step number for the item.                               |
| `active_step` | `int` |       — | Current active step used to determine completion state. |
| `class_name`  | `str` |    `""` | Additional classes applied to the item container.       |
| `**props`     | `Any` |       — | Additional props forwarded to the underlying `div`.     |


## timeline.header

| Prop         | Type  | Default | Description                                         |
| ------------ | ----- | ------: | --------------------------------------------------- |
| `class_name` | `str` |    `""` | Additional classes applied to the header.           |
| `**props`    | `Any` |       — | Additional props forwarded to the underlying `div`. |


## timeline.title

| Prop         | Type  | Default | Description                                        |
| ------------ | ----- | ------: | -------------------------------------------------- |
| `class_name` | `str` |    `""` | Additional classes applied to the title.           |
| `**props`    | `Any` |       — | Additional props forwarded to the underlying `h3`. |

## timeline.content

| Prop         | Type  | Default | Description                                          |
| ------------ | ----- | ------: | ---------------------------------------------------- |
| `class_name` | `str` |    `""` | Additional classes applied to the content container. |
| `**props`    | `Any` |       — | Additional props forwarded to the underlying `div`.  |

## timeline.date

| Prop         | Type  | Default | Description                                          |
| ------------ | ----- | ------: | ---------------------------------------------------- |
| `class_name` | `str` |    `""` | Additional classes applied to the date element.      |
| `**props`    | `Any` |       — | Additional props forwarded to the underlying `time`. |

## timeline.indicator

| Prop          | Type   | Default | Description                                         |
| ------------- | ------ | ------: | --------------------------------------------------- |
| `class_name`  | `str`  |    `""` | Additional classes applied to the indicator.        |
| `aria_hidden` | `bool` |  `True` | Hidden from assistive technologies.                 |
| `**props`     | `Any`  |       — | Additional props forwarded to the underlying `div`. |

## timeline.separator

| Prop          | Type   | Default | Description                                         |
| ------------- | ------ | ------: | --------------------------------------------------- |
| `class_name`  | `str`  |    `""` | Additional classes applied to the separator.        |
| `aria_hidden` | `bool` |  `True` | Hidden from assistive technologies.                 |
| `**props`     | `Any`  |       — | Additional props forwarded to the underlying `div`. |
