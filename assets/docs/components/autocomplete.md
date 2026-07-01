

# Autocomplete

An input that suggests options as you type.

> **Note:** The Autocomplete is a fully custom component with no external dependencies — built as a self-contained JavaScript component exposed through a Python API for use in Reflex.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component autocomplete
```

### Manual Installation

```python
from typing import Any

from reflex.components.component import Component
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..utils.twmerge import cn


class ClassNames:
    ROOT = "relative w-full max-w-sm"
    INPUT = (
        "outline-none flex w-full text-foreground placeholder:text-muted-foreground "
        "disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 "
        "border border-input focus-visible:border-ring aria-invalid:border-destructive "
        "rounded-lg bg-transparent dark:bg-input/30 text-sm transition-colors "
        "focus-visible:ring-ring/50 focus-visible:ring-3 h-8 px-2.5"
    )
    POPUP = (
        "bg-popover text-popover-foreground rounded-lg shadow-md ring-foreground/10 "
        "flex max-h-[min(260px,50vh)] w-full flex-col overscroll-contain py-0.5 "
        "ring-1 z-[9999] duration-100"
    )
    LIST = "px-1 py-1 max-h-64 overflow-y-auto overscroll-contain"
    ITEM = (
        "text-foreground gap-1.5 rounded-md px-1.5 py-1 text-sm relative flex "
        "cursor-default items-center outline-hidden select-none "
        "disabled:pointer-events-none disabled:opacity-50"
    )
    ITEM_HIGHLIGHTED = "bg-accent text-accent-foreground"
    EMPTY = "text-muted-foreground px-2 py-1.5 text-sm text-center"
    GROUP_LABEL = "text-muted-foreground px-1.5 py-1 text-xs font-medium"
    SEPARATOR = "bg-border my-1 mx-1.5 h-px"


