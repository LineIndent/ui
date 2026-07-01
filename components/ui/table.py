"""Custom Table component."""

from typing import Any, Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.vars.base import Var
from reflex_components_core.core.foreach import foreach
from reflex_components_core.el import (
    Caption,
    Div,
    Table,
    Tbody,
    Td,
    Tfoot,
    Th,
    Thead,
    Tr,
)

from ..utils.twmerge import cn
from .component import CoreComponent

LiteralAlign = Literal["left", "center", "right"]


class ClassNames:
    """Class names for table components."""

    ROOT = "w-full overflow-auto rounded-lg border border-input bg-card shadow-sm"
    TABLE = "w-full caption-bottom text-sm border-collapse"
    HEADER = "[&_tr]:border-b bg-secondary/50 backdrop-blur-sm sticky top-0"
    BODY = "[&_tr:last-child]:border-0"
    FOOTER = "border-t bg-muted/50 font-medium [&>tr]:last:border-b-0"
    ROW = "border-b transition-colors data-[state=selected]:bg-muted hover:bg-muted/50"
    HEAD = "h-10 px-4 text-left align-middle font-semibold text-muted-foreground [&:has([role=checkbox])]:pr-0 whitespace-nowrap"
    CELL = "p-4 align-middle [&:has([role=checkbox])]:pr-0"
    CAPTION = "mt-4 text-sm text-muted-foreground"


class TableRoot(Div, CoreComponent):
    """The root of the table, providing the scrolling container."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the table root component."""
        cls.set_class_name(ClassNames.ROOT, props)
        # Separate the table itself from the root container
        table_props = {
            "class_name": ClassNames.TABLE,
        }
        return super().create(Table.create(*children, **table_props), **props)


class TableHeader(Thead, CoreComponent):
    """The header of the table."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class TableBody(Tbody, CoreComponent):
    """The body of the table."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        cls.set_class_name(ClassNames.BODY, props)
        return super().create(*children, **props)


class TableFooter(Tfoot, CoreComponent):
    """The footer of the table."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        cls.set_class_name(ClassNames.FOOTER, props)
        return super().create(*children, **props)


class TableRow(Tr, CoreComponent):
    """A row in the table."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        cls.set_class_name(ClassNames.ROW, props)
        return super().create(*children, **props)


class TableHead(Th, CoreComponent):
    """A cell in the table header."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        cls.set_class_name(ClassNames.HEAD, props)
        return super().create(*children, **props)


class TableCell(Td, CoreComponent):
    """A cell in the table body."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        cls.set_class_name(ClassNames.CELL, props)
        return super().create(*children, **props)


class TableCaption(Caption, CoreComponent):
    """A caption for the table."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        cls.set_class_name(ClassNames.CAPTION, props)
        return super().create(*children, **props)


class HighLevelTable(TableRoot):
    """High level wrapper for the Table component."""

    @classmethod
    def create(
        cls,
        data: Var[list[dict[str, Any]]] | list[dict[str, Any]],
        columns: list[dict[str, Any]] | None = None,
        striped: bool = False,
        **props,
    ) -> Component:
        """Create a high level table component.

        Args:
            data: The list of dictionaries containing the table data.
            columns: Optional list of column definitions.
                Each dict can have 'header', 'accessor', 'align', 'class_name'.
            striped: Whether to apply zebra striping.
            **props: Additional properties to apply to the table root.

        Returns:
            The table component with all necessary subcomponents.
        """
        if columns is None and isinstance(data, list) and len(data) > 0:
            # Auto-generate columns from the first row keys
            columns = [
                {"header": k.replace("_", " ").title(), "accessor": k}
                for k in data[0].keys()
            ]
        elif columns is None:
            columns = []

        # Header
        header_row = TableRow.create(
            *[
                TableHead.create(
                    col.get("header", ""),
                    class_name=cn(
                        "text-right" if col.get("align") == "right" else "",
                        "text-center" if col.get("align") == "center" else "",
                        col.get("class_name", ""),
                    ),
                )
                for col in columns
            ]
        )

        # Body
        if isinstance(data, Var):
            # Dynamic data via foreach
            body_content = foreach(
                data,
                lambda row: TableRow.create(
                    *[
                        TableCell.create(
                            row[col["accessor"]],
                            class_name=cn(
                                "text-right" if col.get("align") == "right" else "",
                                "text-center" if col.get("align") == "center" else "",
                                col.get("class_name", ""),
                            ),
                        )
                        for col in columns
                    ],
                    class_name=cn(
                        "even:bg-secondary/30" if striped else "",
                    ),
                ),
            )
        else:
            # Static data
            body_content = [
                TableRow.create(
                    *[
                        TableCell.create(
                            row.get(col["accessor"], ""),
                            class_name=cn(
                                "text-right" if col.get("align") == "right" else "",
                                "text-center" if col.get("align") == "center" else "",
                                col.get("class_name", ""),
                            ),
                        )
                        for col in columns
                    ],
                    class_name=cn(
                        "even:bg-secondary/30" if striped and i % 2 == 1 else "",
                    ),
                )
                for i, row in enumerate(data)
            ]

        return super().create(
            TableHeader.create(header_row),
            TableBody.create(
                body_content if not isinstance(body_content, Var) else body_content
            ),
            **props,
        )


class TableNamespace(ComponentNamespace):
    """Namespace for Table components."""

    root = staticmethod(TableRoot.create)
    header = staticmethod(TableHeader.create)
    body = staticmethod(TableBody.create)
    footer = staticmethod(TableFooter.create)
    row = staticmethod(TableRow.create)
    head = staticmethod(TableHead.create)
    cell = staticmethod(TableCell.create)
    caption = staticmethod(TableCaption.create)
    __call__ = staticmethod(HighLevelTable.create)


table = TableNamespace()
