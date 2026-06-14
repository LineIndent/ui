"""Custom Metric component."""

from typing import Literal

import reflex as rx
from reflex.components.component import Component, ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.el import Div

from ..utils.twmerge import cn
from .component import CoreComponent

LiteralTrendDirection = Literal["up", "down", "neutral"]


class ClassNames:
    """Class names for metric components."""

    ROOT = (
        "flex flex-col gap-y-2 p-4 rounded-radius border border-input bg-card shadow-sm"
    )
    LABEL = "text-sm font-medium text-muted-foreground"
    VALUE = "text-3xl font-bold tracking-tight text-foreground"
    TREND_CONTAINER = "flex flex-row items-center gap-x-1.5"
    TREND_BADGE = "flex flex-row items-center gap-x-1 px-1.5 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider"


class MetricRoot(Div, CoreComponent):
    """The root container for a metric."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class HighLevelMetric(MetricRoot):
    """High level wrapper for the Metric component."""

    @classmethod
    def create(
        cls,
        label: Var[str] | str,
        value: Var[str] | str,
        trend: Var[str] | str | None = None,
        trend_direction: Var[LiteralTrendDirection] | LiteralTrendDirection = "neutral",
        **props,
    ) -> Component:
        """Create a high level metric component."""

        trend_color = rx.match(
            trend_direction,
            ("up", "text-emerald-600 bg-emerald-500/10 dark:text-emerald-400"),
            ("down", "text-destructive bg-destructive/10"),
            "text-muted-foreground bg-secondary",
        )

        return MetricRoot.create(
            rx.el.div(
                rx.el.p(label, class_name=ClassNames.LABEL),
                class_name="flex flex-row items-center justify-between w-full",
            ),
            rx.el.div(
                rx.el.p(value, class_name=ClassNames.VALUE),
                rx.cond(
                    trend,
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(trend),
                            class_name=cn(ClassNames.TREND_BADGE, trend_color),
                        ),
                        class_name=ClassNames.TREND_CONTAINER,
                    ),
                ),
                class_name="flex flex-row items-baseline justify-between w-full",
            ),
            **props,
        )


class MetricNamespace(ComponentNamespace):
    """Namespace for Metric components."""

    root = staticmethod(MetricRoot.create)
    __call__ = staticmethod(HighLevelMetric.create)


metric = MetricNamespace()
