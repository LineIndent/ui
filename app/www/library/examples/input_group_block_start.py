import reflex as rx

from components.icons.hugeicon import hi
from components.ui.field import field
from components.ui.input_group import input_group


def input_group_block_start() -> rx.Component:
    return rx.el.div(
        field.root(
            field.label("Input", html_for="block-start-input"),
            field.content(
                input_group.root(
                    input_group.input(
                        id="block-start-input",
                        placeholder="Enter your name",
                    ),
                    input_group.addon(
                        input_group.text("Full Name"),
                        align="block-start",
                    ),
                    class_name="h-auto",
                )
            ),
            field.description("Header positioned above the input."),
            orientation="vertical",
        ),
        field.root(
            field.label("Textarea", html_for="block-start-textarea"),
            field.content(
                input_group.root(
                    input_group.textarea(
                        id="block-start-textarea",
                        placeholder="console.log('Hello, world!');",
                        class_name="font-mono text-sm",
                    ),
                    input_group.addon(
                        hi("FileCodeIcon", class_name="text-muted-foreground"),
                        input_group.text("script.py", class_name="font-mono"),
                        input_group.button(
                            hi("CopyIcon"),
                            rx.el.span("Copy", class_name="sr-only"),
                            size="icon-xs",
                            class_name="ml-auto",
                        ),
                        align="block-start",
                    ),
                )
            ),
            field.description("Header positioned above the textarea."),
            orientation="vertical",
        ),
        class_name="flex flex-col gap-y-6 max-w-sm w-full",
    )
