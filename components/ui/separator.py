from typing import Literal

from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from .base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    SEPARATOR = "shrink-0 bg-input data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:w-px data-[orientation=vertical]:self-stretch"


class SeparatorComponent(BaseUIComponent):
    tag = "Separator"
    library = f"{PACKAGE_NAME}/separator"

    orientation: Var[Literal["horizontal", "vertical"]]

    @property
    def import_var(self):
        return ImportVar(tag="Separator", package_path="", install=False)

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        props["data-slot"] = "separator"
        if "orientation" not in props:
            props["orientation"] = "horizontal"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


separator = SeparatorComponent.create
