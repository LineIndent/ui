---
name: buridan-support
description: Specialized support for Buridan UI. Use when building Reflex apps with Buridan UI components, managing themes, or using the buridan-create CLI.
---

# Buridan UI Support

This skill provides expert guidance for building Reflex applications using the Buridan UI design system.

## Core Workflows

### 1. Project Initialization
When a user wants to start using Buridan UI:
1.  Verify the project is a Reflex project (look for `rxconfig.py`).
2.  Run `buridan init --preset <ID>` to set up the theme and core components.
3.  Ensure `rx.App(stylesheets=["globals.css"])` is set in the main app file.

### 2. Adding Components
When asked to add a specific UI component:
- **Command**: Run `buridan add <name>`.
- **Reference**: See [components.md](references/components.md) for dependencies.
- **Import**: Follow the patterns in [patterns.md](references/patterns.md).

### 3. Theming & Customization
For theme adjustments:
- Reference [theming.md](references/theming.md).
- Edit `assets/globals.css` using OKLCH variables.
- Use `rx.match` or `rx.cond` with `ClientStateVar` for dynamic UI changes.

### 4. Best Practices
- **Layouts**: Always use the `@layout_decorator` for consistency.
- **Icons**: Prefer the `hugeicon` (hi) and `others_icons` packages.
- **State**: Use `ClientStateVar` for client-side interactions to ensure maximum performance.

## Resource Links
- [CLI Reference](references/cli.md)
- [Component Registry](references/components.md)
- [Theming Guide](references/theming.md)
- [Architectural Patterns](references/patterns.md)
