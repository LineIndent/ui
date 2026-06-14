from components.icons.hugeicon import hi
from components.ui.toggle import toggle


def toggle_pressed_state():
    return toggle(hi("TextItalicIcon", class_name="size-4"), default_pressed=True)
