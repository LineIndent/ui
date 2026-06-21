---
title: "Frame"
description: "Displays related content in a structured frame."
order: 0
---

# Frame

Displays related content in a structured frame.

> **Note:** The Frame component is a fully custom implementation with no external dependencies.

# Installation

Copy the following code into your app directory.

--INSTALL(frame)--

# Usage

--USAGE(frame)--

# Anatomy 
Use the following composition to build an `Frame`

--ANATOMY(frame)--

# Examples

## Basic Panels

A basic frame with a header and two panels.

--DEMO(frame_basic)--

## Stacked Panels

Set the `stacked` prop to `True` to get the panels stacked. 

--DEMO(frame_stacked)--

## Dense Panels

Set the `dense` prop to `True` to get minimal frame padding. 

--DEMO(frame_dense)--

## Outer Border

Set the `variant` prop to `ghost` to remove the frame outer border. 

--DEMO(frame_no_border)--

# API Reference

## frame.root

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `variant` | `"default" \| "inverse" \| "ghost"` | `"default"` | Controls the visual style of the frame container. |
| `spacing` | `"xs" \| "sm" \| "default" \| "lg"` | `"default"` | Controls the internal padding of panels, headers, and footers via CSS variables. |
| `stacked` | `bool` | `False` | When `True`, removes gaps and merges panel borders so they appear as one continuous block. |
| `dense` | `bool` | `False` | When `True`, removes all padding and gaps and pulls panels edge-to-edge with negative margins. |
| `class_name` | `str` | `None` | Additional Tailwind classes merged onto the root wrapper. |

## frame.panel

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `class_name` | `str` | `None` | Additional Tailwind classes merged onto the panel. Overrides default bg, border, and padding. |

## frame.header

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `class_name` | `str` | `None` | Additional Tailwind classes merged onto the header element. |

## frame.title

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `class_name` | `str` | `None` | Additional Tailwind classes merged onto the title element. |

## frame.description

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `class_name` | `str` | `None` | Additional Tailwind classes merged onto the description element. |

## frame.footer
| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `class_name` | `str` | `None` | Additional Tailwind classes merged onto the footer element. |
