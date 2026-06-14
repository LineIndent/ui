# Buridan UI CLI Reference

The Buridan UI CLI (`buridan-create`) is the primary tool for managing the design system in a Reflex project.

## Core Commands

### init
Initializes the theme and adds core components.
```bash
buridan init --preset <ID>
```
- Creates `assets/globals.css`.
- Updates `rxconfig.py` with Tailwind configuration.
- Adds essential components by default.

### add
Adds specific components and their dependencies.
```bash
buridan add <component1> [component2 ...]
```
- Automatically resolves dependencies.
- Maintains `components/ui/`, `components/icons/`, and `components/utils/` structure.
- Creates `__init__.py` files automatically.

### list
Lists all available components in the registry.
```bash
buridan list
```

## Agent Guidelines
- **Always prefer the CLI**: When a user asks to "add a button", do NOT copy code manually. Run `buridan add button`.
- **Project Root**: Commands must be run from the directory containing `rxconfig.py`.
- **Environment**: If `uv` is available, prefer `uv run buridan ...`.
