---
title: "Changelog"
description: "Latest updates and announcements."
order: 5
---

# Changelog

Latest updates and announcements.


# June 2026 - buridan/create

The key feature introduced is the `buridan/create` feature. Based on the popular shadcn/ui, this feature allows users to generate their own CSS tokens and apply it to their Reflex projects. Local development or via [Reflex Build](https://build.reflex.dev/), both are covered. 

No more purple/green dashboards and components with inconsistent spacing and obscure alignments, with /create users have full control of their theme system that provides clean, minimal, and consistent styling that can be applied to any Reflex app. 

[buridan/create](/create) lets users generate unique presets that can be saved and shared. You can customize everything from the ground up and that includes fonts, color schemes, and more.

> Want to build your theme visually? Use [buridan/create](/create) to preview colors, radius, and fonts, then generate a preset for your project.


# May 2026 - buridan v0.9.0

The buridan library went through some major site changes in `v0.9.0`. As Reflex gets closer to `v1.0`, the buridan UI library is getting closer to establishing a solid API for its components as well as a strong [theme system](/resources/theming). 

Because this library is heavily influenced by the popular React library [shadcn/ui](https://ui.shadcn.com/), the first major change was getting the site to look and feel like shadcn. This meant changing the entire way core site components were built, namely the sidebar, navbar, and the main content area. 

Next, markdown content had to be revised. Previously, there were mismatches between components and their dependencies as well as the actual code output. All this changed as a centralized registry system was introduced. Now each component correctly outputs its dependencies and source code. 

Finally, a command line interface was needed to make everything accessible to end users. So the buridan [CLI](/getting-started/cli) was created to handle two main things:

- Distribute the components and their dependencies in a systematic way.
- Apply CSS theme tokens to a Reflex app to enure good practice theme usage across projects. 

The CLI package is available on PyPI and can be added to any Reflex project.

```uv
uv add buridan-create
```

In conjunction with the CLI, as the site documentation began to grow, local development was an area of concern, mainly because running or hot-reloading the entire site after each change would take a few seconds, even more as more documentation pages were being added. 

To solve this another CLI was created called `dev.py`. This interactive CLI lets users choose which and how many pages to load onto the local server, cutting the hot-reload times by a significant amount. 

To learn more about how to use `dev,py`, visit its documentation [here](/getting-started/dev).
