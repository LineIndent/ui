from components.icons.hugeicon import hi
from components.ui.button import button


def button_icon():
    return button(
        hi("Mail01Icon", class_name="size-4"), variant="outline", size="icon-sm"
    )
