

# Theming
Using CSS variables and theme tokens.

> Want to build your theme visually? Use [buridan/create](/create) to preview colors, radius, and fonts, then generate a preset for your project.

We use and recommend CSS variables for theming. This approach provides semantic design tokens such as `background`, `foreground`, and `primary`, which components rely on by default. You can customize the appearance of your application by overriding these tokens in your CSS, without needing to modify component-level classes.

```reflex
rx.el.div(class_name="bg-background text-foreground")
```

# rxconfig.py

To use CSS variables for theming, make the following changes to your `rxconfig.py` file found at the root of your Reflex app. 

Import the tailwind plugin `TailwindConfig`, add it to the `plugins=[...]` list, define (or remove if unnecessary) `darkMode` or specific `plugins`, then finally set the `theme` and extend the colors based on the CSS tokens in your `globals.css` file in your assets folder.

```rxconfig.py
from reflex.plugins.shared_tailwind import TailwindConfig

config = rx.Config(
    plugins=[
        rx.plugins.TailwindV4Plugin(
            TailwindConfig(
                darkMode="class",
                plugins=[
                    "@tailwindcss/typography",
                    "tailwind-scrollbar",
                    "tailwindcss-animate",
                ],
                theme={
                    "extend": {
                        "colors": {
                            "background": "var(--background)",
                            "foreground": "var(--foreground)",
                        },
                    }
                },
            )
        ),
    ]
)
```

Further extensions are possible, such as `fontFamily`, `borderRadius`, and `boxShadow` by further extending the `theme` dictionary as such, making sure each `var(...)` token is defined in a CSS file.

```rxconfig.py
theme={
    "extend": {
        "colors": {...},
        "fontFamily": {
            "theme": "var(--font-family)",
        },
        "borderRadius": {
            "radius": "var(--radius)",
        },
        "boxShadow": {
            "default": "var(--shadow)",
        },
    }
},
```

Make sure to pull your CSS files where your tokens are defined in your `rx.App` instance.

```rx.App
app = rx.App(stylesheets=["globals.css"])
```

Tailwind maps these tokens into utilities like `bg-background`, `text-foreground`, `border-border`, and `rounded-radius`. Dark mode works by overriding the same tokens inside a `.dark` selector.


# Theme Tokens

These tokens live in your CSS file under `:root` and `.dark`.

| Token                                            | What it controls                                       | Used by                                                                      |
| ------------------------------------------------ | ------------------------------------------------------ | ---------------------------------------------------------------------------- |
| `background` / `foreground`                      | The default app background and text color.             | The page shell, page sections, and default text.                             |
| `card` / `card-foreground`                       | Elevated surfaces and the content inside them.         | `Card`, dashboard panels, settings panels.                                   |
| `popover` / `popover-foreground`                 | Floating surfaces and the content inside them.         | `Popover`, `DropdownMenu`, `ContextMenu`, and other overlays.                |
| `primary` / `primary-foreground`                 | High-emphasis actions and brand surfaces.              | Default `Button`, selected states, badges, and active accents.               |
| `secondary` / `secondary-foreground`             | Lower-emphasis filled actions and supporting surfaces. | Secondary buttons, secondary badges, and supporting UI.                      |
| `muted` / `muted-foreground`                     | Subtle surfaces and lower-emphasis content.            | Descriptions, placeholders, empty states, helper text, and subdued surfaces. |
| `accent` / `accent-foreground`                   | Interactive hover, focus, and active surfaces.         | Ghost buttons, menu highlight states, hovered rows, and selected items.      |
| `destructive`                                    | Destructive actions and error emphasis.                | Destructive buttons, invalid states, and destructive menu items.             |
| `border`                                         | Default borders and separators.                        | Cards, menus, tables, separators, and layout dividers.                       |
| `input`                                          | Form control borders and input surface treatment.      | `Input`, `Textarea`, `Select`, and outline-style controls.                   |
| `ring`                                           | Focus rings and outlines.                              | Buttons, inputs, checkboxes, menus, and other focusable controls.            |
| `chart-1` ... `chart-5`                          | The default chart palette.                             | Charts and chart-driven dashboard blocks.                                    |
| `sidebar` / `sidebar-foreground`                 | The base sidebar surface and default sidebar text.     | The `Sidebar` container and its default content.                             |
| `sidebar-primary` / `sidebar-primary-foreground` | High-emphasis actions inside the sidebar.              | Active items, icon tiles, badges, and sidebar CTAs.                          |
| `sidebar-accent` / `sidebar-accent-foreground`   | Hover and selected states inside the sidebar.          | Sidebar menu hover states, open items, and interactive rows.                 |
| `sidebar-border`                                 | Sidebar-specific borders and separators.               | Sidebar headers, groups, and internal dividers.                              |
| `sidebar-ring`                                   | Sidebar-specific focus rings.                          | Focused controls inside the sidebar.                                         |
| `radius`                                         | The base corner radius scale.                          | Cards, inputs, buttons, popovers, and the derived `radius-*` tokens.         |


