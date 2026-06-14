import reflex as rx

from components.ui.skeleton import skeleton_component


def skeleton_table():
    """Skeleton table matching shadcn SkeletonTable layout."""

    return rx.el.div(
        *[
            rx.el.div(
                skeleton_component(class_name="h-4 flex-1"),
                skeleton_component(class_name="h-4 w-24"),
                skeleton_component(class_name="h-4 w-20"),
                class_name="flex gap-4",
                key=str(i),
            )
            for i in range(5)
        ],
        class_name="flex w-full max-w-sm flex-col gap-2",
    )
