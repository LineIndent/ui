# Buridan UI Theming

Buridan UI uses an OKLCH-based theme system defined in `assets/globals.css`.

## CSS Variables
The theme is controlled by CSS variables in `:root` and `.dark`.

```css
:root {
    --background: oklch(1 0 0);
    --primary: oklch(0.205 0 0);
    --chart-1: oklch(0.87 0 0);
    /* ... */
}
```

## Modifying Themes
- **Preset Initialization**: Run `buridan init --preset <ID>` to overwrite the theme.
- **Manual Adjustments**: Directly edit `assets/globals.css`.
- **Chart Colors**: Charts consume `--chart-1` through `--chart-5`.

## Best Practices
- **Use semantic names**: Always prefer `bg-background`, `text-primary`, `border-input` over hardcoded hex codes.
- **Dark Mode**: Support dark mode by using the `.dark` class or `rx.color_mode_cond`.
- **OKLCH**: Use OKLCH for perceptually uniform colors.