# Adding New Tokens

To add a new token, define it under `:root` and `.dark`, then expose it to Tailwind by appending `rxconfig.py`.

```assets/globals.css
:root {
  --warning: oklch(0.84 0.16 84);
  --warning-foreground: oklch(0.28 0.07 46);
}

.dark {
  --warning: oklch(0.41 0.11 46);
  --warning-foreground: oklch(0.99 0.02 95);
}
```

You can now use `bg-warning` and `text-warning-foreground` in your components.

```reflex
rx.el.div(class_name="bg-warning text-warning-foreground")
```

# Default Theme CSS

The following is the full default `neutral` theme scaffold. Copy it into your global CSS file and adjust the tokens as needed.
This scaffold also corresponds to preset `b0` in [buridan/create](/create?preset=b0).

```assets/globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
    --background: oklch(1 0 0);
    --foreground: oklch(0.145 0 0);
    --card: oklch(1 0 0);
    --card-foreground: oklch(0.145 0 0);
    --popover: oklch(1 0 0);
    --popover-foreground: oklch(0.145 0 0);
    --primary: oklch(0.205 0 0);
    --primary-foreground: oklch(0.985 0 0);
    --secondary: oklch(0.97 0 0);
    --secondary-foreground: oklch(0.205 0 0);
    --muted: oklch(0.97 0 0);
    --muted-foreground: oklch(0.556 0 0);
    --accent: oklch(0.97 0 0);
    --accent-foreground: oklch(0.205 0 0);
    --destructive: oklch(0.577 0.245 27.325);
    --border: oklch(0.922 0 0);
    --input: oklch(0.922 0 0);
    --ring: oklch(0.708 0 0);
    --chart-1: oklch(0.87 0 0);
    --chart-2: oklch(0.556 0 0);
    --chart-3: oklch(0.439 0 0);
    --chart-4: oklch(0.371 0 0);
    --chart-5: oklch(0.269 0 0);
    --sidebar: oklch(0.985 0 0);
    --sidebar-foreground: oklch(0.145 0 0);
    --sidebar-primary: oklch(0.205 0 0);
    --sidebar-primary-foreground: oklch(0.985 0 0);
    --sidebar-accent: oklch(0.97 0 0);
    --sidebar-accent-foreground: oklch(0.205 0 0);
    --sidebar-border: oklch(0.922 0 0);
    --sidebar-ring: oklch(0.708 0 0);
    --radius: 0.625rem;
    --shadow: 0 1px 3px rgba(0,0,0,0.08);
    --border-width: 1px;
    --card-padding: 1.25rem;
    --card-gap: 1rem;
}

.dark {
    --background: oklch(0.145 0 0);
    --foreground: oklch(0.985 0 0);
    --card: oklch(0.205 0 0);
    --card-foreground: oklch(0.985 0 0);
    --popover: oklch(0.205 0 0);
    --popover-foreground: oklch(0.985 0 0);
    --primary: oklch(0.922 0 0);
    --primary-foreground: oklch(0.205 0 0);
    --secondary: oklch(0.269 0 0);
    --secondary-foreground: oklch(0.985 0 0);
    --muted: oklch(0.269 0 0);
    --muted-foreground: oklch(0.708 0 0);
    --accent: oklch(0.269 0 0);
    --accent-foreground: oklch(0.985 0 0);
    --destructive: oklch(0.704 0.191 22.216);
    --border: oklch(1 0 0 / 10%);
    --input: oklch(1 0 0 / 15%);
    --ring: oklch(0.556 0 0);
    --chart-1: oklch(0.87 0 0);
    --chart-2: oklch(0.556 0 0);
    --chart-3: oklch(0.439 0 0);
    --chart-4: oklch(0.371 0 0);
    --chart-5: oklch(0.269 0 0);
    --sidebar: oklch(0.205 0 0);
    --sidebar-foreground: oklch(0.985 0 0);
    --sidebar-primary: oklch(0.488 0.243 264.376);
    --sidebar-primary-foreground: oklch(0.985 0 0);
    --sidebar-accent: oklch(0.269 0 0);
    --sidebar-accent-foreground: oklch(0.985 0 0);
    --sidebar-border: oklch(1 0 0 / 10%);
    --sidebar-ring: oklch(0.556 0 0);
    --radius: 0.625rem;
    --shadow: 0 1px 3px rgba(0,0,0,0.08);
    --border-width: 1px;
    --card-padding: 1.25rem;
    --card-gap: 1rem;
}
```
