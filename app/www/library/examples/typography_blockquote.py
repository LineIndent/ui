import reflex as rx


def blockquote():
    return rx.el.blockquote(
        """
        "Five hundred times have the red leaves fallen in Mirkwood in my home since then," said Legolas, "and but a little while does that seem to us."
        """,
        class_name="mt-6 border-l-2 pl-6 italic",
    )
