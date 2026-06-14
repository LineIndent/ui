import reflex as rx


def typography_h1(*children, class_name: str = "", **props):
    """Large heading - h1"""
    base_classes = "scroll-m-20 text-4xl font-extrabold tracking-tight text-balance"
    return rx.el.h1(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_h2(*children, class_name: str = "", **props):
    """Section heading - h2"""
    base_classes = "scroll-m-20 border-b border-input pb-2 text-3xl font-semibold tracking-tight first:mt-0"
    return rx.el.h2(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_h3(*children, class_name: str = "", **props):
    """Subsection heading - h3"""
    base_classes = "scroll-m-20 text-2xl font-semibold tracking-tight"
    return rx.el.h3(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_h4(*children, class_name: str = "", **props):
    """Small heading - h4"""
    base_classes = "scroll-m-20 text-xl font-semibold tracking-tight"
    return rx.el.h4(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_p(*children, class_name: str = "", **props):
    """Paragraph text"""
    base_classes = "leading-7 [&:not(:first-child)]:mt-6"
    return rx.el.p(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_blockquote(*children, class_name: str = "", **props):
    """Blockquote for quotes"""
    base_classes = "mt-6 border-l-2 pl-6 italic"
    return rx.el.blockquote(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_list(*children, class_name: str = "", **props):
    """Unordered list"""
    base_classes = "my-6 ml-6 list-disc [&>li]:mt-2"
    return rx.el.ul(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_inline_code(*children, class_name: str = "", **props):
    """Inline code"""
    base_classes = "bg-[var(--muted)] relative rounded px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold"
    return rx.el.code(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_lead(*children, class_name: str = "", **props):
    """Lead paragraph (larger intro text)"""
    base_classes = "text-[var(--muted-foreground)] text-xl"
    return rx.el.p(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_large(*children, class_name: str = "", **props):
    """Large text"""
    base_classes = "text-lg font-semibold"
    return rx.el.div(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_small(*children, class_name: str = "", **props):
    """Small text"""
    base_classes = "text-sm leading-none font-medium"
    return rx.el.small(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_muted(*children, class_name: str = "", **props):
    """Muted text"""
    base_classes = "text-[var(--muted-foreground)] text-sm"
    return rx.el.p(
        *children, class_name=f"{base_classes} {class_name}".strip(), **props
    )


def typography_table(*children, class_name: str = "", **props):
    """Table wrapper with styling"""
    base_classes = "my-6 w-full overflow-y-auto"
    return rx.el.div(
        rx.el.table(
            *children,
            class_name="w-full",
        ),
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def typography_table_header(*children, **props):
    """Table header row"""
    return rx.el.tr(
        *children,
        class_name="even:bg-[var(--muted)] m-0 border-t border-input p-0",
        **props,
    )


def typography_table_head(*children, **props):
    """Table header cell"""
    return rx.el.th(
        *children,
        class_name="border border-input px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right",
        **props,
    )


def typography_table_row(*children, **props):
    """Table body row"""
    return rx.el.tr(
        *children,
        class_name="even:bg-[var(--muted)] m-0 border-t border-input p-0",
        **props,
    )


def typography_table_cell(*children, **props):
    """Table body cell"""
    return rx.el.td(
        *children,
        class_name="border border-input px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right",
        **props,
    )
