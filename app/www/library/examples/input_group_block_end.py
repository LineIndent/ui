import reflex as rx

from components.ui.field import field
from components.ui.input_group import input_group


def input_group_block_end() -> rx.Component:
    return rx.el.div(
        field.root(
            field.label("Input", html_for="block-end-input"),
            field.content(
                input_group.root(
                    input_group.input(
                        id="block-end-input",
                        placeholder="Enter amount",
                    ),
                    input_group.addon(
                        input_group.text("USD"),
                        align="block-end",
                    ),
                    class_name="h-auto",
                )
            ),
            field.description("Footer positioned below the input."),
            orientation="vertical",
        ),
        field.root(
            field.label("Textarea", html_for="block-end-textarea"),
            field.content(
                input_group.root(
                    input_group.textarea(
                        id="block-end-textarea",
                        placeholder="Write a comment...",
                    ),
                    input_group.addon(
                        input_group.text("0/280"),
                        input_group.button(
                            "Post",
                            variant="default",
                            size="sm",
                            class_name="ml-auto",
                        ),
                        align="block-end",
                    ),
                )
            ),
            field.description("Footer positioned below the textarea."),
            orientation="vertical",
        ),
        class_name="flex flex-col gap-y-6 max-w-sm w-full",
    )
