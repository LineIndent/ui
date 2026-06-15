

# ClientStateVar Patterns

Common implementation patterns for responsive, performant UI components.

# Toggle Pattern

Use a boolean ClientStateVar to drive UI visibility or style changes instantly.

```python
is_expanded = ClientStateVar.create("is_expanded", False)

def toggle_component():
    return rx.vstack(
        rx.button(
            "Toggle Content", 
            on_click=is_expanded.set_value(not is_expanded.value)
        ),
        rx.cond(
            is_expanded.value,
            rx.text("Hidden content is now visible!"),
            rx.text("Content is hidden.")
        )
    )
```

# Form State Pattern

Manage input draft state or real-time validation locally before pushing a final, validated payload to the backend.

```python
draft_input = ClientStateVar.create("draft_input", "")

def form_component():
    return rx.vstack(
        rx.input(
            value=draft_input.value,
            on_change=draft_input.set_value
        ),
        rx.button(
            "Submit",
            # Send the client-side draft to the backend for processing
            on_click=draft_input.retrieve(BackendState.process_input)
        )
    )
```

# Conditional Rendering (Tab System)

Control UI state flow without triggering backend re-renders, perfect for tabbed navigation or step-based interfaces.

```python
active_tab = ClientStateVar.create("active_tab", "home")

def tab_system():
    return rx.vstack(
        rx.hstack(
            rx.button("Home", on_click=active_tab.set_value("home")),
            rx.button("Profile", on_click=active_tab.set_value("profile")),
        ),
        rx.match(
            active_tab.value,
            ("home", rx.text("Welcome to the home page.")),
            ("profile", rx.text("User profile settings.")),
            rx.text("404 - Unknown Tab")
        )
    )
```

# Session Management (Backend Integration)

This advanced pattern shows how to handle editable UI states on the frontend while syncing changes to the backend.

```python
EditSessionName = ClientStateVar.create("EditSessionName", False)

class SessionState(rx.State):
    def save_name(self, session_id: str, new_name: str):
        # Backend logic to persist the change
        print(f"Session {session_id} renamed to {new_name}")

    def trigger_save(self, session_id: str):
        # Retrieve client-side text content via JS and pass to backend
        return rx.call_script(
            f'document.getElementById("{session_id}").innerText',
            callback=lambda val: self.save_name(session_id, val)
        )

def session_editor(session_id: str, name: str):
    return rx.text(
        name,
        id=session_id,
        content_editable=EditSessionName.value,
        on_double_click=EditSessionName.set_value(True),
        on_blur=[
            EditSessionName.set_value(False),
            SessionState.trigger_save(session_id),
        ],
    )
```

# API Reference

This section describes the available methods for interacting with frontend and backend state.

| Method | Context | Description |
|---------|---------|-------------|
| .value | Frontend Component | Access the current state value for rendering. |
| .set_value(v) | Frontend Event | Update the state value from an event handler. |
| .set | Frontend Event | A property alias for `.set_value()` that returns an event chain. |
| .retrieve(cb) | Backend Handler | Pull the current client-side value into a backend event handler callback. |
| .push(v) | Backend Handler | Send a value from the backend to update the client-side state. |
