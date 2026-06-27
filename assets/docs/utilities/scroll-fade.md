

# Scroll Fade

Utilities for adding a fade effect to the edges of a scroll container.

>The **scroll-fade** utility is purely composed of CSS and is based on [shadcn/scroll-fade](https://ui.shadcn.com/docs/utils/scroll-fade). No extensions to **rxconfig.py** are needed as it uses **Tailwind v4** syntax. 

# Installation 

If your project was set up with `buridan init`, you already have scroll-fade. It ships with the `buridan` package, which the CLI imports in your global CSS file.

Otherwise install the `buirdan` package:

```uv
uv run buridan init
```

# Usage

| Class                             | Styles                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `scroll-fade`                     | `mask-image: var(--scroll-fade-mask, var(--scroll-fade-block));` <br /> `animation-timeline: scroll(self y);`       |
| `scroll-fade-y`                   | `mask-image: var(--scroll-fade-mask, var(--scroll-fade-block));` <br /> `animation-timeline: scroll(self y);`       |
| `scroll-fade-x`                   | `mask-image: var(--scroll-fade-mask, var(--scroll-fade-inline));` <br /> `animation-timeline: scroll(self inline);` |
| `scroll-fade-t`                   | Fade mask on the top edge. <br /> `animation-timeline: scroll(self y);`                                             |
| `scroll-fade-b`                   | Fade mask on the bottom edge. <br /> `animation-timeline: scroll(self y);`                                          |
| `scroll-fade-l`                   | Fade mask on the left edge. <br /> `animation-timeline: scroll(self x);`                                            |
| `scroll-fade-r`                   | Fade mask on the right edge. <br /> `animation-timeline: scroll(self x);`                                           |
| `scroll-fade-s`                   | Fade mask on the start edge, mirrors in RTL. <br /> `animation-timeline: scroll(self inline);`                      |
| `scroll-fade-e`                   | Fade mask on the end edge, mirrors in RTL. <br /> `animation-timeline: scroll(self inline);`                        |
| `scroll-fade-<number>`            | `--scroll-fade-size: calc(var(--spacing) * <number>);`                                                              |
| `scroll-fade-[<value>]`           | `--scroll-fade-size: <value>;`                                                                                      |
| `scroll-fade-{t,b,s,e}-<number>`  | `--scroll-fade-{t,b,s,e}-size: calc(var(--spacing) * <number>);`                                                    |
| `scroll-fade-{t,b,s,e}-[<value>]` | `--scroll-fade-{t,b,s,e}-size: <value>;`                                                                            |
| `scroll-fade-none`                | `--scroll-fade-mask: none;`                                                                                         |

Add `scroll-fade` or `scroll-fade-y` to the scroll container, i.e. the element that has overflow-y-auto.

The fade is scroll-aware and tracks the scroll position:

- At rest, the top edge is crisp and the bottom edge fades to hint at more content.
- As you scroll, a fade appears at the top and both edges stay faded mid-scroll.
- At the end, the bottom edge sharpens to show you have reached the last item.

The fade is applied with `mask-image`, so it dissolves the content itself rather than overlaying a color. The mask uses a linear fade from transparent to black, so it adapts to any background without configuration. If your scroll area sits inside a card, put the background and border on a wrapper and `scroll-fade` on the inner scroller, so the fade dissolves the content and not the card.


# Scroll Fade Demo


```python
def scroll_fade_demo():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                *[
                    rx.el.div(
                        f"Item {index + 1}",
                        class_name="rounded-lg bg-muted px-3 py-2.5 text-sm",
                    )
                    for index in range(12)
                ],
                class_name="flex flex-col gap-1.5 p-1.5",
            ),
            class_name="h-72 scroll-fade scrollbar-none overflow-y-auto",
        ),
        class_name="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border border-input",
    )
```


# No Overflow, No Fade

If the content does not overflow, no fade is shown. You can apply `scroll-fade` to any list without checking whether it scrolls.


```python
def scroll_fade_no_fade():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                *[
                    rx.el.div(
                        f"Item {index + 1}",
                        class_name="rounded-lg bg-muted px-3 py-2.5 text-sm",
                    )
                    for index in range(3)
                ],
                class_name="flex flex-col gap-1.5 p-1.5",
            ),
            class_name="scroll-fade scrollbar-none overflow-y-auto",
        ),
        class_name="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border border-input",
    )
```


# Horizontal Scrolling

Use `scroll-fade-x` on containers that scroll horizontally, i.e. the element that has `overflow-x-auto`.


```python
def scroll_fade_horizontal():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                *[
                    rx.el.div(
                        tag,
                        class_name="shrink-0 rounded-lg bg-muted px-3 py-2.5 text-sm",
                    )
                    for tag in tags
                ],
                class_name="flex w-max gap-1.5 p-1.5",
            ),
            class_name="scroll-fade-x scrollbar-none overflow-x-auto",
        ),
        class_name="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border border-input",
    )
```


# Edge Fades

Use edge utilities when only one edge should track the scroll position.


```python
def scroll_fade_edge():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_edge_items(),
                    class_name="h-36 scroll-fade-t scrollbar-none overflow-y-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-t",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_edge_items(),
                    class_name="h-36 scroll-fade-b scrollbar-none overflow-y-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-b",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_edge_tags(),
                    class_name="scroll-fade-s scrollbar-none overflow-x-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-s",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_edge_tags(),
                    class_name="scroll-fade-e scrollbar-none overflow-x-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-e",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto flex max-w-xs min-w-0 flex-col gap-6",
    )
```


The edge utilities are scroll-aware. Start edges fade in after you scroll away from the start, and end edges fade out when you reach the end. Use `scroll-fade-t`, `scroll-fade-b`, `scroll-fade-l`, and `scroll-fade-r` for physical edges. Use `scroll-fade-s` and `scroll-fade-e` for logical inline edges.

# Fade Size

The fade depth defaults to 12% of the container, capped at 40px so tall scrollers stay subtle. Use `scroll-fade-<number>` to set a fixed size on the spacing scale instead, the same way `scroll-mt-<number>` works.


```python
def scroll_fade_size():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_size_items(),
                    class_name="h-48 scroll-fade scrollbar-none overflow-y-auto scroll-fade-4",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-4",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_size_items(),
                    class_name="h-48 scroll-fade scrollbar-none overflow-y-auto scroll-fade-24",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade-24",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto flex w-full max-w-xs flex-col gap-6",
    )
```


For one-off values, use an arbitrary length or percentage:

```reflex
rx.el.div(..., class_name="scroll-fade overflow-y-auto scroll-fade-[15%]")
```

To fade opposite edges by different amounts, use the per-edge modifiers `scroll-fade-t-<number>`, `scroll-fade-b-<number>`, `scroll-fade-s-<number>`, and `scroll-fade-e-<number>`. They override scroll-fade-<number> on the edge they target and accept arbitrary values too.

```reflex
rx.el.div(..., class_name="scroll-fade overflow-y-auto scroll-fade-b-8 scroll-fade-t-2")
```

# Disabling the Fade

Use `scroll-fade-none` to remove the fade. It works in any class order, so the typical use is responsive or stateful.


```python
def scroll_fade_none():
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_none_items(),
                    class_name="h-48 scroll-fade scrollbar-none overflow-y-auto",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    scroll_fade_none_items(),
                    class_name="h-48 scroll-fade scrollbar-none overflow-y-auto scroll-fade-none",
                ),
                class_name="overflow-hidden rounded-2xl border border-input",
            ),
            rx.el.p(
                "scroll-fade scroll-fade-none",
                class_name="text-center font-mono text-xs text-muted-foreground",
            ),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto flex w-full max-w-xs min-w-0 flex-col gap-6",
    )
```



# Fallback

The scroll-aware behavior is implemented with [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations), with no JavaScript and no scroll listeners. In browsers that do not support scroll-driven animations, `scroll-fade` falls back to a static fade on both edges, and edge utilities fall back to a static fade on the selected edge.

Since the mask is applied to the scroll container itself, a visible scrollbar fades with the content at the edges. Pair `scroll-fade` with `no-scrollbar`, which ships in the same package, if you want to hide the scrollbar entirely.
