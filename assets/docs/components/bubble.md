

# Bubble

Displays conversational content in a message bubble. Supports variants, alignment, grouping, reactions, and collapsible content.

The `Bubble` component displays framed conversational content. Use it for chat text, short structured output, quoted replies, suggestions, and reactions.

For full-featured chat interfaces, use the [`Message`](/docs/components/message) component. `Bubble` is intentionally scoped to the bubble surface. Place avatars, names, timestamps, metadata, and message-level actions in [`Message`](/docs/components/message).

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component bubble
```

### Manual Installation

```python
"""Bubble component — chat message bubble with variants, content, and reactions slots."""

from typing import Literal

import reflex as rx
from reflex.components.component import ComponentNamespace

from ..utils.twmerge import cn

BubbleVariant = Literal[
    "default", "secondary", "muted", "tinted", "outline", "ghost", "destructive"
]
BubbleAlign = Literal["start", "end"]
BubbleSide = Literal["top", "bottom"]


class ClassNames:
    GROUP = "flex min-w-0 flex-col gap-2"

    VARIANTS: dict[str, str] = {
        "default": (
            "*:data-[slot=bubble-content]:bg-primary "
            "*:data-[slot=bubble-content]:text-primary-foreground"
        ),
        "secondary": (
            "*:data-[slot=bubble-content]:bg-secondary "
            "*:data-[slot=bubble-content]:text-secondary-foreground"
        ),
        "muted": ("*:data-[slot=bubble-content]:bg-muted"),
        "tinted": (
            "*:data-[slot=bubble-content]:bg-[oklch(from_var(--primary)_0.93_calc(c*0.4)_h)] "
            "*:data-[slot=bubble-content]:text-foreground "
            "dark:*:data-[slot=bubble-content]:bg-[oklch(from_var(--primary)_0.3_calc(c*0.4)_h)]"
        ),
        "outline": (
            "*:data-[slot=bubble-content]:border-border "
            "*:data-[slot=bubble-content]:bg-background"
        ),
        "ghost": (
            "border-none "
            "*:data-[slot=bubble-content]:rounded-none "
            "*:data-[slot=bubble-content]:bg-transparent "
            "*:data-[slot=bubble-content]:p-0"
        ),
        "destructive": (
            "*:data-[slot=bubble-content]:bg-destructive/10 "
            "*:data-[slot=bubble-content]:text-destructive "
            "dark:*:data-[slot=bubble-content]:bg-destructive/20"
        ),
    }

    ROOT = (
        "group/bubble relative flex w-fit max-w-[80%] min-w-0 flex-col gap-1 "
        "group-data-[align=end]/message:self-end "
        "data-[align=end]:self-end "
        "data-[variant=ghost]:max-w-full"
    )

    CONTENT = (
        "w-fit max-w-full min-w-0 overflow-hidden rounded-3xl border border-transparent "
        "px-3 py-2.5 text-sm leading-relaxed break-words "
        "group-data-[align=end]/bubble:self-end"
    )

    REACTIONS_BASE = (
        "absolute z-10 flex w-fit shrink-0 items-center justify-center gap-1 "
        "rounded-full bg-muted px-1.5 py-0.5 text-sm ring-3 ring-card has-[button]:p-0"
    )

    REACTIONS_SIDE: dict[str, str] = {
        "top": "top-0 -translate-y-3/4",
        "bottom": "bottom-0 translate-y-3/4",
    }

    REACTIONS_ALIGN: dict[str, str] = {
        "start": "left-3",
        "end": "right-3",
    }


def bubble_group(*children, class_name: str = "", **props) -> rx.Component:
    """Vertical stack of bubbles."""
    return rx.el.div(
        *children,
        data_slot="bubble-group",
        class_name=cn(ClassNames.GROUP, class_name),
        **props,
    )


def bubble_root(
    *children,
    variant: BubbleVariant = "default",
    align: BubbleAlign = "start",
    class_name: str = "",
    **props,
) -> rx.Component:
    """
    Bubble root container.

    Variants: default, secondary, muted, tinted, outline, ghost, destructive
    Align:    start (incoming), end (outgoing)
    """
    return rx.el.div(
        *children,
        data_slot="bubble",
        data_variant=variant,
        data_align=align,
        class_name=cn(
            ClassNames.ROOT,
            ClassNames.VARIANTS.get(variant, ""),
            class_name,
        ),
        **props,
    )


def bubble_content(*children, class_name: str = "", **props) -> rx.Component:
    """The bubble content pill — rounded, padded, colored by the parent variant."""
    return rx.el.div(
        *children,
        data_slot="bubble-content",
        class_name=cn(ClassNames.CONTENT, class_name),
        **props,
    )


