import reflex as rx

from components.ui.scroll_area import scroll_area

works = [
    {
        "artist": "Ornella Binni",
        "art": "https://images.unsplash.com/photo-1465869185982-5a1a7522cbcb?auto=format&fit=crop&w=300&q=80",
    },
    {
        "artist": "Tom Byrom",
        "art": "https://images.unsplash.com/photo-1548516173-3cabfa4607e9?auto=format&fit=crop&w=300&q=80",
    },
    {
        "artist": "Vladimir Malyavko",
        "art": "https://images.unsplash.com/photo-1494337480532-3725c85fd2ab?auto=format&fit=crop&w=300&q=80",
    },
]


def scroll_area_horizontal():
    return scroll_area.root(
        scroll_area.viewport(
            scroll_area.content(
                *[
                    rx.el.figure(
                        rx.el.div(
                            rx.el.image(
                                src=work["art"],
                                alt=f"Photo by {work['artist']}",
                                class_name="aspect-[3/4] h-64 object-cover",
                            ),
                            class_name="overflow-hidden rounded-md",
                        ),
                        rx.el.figcaption(
                            "Photo by ",
                            rx.el.span(
                                work["artist"],
                                class_name="font-semibold text-foreground",
                            ),
                            class_name="pt-2 text-xs text-muted-foreground",
                        ),
                        class_name="shrink-0",
                    )
                    for work in works
                ],
                class_name="flex w-max space-x-4 p-4",
            ),
        ),
        scroll_area.scrollbar(scroll_area.thumb(), orientation="horizontal"),
        scroll_area.corner(),
        class_name="w-96 rounded-radius border border-input",
    )
