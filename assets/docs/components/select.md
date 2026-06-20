

# Select
Displays a list of options for the user to pick from—triggered by a button.

# Installation
Copy the following code into your app directory.


> **Error: 'select' not found in registry**


# Usage

> **Error: 'select' not found in registry**


# Anatomy 
Use the following composition to build a `Select`

```python
select.root(
    select.trigger(
        select.value(),
        select.icon(),
    ),
    select.portal(
        select.positioner(
            select.popup(
                select.group(
                    select.group_label(),
                    select.item(
                        select.item_text(),
                        select.item_indicator(),
                    ),
                ),
                select.separator(),
            ),
        ),
    ),
)
```


# Examples

## Align Item
Use `align_item_with_trigger` on `select.positioner()` to control whether the selected item aligns with the trigger. When true (default), the popup positions so the selected item appears over the trigger. When false, the popup aligns to the trigger edge.


> **Error: 'select_align_with_items' not found in registry**


## Groups
Use `select.group` to organize items into sections, `select.group_label` to label each section, and `select.separator` to visually divide groups.


> **Error: 'select_groups' not found in registry**


## Scrollable
Use `select.scroll_up_arrow` and `select.scroll_down_arrow` to provide navigation controls for scrolling through long lists of select items within the dropdown.


> **Error: 'select_with_scroll_arrows' not found in registry**

