# buridan

A command line interface (CLI) for adding components and themes to your project.

## create

Opens the Buridan UI theme builder in your browser. Use it to customize your design system and generate a unique preset ID.

```bash
buridan create
```

## init

Initialize Buridan UI in your project. This command sets up CSS utilities (shimmer, scroll fade) in `assets/globals.css` and updates `rxconfig.py` with the required Tailwind configuration.

```bash
buridan init
```

## apply

Apply a theme preset to your project. Generates `:root` and `.dark` CSS variable blocks in `assets/globals.css` based on the preset ID from the theme builder.

```bash
buridan apply --preset <ID>
```

Arguments:
- `--preset`: The theme preset ID from the Buridan UI theme builder. Use `b0` for the default theme.

Example:

```bash
buridan apply --preset b0
buridan apply --preset b2D0wqNxT
```

## add

Add components and their dependencies to your project.

```bash
buridan add <name>
```

You can add multiple components at once:

```bash
buridan add button input select
```

Blocks (charts, dashboards, etc.) can be added the same way:

```bash
buridan add line_chart_01
```

Components are placed in `components/`, blocks in `blocks/`. Dependencies are resolved and added automatically.

> **Note:** Components require a theme to render correctly. Run `buridan apply` before using components.

## list

Display all available components and blocks.

```bash
buridan list
```

## Recommended workflow

```bash
buridan create                    # build your theme, copy the preset ID
buridan init                      # set up utilities and Tailwind config
buridan apply --preset <ID>       # apply your theme
buridan add button input select   # add the components you need
```

# Documentation

Visit [https://ui.buridan.dev/components](https://ui.buridan.dev/components) to see all the components.

Visit [https://ui.buridan.dev/docs/getting-started/cli](https://ui.buridan.dev/docs/getting-started/cli) section to get started.


## License

Licensed under the [MIT license](https://github.com/LineIndent/ui/blob/main/LICENSE.md)
