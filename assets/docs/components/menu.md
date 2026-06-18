

# Menu

Displays a menu to the user — such as a set of actions or functions — triggered by a button.

# Installation

Copy the following code into your app directory.


> **Error: 'menu' not found in registry**


# Usage


> **Error: 'menu' not found in registry**


# Anatomy 
Use the following composition to build a `Menu`


```python
menu.root(
    menu.trigger(),
    menu.portal(
        menu.positioner(
            menu.popup(
                menu.item(),
                menu.separator(),
                menu.group(
                    menu.group_label(),
                    menu.item(),
                ),
                menu.checkbox_item(
                    menu.checkbox_item_indicator(),
                ),
                menu.radio_group(
                    menu.radio_item(
                        menu.radio_item_indicator(),
                    ),
                ),
                menu.submenu_root(
                    menu.submenu_trigger(),
                    menu.portal(
                        menu.positioner(
                            menu.popup(),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
```



# Example
A basic dropdown menu that opens when the user clicks a trigger button.

## High Level
Uses low-level API to create a menu component.


> **Error: 'menu_high_level' not found in registry**


## Submenu
Use `menu.submenu_root()` to nest secondary actions.


> **Error: 'menu_submenu' not found in registry**


## Checkboxes
Use `menu.checkbox_item()` for toggles. 


> **Error: 'menu_checkboxes' not found in registry**

