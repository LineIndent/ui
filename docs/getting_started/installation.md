---
title: "Installation"
description: "Steps to install and start using Buridan in your project."
order: 2
---

# Installation

How to install dependencies and structure your app.

>Recommended for new projects: Use [buridan/create](/create) to build your preset visually and generate the right setup command for your framework.

# Use buridan/create

Build your preset visually, preview your choices, and generate a framework-specific setup command. You can use your final theme system locally or pipelined to Reflex Build. Start with the default preset [Neutral](/create?preset=b0)

## Prerequisites

Python 3.10+ (required by Reflex)

# Local Environment 

It's recommended to use the [uv](https://docs.astral.sh/uv/) package manager when working with Reflex apps. 

The following page provides a step-by-step [installation](https://reflex.dev/docs/getting-started/installation/) guide for Reflex apps. 

After setting up your Reflex environment, you can install the `buridan` package by adding it to your `pyproject.toml` file.

```toml
dependencies = ["buridan-create=={current version}"]
```

After adding the package with the latest vesion, you can run the following command to install it. 


```uv
uv sync
```

Installing it will give access to the full [CLI](/docs/getting-started/cli) tool.
