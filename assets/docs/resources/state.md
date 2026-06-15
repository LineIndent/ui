

# States

In Reflex, **State** is the single source of truth for your application's data. Unlike React where state is typically client-side, Reflex state lives on the server, allowing you to use Python's full power for business logic while keeping the UI in sync.

# Substates & Organization

As your app grows, putting everything in one `rx.State` class becomes unmanageable and slow. Reflex allows you to split logic into **Substates**.

```python
class ThemeState(rx.State):
    is_dark: bool = False

    def toggle_mode(self):
        self.is_dark = not self.is_dark

class AuthState(rx.State):
    user_id: str | None = None

    @rx.var
    def is_authenticated(self) -> bool:
        return self.user_id is not None
```

# Cross-State Communication

Sometimes one state needs to know about another. Reflex provides two key async methods for this:

## get_state()
Retrieves the entire instance of another state. Use this when you need to call methods or modify multiple variables in the target state.

```python
class CartState(rx.State):
    async def checkout(self):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/login")
        # Proceed with checkout...
```

## get_var_value
A more efficient way to retrieve a single value without loading the entire target state object.

```python
class AnalyticsState(rx.State):
    async def track_view(self):
        user_id = await self.get_var_value(AuthState.user_id)
        # Track view for user_id...
```
