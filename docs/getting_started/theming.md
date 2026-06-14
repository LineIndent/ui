---
title: "Theming"
description: "Customize your app’s appearance using themes and tokens."
order: 3
---

# Introduction

Buridan UI includes built-in support for **chart theming** using CSS variables and the `oklch()` color format — giving you full control over chart palettes in both light and dark modes. Themes are defined at the CSS level and can be easily extended or customized.

This guide explains how to:

- Add the theming CSS to your Reflex project
- Switch between color themes
- Access chart colors via CSS variables in your components

Whether you're building dashboards, reports, or data apps — theming helps you keep things consistent and beautiful across the board.

# Adding the Theme CSS File

To use Buridan's chart themes, you need to include the theme CSS in your project. Here's how to do it:

Create a new file in your Reflex app’s `assets/` folder (if it doesn't exist, create it):

```text
assets/
└── theme.css
```

Paste the following content into **theme.css**:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Default theme */
:root {
    --chart-1: oklch(0.81 0.1 252);
    --chart-2: oklch(0.62 0.19 260);
    --chart-3: oklch(0.55 0.22 263);
    --chart-4: oklch(0.49 0.22 264);
    --chart-5: oklch(0.42 0.18 266);
}

/* Dark theme */
.dark { ... }

/* Theme overrides */
.theme-blue { ... }
.theme-red { ... }
.theme-green { ... }
.theme-amber { ... }
.theme-purple { ... }
```

You can copy the full content from the chart theme [source](https://github.com/buridan-ui/ui/blob/main/assets/css/globals.css).

Import this CSS file in your **rx.App** declaration. Once imported, your app will automatically apply the default :root colors for charts:

```python
import reflex as rx

app = rx.App(stylesheets=["/theme.css"])
```

# Usage Example: Using Chart Colors in Components

After importing the theme, any component that supports inline styles or Tailwind class bindings can access the chart colors via:

```css
var(--chart-1)
var(--chart-2)
```


For example, in a chart that takes in **fill** prop (such as that in area charts or bar charts):

```python
fill="var(--chart-1)"
```

This will set the fill color to the default value and theme (from inside the **.root**). Buridan ships with multiple pre-defined color themes for charts. To switch themes, apply one of the pre-defined theme system crated inside your **theme.css** file. For example, the following will set the **--chart-1** color to the **red theme** if we apply that theme to an outter component:

--CODE(["theme_red_example", "python"])--

The theme system is fully CSS-based, so switching themes won’t trigger any extra rendering — it’s instant, clean, and declarative.

# Customizing or Extending Themes

Want to create your own chart palette? Just define a new theme block in theme.css:

```css
.theme-coral {
    --chart-1: oklch(0.82 0.18 40);
    --chart-2: oklch(0.7 0.19 38);
```

# Summary

Buridan UI’s theming system gives you centralized control over color palettes, built-in support for light and dark modes, and simple switching between blue, red, green, amber, and purple themes. Designed with CSS-native flexibility, it works seamlessly across components, charts, and any custom UI elements. Add the CSS file once, and your entire app stays visually consistent and easy to style.

Happy theming! 🎨
