import reflex as rx

PARAGRAPH_CLASS = "text-sm leading-7 mb-4"

HEADING_1_CLASS = "text-2xl font-semibold mt-8 mb-3 first:mt-0 scroll-mt-14"

HEADING_2_CLASS = "text-xl font-semibold mt-6 mb-2 scroll-mt-14"

LIST_ITEM_CLASS = "text-sm leading-7 text-slate-11"

LINK_CLASS = (
    "font-medium "
    "text-foreground "
    "underline underline-offset-4 "
    "decoration-foreground "
    "hover:!text-foreground "
    "hover:!decoration-foreground"
)


# --- Helper error functions during parsing ---
def render_parse_error(msg: str):
    return rx.el.p(msg, class_name="text-sm text-red-500")


# # --- Helper functions ---
# def render_heading(level: int, text: str) -> rx.Component:
#     return rx.el.header(
#         text, class_name=HEADING_1_CLASS if level == 1 else HEADING_2_CLASS, id=text
#     )


def render_heading(level: int, text: str) -> rx.Component:
    normalized_id = rx.Var.create(text).to(str).lower().replace(" ", "-")

    if level == 1:
        return rx.el.h1(
            rx.el.a(
                rx.el.span(
                    text,
                    class_name="hover:underline hover:underline-offset-6",
                ),
                href=f"#{normalized_id}",
                class_name=(
                    "after:content-['#'] after:ml-2 after:opacity-0 hover:after:opacity-100 after:text-muted-foreground"
                ),
            ),
            class_name=HEADING_1_CLASS if level == 1 else HEADING_2_CLASS,
            id=normalized_id,
        )

    else:
        return rx.el.h2(
            rx.el.a(
                rx.el.span(
                    text,
                    class_name="hover:underline hover:underline-offset-6",
                ),
                href=f"#{normalized_id}",
                class_name=(
                    "after:content-['#'] after:ml-2 after:opacity-0 hover:after:opacity-100 after:text-muted-foreground"
                ),
            ),
            class_name=HEADING_1_CLASS if level == 1 else HEADING_2_CLASS,
            id=normalized_id,
        )

    return rx.el.header(
        rx.el.a(
            rx.el.span(
                text,
                class_name="hover:underline hover:underline-offset-6",
            ),
            href=f"#{normalized_id}",
            class_name=(
                "after:content-['#'] after:ml-2 after:opacity-0 hover:after:opacity-100 after:text-muted-foreground"
            ),
        ),
        class_name=HEADING_1_CLASS if level == 1 else HEADING_2_CLASS,
        id=normalized_id,
    )


def render_paragraph(text: str) -> rx.Component:
    return rx.el.p(text, class_name=PARAGRAPH_CLASS)


def render_list_item(text: str) -> rx.Component:
    return rx.list_item(rx.el.p(text, class_name=LIST_ITEM_CLASS))


def render_link(*args, **props) -> rx.Component:
    return rx.link(*args, class_name=LINK_CLASS, **props)


def render_pre(*children, **props) -> rx.Component:
    language = props.get("language")

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    language,
                    class_name="text-muted-foreground text-sm font-normal px-[1rem] py-2",
                ),
                class_name="w-full border-b border-input/70 flex flex-row items-center justify-between",
            ),
            rx.el.div(
                rx.el.pre(
                    rx.el.code(
                        *children,
                        style={
                            "white-space": "pre",
                            "color": "var(--foreground)",
                            "font-size": "13px",
                            "padding": "1rem 1rem",
                            "display": "block",
                        },
                    ),
                ),
                class_name="overflow-x-auto overflow-y-auto scrollbar-none flex-1 min-h-0 pr-[1rem]",
            ),
            class_name="w-full flex-1 min-h-0 flex flex-col h-full",
        ),
        class_name="rounded-[1rem] flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card my-4",
    )


def render_blockquote(*children, **props) -> rx.Component:
    return rx.el.div(
        *children,
        class_name="w-full rounded-[1rem] bg-secondary dark:bg-card flex items-center justify-center p-4 mb-4 "
        + "[&>p]:mb-0 [&>p]:leading-6",
    )


# --- Final Component Map ---
markdown_component_map = {
    "h1": lambda text: render_heading(1, text),
    "h2": lambda text: render_heading(2, text),
    "p": render_paragraph,
    "li": render_list_item,
    "a": render_link,
    "blockquote": render_blockquote,
    "code": lambda text: rx.el.span(text, class_name="bg-secondary rounded-md p-1"),
    "pre": render_pre,
    "table": lambda *children, **props: rx.el.div(
        rx.el.div(
            rx.el.table(
                *children,
                **props,
                class_name="w-max min-w-full",
            ),
            class_name="w-full overflow-x-auto scrollbar-none",
        ),
        class_name="w-full !text-sm rounded-[1rem] border border-input mb-4",
    ),
    "thead": lambda *children, **props: rx.el.thead(
        *children, **props, class_name="border-input border-b"
    ),
    "tbody": lambda *children, **props: rx.el.tbody(
        *children, **props, class_name="divide-input divide-y"
    ),
    "tr": lambda *children, **props: rx.el.tr(
        *children,
        **props,
        class_name="m-0 p-0",
    ),
    "th": lambda *children, **props: rx.el.th(
        *children,
        **props,
        class_name=(
            "px-4 py-2 text-left font-bold "
            "[&[align=center]]:text-center "
            "whitespace-nowrap "
            "[&[align=right]]:text-right"
        ),
    ),
    "td": lambda *children, **props: rx.el.td(
        *children,
        **props,
        class_name=(
            "px-4 py-2 text-left "
            "[&[align=center]]:text-center "
            "whitespace-nowrap "
            "[&[align=right]]:text-right"
        ),
    ),
}
