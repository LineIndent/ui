import reflex as rx

from components.icons.hugeicon import hi
from components.ui.attachment import attachment

items = [
    {"name": "briefing-notes.pdf", "meta": "PDF · 1.4 MB", "type": "file"},
    {
        "name": "workspace.png",
        "meta": "PNG · 820 KB",
        "src": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80",
        "type": "image",
    },
    {"name": "customers.csv", "meta": "CSV · 18 KB", "type": "file"},
    {"name": "renderer.tsx", "meta": "TSX · 12 KB", "type": "file"},
]


def attachment_group_demo():
    return rx.el.div(
        attachment.group(
            rx.foreach(
                items,
                lambda item: attachment.root(
                    rx.cond(
                        item["type"] == "image",
                        attachment.media(
                            rx.el.img(src=item["src"], alt=item["name"]),
                            variant="image",
                        ),
                        attachment.media(hi("File02Icon")),
                    ),
                    attachment.content(
                        attachment.title(item["name"]),
                        attachment.description(item["meta"]),
                    ),
                    attachment.actions(
                        attachment.action(
                            hi("Cancel01Icon"), aria_label=f"Remove {item['name']}"
                        )
                    ),
                    class_name="w-64",
                ),
            ),
            class_name="full",
        ),
        class_name="mx-auto w-full max-w-sm py-12",
    )