BURIDAN_AUTOCOMPLETE_JS = """
function injectScrollLockStyle() {
    if (document.getElementById("buridan-autocomplete-scroll-lock-style")) return;

    const style = document.createElement("style");
    style.id = "buridan-autocomplete-scroll-lock-style";
    style.innerHTML = `
        body.buridan-autocomplete-scroll-lock {
            overflow: hidden;
        }
    `;
    document.head.appendChild(style);
}

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
    groupLabelClass,
    separatorClass,
    setQueryOnSelect = true,
}) {
    const [query, setQuery] = React.useState("");
    const [open, setOpen] = React.useState(false);
    const [popupVisible, setPopupVisible] = React.useState(false);
    const [closing, setClosing] = React.useState(false);

    const [highlighted, setHighlighted] = React.useState(-1);
    const [flipUp, setFlipUp] = React.useState(false);
    const [popupStyle, setPopupStyle] = React.useState({});

    const rootRef = React.useRef(null);
    const closeTimer = React.useRef(null);

    React.useEffect(() => {
        injectScrollLockStyle();
    }, []);

    // ── BODY SCROLL LOCK ─────────────────────────────────────────────
    React.useEffect(() => {
        if (!popupVisible) return;

        document.body.classList.add("buridan-autocomplete-scroll-lock");

        return () => {
            document.body.classList.remove("buridan-autocomplete-scroll-lock");
        };
    }, [popupVisible]);

    const isGrouped =
        Array.isArray(items) && items.length > 0 && items[0]?.group !== undefined;

    function fuzzyMatch(str, q) {
        str = str.toLowerCase();
        q = q.toLowerCase();

        let si = 0, qi = 0, score = 0, lastMatch = -1;

        while (si < str.length && qi < q.length) {
            if (str[si] === q[qi]) {
                score += lastMatch === si - 1 ? 2 : 1;
                lastMatch = si;
                qi++;
            }
            si++;
        }

        return qi === q.length ? score : -1;
    }

    function getLabel(item) {
        return typeof item === "string"
            ? item
            : item.label ?? JSON.stringify(item);
    }

    const filtered = React.useMemo(() => {
        if (!query) {
            return isGrouped
                ? items.map(g => ({ group: g.group, items: g.items }))
                : items;
        }

        if (isGrouped) {
            return items
                .map(g => {
                    const matchedItems = g.items
                        .map(item => ({
                            item,
                            score: fuzzyMatch(getLabel(item), query),
                        }))
                        .filter(({ score }) => score > 0)
                        .sort((a, b) => b.score - a.score)
                        .map(({ item }) => item);

                    return { group: g.group, items: matchedItems };
                })
                .filter(g => g.items.length > 0);
        }

        return items
            .map(item => ({
                item,
                score: fuzzyMatch(getLabel(item), query),
            }))
            .filter(({ score }) => score > 0)
            .sort((a, b) => b.score - a.score)
            .map(({ item }) => item);
    }, [items, query, isGrouped]);

    const flatItems = React.useMemo(() => {
        if (!isGrouped) return filtered;
        return filtered.flatMap(g => g.items);
    }, [filtered, isGrouped]);

    const totalCount = flatItems.length;

    function updatePopupPosition() {
        if (!rootRef.current) return;

        const rect = rootRef.current.getBoundingClientRect();
        const spaceBelow = window.innerHeight - rect.bottom;
        const spaceAbove = rect.top;
        const flip = spaceBelow < 260 && spaceAbove > spaceBelow;

        setFlipUp(flip);

        setPopupStyle({
            position: "fixed",
            left: rect.left + "px",
            width: rect.width + "px",
            ...(flip
                ? {
                    bottom: window.innerHeight - rect.top + 4 + "px",
                    top: "auto",
                }
                : {
                    top: rect.bottom + 4 + "px",
                    bottom: "auto",
                }),
        });
    }

    function openPopup() {
        if (closeTimer.current) clearTimeout(closeTimer.current);
        setClosing(false);
        setOpen(true);
        setPopupVisible(true);
    }

    function closePopup() {
        setClosing(true);

        closeTimer.current = setTimeout(() => {
            setOpen(false);
            setPopupVisible(false);
            setClosing(false);
            setHighlighted(-1);
        }, 100);
    }

    function handleSelect(item) {
        const val = getLabel(item);

        setOpen(false);
        setPopupVisible(false);
        setHighlighted(-1);

        if (setQueryOnSelect) {
            setQuery(val);
        } else {
            setQuery("");
        }

        onSelectItem?.(val);
    }

    function handleKeyDown(e) {
        if (!open) return;

        if (e.key === "ArrowDown") {
            e.preventDefault();
            setHighlighted(h => Math.min(h + 1, totalCount - 1));
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            setHighlighted(h => Math.max(h - 1, 0));
        } else if (e.key === "Enter") {
            e.preventDefault();
            if (highlighted >= 0 && flatItems[highlighted]) {
                handleSelect(flatItems[highlighted]);
            }
        } else if (e.key === "Escape") {
            closePopup();
        }
    }

    const isEmpty = totalCount === 0;

    const popupEl = popupVisible
        ? ReactDOM.createPortal(
            <div
                className={
                    popupClass +
                    (flipUp ? " origin-bottom" : " origin-top") +
                    (closing
                        ? " animate-out fade-out-0 zoom-out-95"
                        : flipUp
                            ? " animate-in fade-in-0 zoom-in-95 slide-in-from-bottom-2"
                            : " animate-in fade-in-0 zoom-in-95 slide-in-from-top-2")
                }
                style={popupStyle}
            >
                {isEmpty ? (
                    <div className={emptyClass}>No results found.</div>
                ) : isGrouped ? (
                    <ul className={listClass}>
                        {(() => {
                            let offset = 0;

                            return filtered.map((group, gi) => {
                                const groupOffset = offset;

                                const nodes = (
                                    <React.Fragment key={group.group}>
                                        {gi > 0 && (
                                            <div className={separatorClass} />
                                        )}

                                        <li className={groupLabelClass}>
                                            {group.group}
                                        </li>

                                        {group.items.map((item, ii) => {
                                            const flatIndex =
                                                groupOffset + ii;

                                            const label = getLabel(item);
                                            const isHighlighted =
                                                highlighted === flatIndex;

                                            return (
                                                <li
                                                    key={label}
                                                    className={
                                                        isHighlighted
                                                            ? itemClass +
                                                              " " +
                                                              itemHighlightedClass
                                                            : itemClass
                                                    }
                                                    onMouseDown={() =>
                                                        handleSelect(item)
                                                    }
                                                    onMouseEnter={() =>
                                                        setHighlighted(flatIndex)
                                                    }
                                                >
                                                    {label}
                                                </li>
                                            );
                                        })}
                                    </React.Fragment>
                                );

                                offset += group.items.length;
                                return nodes;
                            });
                        })()}
                    </ul>
                ) : (
                    <ul className={listClass}>
                        {filtered.map((item, idx) => {
                            const label = getLabel(item);
                            const isHighlighted = highlighted === idx;

                            return (
                                <li
                                    key={label}
                                    className={
                                        isHighlighted
                                            ? itemClass +
                                              " " +
                                              itemHighlightedClass
                                            : itemClass
                                    }
                                    onMouseDown={() => handleSelect(item)}
                                    onMouseEnter={() => setHighlighted(idx)}
                                >
                                    {label}
                                </li>
                            );
                        })}
                    </ul>
                )}
            </div>,
            document.body,
        )
        : null;

    return (
        <div ref={rootRef} className={rootClass}>
            <input
                className={inputClass}
                placeholder={placeholder}
                value={query}
                onChange={(e) => {
                    const val = e.target.value;
                    setQuery(val);

                    if (val.length === 0) {
                        setClosing(false);
                        setOpen(false);
                        setPopupVisible(false);
                        setHighlighted(-1);
                        return;
                    }

                    openPopup();
                    setHighlighted(-1);
                    onChangeQuery?.(val);
                    updatePopupPosition();
                }}
                onFocus={() => {
                    if (query.length > 0) {
                        updatePopupPosition();
                        openPopup();
                    }
                }}
                onBlur={() => {
                    setTimeout(() => {
                        if (!query || query.length === 0) {
                            setClosing(false);
                            setOpen(false);
                            setPopupVisible(false);
                            setHighlighted(-1);
                            return;
                        }
                        closePopup();
                    }, 150);
                }}
                onKeyDown={handleKeyDown}
            />

            {popupEl}
        </div>
    );
}
"""


