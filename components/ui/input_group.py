from typing import Literal

from reflex.components.component import ComponentNamespace
from reflex_components_core.el import Div as ElDiv
from reflex_components_core.el import Span as ElSpan

from ..utils.twmerge import cn
from .button import button
from .component import CoreComponent
from .input import input
from .textarea import textarea

LiteralAlign = Literal["inline-start", "inline-end", "block-start", "block-end"]
LiteralSize = Literal["xs", "sm", "icon-xs", "icon-sm"]


class ClassNames:
    """Design tokens for the input group structural parts."""

    ROOT = (
        "group/input-group relative flex h-8 w-full min-w-0 items-center rounded-lg border border-input "
        "transition-colors outline-none in-data-[slot=combobox-content]:focus-within:border-inherit "
        "in-data-[slot=combobox-content]:focus-within:ring-0 has-disabled:bg-input/50 has-disabled:opacity-50 "
        "has-[[data-slot=input-group-control]:focus-visible]:border-ring has-[[data-slot=input-group-control]:focus-visible]:ring-3 "
        "has-[[data-slot=input-group-control]:focus-visible]:ring-ring/50 has-[[data-slot][aria-invalid=true]]:border-destructive "
        "has-[[data-slot][aria-invalid=true]]:ring-3 has-[[data-slot][aria-invalid=true]]:ring-destructive/20 "
        "has-[>[data-align=block-end]]:h-auto has-[>[data-align=block-end]]:flex-col has-[>[data-align=block-start]]:h-auto "
        "has-[>[data-align=block-start]]:flex-col has-[>textarea]:h-auto dark:bg-input/30 dark:has-disabled:bg-input/80 "
        "dark:has-[[data-slot][aria-invalid=true]]:ring-destructive/40 has-[>[data-align=block-end]]:[&>input]:pt-3 "
        "has-[>[data-align=block-start]]:[&>input]:pb-3 has-[>[data-align=inline-end]]:[&>input]:pr-1.5 "
        "has-[>[data-align=inline-start]]:[&>input]:pl-1.5"
    )

    ADDON = (
        "flex h-auto cursor-text items-center justify-center gap-2 py-1.5 text-sm font-medium text-muted-foreground "
        "select-none group-data-[disabled=true]/input-group:opacity-50 [&>kbd]:rounded-[calc(var(--radius)-5px)] "
        "[&>svg:not([class*='size-'])]:size-4"
    )

    TEXT = "flex items-center gap-2 text-sm text-muted-foreground [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4"

    CONTROL_INPUT = (
        "flex-1 rounded-none border-0 bg-transparent shadow-none ring-0 focus-visible:ring-0 "
        "disabled:bg-transparent aria-invalid:ring-0 dark:bg-transparent dark:disabled:bg-transparent"
    )

    CONTROL_TEXTAREA = (
        "flex-1 resize-none rounded-none border-0 bg-transparent py-2 shadow-none ring-0 focus-visible:ring-0 "
        "disabled:bg-transparent aria-invalid:ring-0 dark:bg-transparent dark:disabled:bg-transparent"
    )

    @classmethod
    def get_addon_align(cls, align: str) -> str:
        variants = {
            "inline-start": "order-first pl-2 has-[>button]:ml-[-0.3rem] has-[>kbd]:ml-[-0.15rem]",
            "inline-end": "order-last pr-2 has-[>button]:mr-[-0.3rem] has-[>kbd]:mr-[-0.15rem]",
            "block-start": "order-first w-full justify-start px-2.5 pt-2 group-has-[>input]/input-group:pt-2 [.border-b]:pb-2",
            "block-end": "order-last w-full justify-start px-2.5 pb-2 group-has-[>input]/input-group:pb-2 [.border-t]:pt-2",
        }
        return variants.get(align, variants["inline-start"])

    @classmethod
    def get_button_size(cls, size: str) -> str:
        variants = {
            "xs": "h-6 gap-1 rounded-[calc(var(--radius)-3px)] px-1.5 [&>svg:not([class*='size-'])]:size-3.5",
            "sm": "",
            "icon-xs": "size-6 rounded-[calc(var(--radius)-3px)] p-0 has-[>svg]:p-0",
            "icon-sm": "size-8 p-0 has-[>svg]:p-0",
        }
        return variants.get(size, variants["xs"])


