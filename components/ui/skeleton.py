"""Custom skeleton component."""

from reflex.components.component import Component
from reflex.vars.base import Var
from reflex_components_core.el import Div

from ..utils.twmerge import cn


class ClassNames:
    """Class names for skeleton component."""

    ROOT = "animate-pulse bg-secondary"


def skeleton_component(
    class_name: str | Var[str] = "",
) -> Component:
    """Skeleton component."""
    return Div.create(class_name=cn(ClassNames.ROOT, class_name))


skeleton = skeleton_component