def bubble_reactions(
    *children,
    side: BubbleSide = "bottom",
    align: BubbleAlign = "end",
    class_name: str = "",
    **props,
) -> rx.Component:
    """
    Emoji reactions overlay — positioned relative to the bubble.

    Side:  top | bottom (default: bottom)
    Align: start | end  (default: end)
    """
    return rx.el.div(
        *children,
        data_slot="bubble-reactions",
        data_align=align,
        data_side=side,
        class_name=cn(
            ClassNames.REACTIONS_BASE,
            ClassNames.REACTIONS_SIDE.get(side, ""),
            ClassNames.REACTIONS_ALIGN.get(align, ""),
            class_name,
        ),
        **props,
    )


class Bubble(ComponentNamespace):
    """Bubble namespace."""

    group = staticmethod(bubble_group)
    root = staticmethod(bubble_root)
    content = staticmethod(bubble_content)
    reactions = staticmethod(bubble_reactions)

    class_names = ClassNames


bubble = Bubble()
```


# Usage


```python
from components.ui.bubble import Bubble
```


# Anatomy
Use the following composition to build a `Bubble` component.


```python
bubble.root(
    bubble.content(),
    bubble.reactions(),
)
```


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


```python
def bubble_with_variants():
    return rx.el.div(
        bubble.root(
            bubble.content("This is the default primary bubble."),
            variant="default",
        ),
        bubble.root(
            bubble.content("This is the secondary variant."),
            variant="secondary",
            align="end",
        ),
        bubble.root(
            bubble.content(
                "This one is muted. It uses a lower emphasis color for the chat bubble."
            ),
            bubble.reactions(
                rx.el.span("👍"),
                role="img",
                aria_label="Reaction: thumbs up",
            ),
            variant="muted",
        ),
        bubble.root(
            bubble.content(
                "This one is tinted. The tint is a softer color derived from the primary color."
            ),
            variant="tinted",
            align="end",
        ),
        bubble.root(
            bubble.content("We can also use an outlined variant."),
            variant="outline",
        ),
        bubble.root(
            bubble.content("Or a destructive variant with a reaction."),
            bubble.reactions(
                rx.el.span("🔥"),
                role="img",
                aria_label="Reaction: fire",
            ),
            variant="destructive",
            align="end",
        ),
        bubble.root(
            bubble.content(
                rx.markdown(
                    """
                    Ghost bubbles work for assistant text, **markdown**, and other content that should not be framed.

                    This is perfect for assistant messages that should not have a frame and can take the full width of the container. You can also render `code` in it.

                    Ghost bubbles are full width and can take the full width of the container.
                    """
                )
            ),
            variant="ghost",
        ),
        class_name="flex w-full max-w-sm flex-col gap-12 py-12",
    )
