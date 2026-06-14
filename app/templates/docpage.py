import reflex as rx

from app.templates.docsidebar import sidebar
from app.templates.footer import footer
from app.templates.navbar import navbar


def docpage(main_content, toc_content):
    """The template for all documentation pages."""
    return rx.el.div(
        rx.el.header(navbar(), class_name="sticky top-0 z-50"),
        rx.el.main(
            rx.el.div(
                sidebar(),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            main_content,
                            class_name="mx-auto flex w-full max-w-[40rem] min-w-0 flex-1 px-2 py-6 md:px-0 lg:py-8",
                        ),
                        class_name="flex-1 min-w-0",
                    ),
                    toc_content,
                    class_name="flex items-start w-full flex-1 min-w-0",
                ),
                class_name="flex w-full gap-x-0 xl:max-w-[96rem] 2xl:max-w-[96rem] mx-auto px-7",
            ),
            class_name="w-full",
        ),
        rx.el.footer(
            footer(),
            class_name="w-full flex items-center justify-center py-8 text-muted-foreground !text-sm !text-center",
        ),
        class_name="bg-background relative flex min-h-screen flex-col",
    )
