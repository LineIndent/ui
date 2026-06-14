from pathlib import Path

import reflex as rx

from app.templates.layout import layout_decorator
from components.icons.hugeicon import hi
from components.ui.button import button

BASE_PATH = Path("components/ui")


def get_component_links():
    links = []

    for file in sorted(BASE_PATH.glob("*.py")):
        if file.name == "__init__.py":
            continue

        name = file.stem.replace("_", " ").title()
        slug = file.stem.replace("_", "-")

        links.append(
            rx.el.a(
                name,
                href=f"/docs/components/{slug}",
                class_name="py-1 hover:underline text-center",
            )
        )

    return links


@layout_decorator(
    title="Components for Every App",
    description="A collection of ready-to-use UI components for building modern applications. From simple controls to complex interface patterns, copy and paste into your apps.",
    ctas=[
        rx.el.a(
            button(
                "Build Your Own", hi("ArrowRight02Icon", class_name="size-4"), size="sm"
            ),
            href="/create",
        )
    ],
)
def components_page():
    return rx.el.div(
        rx.el.div(
            *get_component_links(),
            class_name=" ".join(
                [
                    "grid",
                    "grid-cols-1",
                    "sm:grid-cols-2",
                    "md:grid-cols-3",
                    "lg:grid-cols-4",
                    "gap-6",
                    "max-w-6xl",
                    "mx-auto",
                ]
            ),
        ),
        class_name=" ".join(
            [
                "max-w-[96rem]",
                "mx-auto",
                "px-7",
                "py-6",
            ]
        ),
    )