class BuridanAutocomplete(Component):
    tag = "BuridanAutocompleteRoot"

    is_default = False

    items: Var[Any]

    placeholder: Var[str]

    root_class: Var[str]

    input_class: Var[str]

    popup_class: Var[str]

    list_class: Var[str]

    item_class: Var[str]

    item_highlighted_class: Var[str]

    empty_class: Var[str]

    group_label_class: Var[str]

    separator_class: Var[str]

    set_query_on_select: Var[bool] = True

    on_change_query: EventHandler[passthrough_event_spec(str)]

    on_select_item: EventHandler[passthrough_event_spec(str)]

    def add_custom_code(self) -> list[str]:
        return [BURIDAN_AUTOCOMPLETE_JS]

    def add_imports(self) -> dict:
        return {
            "react": ImportVar(tag="React", is_default=True),
            "react-dom": ImportVar(tag="ReactDOM", is_default=True),
        }

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
        props["group_label_class"] = cn(
            ClassNames.GROUP_LABEL, props.pop("group_label_class", "")
        )
        props["separator_class"] = cn(
            ClassNames.SEPARATOR, props.pop("separator_class", "")
        )
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


## Grouped List

Pass a `group` key to your data structure to group items together. 


```python
def autocomplete_grouping():
    return autocomplete(
        items=[
            {"group": "Fruits", "items": ["Apple", "Banana", "Mango"]},
            {"group": "Vegetables", "items": ["Carrot", "Broccoli"]},
            {"group": "Grains", "items": ["Rice", "Wheat", "Oats"]},
        ],
        placeholder="Search tags...",
        separator_class="bg-transparent",
        popup_class="mt-2",
        root_class="scrollbar-none",
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

**autocomplete**

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
| `set_query_on_select` | `bool` | `True`  | Controls whether selecting an item updates the input value. If `False`, selection clears the input (useful for command palette / navigation mode). |
