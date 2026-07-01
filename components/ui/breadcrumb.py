import reflex as rx

from ..icons.hugeicon import hi
from ..utils.twmerge import cn


class Breadcrumb:
    @classmethod
    def root(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["aria-label"] = "breadcrumb"

        props["data-slot"] = "breadcrumb"

        return rx.el.nav(
            *children,
            class_name=cn(custom_classes),
            **props,
        )

    @classmethod
    def list(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-list"

        base_classes = (
            "flex flex-wrap items-center gap-1.5 text-sm wrap-break-word "
            "text-muted-foreground"
        )

        return rx.el.ol(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def item(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-item"

        base_classes = "inline-flex items-center gap-1"

        return rx.el.li(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def link(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-link"

        props.setdefault("href", "#")

        base_classes = "transition-colors hover:text-foreground no-underline"

        return rx.el.a(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def page(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-page"

        props["role"] = "link"

        props["aria-disabled"] = "true"

        props["aria-current"] = "page"

        base_classes = "font-normal text-foreground"

        return rx.el.span(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def separator(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-separator"

        props["role"] = "presentation"

        props["aria-hidden"] = "true"

        base_classes = "[&>svg]:size-3.5"

        if not children:
            children = (hi("ArrowRight01Icon"),)

        return rx.el.li(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )

    @classmethod
    def ellipsis(cls, *children, **props) -> rx.Component:
        custom_classes = props.pop("class_name", "")

        props["data-slot"] = "breadcrumb-ellipsis"

        props["role"] = "presentation"

        props["aria-hidden"] = "true"

        base_classes = "flex size-5 items-center justify-center [&>svg]:size-4"

        if not children:
            children = (
                rx.icon(tag="ellipsis"),
                rx.el.span("More", class_name="sr-only"),
            )

        return rx.el.span(
            *children,
            class_name=cn(base_classes, custom_classes),
            **props,
        )


breadcrumb = Breadcrumb
