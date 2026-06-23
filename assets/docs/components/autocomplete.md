

# Autocomplete

An input that suggests options as you type.

> **Note:** The Autocomplete component is a fully custom implementation with no external dependencies. It's a JavaScript component with a Python API used in Reflex.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component autocomplete
```

### Manual Installation

```python
"""Custom autocomplete component."""

from typing import Any

from reflex.components.component import Component
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..utils.twmerge import cn


class ClassNames:
    ROOT = "relative w-full max-w-sm"
    INPUT = "outline-none flex w-full text-foreground placeholder:text-muted-foreground disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 border border-input focus-visible:border-ring aria-invalid:border-destructive rounded-lg bg-transparent dark:bg-input/30 text-sm transition-colors focus-visible:ring-ring/50 focus-visible:ring-3 h-8 px-2.5"
    POPUP = "bg-popover text-popover-foreground rounded-lg shadow-md ring-foreground/10 flex max-h-[min(260px,50vh)] w-full flex-col overscroll-contain py-0.5 ring-1 absolute z-50 left-0"
    LIST = "px-1 py-1 max-h-64 overflow-y-auto overscroll-contain"
    ITEM = "text-foreground gap-1.5 rounded-md px-1.5 py-1 text-sm relative flex cursor-default items-center outline-hidden select-none disabled:pointer-events-none disabled:opacity-50"
    ITEM_HIGHLIGHTED = "bg-accent text-accent-foreground"
    EMPTY = "text-muted-foreground px-2 py-1.5 text-sm text-center"
    GROUP_LABEL = "text-muted-foreground px-1.5 py-1 text-xs font-medium"
    SEPARATOR = "bg-border my-1.5 h-px"


BURIDAN_AUTOCOMPLETE_JS = """
function BuridanAutocompleteRoot({
    items = [],
    placeholder,
    onChangeQuery,
    onSelectItem,
    rootClass,
    inputClass,
    popupClass,
    listClass,
    itemClass,
    itemHighlightedClass,
    emptyClass,
}) {
    const [query, setQuery] = React.useState("");
    const [open, setOpen] = React.useState(false);
    const [highlighted, setHighlighted] = React.useState(-1);
    const [flipUp, setFlipUp] = React.useState(false);
    const rootRef = React.useRef(null);

    function fuzzyMatch(str, query) {
        str = str.toLowerCase();
        query = query.toLowerCase();
        let si = 0, qi = 0, score = 0, lastMatch = -1;
        while (si < str.length && qi < query.length) {
            if (str[si] === query[qi]) {
                score += lastMatch === si - 1 ? 2 : 1; // bonus for consecutive matches
                lastMatch = si;
                qi++;
            }
            si++;
        }
        return qi === query.length ? score : -1; // -1 means no match
    }

    const filtered = query
        ? items
            .map(i => {
                const label = typeof i === "string" ? i : i.label ?? JSON.stringify(i);
                const score = fuzzyMatch(label, query);
                return { item: i, score };
            })
            .filter(({ score }) => score > 0)
            .sort((a, b) => b.score - a.score)
            .map(({ item }) => item)
        : items;

    function checkFlip() {
        if (!rootRef.current) return;
        const rect = rootRef.current.getBoundingClientRect();
        const spaceBelow = window.innerHeight - rect.bottom;
        const spaceAbove = rect.top;
        setFlipUp(spaceBelow < 260 && spaceAbove > spaceBelow);
    }

    function handleSelect(item) {
        const val = typeof item === "string" ? item : item.label ?? JSON.stringify(item);
        setQuery(val);
        setOpen(false);
        setHighlighted(-1);
        onSelectItem?.(val);
    }

    function handleKeyDown(e) {
        if (!open) return;
        if (e.key === "ArrowDown") {
            e.preventDefault();
            setHighlighted(h => Math.min(h + 1, filtered.length - 1));
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            setHighlighted(h => Math.max(h - 1, 0));
        } else if (e.key === "Enter") {
            e.preventDefault();
            if (highlighted >= 0 && filtered[highlighted]) {
                handleSelect(filtered[highlighted]);
            }
        } else if (e.key === "Escape") {
            setOpen(false);
            setHighlighted(-1);
        }
    }

    const popupPositionClass = flipUp
        ? "bottom-[calc(100%+4px)] top-auto"
        : "top-[calc(100%+4px)] bottom-auto";

    return (
        <div ref={rootRef} className={rootClass} style={{ position: "relative" }}>
            <input
                className={inputClass}
                placeholder={placeholder}
                value={query}
                onChange={(e) => {
                    const val = e.target.value;
                    setQuery(val);
                    setOpen(val.length > 0);
                    setHighlighted(-1);
                    onChangeQuery?.(val);
                    checkFlip();
                }}
                onFocus={() => {
                    if (query.length > 0) {
                        checkFlip();
                        setOpen(true);
                    }
                }}
                onBlur={() => setTimeout(() => { setOpen(false); setHighlighted(-1); }, 150)}
                onKeyDown={handleKeyDown}
            />
            {open && (
                <div className={popupClass + " " + popupPositionClass}>
                    {filtered.length === 0 ? (
                        <div className={emptyClass}>No results found.</div>
                    ) : (
                        <ul className={listClass}>
                            {filtered.map((item, idx) => {
                                const label = typeof item === "string" ? item : item.label ?? JSON.stringify(item);
                                const isHighlighted = highlighted === idx;
                                return (
                                    <li
                                        key={label}
                                        className={isHighlighted ? itemClass + " " + itemHighlightedClass : itemClass}
                                        onMouseDown={() => handleSelect(item)}
                                        onMouseEnter={() => setHighlighted(idx)}
                                    >
                                        {label}
                                    </li>
                                );
                            })}
                        </ul>
                    )}
                </div>
            )}
        </div>
    );
}
"""


