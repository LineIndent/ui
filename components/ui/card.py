"""Custom card component."""

from reflex.components.component import Component, ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.el import Div

from components.ui.component import CoreComponent


class ClassNames:
    """Class names for the card component."""

    ROOT = "flex flex-col p-5 gap-4 overflow-hidden text-sm text-card-foreground"
    HEADER = "grid auto-rows-min items-start gap-1"
    TITLE = "text-base leading-snug font-medium"
    DESCRIPTION = "text-sm text-muted-foreground"
    CONTENT = ""
    FOOTER = "flex items-center"


class CardComponent(Div, CoreComponent):
    """Base component for the card component."""


class CardRoot(CardComponent):
    """A card component that displays content in a card format."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card component."""
        props["data-slot"] = "card"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CardHeader(CardComponent):
    """A header component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card header component."""
        props["data-slot"] = "card-header"
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class CardTitle(CardComponent):
    """A title component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card title component."""
        props["data-slot"] = "card-title"
        cls.set_class_name(ClassNames.TITLE, props)
        return super().create(*children, **props)


class CardDescription(CardComponent):
    """A description component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card description component."""
        props["data-slot"] = "card-description"
        cls.set_class_name(ClassNames.DESCRIPTION, props)
        return super().create(*children, **props)


class CardContent(CardComponent):
    """A content component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card content component."""
        props["data-slot"] = "card-content"
        cls.set_class_name(ClassNames.CONTENT, props)
        return super().create(*children, **props)


class CardFooter(CardComponent):
    """A footer component for the card."""

    @classmethod
    def create(cls, *children, **props):
        """Create the card footer component."""
        props["data-slot"] = "card-footer"
        cls.set_class_name(ClassNames.FOOTER, props)
        return super().create(*children, **props)


class HighLevelCard(CardComponent):
    """A high level card component that displays content in a card format."""

    # Card props
    title: Var[str | Component | None]
    description: Var[str | Component | None]
    content: Var[str | Component | None]
    footer: Var[str | Component | None]

    @classmethod
    def create(cls, *children, **props):
        """Create the card component."""
        title = props.pop("title", "")
        description = props.pop("description", "")
        content = props.pop("content", "")
        footer = props.pop("footer", "")

        return CardRoot.create(
            (
                CardHeader.create(
                    CardTitle.create(title) if title is not None else None,
                    (
                        CardDescription.create(description)
                        if description is not None
                        else None
                    ),
                )
                if title or description
                else None
            ),
            CardContent.create(content) if content is not None else None,
            CardFooter.create(footer) if footer is not None else None,
            *children,
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "title",
            "description",
            "content",
            "footer",
        ]


class Card(ComponentNamespace):
    """A card component that displays content in a card format."""

    root = staticmethod(CardRoot.create)
    header = staticmethod(CardHeader.create)
    title = staticmethod(CardTitle.create)
    description = staticmethod(CardDescription.create)
    content = staticmethod(CardContent.create)
    footer = staticmethod(CardFooter.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelCard.create)


card = Card()
