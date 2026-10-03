import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from components.ui.context_menu import ClassNames, ContextMenuShortcut  # noqa: E402


def test_context_menu_shortcut_uses_default_classes() -> None:
    shortcut = ContextMenuShortcut.create("Ctrl+C")

    assert ClassNames.SHORTCUT in str(shortcut.class_name)


def test_context_menu_shortcut_merges_custom_class_name() -> None:
    shortcut = ContextMenuShortcut.create("Ctrl+C", class_name="custom-shortcut")

    assert ClassNames.SHORTCUT in str(shortcut.class_name)
    assert "custom-shortcut" in str(shortcut.class_name)


def test_context_menu_shortcut_unstyled_omits_default_classes() -> None:
    shortcut = ContextMenuShortcut.create("Ctrl+C", unstyled=True)

    assert str(shortcut.class_name) == ""


def test_context_menu_shortcut_unstyled_keeps_custom_class_name() -> None:
    shortcut = ContextMenuShortcut.create(
        "Ctrl+C", class_name="custom-shortcut", unstyled=True
    )

    assert str(shortcut.class_name) == "custom-shortcut"
