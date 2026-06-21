

# dev.py

The `dev.py` script is an interactive CLI tool used to control which documentation pages are loaded during local development.

It replaces manual environment variable setup and makes it easier to selectively run parts of the documentation site while developing.


# Requirements

This script uses [questionary](https://github.com/tmbo/questionary) for interactive prompts.

Install it using your project setup:

```uv
uv add questionary
```

You can also add it manually to your `pyproject.toml`:

```pyproject.toml
dependencies = ["questionary"]
```

# Overview

Instead of running the full documentation build every time, `dev.py` lets you:

- Select specific pages
- Select entire sections
- Select pages within specific sections
- Run the app in dev or prod mode

It then automatically configures the correct environment variables and starts the Reflex server.

# Usage

Run the script from your project root to start the interactive flow:

```uv
uv run dev.py
```

# Flow

The CLI follows this flow:

1. Select environment (dev / prod)
2. Select mode (pages / sections / section-pages)
3. Select pages or sections depending on mode
4. Confirm execution
5. Launch Reflex


# Environment

Before selecting what to run, you must choose the environment.

This determines whether the CLI runs the full documentation site or a filtered development subset.

## Dev

Development mode allows you to work on specific parts of the documentation without loading the entire site.

It enables selective loading of pages through the `dev.py` CLI.

Use this mode when:

- Working on specific documentation pages
- Debugging content structure
- Speeding up local development

## Prod

Production mode runs the full documentation site without any filtering.

# Modes

## Pages

Select individual pages from all available documentation. Useful when working on specific content or debugging a single page.

## Sections

Select one or more sections. All pages inside those sections will be loaded automatically. Useful when working on a feature area.

## Section Pages

Select one or more sections first, then choose specific pages inside them. Useful when you want focused work inside a feature area without loading everything.
