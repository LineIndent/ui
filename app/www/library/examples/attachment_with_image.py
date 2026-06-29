import reflex as rx

from components.icons.hugeicon import hi
from components.ui.attachment import attachment

images = [
    {
        "name": "workspace.png",
        "meta": "PNG · 820 KB",
        "src": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80",
        "alt": "Workspace",
    },
    {
        "name": "desk-reference.jpg",
        "meta": "JPG · 1.1 MB",
        "src": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=900&auto=format&fit=crop&q=80",
        "alt": "Desk",
    },
    {
        "name": "office-reference.jpg",
        "meta": "JPG · 940 KB",
        "src": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=900&auto=format&fit=crop&q=80",
        "alt": "Office",
    },
]


def attachment_image_demo():
    return rx.el.div(
        attachment.group(
            rx.foreach(
                images,
                lambda image: attachment.root(
                    attachment.trigger(
                        link=True,
                        href=image["src"],
                        target="_blank",
                        rel="noreferrer",
                        aria_label=f"Open {image['name']}",
                    ),
                    attachment.media(
                        rx.el.img(src=image["src"], alt=image["alt"]),
                        variant="image",
                    ),
                    attachment.content(
                        attachment.title(image["name"]),
                        attachment.description(image["meta"]),
                    ),
                    attachment.actions(
                        attachment.action(
                            hi("Cancel01Icon"),
                            aria_label=f"Remove {image['name']}",
                        )
                    ),
                    orientation="vertical",
                ),
            ),
            class_name="w-full",
        ),
        class_name="mx-auto w-full max-w-sm py-12",
    )
