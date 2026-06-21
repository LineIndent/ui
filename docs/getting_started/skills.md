---
title: "Skills"
description: "How to use Buridan UI with AI Skills."
order: 2
---

# Skills

AI Skills are specialized expert guides that enable AI agents (like Gemini CLI, Cursor, or ChatGPT) to understand how to build applications using Buridan UI.

Instead of the AI simply "guessing" or copy-pasting code, a Skill provides it with procedural knowledge, such as using our CLI for dependency resolution and following our OKLCH theming system.

## Gemini CLI

Buridan UI provides a specialized `.skill` file for the Gemini CLI. When activated, the agent becomes an expert in our design system.

### Activation

```bash
gemini activate buridan-support
```

### Key Capabilities

- **CLI-First**: The agent knows to run `buridan add <component>` instead of manual code copying.
- **Dependency Resolution**: Automatically identifies and adds required utilities and icons.
- **Theming**: Understands how to correctly modify `assets/globals.css` using OKLCH variables.
- **Patterns**: Automatically uses `@layout_decorator` and `ClientStateVar` for new pages.

## Cursor and Windsurf

For users of Cursor or Windsurf, we provide a `.cursorrules` file in the project root. This acts as a persistent instruction set that forces the AI to follow Buridan UI's architectural best practices.

## OpenAI and Claude

Our documentation is "AI-Ready" via the `llms.txt` file located in the root of the repository. You can provide this URL to any LLM to give it context on how to use Buridan UI correctly.

```
https://buridan-ui.reflex.run/llms.txt
```
