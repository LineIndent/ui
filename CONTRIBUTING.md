# Contributing to Buridan UI

We love contributions! Whether you're fixing a bug, adding a new component, or improving the theme engine, here's how you can help.

## Development Setup

1. Fork and clone the repository.
2. Install dependencies using `uv` (recommended) or `pip install -r requirements.txt`.
3. Run the development server: `reflex run`.

## Adding Components

- New components should be added to `app/base_ui/components/base/`.
- Use `CoreComponent` or `BaseUIComponent` as base classes to ensure theme compatibility.
- Use `oklch` CSS variables for all colors.

## Adding Examples

- Add your example card to `app/examples/components.py`.
- Use the `@masonry_card(label="Category")` decorator.
- Categories include: `General`, `Finance`, `Healthcare`, `Tech`, `Government`.

## Coding Standards

- Follow PEP 8 for Python code.
- Ensure all components are accessible (ARIA roles, keyboard support).
- Use `rx.cond` and `rx.match` for dynamic, client-side logic where possible.

## Pull Requests

- Create a feature branch for your changes.
- Provide a clear description of the problem solved or the feature added.
- Include a screenshot or recording of new UI components.

Thank you for helping make Buridan UI the standard for Reflex applications!
