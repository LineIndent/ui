---
title: "ClientStateVar"
description: "Use client-side state variables to manage local interactivity."
order: 6
---

# Introduction
ClientStateVar is Reflex's solution for frontend-only state management, modeled after React's familiar useState hook. It enables responsive UI updates directly in the browser without requiring a round trip to the backend server. This makes ClientStateVar perfect for interactive elements like active tabs, toggles, form inputs, modals, and any UI state that doesn't need server persistence.

# What is ClientStateVar?
Unlike regular Reflex **State** variables which are backend-driven and persistent across sessions, ClientStateVar exists only in the browser's memory and updates instantly. This separation enables:

- **Instant UI Updates**: No network latency for immediate visual feedback
- **Reduced Server Load**: Client-side state doesn't hit your backend
- **Better UX**: Snappy interactions that feel native to modern web apps
- **Stateless Logic**: Clean separation between client UI state and server business logic

ClientStateVar integrates seamlessly into Reflex components and can optionally be made globally accessible across your entire application.

# Creating Your First ClientStateVar
To create a ClientStateVar, import it from `reflex.experimental` and use the `create` method:

```python
import reflex as rx
from reflex.experimental import ClientStateVar

# Create a simple counter
counter = ClientStateVar.create("counter", 0)

# Create a tab selector with default first tab
active_tab = ClientStateVar.create("active_tab", 0)

# Create a toggle state
is_open = ClientStateVar.create("modal_open", False)
```

- `var_name`: Unique identifier for the variable (optional, auto-generated if not provided)
- `default`: Initial value for the state variable
- `global_ref`: Whether the state should be accessible across components (default: True)

# API Reference & Methods
ClientStateVar provides several methods for different use cases:

<div  style="overflow-x: scroll;">


| Method | Description | Usage Context |
|--------|-------------|---------------|
| `.value` | Access current value in component render | Frontend rendering only |
| `.set_value(v)` | Set value with specific data | Frontend event handlers |
| `.set` | Returns event handler that updates value | Frontend event triggers |
| `.retrieve(callback)` | Pull client value into backend handler | Backend event handlers |
| `.push(value)` | Push value from backend to client | Backend event handlers |

</div>

- `.value`, `.set_value()`, and `.set` work only in frontend contexts
- `.retrieve()` and `.push()` require `global_ref=True` and work in backend contexts
- Use `.retrieve()` to get client state values in backend event handlers
- Use `.push()` to update client state from backend event handlers

# Simple Example: Tab Navigation
Here's a basic implementation showing tab switching functionality:


--CODE(["tab_navigation_example", ""])--

- `ActiveTab.value` renders the current selected tab index
- `ActiveTab.set_value(i)` creates an event handler that updates the active tab
- `rx.cond()` conditionally applies styles based on the current state


# Complex Example: Session Management
Here's an advanced example showing editable session names with backend integration:

```python
from reflex.experimental import ClientStateVar
import reflex as rx

# Client state for edit mode
EditSessionName = ClientStateVar.create("EditSessionName", False)

class SessionState(rx.State):
    sessions: list[Session] = []
    _id: str

    def change_name(self, title: str):
        self.sessions = [
            (
                session
                if session.session_id != self._id
                else session.copy(update={"name": name})
            )
            for session in self.sessions
        ]

    def change_session_name(self, session_id: str):
        self._id = session_id
        # Use retrieve to get the edited name from the client
        yield rx.call_script(
            f'''
            function getNewName() {{
                var name = document
                    .getElementById("{session_id}")
                    .innerText;
                return name;
            }}
            getNewName();
            ''',
            SessionState.change_name,
        )

def create_session(session: Session, index: int):
    return rx.div(
        rx.label(
            session.name,
            id=session.session_id,
            class_name="text-sm font-medium w-[90px] truncate cursor-pointer",
            content_editable=EditSessionName.value,
            spell_check=False,
            # Double-click to enable editing
            on_double_click=EditSessionName.set_value(True),
            # Exit edit mode and save changes
            on_blur=[
                EditSessionName.set_value(False),
                SessionState.change_session_name(session.session_id),
            ],
        ),
        rx.label(
            f"Total Blocks {len(session.blocks)}",
            class_name="text-sm font-light italic",
        ),
        class_name="flex flex-row justify-between items-center p-4 border rounded-lg",
    )
```

- **Client-Server Integration**: EditSessionName controls UI state while SessionState handles data persistence
- **Conditional Rendering**: `content_editable=EditSessionName.value` toggles edit mode
- **Event Chaining**: Multiple actions triggered on `on_blur`
- **Backend Communication**: Using custom JavaScript to retrieve edited content

# Best Practices & Patterns

## When to Use ClientStateVar
- **UI State**: Active tabs, modal visibility, form input states
- **Temporary Data**: Shopping cart items, form drafts, client-side filters
- **Interactive Elements**: Hover states, dropdown selections, toggle switches
- **Performance Critical**: Frequent updates that don't need server persistence

## When NOT to Use ClientStateVar
- **Persistent Data**: User settings, saved preferences, database records
- **Security Sensitive**: Authentication tokens, user permissions
- **Cross-Session Data**: Data that needs to survive page refreshes
- **Server Logic**: Business rules, validation, data processing

## Global vs Local State
```python
# Global state - accessible across components
global_state = ClientStateVar.create("global_counter", 0, global_ref=True)

# Local state - only accessible in current component tree
local_state = ClientStateVar.create("local_toggle", False, global_ref=False)
```

## Error Handling
Always wrap backend interactions with proper error handling:

```python
def safe_retrieve_handler(self):
    try:
        yield my_client_state.retrieve(self.process_client_value)
    except Exception as e:
        yield rx.toast(f"Error retrieving client state: {e}")
```

# Advanced Usage: Backend Integration

## Retrieving Client State in Backend
Use `.retrieve()` to pull client-side values into backend event handlers:

```python
class MyState(rx.State):
    def process_form(self):
        # Get current client state value
        yield form_data.retrieve(self.save_form_data)

    def save_form_data(self, client_value):
        # Process the retrieved value
        print(f"Received from client: {client_value}")
        # Save to database, validate, etc.
```

## Pushing Updates from Backend
Use `.push()` to update client state from backend:

```python
class MyState(rx.State):
    def reset_form(self):
        # Clear client-side form state
        yield form_data.push({})
        yield rx.toast("Form cleared!")

    def load_saved_data(self):
        # Load data and push to client
        saved_data = self.load_from_database()
        yield form_data.push(saved_data)
```

# Common Patterns

## Toggle Pattern
--CODE(["toggle_pattern_example", ""])--

## Form State Pattern
--CODE(["form_state_pattern_example", ""])--

## Conditional Rendering Pattern
--CODE(["conditional_rendering_pattern_example", ""])--

# Final Thoughts
ClientStateVar bridges the gap between Reflex's backend-focused architecture and modern frontend interactivity needs. By understanding when and how to use client-side state, you can build responsive, performant applications that feel native to users while maintaining clean separation between UI logic and business logic.

- Use ClientStateVar for ephemeral UI state that doesn't need server persistence
- Leverage `.retrieve()` and `.push()` for backend integration when needed
- Consider performance implications and choose between global and local state appropriately
- Follow React patterns and conventions for familiar developer experience
