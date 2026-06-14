

# Typography

Styles for headings, paragraphs, lists, etc.

# Installation
No installation is used for typographies. This page is an example of how you can use utility classes to style your text.

## h1

```python
def header_1():
    return rx.el.h1(
        "All we have to decide is what to do with the time that is given us.",
        class_name="scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance",
    )
```


## h2

```python
def header_2():
    return rx.el.h2(
        "Not all those who wander are lost.",
        class_name="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0",
    )
```


## h3

```python
def header_3():
    return rx.el.h3(
        "The Grey Havens lie beyond the reach of mortal sight.",
        class_name="scroll-m-20 text-2xl font-semibold tracking-tight",
    )
```


## h4

```python
def header_4():
    return rx.el.h4(
        "Far over the misty mountains cold.",
        class_name="scroll-m-20 text-xl font-semibold tracking-tight",
    )
```


## p

```python
def paragraph():
    return rx.el.p(
        "I have seen many an oak grow from acorn to ruinous age.",
        class_name="leading-7 [&:not(:first-child)]:mt-6",
    )
```


## blockquote

```python
def blockquote():
    return rx.el.blockquote(
        """
        "Five hundred times have the red leaves fallen in Mirkwood in my home since then," said Legolas, "and but a little while does that seem to us."
        """,
        class_name="mt-6 border-l-2 pl-6 italic",
    )
```


## table

```python
def table_list():
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "Character",
                        class_name="border border-input px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    rx.el.th(
                        "Role",
                        class_name="border border-input px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    class_name="m-0 border-t border-input p-0 even:bg-muted",
                )
            ),
            rx.el.tbody(
                rx.el.tr(
                    rx.el.td(
                        "Frodo",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    rx.el.td(
                        "Ring Bearer",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    class_name="m-0 border-t border-input p-0 even:bg-muted",
                ),
                rx.el.tr(
                    rx.el.td(
                        "Gandlaf",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    rx.el.td(
                        "The Grey / White Wizard",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    class_name="m-0 border-t border-input p-0 even:bg-muted",
                ),
                rx.el.tr(
                    rx.el.td(
                        "Legolas",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    rx.el.td(
                        "Elven archer",
                        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
                    ),
                    class_name="m-0 border-t border-input p-0 even:bg-muted",
                ),
            ),
            class_name="w-full",
        ),
        class_name="my-6 w-full overflow-y-auto",
    )
```


## list

```python
def list():
    return rx.el.ul(
        rx.el.li("Not all those who wander are lost."),
        rx.el.li("Even darkness must pass."),
        rx.el.li("Courage will now be your best defence."),
        class_name="my-6 ml-6 list-disc [&>li]:mt-2",
    )
```


## Inline code

```python
def inline_code():
    return rx.el.code(
        "@buridan-ui/ui/accordion",
        class_name="relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-medium",
    )
```

