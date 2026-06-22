from typing import Optional, Union

import reflex as rx
from reflex_components_core.el import Input as ElInput
from reflex_components_core.el import Textarea as ElTextarea


class ComponentFactory:
    def __init__(self, base_component_class, base_classes: str):
        self.base_class = base_component_class
        self.base_classes = base_classes

    def __call__(self, **props):
        custom_classes = props.get("class_name", "")
        props["class_name"] = f"{self.base_classes} {custom_classes}".strip()
        props["data_slot"] = "input"

        return self.base_class.create(**props)


Input = ComponentFactory(
    ElInput,
    "flex-1 bg-transparent border-0 outline-none text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] px-2 py-2 text-sm",
)

TextareaComp = ComponentFactory(
    ElTextarea,
    "flex-1 bg-transparent border-0 outline-none resize-none text-[var(--foreground)] placeholder:text-[var(--muted-foreground)] placeholder:text-sm px-3 py-3 text-sm",
)


def input_with_addons(
    *children,
    placeholder: str = "",
    prefix: Optional[Union[str, rx.Component]] = None,
    suffix: Optional[Union[str, rx.Component]] = None,
    input_type: str = "text",
    class_name: str = "",
    **props,
):
    children = list(children)
    if prefix:
        if isinstance(prefix, str):
            prefix = rx.el.p(
                prefix,
                class_name="text-[var(--muted-foreground)] text-sm font-medium pl-2 select-none pointer-events-none",
            )
        children.insert(0, prefix)

    children.append(Input(type=input_type, placeholder=placeholder, **props))

    if suffix:
        if isinstance(suffix, str):
            suffix = rx.el.p(
                suffix,
                class_name="text-[var(--muted-foreground)] text-sm font-medium pr-2 select-none pointer-events-none",
            )
        children.append(suffix)

    return rx.el.div(
        *children,
        class_name=f"flex items-center w-full h-9 bg-transparent border border-[var(--input)] dark:bg-[var(--input)]/30 rounded-[var(--radius)] shadow-xs focus-within:border-[var(--ring)] focus-within:ring-[var(--ring)]/50 focus-within:ring-[3px] transition-[color,box-shadow] {class_name}",
    )


def textarea_with_footer(
    placeholder: str = "",
    footer_text: Optional[str] = None,
    class_name: str = "",
    **props,
):
    children = [TextareaComp(placeholder=placeholder, **props)]
    if footer_text:
        children.append(
            rx.el.p(
                footer_text,
                class_name="text-[var(--muted-foreground)] text-xs px-3 pb-3 pt-0 select-none pointer-events-none",
            )
        )


input_group = input_with_addons