class InputGroupRoot(ElDiv, CoreComponent):
    """The master wrapper layout that manages inner contextual focus states."""

    @classmethod
    def create(cls, *children, **props) -> ElDiv:
        props["role"] = "group"
        props["data_slot"] = "input-group"

        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class InputGroupAddon(ElDiv, CoreComponent):
    """Slots for badges, icons, prefix indicators, and descriptive side notes."""

    @classmethod
    def create(cls, *children, **props) -> ElDiv:
        props["role"] = "group"
        props["data_slot"] = "input-group-addon"

        align = props.pop("align", "inline-start")
        props["data_align"] = align

        addon_defaults = cn(ClassNames.ADDON, ClassNames.get_addon_align(align))

        cls.set_class_name(addon_defaults, props)
        return super().create(*children, **props)

    def add_custom_code(self) -> list[str]:
        """Injects the focus redirection script directly into the component scope."""
        focus_script = """
        if (typeof window !== "undefined") {
            const bindInputGroupAddons = () => {
                document.querySelectorAll('[data-slot="input-group-addon"]').forEach(addon => {
                    if (!addon.onclick) {
                        addon.onclick = (e) => {
                            if (!e.target.closest('button')) {
                                addon.parentElement?.querySelector('input')?.focus();
                            }
                        };
                    }
                });
            };

            // Run immediately if DOM is already cooked
            if (document.readyState === "loading") {
                document.addEventListener("DOMContentLoaded", bindInputGroupAddons);
            } else {
                bindInputGroupAddons();
            }

            // Keep it active across single-page transitions or dynamic updates
            const observer = new MutationObserver(bindInputGroupAddons);
            observer.observe(document.body, { childList: true, subtree: true });
        }
        """
        return [focus_script]


class InputGroupText(ElSpan, CoreComponent):
    """Inline typography labels tailored for input headers."""

    @classmethod
    def create(cls, *children, **props) -> ElSpan:
        cls.set_class_name(ClassNames.TEXT, props)
        return super().create(*children, **props)


class InputGroupButton(CoreComponent):
    """Clean mini action button targeting inside input headers or tags."""

    @classmethod
    def create(cls, *children, **props):
        props.setdefault("type", "button")
        props.setdefault("variant", "ghost")

        size = props.pop("size", "xs")
        props["data_size"] = size

        props["class_name"] = cn(
            "flex items-center gap-2 text-sm shadow-none",
            ClassNames.get_button_size(size),
            props.get("class_name", ""),
        )

        return button(*children, **props)


class InputGroupInput(CoreComponent):
    """Stripped field layout optimized for placement inside a group box row."""

    @classmethod
    def create(cls, *children, **props):
        props.setdefault("type", "text")
        props["data_slot"] = "input-group-control"
        props["class_name"] = cn(
            ClassNames.CONTROL_INPUT,
            props.get("class_name", ""),
        )

        return input(*children, **props)


class InputGroupTextarea(CoreComponent):
    """Stripped textarea configuration context optimized for layout flow blocks."""

    @classmethod
    def create(cls, *children, **props):
        props["data_slot"] = "input-group-control"
        props["class_name"] = cn(
            ClassNames.CONTROL_TEXTAREA, props.get("class_name", "")
        )

        return textarea(*children, **props)


class InputGroupNamespace(ComponentNamespace):
    """Unified layout construction tree for complex group components."""

    root = staticmethod(InputGroupRoot.create)
    addon = staticmethod(InputGroupAddon.create)
    button = staticmethod(InputGroupButton.create)
    text = staticmethod(InputGroupText.create)
    input = staticmethod(InputGroupInput.create)
    textarea = staticmethod(InputGroupTextarea.create)
    class_names = ClassNames


input_group = InputGroupNamespace()
