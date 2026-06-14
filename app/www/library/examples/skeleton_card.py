from components.ui.card import card
from components.ui.skeleton import skeleton_component


def skeleton_card():
    return card.root(
        card.header(
            skeleton_component(class_name="h-4 w-2/3 rounded-md"),
            skeleton_component(class_name="h-4 w-1/2 rounded-md"),
        ),
        card.content(
            skeleton_component(class_name="aspect-video w-full rounded-md"),
        ),
        class_name="w-full max-w-xs border border-input rounded-radius",
    )
