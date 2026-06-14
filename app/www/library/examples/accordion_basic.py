import reflex as rx
from components.ui.accordion import accordion


def accordion_basic():
    return rx.el.div(
        accordion.root(
            accordion.item(
                accordion.header(
                    accordion.trigger("Models"),
                ),
                accordion.panel(
                    rx.el.div(
                        rx.el.p(
                            "- Genesis launched a new era of exploration.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- Explorer uncovered new planets beyond our reach.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- Voyager 1 ventured into interstellar space.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- Apollo landed humans on the Moon.",
                            class_name="mb-2",
                        ),
                        class_name="py-2 text-sm",
                    ),
                ),
                value="section-1",
            ),
            accordion.item(
                accordion.header(
                    accordion.trigger("Spacecraft"),
                ),
                accordion.panel(
                    rx.el.div(
                        rx.el.p(
                            "- Curiosity sent back valuable data from Mars.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- The Hubble Telescope captured distant galaxies.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- James Webb will explore the universe's origins.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- The ISS orbits Earth, conducting critical experiments.",
                            class_name="mb-2",
                        ),
                        class_name="py-2 text-sm",
                    ),
                ),
                value="section-2",
            ),
            accordion.item(
                accordion.header(
                    accordion.trigger("Space Discoveries"),
                ),
                accordion.panel(
                    rx.el.div(
                        rx.el.p(
                            "- Saturn's rings have fascinated scientists for years.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- The Mars Rover is studying the planet's surface.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- NASA's Artemis program aims to return humans to the Moon.",
                            class_name="mb-2",
                        ),
                        rx.el.p(
                            "- Solar missions help us understand space weather.",
                            class_name="mb-2",
                        ),
                        class_name="py-2 text-sm",
                    ),
                ),
                value="section-3",
            ),
            class_name="w-full max-w-md mx-auto",
            open_multiple=False,
            default_value=["section-1"],
        ),
        class_name="h-[45vh] w-full justify-center pt-10 px-8",
    )
