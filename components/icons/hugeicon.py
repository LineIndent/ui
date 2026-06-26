"""Hugeicons Icon component."""

from reflex.components.component import Component
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var, VarData
from reflex_components_internal.components.component import CoreComponent

REACT_LIBRARY = "@hugeicons/react@1.1.6"
CORE_ICONS_LIBRARY = "@hugeicons/core-free-icons@4.2.1"


class HugeIcon(CoreComponent):
    """A HugeIcon component using HugeiconsIcon from @hugeicons/react."""

    library = REACT_LIBRARY
    tag = "HugeiconsIcon"

    # Main icon
    icon: Var[str]

    # Alternative icon
    alt_icon: Var[str | None]

    # Toggle alt icon
    show_alt: Var[bool]

    # Size (px or css value)
    size: Var[int | str] = Var.create(16)

    # Colors
    color: Var[str]
    primary_color: Var[str]
    secondary_color: Var[str]

    # Stroke options
    stroke_width: Var[float] = Var.create(1.5)
    absolute_stroke_width: Var[bool]

    # Multicolor option
    disable_secondary_opacity: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create icon component."""

        # Support:
        # hi("HomeIcon")
        if children and isinstance(children[0], str) and "icon" not in props:
            props["icon"] = children[0]
            children = children[1:]

        # Convert icon strings into import-backed Vars
        for prop in ("icon", "alt_icon"):
            value = props.get(prop)

            if isinstance(value, str):
                props[prop] = Var(
                    value,
                    _var_data=VarData(
                        imports={CORE_ICONS_LIBRARY: [ImportVar(tag=value)]}
                    ),
                )

        stroke_width = props.get("stroke_width", 1.5)

        cls.set_class_name(
            f"[&_path]:stroke-[{stroke_width}]",
            props,
        )

        return super().create(*children, **props)


hi = icon = HugeIcon.create
