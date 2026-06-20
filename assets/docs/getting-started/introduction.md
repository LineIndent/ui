

# Introduction

buridan/ui is a set of composable, themeable components designed for [Reflex](https://reflex.dev/). Extend, override, and ship without fighting the framework. Open source. 

The library is heavily influenced by the popular [shadcn/ui](https://ui.shadcn.com/) library for the React ecosystem. 

Much like `shadcn/ui`, buridan/ui aims to provide a way to build your own component library with full control over your themes, styles, and other UI aspects. 

# Open Source

Everything attributed to buridan/ui is open source. The entire codebase, including this site, can be found on [GitHub](https://github.com/LineIndent/ui). This means you have full control to customize and extend the components to your needs.

- **Full Transparency**: You see exactly how each component is built.
- **Easy Customization**: Modify any part of a component to fit your design and functionality requirements.
- **AI Integration**: Access to the code makes it straightforward for LLMs to read, understand, and even improve your components.


# Composition

Currently, buridan/ui wraps the new and popular [Base UI](https://base-ui.com/react/overview/quick-start) component library. That means shared APIs and similar anatomies between the two. The only difference is buridan/ui is a UI library for the `Reflex` web framework. 

This approach in combination with the open source nature of the library makes it easy for users to adjust, tweak, and refine any part of the component composition. If an API is missing from any of the components, it can easily be integrated into the API by matching it with the API found in `Base UI` documentation. 

# Architecture 

buridan/ui is a three-layered system that does the following. 

- **Component Schema**: File system that outlines components, what they depend on, and their properties.
- **CLI**: A command-line tool to install components across projects.
- **AI Pipeline**: Use your custom schema, theme tokens, and more to easily integrate with Reflex's [AI Builder](https://build.reflex.dev/). 

# Design Consistency

Buridan's components are designed as a unified system, with shared patterns, styling conventions, and behaviors that work together seamlessly.

- **Unified Experience**: Components look and feel like part of the same design system.
- **Predictable Patterns**: Consistent styling and behavior reduce complexity for both users and developers.
- **Customizable**: Extend and adapt components while maintaining a cohesive design language.

# Python-First Development

Buridan is built specifically for the Reflex ecosystem, allowing you to create modern user interfaces using Python alone. Define components, manage state, and build interactive applications without leaving the Python language.

- **Native Python API**: Build UIs using familiar Python syntax and patterns.
- **Reflex Integration**: Designed to work seamlessly with the Reflex framework and its development workflow.
- **Reduced Context Switching**: Stay focused in Python instead of splitting development across multiple languages and frameworks.
- **Productive Development**: Leverage Python's simplicity and extensive ecosystem while building rich, modern web applications.
