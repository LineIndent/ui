from reflex.components.component import ComponentNamespace
from reflex_components_core.el import Input as BaseInput

from ..utils.twmerge import cn
from .component import CoreComponent


class ClassNames:
    INPUT = (
        "w-full file:text-foreground placeholder:text-muted-foreground "
        "selection:bg-primary selection:text-primary-foreground "
        "dark:bg-input/30 border-input "
        "h-8 w-full min-w-0 rounded-lg border bg-transparent px-3 py-1 text-base "
        "transition-[color,box-shadow] outline-none "
        "file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium "
        "disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 "
        "md:text-sm "
        "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] "
        "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 "
        "aria-invalid:border-destructive"
    )


class InputComponent(BaseInput, CoreComponent):
    @classmethod
    def create(cls, *children, **props) -> BaseInput:

        existing_class = props.get("class_name", "")

        props["class_name"] = cn(ClassNames.INPUT, existing_class)

        props.setdefault("data_slot", "input")

        if "type" not in props:
            props["type"] = "text"

        return super().create(*children, **props)


class Input(ComponentNamespace):
    __call__ = staticmethod(InputComponent.create)
    class_name = ClassNames


input = Input()
