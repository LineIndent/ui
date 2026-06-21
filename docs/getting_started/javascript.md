---
title: "JavaScript"
description: "How to use buridan/ui with JavaScript"
order: 4
---


# JavaScript

How to use buridan/ui with JavaScript.

Although 99% of your Reflex apps will be in pure Python, the occasional [JavaScript](https://reflex.dev/docs/api-reference/browser-javascript) may come in handy to make things more feasible.

Two main ways to run in-line JavaScript in your Reflex app:

- `rx.script` → load inline or external scripts
- `rx.call_script` → run JS from event handlers

To use `rx.script`, you need to add the path to the JavaScript code into your `rx.App` instance.

```reflex
rx.App(head_components=[rx.script(...)])
```

To use `rx._call_script`, you can attach it to any of the event triggers available to Reflex components. 

```python
rx.el.button(
    "Expand",
    class_name="!text-xs text-muted-foreground hover:text-foreground",
    on_click=rx.call_script("""
        const btn = event.currentTarget;
    
        if (btn.innerText === "Expand") {
            btn.innerText = "Collapse";
        } else {
            btn.innerText = "Expand";
        }
    """),
)
```

>Custom Javascript code in your Reflex app presents a maintenance challenge, as it will be harder to debug and may be unstable across Reflex versions. Prefer to use the Python API whenever possible and file an issue if you need additional functionality that is not currently provided.
