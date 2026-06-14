import reflex as rx


def breadcrumb(*children, **props):
    """Breadcrumb navigation container"""
    return rx.el.nav(
        *children, aria_label="breadcrumb", data_slot="breadcrumb", **props
    )


def breadcrumb_list(*children, class_name: str = "", **props):
    """Ordered list container for breadcrumb items"""
    base_classes = (
        "text-[var(--muted-foreground)] flex flex-wrap items-center gap-1 text-sm "
        "break-words sm:gap-2.5"
    )

    return rx.el.ol(
        *children,
        data_slot="breadcrumb-list",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_item(*children, class_name: str = "", **props):
    """Individual breadcrumb item"""
    base_classes = "inline-flex items-center gap-1.5"

    return rx.el.li(
        *children,
        data_slot="breadcrumb-item",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_link(*children, href: str = "#", class_name: str = "", **props):
    """Breadcrumb link (clickable)"""
    base_classes = "hover:text-[var(--foreground)] transition-colors no-underline"

    return rx.el.a(
        *children,
        href=href,
        data_slot="breadcrumb-link",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_page(*children, class_name: str = "", **props):
    """Current page breadcrumb (non-clickable)"""
    base_classes = "text-[var(--foreground)] font-normal"

    return rx.el.span(
        *children,
        role="link",
        aria_disabled="true",
        aria_current="page",
        data_slot="breadcrumb-page",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_separator(*children, class_name: str = "", **props):
    """Separator between breadcrumb items"""
    base_classes = "[&>svg]:size-3.5"

    if not children:
        children = (rx.icon(tag="chevron-right", size=14),)

    return rx.el.li(
        *children,
        role="presentation",
        aria_hidden="true",
        data_slot="breadcrumb-separator",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )


def breadcrumb_ellipsis(class_name: str = "", **props):
    """Ellipsis for collapsed breadcrumb items"""
    base_classes = "flex size-9 items-center justify-center"

    return rx.el.span(
        rx.icon(tag="ellipsis", size=16),
        rx.el.span("More", class_name="sr-only"),
        role="presentation",
        aria_hidden="true",
        data_slot="breadcrumb-ellipsis",
        class_name=f"{base_classes} {class_name}".strip(),
        **props,
    )