class BuridanAutocomplete(Component):
    """A fully custom autocomplete component with no external dependencies."""

    tag = "BuridanAutocompleteRoot"
    is_default = False

    # The list of items to display
    items: Var[Any]

    # Placeholder text for the input
    placeholder: Var[str]

    # CSS class for the root wrapper
    root_class: Var[str]

    # CSS class for the input
    input_class: Var[str]

    # CSS class for the popup
    popup_class: Var[str]

    # CSS class for the list
    list_class: Var[str]

    # CSS class for each item
    item_class: Var[str]

    # CSS class for the highlighted item
    item_highlighted_class: Var[str]

    # CSS class for the empty state
    empty_class: Var[str]

    # Fired when the input value changes
    on_change_query: EventHandler[passthrough_event_spec(str)]

    # Fired when an item is selected
    on_select_item: EventHandler[passthrough_event_spec(str)]

    def add_custom_code(self) -> list[str]:
        return [BURIDAN_AUTOCOMPLETE_JS]

    def add_imports(self) -> dict:
        return {"react": ImportVar(tag="React", is_default=True)}

    @classmethod
    def create(cls, *children, **props):
        props["root_class"] = cn(ClassNames.ROOT, props.pop("root_class", ""))
        props["input_class"] = cn(ClassNames.INPUT, props.pop("input_class", ""))
        props["popup_class"] = cn(ClassNames.POPUP, props.pop("popup_class", ""))
        props["list_class"] = cn(ClassNames.LIST, props.pop("list_class", ""))
        props["item_class"] = cn(ClassNames.ITEM, props.pop("item_class", ""))
        props["item_highlighted_class"] = cn(
            ClassNames.ITEM_HIGHLIGHTED, props.pop("item_highlighted_class", "")
        )
        props["empty_class"] = cn(ClassNames.EMPTY, props.pop("empty_class", ""))
        return super().create(*children, **props)


autocomplete = BuridanAutocomplete.create
```


# Usage


```python
from components.ui.autocomplete import autocomplete
```


# Anatomy 
Use the following composition to build an `Autocomplete` component. 


```python
autocomplete(
    items=[...],
)
```


# Examples

## Basic

A minimal autocomplete with a static list of items.


```python
def autocomplete_basic():
    return autocomplete(
        items=["feature", "fix", "bug", "docs", "internal", "mobile"],
        placeholder="Search tags...",
    )
```


## Selected Value

Wire up `on_select_item` to capture the selected value.


```python
def autocomplete_select_value():
    return autocomplete(
        items=["feature", "fix", "bug", "docs", "internal", "mobile"],
        placeholder="Search and select...",
        on_select_item=lambda value: rx.toast(value),
    )
```


## Large List

Autocomplete works efficiently with large lists — filtering happens entirely in the browser.


```python
def autocomplete_large_list():
    return autocomplete(
        items=ITEMS,
        placeholder="Search components and charts...",
    )
```


## Custom Styling

Override any part of the component by passing a `*_class` prop. Classes are merged with the defaults via `cn`.


```python
def autocomplete_custom_styling():
    return autocomplete(
        items=["feature", "fix", "bug", "docs", "internal", "mobile"],
        placeholder="Search tags...",
        input_class="h-10 rounded-full px-4 border-ring",
        popup_class="rounded-xl",
        item_class="rounded-full px-3",
        item_highlighted_class="bg-primary text-primary-foreground",
    )
```


## Empty State

When no items match the query, the empty state is shown automatically.


```python
def autocomplete_empty_state():
    return autocomplete(
        items=["feature", "fix", "bug"],
        placeholder="Try typing something that won't match...",
        empty_class="text-destructive py-6",
    )
```


# API Reference

| Prop | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `items` | `list[str]` | `[]` | The list of items to display in the dropdown. |
| `placeholder` | `str` | `None` | Placeholder text shown inside the input when empty. |
| `on_change_query` | `EventHandler` | `None` | Fired on every keystroke with the current input value. |
| `on_select_item` | `EventHandler` | `None` | Fired when an item is selected, with the selected value as argument. |
| `root_class` | `str` | `None` | Additional Tailwind classes merged onto the root wrapper. |
| `input_class` | `str` | `None` | Additional Tailwind classes merged onto the input element. |
| `popup_class` | `str` | `None` | Additional Tailwind classes merged onto the dropdown popup. |
| `list_class` | `str` | `None` | Additional Tailwind classes merged onto the scrollable list. |
| `item_class` | `str` | `None` | Additional Tailwind classes merged onto each list item. |
| `item_highlighted_class` | `str` | `None` | Additional Tailwind classes merged onto the currently highlighted item. |
| `empty_class` | `str` | `None` | Additional Tailwind classes merged onto the empty state element. |
