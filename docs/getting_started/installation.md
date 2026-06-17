---
title: "Installation"
description: "Steps to install and start using Buridan in your project."
order: 2
---

# Installation
How to install dependencies and structure your app.

>Recommended for new projects: Use [buridan/create](/create) to build your preset visually and generate the right setup command for your framework.

# Use buridan/crate

# Check your Python version

To use Buridan UI components, you need to have **Python version 3.11 or above** installed on your system.

```bash 
python3 --version
```

# Install Reflex (if you haven't already)

Buridan UI components are built with Reflex. If you don't have Reflex installed, use the following command:

```bash
pip install reflex
```

Make sure the latest version of Reflex is installed:

```bash
reflex --version
```

# Install the Buridan UI CLI

The Buridan UI CLI allows you to easily add components to your Reflex project.

```bash
pip install buridan-ui
```

# Create or navigate to your Reflex Web Application

The `buridan` CLI commands must be run from the root directory of your Reflex project (where your `rxconfig.py` file is located).

If you need to create a new Reflex app:

```bash
reflex init my_app_name
cd my_app_name
```

# Using the Buridan UI CLI

For detailed instructions on how to use the Buridan UI CLI to add components, wrapped React components, and themes to your project, please refer to the [CLI Documentation](/docs/getting-started/cli).
