

# Events

Events are how Reflex responds to user interactions like clicking a button, submitting a form, or hovering over an element. In Reflex, events trigger **Event Handlers** in your State class.

# Event Handlers

An event handler is a method in your state class that logic.

```python
class CounterState(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1
```

You hook this up in your UI using component props:

```python
rx.el.button("Add", on_click=CounterState.increment)
```

# Async Handlers & Yielding

If an event handler performs a long-running task (like an API call), it should be `async`. Reflex also allows you to **yield** actions to update the UI progressively.

```python
class SearchState(rx.State):
    results: list[str] = []
    loading: bool = False

    async def run_search(self, query: str):
        self.loading = True
        yield  # Update UI to show loading spinner

        # Simulate API call
        await asyncio.sleep(2)
        self.results = ["Result 1", "Result 2"]
        
        self.loading = False
```

# Chaining Events

You can trigger multiple events from a single interaction by passing a list to the event prop.

```python
rx.el.button(
    "Save", 
    on_click=[
        State.save_data,
        rx.toast("Data Saved!"),
        rx.redirect("/dashboard")
    ]
)
```

# Common Event Triggers

- `on_click`: Triggered on mouse click.
- `on_change`: Triggered when an input value changes.
- `on_submit`: Triggered when a form is submitted.
- `on_mount`: Triggered when a component is first rendered on the page.
- `on_blur`: Triggered when a component loses focus.

# Special Actions

Reflex provides built-in "Special Actions" that can be triggered from handlers:

- `rx.redirect(url)`: Navigate to a new page.
- `rx.set_clipboard(text)`: Copy text to the user's clipboard.
- `rx.toast(message)`: Show a brief notification.
- `rx.call_script(js)`: Execute custom JavaScript in the browser.
