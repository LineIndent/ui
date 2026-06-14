from components.ui.button import button
from components.ui.tooltip import tooltip


def tooltip_general():
    return tooltip.provider(
        tooltip.root(
            tooltip.trigger(
                render_=button("Hover", variant="outline", size="sm"),
            ),
            tooltip.portal(
                tooltip.positioner(
                    tooltip.popup(tooltip.arrow(), "Add to library"),
                ),
            ),
        ),
        delay=0,
    )
