

# Timeline

A visual representation of events in chronological order.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component timeline
```

### Manual Installation

```python
"""Custom Timeline component."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..utils.twmerge import cn

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    ROOT = "group/timeline flex data-[orientation=horizontal]:w-full data-[orientation=horizontal]:flex-row data-[orientation=vertical]:flex-col"
    ITEM = "group/timeline-item relative flex flex-1 flex-col gap-0.5 group-data-[orientation=vertical]/timeline:ms-8 group-data-[orientation=horizontal]/timeline:mt-8 group-data-[orientation=horizontal]/timeline:not-last:pe-8 group-data-[orientation=vertical]/timeline:not-last:pb-6 has-[+[data-completed]]:**:data-[slot=timeline-separator]:bg-primary"
    HEADER = ""
    TITLE = "font-medium text-sm"
    CONTENT = "text-muted-foreground text-sm"
    DATE = "mb-1 block font-medium text-muted-foreground text-xs group-data-[orientation=vertical]/timeline:max-sm:h-4"
    INDICATOR = "group-data-[orientation=horizontal]/timeline:-top-6 group-data-[orientation=horizontal]/timeline:-translate-y-1/2 group-data-[orientation=vertical]/timeline:-left-6 group-data-[orientation=vertical]/timeline:-translate-x-1/2 absolute size-4 rounded-full border-2 border-primary/20 group-data-[orientation=vertical]/timeline:top-0 group-data-[orientation=horizontal]/timeline:left-0 group-data-completed/timeline-item:border-primary"
    SEPARATOR = "group-data-[orientation=horizontal]/timeline:-top-6 group-data-[orientation=horizontal]/timeline:-translate-y-1/2 group-data-[orientation=vertical]/timeline:-left-6 group-data-[orientation=vertical]/timeline:-translate-x-1/2 absolute self-start bg-primary/10 group-last/timeline-item:hidden group-data-[orientation=horizontal]/timeline:h-0.5 group-data-[orientation=vertical]/timeline:h-[calc(100%-1rem-0.25rem)] group-data-[orientation=horizontal]/timeline:w-[calc(100%-1rem-0.25rem)] group-data-[orientation=vertical]/timeline:w-0.5 group-data-[orientation=horizontal]/timeline:translate-x-4.5 group-data-[orientation=vertical]/timeline:translate-y-4.5"


def timeline_root(
    *children,
    orientation: LiteralOrientation = "vertical",
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.ROOT, class_name),
        data_slot="timeline",
        data_orientation=orientation,
        **props,
    )


def timeline_item(
    *children,
    step: int,
    active_step: int,
    class_name: str = "",
    **props,
) -> rx.Component:
    completed = step <= active_step

    return rx.el.div(
        *children,
        class_name=cn(ClassNames.ITEM, class_name),
        data_slot="timeline-item",
        data_completed="" if completed else None,
        **props,
    )


def timeline_header(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.HEADER, class_name),
        data_slot="timeline-header",
        **props,
    )


def timeline_title(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.h3(
        *children,
        class_name=cn(ClassNames.TITLE, class_name),
        data_slot="timeline-title",
        **props,
    )


def timeline_content(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.CONTENT, class_name),
        data_slot="timeline-content",
        **props,
    )


def timeline_date(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.time(
        *children,
        class_name=cn(ClassNames.DATE, class_name),
        data_slot="timeline-date",
        **props,
    )


def timeline_indicator(
    *children,
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        *children,
        class_name=cn(ClassNames.INDICATOR, class_name),
        data_slot="timeline-indicator",
        aria_hidden=True,
        **props,
    )


def timeline_separator(
    class_name: str = "",
    **props,
) -> rx.Component:
    return rx.el.div(
        class_name=cn(ClassNames.SEPARATOR, class_name),
        data_slot="timeline-separator",
        aria_hidden=True,
        **props,
    )


class Timeline(ComponentNamespace):
    """Namespace for Timeline components."""

    root = staticmethod(timeline_root)
    item = staticmethod(timeline_item)
    header = staticmethod(timeline_header)
    title = staticmethod(timeline_title)
    content = staticmethod(timeline_content)
    date = staticmethod(timeline_date)
    indicator = staticmethod(timeline_indicator)
    separator = staticmethod(timeline_separator)
    __call__ = staticmethod(timeline_root)


timeline = Timeline()
```


# Usage


```python
from components.ui.timeline import timeline
```


# Anatomy


```python
timeline.root(
    timeline.item(
        timeline.indicator(),
        timeline.separator(),
        timeline.header(
            timeline.date(),
            timeline.title(),
        ),
        timeline.content(),
    ),
)
```


# Examples

## Basic Timeline


```python
def timeline_basic():
    return timeline.root(
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date(
                    "Jan 2024",
                    class_name="sm:group-data-[orientation=vertical]/timeline:absolute sm:group-data-[orientation=vertical]/timeline:-left-32 sm:group-data-[orientation=vertical]/timeline:w-20 sm:group-data-[orientation=vertical]/timeline:text-right",
                ),
                timeline.title("Project kickoff"),
            ),
            timeline.content("Initial planning and team onboarding."),
            step=1,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Feb 2024"),
                timeline.title("Design phase"),
            ),
            timeline.content("Wireframes and prototypes completed."),
            step=2,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Mar 2024"),
                timeline.title("Development"),
            ),
            timeline.content("Core features implemented."),
            step=3,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Apr 2024"),
                timeline.title("Launch"),
            ),
            timeline.content("Public release."),
            step=4,
            active_step=3,
        ),
        orientation="vertical",
    )
```


## Left-Aligned Dates

Set the `data-[]` CSS prop to `-left-32` to align dates to the left.


```python
def timeline_left_aligned_dates():
    return timeline.root(
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Jan 2024", class_name=left_align_date),
                timeline.title("Project kickoff"),
            ),
            timeline.content("Initial planning and team onboarding."),
            step=1,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Feb 2024", class_name=left_align_date),
                timeline.title("Design phase"),
            ),
            timeline.content("Wireframes and prototypes completed."),
            step=2,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Mar 2024", class_name=left_align_date),
                timeline.title("Development"),
            ),
            timeline.content("Core features implemented."),
            step=3,
            active_step=3,
        ),
        timeline.item(
            timeline.indicator(),
            timeline.separator(),
            timeline.header(
                timeline.date("Apr 2024", class_name=left_align_date),
                timeline.title("Launch"),
            ),
            timeline.content("Public release."),
            step=4,
            active_step=3,
        ),
        orientation="vertical",
    )
```


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
