import reflex as rx
from reflex.experimental import ClientStateVar
from dataclasses import dataclass  # Added for Session class placeholder


# Placeholder for Session class used in Complex Example
@dataclass
class Session:
    session_id: str
    name: str
    blocks: list  # Assuming blocks is a list, adjust as needed

    def copy(self, update: dict):
        # Simple copy for demonstration
        new_session = Session(self.session_id, self.name, self.blocks)
        if "name" in update:
            new_session.name = update["name"]
        return new_session


# Used in --show_code(tab_navigation_example)--
def tab_navigation_example():
    # Create the client state variable
    ActiveTab = ClientStateVar.create("tab_v1", 0)
    TabList = ["GitHub", "Twitter", "YouTube"]

    return rx.box(
        rx.hstack(
            rx.foreach(
                TabList,
                lambda tab, i: rx.button(
                    rx.text(
                        tab,
                        color=rx.cond(
                            ActiveTab.value == i,
                            rx.color("slate", 12),
                            rx.color("slate", 10),
                        ),
                    ),
                    on_click=ActiveTab.set_value(i),
                    background=rx.cond(
                        ActiveTab.value == i,
                        rx.color("gray", 3),
                        "transparent",
                    ),
                    border_radius=rx.cond(ActiveTab.value == i, "0.375rem", "0.5rem"),
                    padding="0.5rem 0.75rem",
                    cursor="pointer",
                ),
            ),
            style={
                "display": "inline-flex",
                "height": "2.125rem",
                "align_items": "baseline",
                "border_radius": "0.5rem",
                "padding": "0.25rem",
                "border": f"1.25px dashed {rx.color('gray', 4)}",
            },
        )
    )


# Used in --show_code(toggle_pattern_example)--
def toggle_pattern_example():
    is_visible = ClientStateVar.create("visibility", False)

    return rx.fragment(
        # Toggle with current value
        rx.button("Toggle", on_click=is_visible.set_value(~is_visible.value)),
        # Or use a more explicit approach
        rx.button("Show", on_click=is_visible.set_value(True)),
        rx.button("Hide", on_click=is_visible.set_value(False)),
    )


# Used in --show_code(form_state_pattern_example)--
def form_state_pattern_example():
    form_state = ClientStateVar.create("form", {})

    return rx.input(
        value=form_state.value.get("username", ""),
        on_change=lambda v: form_state.set_value({**form_state.value, "username": v}),
    )


# Used in --show_code(conditional_rendering_pattern_example)--
def conditional_rendering_pattern_example():
    show_details = ClientStateVar.create("show_details", False)

    return rx.box(
        rx.button(
            "Toggle Details", on_click=show_details.set_value(~show_details.value)
        ),
        rx.cond(
            show_details.value,
            rx.div("Detailed information here..."),
            rx.div("Click to show details"),
        ),
    )
