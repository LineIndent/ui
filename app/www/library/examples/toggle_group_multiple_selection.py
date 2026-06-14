from components.icons.hugeicon import hi
from components.ui.toggle import toggle
from components.ui.toggle_group import toggle_group

toggle_style = "flex size-8 items-center justify-center rounded-sm active:bg-secondary text-muted-foreground active:text-foreground"


def toggle_group_multiple_selection():
    return toggle_group(
        toggle(hi("TextAlignLeftIcon"), value="left", class_name=toggle_style),
        toggle(hi("TextAlignCenterIcon"), value="center", class_name=toggle_style),
        toggle(hi("TextAlignRightIcon"), value="right", class_name=toggle_style),
        default_value=["left", "right"],
        multiple=True,
        class_name="flex gap-px rounded-md border border-input bg-background p-0.5",
    )
