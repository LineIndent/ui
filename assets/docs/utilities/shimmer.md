

# Shimmer

Utilities for adding a shimmer effect to text elements.

>The **shimmer** utility is purely composed of CSS and is based on [shadcn/shimmer](https://ui.shadcn.com/docs/utils/shimmer). No extensions to **rxconfig.py** are needed as it uses **Tailwind v4** syntax. 


# Installation 

If your project was set up with `buridan init`, you already have shimmer. It ships with the `buridan` package, which the CLI imports in your global CSS file.

Otherwise install the `buirdan` package:

```uv
uv run buridan init
```

You can also copy paste the `shimmer` source directly into your `globals.css` file. Make sure you also include the correct imports, such as `@tailwind utilities;` at the top of your CSS file. 

```css
@property --shimmer-angle {
    syntax: "<angle>";
    inherits: true;
    initial-value: 20deg;
}
@property --shimmer-image {
    syntax: "*";
    inherits: false;
}
@property --shimmer-text-fill {
    syntax: "*";
    inherits: false;
}

@theme inline {
    @keyframes tw-shimmer {
        from {
            background-position: 100% 0;
        }
        to {
            background-position: 0 0;
        }
    }
}

@utility shimmer {
    --_spread: var(--shimmer-spread, calc(3ch + 40px));
    --_base: currentColor;
    --_highlight: var(
        --shimmer-color,
        oklch(from currentColor l c h / calc(alpha* 0.2))
    );

    background-image: var(
        --shimmer-image,
        linear-gradient(
            calc(90deg + var(--shimmer-angle)),
            var(--_base) calc(50% - var(--_spread)),
            color-mix(in oklch, var(--_highlight), var(--_base) 50%)
                calc(50% - var(--_spread) * 0.5),
            var(--_highlight) 50%,
            color-mix(in oklch, var(--_highlight), var(--_base) 50%)
                calc(50% + var(--_spread) * 0.5),
            var(--_base) calc(50% + var(--_spread))
        )
    );
    background-repeat: no-repeat;
    background-size: calc(200% + var(--_spread) * 2) 100%;
    background-position: 0 0;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: var(--shimmer-text-fill, transparent);
    animation: tw-shimmer var(--shimmer-duration, 2s) linear infinite;

    @variant dark {
        --_highlight: var(
            --shimmer-color,
            oklch(
                from currentColor max(0.8, calc(l + 0.4)) c h /
                    calc(alpha + 0.4)
            )
        );
    }

    &:where([dir="rtl"], [dir="rtl"] *) {
        animation-direction: reverse;
    }
}

@utility shimmer-once {
    animation-iteration-count: 1;
}

@utility shimmer-reverse {
    animation-direction: reverse;
}

@utility shimmer-none {
    --shimmer-image: none;
    --shimmer-text-fill: currentColor;
}

@utility shimmer-color-* {
    --shimmer-color: --value(--color, [color]);
    --shimmer-color: color-mix(
        in oklch,
        --value(--color, [color]) calc(--modifier(integer) * 1%),
        transparent
    );
}

@utility shimmer-duration-* {
    --shimmer-duration: calc(--value(integer) * 1ms);
}

@utility shimmer-spread-* {
    --shimmer-spread: calc(var(--spacing) * --value(integer));
    --shimmer-spread: --value([length], [percentage]);
}

@utility shimmer-angle-* {
    --shimmer-angle: calc(--value(integer) * 1deg);
}

@media (prefers-reduced-motion: reduce) {
    .shimmer {
        animation: none;
        background-image: none;
        -webkit-text-fill-color: currentColor;
    }
}
```


# Usage

| Class                         | Styles                                                                                               |
| ----------------------------- | ---------------------------------------------------------------------------------------------------- |
| `shimmer`                     | `background-clip: text;` <br /> `animation: tw-shimmer var(--shimmer-duration, 2s) linear infinite;` |
| `shimmer-once`                | `animation-iteration-count: 1;`                                                                      |
| `shimmer-reverse`             | `animation-direction: reverse;`                                                                      |
| `shimmer-none`                | `--shimmer-image: none;` <br /> `--shimmer-text-fill: currentColor;`                                 |
| `shimmer-color-<color>`       | `--shimmer-color: <color>;`                                                                          |
| `shimmer-color-[<value>]`     | `--shimmer-color: <value>;`                                                                          |
| `shimmer-color-<color>/<pct>` | `--shimmer-color: color-mix(in oklch, <color> <pct>, transparent);`                                  |
| `shimmer-duration-<number>`   | `--shimmer-duration: calc(<number> * 1ms);`                                                          |
| `shimmer-spread-<number>`     | `--shimmer-spread: calc(var(--spacing) * <number>);`                                                 |
| `shimmer-spread-[<value>]`    | `--shimmer-spread: <value>;`                                                                         |
| `shimmer-angle-<number>`      | `--shimmer-angle: calc(<number> * 1deg);`                                                            |

Add shimmer to a text element.

```reflex
rx.el.p("Generating response", class_name="shimmer text-muted-foreground w-fit")
```

The effect is pure CSS. The text is painted with `background-clip: text`, and the highlight sweeps across it in a seamless loop.

>**Note**: If the **shimmer** utility isn't working properly, try adding **w-fit** to the text styling, as it ensures the animation doesn't exceed the inherit width of the text.

# Color

Use `shimmer-color-<color>` to set the highlight color explicitly. It accepts theme colors with an optional opacity modifier, or any arbitrary color value.


```python
def shimmer_color():
    return rx.el.div(
        rx.el.p(
            "Generating response", class_name="shimmer shimmer-color-blue-500/60 w-fit"
        ),
        rx.el.p(
            "Generating response", class_name="shimmer shimmer-color-[#378ADD] w-fit"
        ),
        class_name="flex flex-col items-center gap-2 text-sm text-muted-foreground",
    )
```


# Duration

Use `shimmer-duration-<number>` to set the duration of one sweep in milliseconds. The default is `2000`, i.e. `2s`.


```python
def shimmer_duration():
    return rx.el.div(
        rx.el.div(
            rx.el.p("Generating response...", class_name="shimmer"),
            rx.el.p("shimmer", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.p(
                "Generating response...", class_name="shimmer shimmer-duration-1000"
            ),
            rx.el.p("shimmer-duration-1000", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto grid w-full max-w-lg gap-6 text-center text-sm text-muted-foreground sm:grid-cols-2",
    )
```


# Spread

Use `shimmer-spread-<number>` to set the width of the highlight band using the spacing scale. The default is `calc(3ch + 40px)`: a fixed base plus a `3ch` term that scales with the font size.


```python
def shimmer_spread():
    return rx.el.div(
        rx.el.div(
            rx.el.p("Generating response...", class_name="shimmer shimmer-spread-4"),
            rx.el.p("shimmer-spread-4", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.p("Generating response...", class_name="shimmer shimmer-spread-24"),
            rx.el.p("shimmer-spread-24", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto grid w-full max-w-lg gap-6 text-center text-sm text-muted-foreground sm:grid-cols-2",
    )
```


# Angle

Use `shimmer-angle-<number>` to set the tilt of the highlight band in degrees. The default is `20`.


```python
def shimmer_angle():
    return rx.el.div(
        rx.el.div(
            rx.el.p("Generating response...", class_name="shimmer"),
            rx.el.p("shimmer", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        rx.el.div(
            rx.el.p("Generating response...", class_name="shimmer shimmer-angle-45"),
            rx.el.p("shimmer-angle-45", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        class_name="mx-auto grid w-full max-w-lg gap-6 text-center text-sm text-muted-foreground sm:grid-cols-2",
    )
```


# Reverse

Use `shimmer-reverse` to sweep the highlight in the opposite direction.


```python
def shimmer_reverse():
    return rx.el.div(
        rx.el.div(
            rx.el.p("Generating response...", class_name="shimmer shimmer-reverse"),
            rx.el.p("shimmer reverse", class_name="font-mono text-xs"),
            class_name="flex flex-col gap-3",
        ),
        class_name="flex text-center items-center gap-2 text-sm text-muted-foreground",
    )
```


# Play Once

Use `shimmer-once` to play a single sweep instead of looping, useful as a reveal when streaming completes. Pair it with `shimmer-duration-<number>` to control how long the sweep takes.


```python
def shimmer_once():
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                "Generating response...",
                class_name=(
                    "shimmer text-sm text-muted-foreground "
                    "shimmer-duration-1100 shimmer-once"
                ),
            ),
            key=shimmer_key.value.to(str),
        ),
        button(
            "Replay",
            variant="outline",
            size="sm",
            on_click=shimmer_key.set_value(shimmer_key.value.to(int) + 1),
        ),
        class_name="flex flex-col items-center gap-4",
    )
```


```reflex
rx.el.p("Response Generated", class_name="shimmer shimmer-duration-1100 shimmer-once")
```

# Disabling the Shimmer

Use `shimmer-none` to turn the effect off and render the text normally. It works in any class order, so the typical use is responsive or stateful.


```python
def shimmer_none():
    return rx.el.div(
        rx.el.p("Generating response...", class_name="shimmer md:shimmer-none"),
        rx.el.p("shimmer md:shimmer-none", class_name="font-mono text-xs"),
        class_name="flex flex-col items-center gap-3 text-sm text-muted-foreground",
    )
```