```



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


```python
def bubble_alignment_demo():
    return rx.el.div(
        bubble.root(
            bubble.content(
                "This bubble is aligned to the start. This is the default alignment."
            ),
            variant="muted",
            align="start",
        ),
        bubble.root(
            bubble.content(
                "This bubble is aligned to the end. Use this for user messages."
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


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


```python
def bubble_group_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("Can you tell me what's the issue?"),
            variant="muted",
        ),
        bubble.group(
            bubble.root(
                bubble.content("You tell me!"),
                align="end",
            ),
            bubble.root(
                bubble.content("It worked yesterday. You broke it!"),
                align="end",
            ),
            bubble.root(
                bubble.content("Find the bug and fix it."),
                bubble.reactions(
                    rx.el.span("👀"),
                    aria_label="Reactions: eyes",
                    align="start",
                ),
                align="end",
            ),
        ),
        bubble.root(
            bubble.content(
                "Want me to diff yesterday's you against today's you? "
                "It's a bit embarrassing."
            ),
            variant="muted",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


## Links and Buttons

You can turn a bubble into a link or button by using the passing the interactive elements directly into the `bubble.content` slot. The `bubble.content` accepts `*children` so simply placing a button or link will render that component. 


```python
def bubble_link_button_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("How can I help you today?"),
            variant="muted",
        ),
        bubble.group(
            bubble.root(
                bubble.content(
                    rx.el.button(
                        "I forgot my password",
                        on_click=rx.toast("You clicked forgot password"),
                        class_name="w-full text-left",
                    )
                ),
                variant="tinted",
                align="end",
            ),
            bubble.root(
                bubble.content(
                    rx.el.button(
                        "I need help with my subscription",
                        on_click=rx.toast("You clicked help with subscription"),
                        class_name="w-full text-left",
                    )
                ),
                variant="tinted",
                align="end",
            ),
            bubble.root(
                bubble.content(
                    rx.el.button(
                        "Something else. Talk to a human.",
                        on_click=rx.toast(
                            "You clicked something else. Talk to a human."
                        ),
                        class_name="w-full text-left",
                    )
                ),
                variant="tinted",
                align="end",
            ),
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


## Reactions

Use `bubble.reactions` for bubble reactions. You can use it to display reactions or quick action buttons. Use `side` and `align` to position the row — `side="top"` anchors it to the upper edge. Reactions overlap the bubble edge, so leave vertical space between rows — the examples below use a larger `gap` for this reason.


```python
def bubble_reactions_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("I don't need tests, I know my code works."),
            bubble.reactions(
                rx.el.span("👍"),
                rx.el.span("😮"),
                align="start",
                role="img",
                aria_label="Reactions: thumbs up, surprised",
            ),
            variant="muted",
            align="end",
        ),
        bubble.root(
            bubble.content(
                "Bold. Fine I'll add some tests. I'll let you know when they're done."
            ),
            bubble.reactions(
                rx.el.span("👀"),
                rx.el.span("🚀"),
                rx.el.span("+2"),
                role="img",
                aria_label="Reactions: eyes, rocket, and 2 more",
            ),
            variant="muted",
        ),
        bubble.root(
            bubble.content(
                "Tests passed on the first try. All 142 of them. Looking good!"
            ),
            bubble.reactions(
                rx.el.span("🎉"),
                rx.el.span("👏"),
                side="top",
                align="start",
                role="img",
                aria_label="Reactions: party popper, clapping hands",
            ),
            variant="default",
            align="end",
        ),
        bubble.root(
            bubble.content("Are you sure I can run this command?"),
            bubble.reactions(
                rx.el.button(
                    "Yes, run it",
                    on_click=rx.toast.success("You clicked yes, running command..."),
                    class_name="px-2 py-0.5 text-xs hover:bg-accent rounded-md",
                ),
            ),
            variant="destructive",
        ),
        class_name="flex w-full max-w-sm flex-col gap-12 py-12",
    )
```



## Show More / Collapsible

Long bubble content can be composed with [`Collapsible`](/docs/components/collapsible) to allow for a show more or show less interaction. Use the `collapsible.trigger` component to trigger the collapsible content.


```python
def bubble_collapsible_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("How can I help you today?"),
            variant="muted",
        ),
        bubble.root(
            bubble.content(
                collapsible.root(
                    rx.el.div(
                        rx.cond(open_var.value, text_val, f"{text_val[:180]}..."),
                        class_name="whitespace-pre-line",
                    ),
                    collapsible.trigger(
                        rx.el.button(
                            rx.cond(open_var.value, "Show less", "Show more"),
                            rx.cond(
                                open_var.value,
                                hi("ArrowUp01Icon"),
                                hi("ArrowDown01Icon"),
                            ),
                            class_name="flex flex-row items-center gap-1 p-0 text-muted-foreground hover:underline",
                        ),
                    ),
                    open=open_var.value,
                    on_open_change=open_var.set_value,
                ),
            ),
            variant="muted",
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-8 py-12",
    )
```


## Tooltip

Wrap a bubble in a [`Tooltip`](/docs/components/tooltip) to reveal metadata on hover, such as when a message was read.


```python
def bubble_tooltip_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("Did you remove the stale route?"),
            variant="secondary",
        ),
        bubble.root(
            bubble.content("Yes, removed it from the registry."),
            bubble.reactions(
                tooltip.provider(
                    tooltip.root(
                        tooltip.trigger(
                            render_=button(
                                hi("Tick02Icon", class_name="size-4"),
                                variant="ghost",
                                class_name="w-6 h-6",
                            )
                        ),
                        tooltip.portal(
                            tooltip.positioner(
                                tooltip.popup(
                                    "Read on Jan 5, 2026 at 4:32 PM",
                                    tooltip.arrow(),
                                ),
                                side="bottom",
                            )
                        ),
                    ),
                    delay=0,
                )
            ),
            align="end",
        ),
        class_name="flex w-full max-w-sm flex-col gap-4 py-12",
    )
```


## Popover

Pair a bubble with a [`Popover`](/docs/components/popover) to surface more information on demand, such as the full error message for a failed action.


```python
def bubble_popover_demo():
    return rx.el.div(
        bubble.root(
            bubble.content("Run the build script."),
            align="end",
        ),
        bubble.root(
            bubble.content("Failed to run the command."),
            bubble.reactions(
                popover.root(
                    popover.trigger(
                        render_=button(
                            hi("InformationCircleIcon"),
                            variant="ghost",
                            aria_label="Show error details",
                            class_name="w-6 h-6 aria-expanded:text-destructive",
                        )
                    ),
                    popover.portal(
                        popover.backdrop(),
                        popover.positioner(
                            popover.popup(
                                popover.header(
                                    popover.title(
                                        "Command failed with exit code 1",
                                        class_name="text-sm",
                                    ),
                                    popover.description(
                                        "ENOENT: no such file or directory, open pnpm-lock.yaml",
                                        class_name="text-sm",
                                    ),
                                ),
                            ),
                        ),
                    ),
                )
            ),
            variant="destructive",
        ),
        class_name="flex w-full max-w-sm flex-col gap-4 py-12",
    )
```


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
