---
title: Introduction
description: Buridan UI is a collection of high-end, accessible components for Reflex developers. It’s not a library you install, but a system you adopt and own.
order: 0
---

# Introduction

Buridan UI is a set of beautifully designed, accessible components built specifically for the [Reflex](https://reflex.dev/) framework. 

**This is not just a component library. It is a philosophy for how you build your design system in Python.**

## The Burden of Choice (and restrictive libraries)

In traditional web development, you often have to choose between a rigid component library that’s hard to customize or building everything from scratch. Python developers using Reflex have faced a similar dilemma: use the built-in primitives or fight with complex CSS and JavaScript wrappers.

Buridan UI offers a third path. Inspired by the principles of shadcn/ui but built natively for the Reflex ecosystem, it provides high-end aesthetics without the "black box" of a traditional package.

## The Buridan Principles

### 1. Radical Ownership (Open Code)
When you add a component with Buridan UI, you aren't just importing it; you're owning it. Our CLI injects the raw Python source code directly into your project. This means the top layer of your UI is always open for modification. Want to change how a `Button` handles its loading state? Just edit the file.

### 2. Composition over Abstraction
Every component is built using a common, composable interface. We don't hide the underlying Reflex primitives; we arrange them into predictable, beautiful patterns. This makes the API intuitive for your team and exceptionally clear for LLMs to reason about.

### 3. CLI-First Distribution
We treat your UI as a living part of your codebase. Our CLI handles the complexities of dependency management, theme synchronization, and component scaffolding. It’s a distribution platform that keeps you in the flow of building, not configuring.

### 4. High-End Defaults
We believe that "functional" shouldn't mean "unpolished." Buridan UI comes with a sophisticated theme system—supporting everything from Neutral to Mauve—with carefully chosen spacing, typography, and dark mode support out of the box.

### 5. LLM-Native
In the age of AI, code visibility is a feature. Because Buridan UI provides clean, typed Python source code instead of compiled binaries, LLMs can "read" your entire UI stack. This allows AI tools to suggest accurate refactors, generate new components that match your style, and help you scale faster.

---

## Why "Buridan"?

Named after Buridan's Ass—the paradox of a creature that starves while unable to choose between two identical options—our goal is to eliminate the paradox of choice for developers. We give you the best of both worlds: the speed of a library and the flexibility of custom code.

Ready to start building? Check out the [Installation](/docs/getting-started/installation.md) guide.
