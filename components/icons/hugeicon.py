"""Hugeicons Icon component."""

from reflex.components.component import Component
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var, VarData

from ..ui.component import CoreComponent


class HugeIcon(CoreComponent):
    """A HugeIcon component."""

    library = "@hugeicons/react@1.1.1"

    tag = "HugeiconsIcon"

    # The main icon to display
    icon: Var[str]

    # Alternative icon for states/interactions
    alt_icon: Var[str | None]

    # Whether to show the alternative icon
    show_alt: Var[bool]

    # The size of the icon in pixels
    size: Var[int] = Var.create(16)

    # The stroke width of the icon
    stroke_width: Var[float] = Var.create(2)

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Initialize the Icon component.

        Args:
            *children: The positional arguments
            **props: The keyword arguments

        Returns:
            The created component.

        """
        if children and isinstance(children[0], str) and "icon" not in props:
            props["icon"] = children[0]
            children = children[1:]
        for prop in ["icon", "alt_icon"]:
            if prop in props and isinstance(props[prop], str):
                icon_name = props[prop]
                props[prop] = Var(
                    icon_name,
                    _var_data=VarData(
                        imports={
                            "@hugeicons/core-free-icons@1.1.0": ImportVar(tag=icon_name)
                        }
                    ),
                )
        stroke_width = props.pop("stroke_width", 2)
        cls.set_class_name(f"[&_path]:stroke-[{stroke_width}]", props)

        return super().create(*children, **props)


hi = icon = HugeIcon.create
