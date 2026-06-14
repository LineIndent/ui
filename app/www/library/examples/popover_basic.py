from components.ui.button import button
from components.ui.popover import popover


def popover_basic():
    return popover.root(
        popover.trigger(render_=button("Open Popover", variant="outline")),
        popover.portal(
            popover.backdrop(),
            popover.positioner(
                popover.popup(
                    popover.header(
                        popover.title("Dimensions"),
                        popover.description("Set the dimensions for the layer."),
                    ),
                ),
            ),
        ),
    )
