import functools

import reflex as rx

from app.templates.footer import footer
from app.templates.navbar import navbar


def layout_decorator(
    title: str,
    description: str,
    ctas: list | None = None,
    with_create_page_cta: bool = False,
):
    """
    Decorator to wrap a page function with a sticky navbar,
    a landing header, and page-specific content.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            page_content = func(*args, **kwargs)

            return rx.el.body(
                rx.el.div(
                    rx.el.header(
                        navbar(with_create_page_cta=with_create_page_cta),
                        class_name="sticky top-0 z-50 w-full bg-background",
                    ),
                    rx.el.main(
                        rx.el.div(
                            rx.el.section(
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.h1(
                                            title,
                                            class_name="leading-tighter text-3xl font-semibold tracking-tight text-balance text-primary lg:leading-[1.1] lg:font-semibold xl:text-5xl xl:tracking-tighter max-w-4xl",
                                        ),
                                        rx.el.p(
                                            description,
                                            class_name="max-w-4xl text-base text-balance text-foreground sm:text-lg",
                                        ),
                                        rx.el.div(
                                            *(ctas if ctas else []),
                                            class_name="flex w-full items-center justify-center gap-2 pt-2 **:data-[slot=button]:shadow-none",
                                        ),
                                        class_name="flex flex-col items-center gap-2 px-6 py-8 text-center md:py-16 lg:py-20 xl:gap-4",
                                    ),
                                    class_name="w-full",
                                ),
                                class_name="border-grid pb-6",
                            ),
                            rx.el.div(
                                page_content,
                                class_name="flex-1 p-0 bg-background",
                            ),
                            class_name="flex flex-1 flex-col bg-background",
                        ),
                        class_name="flex min-h-0 flex-1 flex-col pb-6",
                    ),
                    rx.el.footer(
                        footer(),
                        class_name="w-full flex items-center justify-center py-8 text-muted-foreground !text-sm !text-center",
                    ),
                    class_name="relative z-10 flex min-h-svh flex-col bg-background overscroll-none",
                ),
                class_name="font-theme bg-background",
            )

        return wrapper

    return decorator
