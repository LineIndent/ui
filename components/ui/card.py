from reflex.components.component import ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.el import Div

from components.ui.component import CoreComponent


class ClassNames:
    ROOT = (
        "group/card flex flex-col gap-(--card-spacing) overflow-hidden rounded-xl bg-card "
        "py-(--card-spacing) text-sm text-card-foreground ring-1 ring-foreground/10 "
        "[--card-spacing:--spacing(4)] has-data-[slot=card-footer]:pb-0 "
        "has-[>img:first-child]:pt-0 data-[size=sm]:[--card-spacing:--spacing(3)] "
        "data-[size=sm]:has-data-[slot=card-footer]:pb-0 "
        "*:[img:first-child]:rounded-t-xl *:[img:last-child]:rounded-b-xl"
    )
    HEADER = (
        "group/card-header @container/card-header grid auto-rows-min items-start gap-1 "
        "rounded-t-xl px-(--card-spacing) has-data-[slot=card-action]:grid-cols-[1fr_auto] "
        "has-data-[slot=card-description]:grid-rows-[auto_auto] [.border-b]:pb-(--card-spacing)"
    )
    TITLE = "cn-font-heading text-base leading-snug font-medium group-data-[size=sm]/card:text-sm"
    DESCRIPTION = "text-sm text-muted-foreground"
    ACTION = "col-start-2 row-span-2 row-start-1 self-start justify-self-end"
    CONTENT = "px-(--card-spacing)"
    FOOTER = "flex items-center rounded-b-xl border-t border-input bg-muted/50 p-(--card-spacing)"


class CardRoot(Div, CoreComponent):
    size: Var[str]

    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card"
        if "size" in props:
            props["data-size"] = props.pop("size")
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CardHeader(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-header"
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class CardTitle(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-title"
        cls.set_class_name(ClassNames.TITLE, props)
        return super().create(*children, **props)


class CardDescription(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-description"
        cls.set_class_name(ClassNames.DESCRIPTION, props)
        return super().create(*children, **props)


class CardAction(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-action"
        cls.set_class_name(ClassNames.ACTION, props)
        return super().create(*children, **props)


class CardContent(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-content"
        cls.set_class_name(ClassNames.CONTENT, props)
        return super().create(*children, **props)


class CardFooter(Div, CoreComponent):
    @classmethod
    def create(cls, *children, **props):
        props["data-slot"] = "card-footer"
        cls.set_class_name(ClassNames.FOOTER, props)
        return super().create(*children, **props)


class Card(ComponentNamespace):
    root = staticmethod(CardRoot.create)
    header = staticmethod(CardHeader.create)
    title = staticmethod(CardTitle.create)
    description = staticmethod(CardDescription.create)
    action = staticmethod(CardAction.create)
    content = staticmethod(CardContent.create)
    footer = staticmethod(CardFooter.create)
    class_names = ClassNames


card = Card()
