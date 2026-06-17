

# Context Menu

Custom context menu component.

# Installation

Copy the following code into your app directory.


> **Error: 'ContextMenu' not found in registry**


# Usage


> **Error: 'context_menu' not found in registry**


# Anatomy 
Use the following composition to build a `Context Menu`


```python
context_menu.root(
    context_menu.trigger(),
    context_menu.portal(
        context_menu.positioner(
            context_menu.popup(
                context_menu.item(),
                context_menu.separator(),
                context_menu.group(
                    context_menu.group_label(),
                    context_menu.item(),
                ),
                context_menu.checkbox_item(
                    context_menu.checkbox_item_indicator(),
                ),
                context_menu.radio_group(
                    context_menu.radio_item(
                        context_menu.radio_item_indicator(),
                    ),
                ),
                context_menu.submenu_root(
                    context_menu.submenu_trigger(),
                    context_menu.portal(
                        context_menu.positioner(
                            context_menu.popup(),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
```



# Examples


## Low Level Demo

Uses the low-level context_menu API for full control over state and structure.


> **Error: 'context_menu_low_level_demo' not found in registry**
