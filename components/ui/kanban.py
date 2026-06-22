# """Custom Kanban board component for Reflex — no external Python dependencies."""

# from typing import Any

# from reflex.components.component import Component
# from reflex.event import EventHandler, passthrough_event_spec
# from reflex.utils.imports import ImportVar
# from reflex.vars.base import Var

# from ..utils.twmerge import cn


# class ClassNames:
#     ROOT = "w-full"
#     BOARD = "flex gap-4 w-full items-start"
#     COLUMN = "flex flex-col gap-3 flex-1 min-w-[240px] rounded-xl bg-accent/40 p-3"
#     COLUMN_HEADER = "flex items-center justify-between px-1 pb-1"
#     COLUMN_TITLE = "text-sm font-semibold text-foreground tracking-tight"
#     COLUMN_COUNT = "text-xs text-muted-foreground font-medium tabular-nums"
#     COLUMN_CONTENT = "flex flex-col gap-2 min-h-[60px]"
#     ITEM = "rounded-lg border border-border bg-background px-3 py-2.5 shadow-xs cursor-grab active:cursor-grabbing select-none text-sm text-foreground transition-all duration-150 hover:shadow-md"
#     ITEM_DRAGGING = "opacity-40 shadow-none scale-[0.98]"
#     OVERLAY = "rounded-lg border border-border bg-background px-3 py-2.5 shadow-xl text-sm text-foreground cursor-grabbing"
#     OVER = "ring-2 ring-ring ring-offset-1"


# BURIDAN_KANBAN_JS = """
# (function () {

#   // ── helpers ────────────────────────────────────────────────────────────────
#   function cloneColumns(cols) {
#     const out = {};
#     for (const k of Object.keys(cols)) out[k] = [...cols[k]];
#     return out;
#   }

#   function parseColumns(raw) {
#     if (!raw) return {};
#     if (typeof raw === "string") {
#       try { return JSON.parse(raw); } catch { return {}; }
#     }
#     return raw;
#   }

#   // ── Animated placeholder ───────────────────────────────────────────────────
#   // Mounts at height 0, animates to targetHeight on next frame.
#   // Unmounts by animating back to 0 first (handled by key changes in React).
#   function KanbanPlaceholder({ targetHeight }) {
#     const [height, setHeight] = React.useState(0);
#     React.useLayoutEffect(() => {
#       requestAnimationFrame(() => setHeight(targetHeight));
#     }, [targetHeight]);

#     return (
#       <div style={{
#         height: height + "px",
#         borderRadius: "8px",
#         background: "hsl(var(--accent))",
#         border: "2px dashed hsl(var(--border)/0.6)",
#         transition: "height 160ms cubic-bezier(0.25, 1, 0.5, 1)",
#         overflow: "hidden",
#         flexShrink: 0,
#       }} />
#     );
#   }

#   // ── Main component ─────────────────────────────────────────────────────────
#   function BuridanKanbanRoot({
#     columns: initialColumns,
#     onItemMove,
#     rootClass,
#     boardClass,
#     columnClass,
#     columnHeaderClass,
#     columnTitleClass,
#     columnCountClass,
#     columnContentClass,
#     itemClass,
#     itemDraggingClass,
#     overlayClass,
#   }) {
#     const [columns, setColumns] = React.useState(() => parseColumns(initialColumns));

#     // sync with rx.State prop changes
#     React.useEffect(() => {
#       setColumns(parseColumns(initialColumns));
#     }, [initialColumns]);

#     // ── drag state ────────────────────────────────────────────────────────────
#     // dragging: { itemId, fromCol, fromIndex, label, itemHeight }
#     const [dragging, setDragging]   = React.useState(null);
#     // overInfo: { colId, index } — where the placeholder lives
#     const [overInfo, setOverInfo]   = React.useState(null);

#     // refs for things that must not trigger re-renders mid-drag
#     const dragRef    = React.useRef(null); // { currentCol, currentIndex }
#     const overlayRef = React.useRef(null);
#     const colsRef    = React.useRef(columns);
#     const itemEls    = React.useRef({});   // itemId -> DOM element

#     React.useEffect(() => { colsRef.current = columns; }, [columns]);

#     // ── item helpers ──────────────────────────────────────────────────────────
#     const getLabel = (item) =>
#       typeof item === "string" ? item : (item.label ?? item.id ?? JSON.stringify(item));

#     const getId = (item) =>
#       typeof item === "string" ? item : (item.id ?? JSON.stringify(item));

#     // ── midpoint hit-test against rendered item elements ─────────────────────
#     // Returns { colId, index } for the best drop slot at pointer position (cx, cy).
#     function resolveDropTarget(cx, cy) {
#       const cols = colsRef.current;
#       let bestCol   = null;
#       let bestIndex = 0;
#       let bestDist  = Infinity;

#       for (const [colId, items] of Object.entries(cols)) {
#         for (let i = 0; i < items.length; i++) {
#           const id = getId(items[i]);
#           const el = itemEls.current[id];
#           if (!el) continue;

#           const rect   = el.getBoundingClientRect();
#           const midY   = rect.top + rect.height / 2;
#           const midX   = rect.left + rect.width / 2;
#           const dist   = Math.hypot(cx - midX, cy - midY);

#           if (dist < bestDist) {
#             bestDist  = dist;
#             bestCol   = colId;
#             // if pointer is above midpoint → insert before, else after
#             bestIndex = cy < midY ? i : i + 1;
#           }
#         }
#       }

#       // fall back: find nearest column by horizontal proximity
#       if (!bestCol) {
#         for (const colId of Object.keys(cols)) {
#           bestCol   = colId;
#           bestIndex = (cols[colId] || []).length;
#         }
#       }

#       return { colId: bestCol, index: bestIndex };
#     }

#     // also resolve purely by column rect when pointer is deep inside an empty col
#     function resolveColumnUnderPointer(cx, cy) {
#       const colEls = document.querySelectorAll("[data-buridan-col]");
#       for (const el of colEls) {
#         const rect = el.getBoundingClientRect();
#         if (cx >= rect.left && cx <= rect.right && cy >= rect.top && cy <= rect.bottom) {
#           return el.dataset.buridanCol;
#         }
#       }
#       return null;
#     }

#     // ── drag start ────────────────────────────────────────────────────────────
#     function handleDragStart(e, itemId, colId, index) {
#       e.preventDefault();
#       const col   = colsRef.current[colId];
#       const label = getLabel(col[index]);

#       // measure the item so the placeholder matches its height
#       const el         = itemEls.current[itemId];
#       const itemHeight = el ? el.getBoundingClientRect().height : 38;

#       setDragging({ itemId, fromCol: colId, fromIndex: index, label, itemHeight });
#       setOverInfo({ colId, index });

#       dragRef.current = { currentCol: colId, currentIndex: index };

#       // position overlay immediately without waiting for React paint
#       let ox = e.clientX + 14;
#       let oy = e.clientY - itemHeight / 2;

#       if (overlayRef.current) {
#         overlayRef.current.style.transform = `translate(${ox}px, ${oy}px) rotate(1.5deg) scale(1.03)`;
#       }

#       function onMove(ev) {
#         ox = ev.clientX + 14;
#         oy = ev.clientY - itemHeight / 2;

#         // GPU-composited move — no layout read
#         if (overlayRef.current) {
#           overlayRef.current.style.transform =
#             `translate(${ox}px, ${oy}px) rotate(1.5deg) scale(1.03)`;
#         }

#         // resolve drop target from pointer position
#         const target = resolveDropTarget(ev.clientX, ev.clientY);

#         // if best match is far away, try column fallback for empty columns
#         const colUnder = resolveColumnUnderPointer(ev.clientX, ev.clientY);
#         if (colUnder && colUnder !== target.colId) {
#           const colItems = colsRef.current[colUnder] || [];
#           if (colItems.length === 0) {
#             target.colId  = colUnder;
#             target.index  = 0;
#           }
#         }

#         if (
#           target.colId !== dragRef.current.currentCol ||
#           target.index !== dragRef.current.currentIndex
#         ) {
#           dragRef.current.currentCol   = target.colId;
#           dragRef.current.currentIndex = target.index;
#           setOverInfo({ colId: target.colId, index: target.index });
#         }
#       }

#       function onUp() {
#         commitDrop();
#         window.removeEventListener("pointermove", onMove);
#         window.removeEventListener("pointerup",   onUp);
#       }

#       window.addEventListener("pointermove", onMove);
#       window.addEventListener("pointerup",   onUp);
#     }

#     // ── commit drop ───────────────────────────────────────────────────────────
#     function commitDrop() {
#       const d = dragRef.current;
#       if (!d) { setDragging(null); setOverInfo(null); return; }

#       const fromCol   = draggingRef.current.fromCol;
#       const fromIndex = draggingRef.current.fromIndex;
#       const itemId    = draggingRef.current.itemId;
#       const { currentCol, currentIndex } = d;

#       dragRef.current = null;

#       setColumns(prev => {
#         const next = cloneColumns(prev);
#         const [movedItem] = next[fromCol].splice(fromIndex, 1);
#         // adjust dest index if moving within same column past the removal point
#         const destIndex = (fromCol === currentCol && currentIndex > fromIndex)
#           ? currentIndex - 1
#           : currentIndex;
#         next[currentCol].splice(Math.min(destIndex, next[currentCol].length), 0, movedItem);
#         return next;
#       });

#       if (onItemMove && fromCol !== currentCol) {
#         onItemMove(JSON.stringify({
#           item_id:     itemId,
#           from_column: fromCol,
#           from_index:  fromIndex,
#           to_column:   currentCol,
#           to_index:    currentIndex,
#         }));
#       }

#       setDragging(null);
#       setOverInfo(null);
#     }

#     // commitDrop needs access to the latest dragging snapshot — keep a ref
#     const draggingRef = React.useRef(null);
#     React.useEffect(() => { draggingRef.current = dragging; }, [dragging]);

#     // ── render ────────────────────────────────────────────────────────────────
#     const isDragging = !!dragging;

#     return (
#       <div
#         className={rootClass}
#         style={{ userSelect: isDragging ? "none" : undefined }}
#       >
#         <div className={boardClass}>
#           {Object.entries(columns).map(([colId, items]) => {
#             const isOverCol = overInfo?.colId === colId;

#             return (
#               <div
#                 key={colId}
#                 data-buridan-col={colId}
#                 className={columnClass}
#               >
#                 {/* column header */}
#                 <div className={columnHeaderClass}>
#                   <span className={columnTitleClass}>{colId}</span>
#                   <span className={columnCountClass}>{items.length}</span>
#                 </div>

#                 {/* items + placeholder */}
#                 <div className={columnContentClass}>
#                   {/* placeholder at top / between items */}
#                   {isOverCol && overInfo.index === 0 && dragging && (
#                     <KanbanPlaceholder
#                       key={"ph-" + colId + "-0"}
#                       targetHeight={dragging.itemHeight}
#                     />
#                   )}

#                   {items.map((item, idx) => {
#                     const id             = getId(item);
#                     const label          = getLabel(item);
#                     const isBeingDragged = dragging?.itemId === id;
#                     // show placeholder AFTER this item?
#                     const showPhAfter    = isOverCol && overInfo.index === idx + 1;

#                     return (
#                       <React.Fragment key={id}>
#                         <div
#                           ref={el => {
#                             if (el) itemEls.current[id] = el;
#                             else delete itemEls.current[id];
#                           }}
#                           className={
#                             isBeingDragged
#                               ? itemClass + " " + itemDraggingClass
#                               : itemClass
#                           }
#                           style={{
#                             transition: isDragging
#                               ? "transform 160ms cubic-bezier(0.25,1,0.5,1), opacity 150ms ease, box-shadow 150ms ease"
#                               : undefined,
#                           }}
#                           onPointerDown={e => handleDragStart(e, id, colId, idx)}
#                         >
#                           {label}
#                         </div>

#                         {showPhAfter && dragging && !isBeingDragged && (
#                           <KanbanPlaceholder
#                             key={"ph-" + colId + "-" + (idx + 1)}
#                             targetHeight={dragging.itemHeight}
#                           />
#                         )}
#                       </React.Fragment>
#                     );
#                   })}

#                   {/* placeholder at end of column */}
#                   {isOverCol && overInfo.index >= items.length && dragging && (
#                     <KanbanPlaceholder
#                       key={"ph-" + colId + "-end"}
#                       targetHeight={dragging.itemHeight}
#                     />
#                   )}
#                 </div>
#               </div>
#             );
#           })}
#         </div>

#         {/* drag overlay — position: fixed, moved via transform only (GPU layer) */}
#         {isDragging && (
#           <div
#             ref={overlayRef}
#             className={overlayClass}
#             style={{
#               position:      "fixed",
#               top:           0,
#               left:          0,
#               pointerEvents: "none",
#               zIndex:        9999,
#               minWidth:      "180px",
#               willChange:    "transform",
#               transform:     "translate(-9999px,-9999px)",
#             }}
#           >
#             {dragging.label}
#           </div>
#         )}
#       </div>
#     );
#   }

#   window.BuridanKanbanRoot = BuridanKanbanRoot;
# })();
# """


# class BuridanKanban(Component):
#     """
#     A self-contained Kanban board component with smooth drag-and-drop.

#     Data structure for `columns`:
#         {
#             "To Do":       ["Task A", "Task B"],
#             "In Progress": ["Task C"],
#             "Done":        ["Task D", "Task E"],
#         }

#     Items can also be dicts with `id` and `label` keys:
#         {
#             "To Do": [{"id": "t1", "label": "Fix bug"}],
#         }

#     Event handlers:
#         on_item_move — fired when an item moves to a different column.
#                        Receives a JSON string:
#                        {"item_id", "from_column", "from_index", "to_column", "to_index"}
#     """

#     tag = "BuridanKanbanRoot"
#     is_default = False

#     columns: Var[Any]

#     root_class: Var[str]
#     board_class: Var[str]
#     column_class: Var[str]
#     column_header_class: Var[str]
#     column_title_class: Var[str]
#     column_count_class: Var[str]
#     column_content_class: Var[str]
#     item_class: Var[str]
#     item_dragging_class: Var[str]
#     overlay_class: Var[str]
#     over_class: Var[str]

#     on_item_move: EventHandler[passthrough_event_spec(str)]

#     def add_custom_code(self) -> list[str]:
#         return [BURIDAN_KANBAN_JS]

#     def add_imports(self) -> dict:
#         return {"react": ImportVar(tag="React", is_default=True)}

#     @classmethod
#     def create(cls, *children, **props):
#         props["root_class"] = cn(ClassNames.ROOT, props.pop("root_class", ""))
#         props["board_class"] = cn(ClassNames.BOARD, props.pop("board_class", ""))
#         props["column_class"] = cn(ClassNames.COLUMN, props.pop("column_class", ""))
#         props["column_header_class"] = cn(
#             ClassNames.COLUMN_HEADER, props.pop("column_header_class", "")
#         )
#         props["column_title_class"] = cn(
#             ClassNames.COLUMN_TITLE, props.pop("column_title_class", "")
#         )
#         props["column_count_class"] = cn(
#             ClassNames.COLUMN_COUNT, props.pop("column_count_class", "")
#         )
#         props["column_content_class"] = cn(
#             ClassNames.COLUMN_CONTENT, props.pop("column_content_class", "")
#         )
#         props["item_class"] = cn(ClassNames.ITEM, props.pop("item_class", ""))
#         props["item_dragging_class"] = cn(
#             ClassNames.ITEM_DRAGGING, props.pop("item_dragging_class", "")
#         )
#         props["overlay_class"] = cn(ClassNames.OVERLAY, props.pop("overlay_class", ""))
#         props["over_class"] = cn(ClassNames.OVER, props.pop("over_class", ""))
#         return super().create(*children, **props)


# kanban = BuridanKanban.create

"""Custom Kanban board component for Reflex — no external Python dependencies."""

from typing import Any

from reflex.components.component import Component
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..utils.twmerge import cn


class ClassNames:
    ROOT = "w-full"
    BOARD = "flex gap-3 w-full items-start"
    COLUMN = "flex flex-col gap-2 flex-1 min-w-[260px] rounded-xl bg-accent/40 p-3"
    COLUMN_HEADER = (
        "flex items-center justify-between px-1 pb-2 border-b border-border/60"
    )
    COLUMN_TITLE = "text-sm font-semibold text-foreground tracking-tight"
    COLUMN_COUNT = "text-[11px] font-medium text-muted-foreground bg-accent rounded-full px-2 py-0.5 tabular-nums"
    COLUMN_BODY = "flex flex-col gap-2 min-h-[60px] pt-2"
    # card
    CARD = "rounded-lg border border-border bg-background px-3 py-2.5 shadow-xs cursor-grab active:cursor-grabbing select-none transition-all duration-150 hover:shadow-md hover:border-border/80"
    CARD_DRAGGING = "opacity-40 shadow-none scale-[0.98]"
    # overlay card (the ghost that follows the cursor)
    OVERLAY_CARD = "rounded-lg border border-border bg-background px-3 py-2.5 shadow-xl cursor-grabbing select-none"


BURIDAN_KANBAN_JS = """
(function () {

  // ── helpers ────────────────────────────────────────────────────────────────
  function cloneColumns(cols) {
    const out = {};
    for (const k of Object.keys(cols)) out[k] = [...cols[k]];
    return out;
  }

  function parseColumns(raw) {
    if (!raw) return {};
    if (typeof raw === "string") {
      try { return JSON.parse(raw); } catch { return {}; }
    }
    return raw;
  }

  function getId(item) {
    return typeof item === "string" ? item : (item.id ?? JSON.stringify(item));
  }

  function getLabel(item) {
    return typeof item === "string" ? item : (item.label ?? item.title ?? item.id ?? "");
  }

  // ── priority config ────────────────────────────────────────────────────────
  const PRIORITY = {
    high:   { label: "High",   bg: "oklch(0.58 0.22 27)", color: "oklch(0.985 0 0)",        border: "hsl(var(--destructive)/0.3)"  },
    medium: { label: "Medium", bg: "oklch(0.65 0.19 41)",    color: "oklch(0.985 0 0)",            border: "hsl(var(--primary)/0.3)"      },
    low:    { label: "Low",    bg: "oklch(0.63 0.17 149)",     color: "oklch(0.985 0 0)", border: "hsl(var(--warning,47 96% 53%)/0.3)" },
  };

  // ── Avatar (initials only, no image requests) ─────────────────────────────
  function Avatar({ name }) {
    const initials = name
      .split(" ")
      .slice(0, 2)
      .map(w => w[0] ?? "")
      .join("")
      .toUpperCase();

    // deterministic hue from name
    let hash = 0;
    for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
    const hue = Math.abs(hash) % 360;

    return (
      <div style={{
        width: "18px", height: "18px",
        borderRadius: "50%",
        background: `hsl(${hue} 55% 55%)`,
        display: "flex", alignItems: "center", justifyContent: "center",
        fontSize: "9px", fontWeight: 600, color: "#fff",
        flexShrink: 0,
      }}>
        {initials}
      </div>
    );
  }

  // ── Animated placeholder ───────────────────────────────────────────────────
  function KanbanPlaceholder({ targetHeight }) {
    const [height, setHeight] = React.useState(0);
    React.useLayoutEffect(() => {
      requestAnimationFrame(() => setHeight(targetHeight));
    }, [targetHeight]);

    return (
      <div style={{
        height: height + "px",
        borderRadius: "8px",
        background: "hsl(var(--accent))",
        border: "2px dashed hsl(var(--border)/0.6)",
        transition: "height 160ms cubic-bezier(0.25, 1, 0.5, 1)",
        flexShrink: 0,
      }} />
    );
  }

  // ── Main component ─────────────────────────────────────────────────────────
  function BuridanKanbanRoot({
    columns: initialColumns,
    onItemMove,
    rootClass,
    boardClass,
    columnClass,
    columnHeaderClass,
    columnTitleClass,
    columnCountClass,
    columnBodyClass,
    cardClass,
    cardDraggingClass,
    overlayCardClass,
  }) {
    const [columns, setColumns] = React.useState(() => parseColumns(initialColumns));

    React.useEffect(() => {
      setColumns(parseColumns(initialColumns));
    }, [initialColumns]);

    // drag state
    const [dragging,  setDragging]  = React.useState(null);
    const [overInfo,  setOverInfo]  = React.useState(null);
    const dragRef     = React.useRef(null);
    const draggingRef = React.useRef(null);
    const overlayRef  = React.useRef(null);
    const colsRef     = React.useRef(columns);
    const itemEls     = React.useRef({});

    React.useEffect(() => { colsRef.current   = columns;  }, [columns]);
    React.useEffect(() => { draggingRef.current = dragging; }, [dragging]);

    // ── hit detection ─────────────────────────────────────────────────────────
    function resolveDropTarget(cx, cy) {
      const cols = colsRef.current;
      let bestCol = null, bestIndex = 0, bestDist = Infinity;

      for (const [colId, items] of Object.entries(cols)) {
        for (let i = 0; i < items.length; i++) {
          const id = getId(items[i]);
          const el = itemEls.current[id];
          if (!el) continue;
          const rect = el.getBoundingClientRect();
          const midY = rect.top  + rect.height / 2;
          const midX = rect.left + rect.width  / 2;
          const dist = Math.hypot(cx - midX, cy - midY);
          if (dist < bestDist) {
            bestDist  = dist;
            bestCol   = colId;
            bestIndex = cy < midY ? i : i + 1;
          }
        }
      }

      if (!bestCol) {
        bestCol   = Object.keys(cols)[0] ?? null;
        bestIndex = 0;
      }

      return { colId: bestCol, index: bestIndex };
    }

    function resolveColumnUnderPointer(cx, cy) {
      const els = document.querySelectorAll("[data-buridan-col]");
      for (const el of els) {
        const r = el.getBoundingClientRect();
        if (cx >= r.left && cx <= r.right && cy >= r.top && cy <= r.bottom) {
          return el.dataset.buridanCol;
        }
      }
      return null;
    }

    // ── drag start ────────────────────────────────────────────────────────────
    function handleDragStart(e, itemId, colId, index) {
      e.preventDefault();
      const col   = colsRef.current[colId];
      const item  = col[index];
      const label = getLabel(item);
      const el    = itemEls.current[itemId];
      const itemHeight = el ? el.getBoundingClientRect().height : 42;

      setDragging({ itemId, fromCol: colId, fromIndex: index, item, label, itemHeight });
      setOverInfo({ colId, index });
      dragRef.current = { currentCol: colId, currentIndex: index };

      const ox = e.clientX + 14;
      const oy = e.clientY - itemHeight / 2;
      if (overlayRef.current) {
        overlayRef.current.style.transform =
          `translate(${ox}px,${oy}px) rotate(1.5deg) scale(1.03)`;
      }

      function onMove(ev) {
        if (overlayRef.current) {
          overlayRef.current.style.transform =
            `translate(${ev.clientX + 14}px,${ev.clientY - itemHeight / 2}px) rotate(1.5deg) scale(1.03)`;
        }

        const target = resolveDropTarget(ev.clientX, ev.clientY);
        const colUnder = resolveColumnUnderPointer(ev.clientX, ev.clientY);
        if (colUnder && colUnder !== target.colId) {
          const colItems = colsRef.current[colUnder] || [];
          if (colItems.length === 0) {
            target.colId  = colUnder;
            target.index  = 0;
          }
        }

        if (
          target.colId  !== dragRef.current.currentCol ||
          target.index  !== dragRef.current.currentIndex
        ) {
          dragRef.current.currentCol   = target.colId;
          dragRef.current.currentIndex = target.index;
          setOverInfo({ colId: target.colId, index: target.index });
        }
      }

      function onUp() {
        commitDrop();
        window.removeEventListener("pointermove", onMove);
        window.removeEventListener("pointerup",   onUp);
      }

      window.addEventListener("pointermove", onMove);
      window.addEventListener("pointerup",   onUp);
    }

    // ── commit drop ───────────────────────────────────────────────────────────
    function commitDrop() {
      const d = dragRef.current;
      if (!d) { setDragging(null); setOverInfo(null); return; }

      const { fromCol, fromIndex, itemId } = draggingRef.current;
      const { currentCol, currentIndex }   = d;
      dragRef.current = null;

      setColumns(prev => {
        const next = cloneColumns(prev);
        const [movedItem] = next[fromCol].splice(fromIndex, 1);
        const destIndex = (fromCol === currentCol && currentIndex > fromIndex)
          ? currentIndex - 1 : currentIndex;
        next[currentCol].splice(Math.min(destIndex, next[currentCol].length), 0, movedItem);
        return next;
      });

      if (onItemMove && fromCol !== currentCol) {
        onItemMove(JSON.stringify({
          item_id:     itemId,
          from_column: fromCol,
          from_index:  fromIndex,
          to_column:   currentCol,
          to_index:    currentIndex,
        }));
      }

      setDragging(null);
      setOverInfo(null);
    }

    const isDragging = !!dragging;

    // ── render ────────────────────────────────────────────────────────────────
    return (
      <div
        className={rootClass}
        style={{ userSelect: isDragging ? "none" : undefined }}
      >
        <div className={boardClass}>
          {Object.entries(columns).map(([colId, items]) => {
            const isOverCol = overInfo?.colId === colId;

            return (
              <div
                key={colId}
                data-buridan-col={colId}
                className={columnClass}
              >
                {/* column header */}
                <div className={columnHeaderClass}>
                  <span className={columnTitleClass}>{colId}</span>
                  <span className={columnCountClass}>{items.length}</span>
                </div>

                {/* items */}
                <div className={columnBodyClass}>
                  {isOverCol && overInfo.index === 0 && dragging && (
                    <KanbanPlaceholder
                      key={"ph-" + colId + "-0"}
                      targetHeight={dragging.itemHeight}
                    />
                  )}

                  {items.map((item, idx) => {
                    const id             = getId(item);
                    const isBeingDragged = dragging?.itemId === id;
                    const showPhAfter    = isOverCol && overInfo.index === idx + 1 && !isBeingDragged;

                    return (
                      <React.Fragment key={id}>
                        <KanbanCard
                          item={item}
                          className={isBeingDragged ? cardClass + " " + cardDraggingClass : cardClass}
                          ref={el => {
                            if (el) itemEls.current[id] = el;
                            else delete itemEls.current[id];
                          }}
                          onPointerDown={e => handleDragStart(e, id, colId, idx)}
                          style={{
                            transition: isDragging
                              ? "transform 160ms cubic-bezier(0.25,1,0.5,1), opacity 150ms ease, box-shadow 150ms ease"
                              : undefined,
                          }}
                        />
                        {showPhAfter && dragging && (
                          <KanbanPlaceholder
                            key={"ph-" + colId + "-" + (idx + 1)}
                            targetHeight={dragging.itemHeight}
                          />
                        )}
                      </React.Fragment>
                    );
                  })}

                  {isOverCol && overInfo.index >= items.length && dragging && (
                    <KanbanPlaceholder
                      key={"ph-" + colId + "-end"}
                      targetHeight={dragging.itemHeight}
                    />
                  )}
                </div>
              </div>
            );
          })}
        </div>

        {/* GPU-composited drag overlay */}
        {isDragging && (
          <div
            ref={overlayRef}
            style={{
              position: "fixed", top: 0, left: 0,
              pointerEvents: "none", zIndex: 9999,
              minWidth: "220px", maxWidth: "320px",
              willChange: "transform",
              transform: "translate(-9999px,-9999px)",
            }}
          >
            <KanbanCard item={dragging.item} className={overlayCardClass} />
          </div>
        )}
      </div>
    );
  }

  // forward ref support for KanbanCard so itemEls ref works
  const KanbanCard = React.forwardRef(function KanbanCard({ item, className, style, onPointerDown }, ref) {
    const isString = typeof item === "string";

    if (isString) {
      return (
        <div ref={ref} className={className} style={style} onPointerDown={onPointerDown}>
          <span style={{ fontSize: "13px", fontWeight: 500, lineHeight: 1.4 }}>{item}</span>
        </div>
      );
    }

    const { title, label, description, priority, assignee, due_date, dueDate } = item;
    const displayTitle = title ?? label ?? "";
    const displayDue   = due_date ?? dueDate ?? null;
    const pCfg         = priority ? PRIORITY[priority.toLowerCase()] : null;

    return (
      <div ref={ref} className={className} style={style} onPointerDown={onPointerDown}>
        {/* title + badge */}
        <div style={{
          display: "flex", alignItems: "flex-start",
          justifyContent: "space-between", gap: "8px",
          marginBottom: (description || assignee || displayDue) ? "6px" : "0",
        }}>
          <span style={{ fontSize: "13px", fontWeight: 500, lineHeight: 1.4, flex: 1 }}>
            {displayTitle}
          </span>
          {pCfg && (
            <span style={{
              fontSize: "10px", fontWeight: 600, letterSpacing: "0.02em",
              padding: "2px 6px", borderRadius: "4px", whiteSpace: "nowrap", flexShrink: 0,
              background: pCfg.bg, color: pCfg.color, border: `1px solid ${pCfg.border}`,
            }}>
              {pCfg.label}
            </span>
          )}
        </div>

        {/* description */}
        {description && (
          <p style={{
            fontSize: "11px", color: "hsl(var(--muted-foreground))",
            lineHeight: 1.5, marginBottom: "8px",
            display: "-webkit-box", WebkitLineClamp: 2,
            WebkitBoxOrient: "vertical", overflow: "hidden",
          }}>
            {description}
          </p>
        )}

        {/* footer */}
        {(assignee || displayDue) && (
          <div style={{
            display: "flex", alignItems: "center",
            justifyContent: "space-between", gap: "8px",
            paddingTop: "8px",
            borderTop: "1px solid hsl(var(--border)/0.6)",
          }}>
            {assignee ? (
              <div style={{ display: "flex", alignItems: "center", gap: "5px", minWidth: 0 }}>
                <Avatar name={assignee} />
                <span style={{
                  fontSize: "11px", color: "hsl(var(--muted-foreground))",
                  overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap",
                }}>
                  {assignee}
                </span>
              </div>
            ) : <div />}
            {displayDue && (
              <time style={{
                fontSize: "10px", color: "hsl(var(--muted-foreground))",
                whiteSpace: "nowrap", flexShrink: 0,
              }}>
                {displayDue}
              </time>
            )}
          </div>
        )}
      </div>
    );
  });

  window.BuridanKanbanRoot = BuridanKanbanRoot;
})();
"""


class BuridanKanban(Component):
    """
    A self-contained Kanban board with rich card rendering and smooth drag-and-drop.

    Column data structure — simple strings:
        {
            "To Do":       ["Task A", "Task B"],
            "In Progress": ["Task C"],
            "Done":        [],
        }

    Column data structure — rich cards:
        {
            "To Do": [
                {
                    "id":          "t1",               # required
                    "title":       "Fix login bug",     # required
                    "priority":    "high",              # optional: "high" | "medium" | "low"
                    "description": "OAuth flow broken", # optional
                    "assignee":    "Ahmad Salim",       # optional — renders avatar + name
                    "due_date":    "Jan 10, 2025",      # optional
                },
            ],
        }

    Event handlers:
        on_item_move — fired on cross-column moves.
                       Receives JSON string:
                       {"item_id", "from_column", "from_index", "to_column", "to_index"}
    """

    tag = "BuridanKanbanRoot"
    is_default = False

    columns: Var[Any]

    root_class: Var[str]
    board_class: Var[str]
    column_class: Var[str]
    column_header_class: Var[str]
    column_title_class: Var[str]
    column_count_class: Var[str]
    column_body_class: Var[str]
    card_class: Var[str]
    card_dragging_class: Var[str]
    overlay_card_class: Var[str]

    on_item_move: EventHandler[passthrough_event_spec(str)]

    def add_custom_code(self) -> list[str]:
        return [BURIDAN_KANBAN_JS]

    def add_imports(self) -> dict:
        return {"react": ImportVar(tag="React", is_default=True)}

    @classmethod
    def create(cls, *children, **props):
        props["root_class"] = cn(ClassNames.ROOT, props.pop("root_class", ""))
        props["board_class"] = cn(ClassNames.BOARD, props.pop("board_class", ""))
        props["column_class"] = cn(ClassNames.COLUMN, props.pop("column_class", ""))
        props["column_header_class"] = cn(
            ClassNames.COLUMN_HEADER, props.pop("column_header_class", "")
        )
        props["column_title_class"] = cn(
            ClassNames.COLUMN_TITLE, props.pop("column_title_class", "")
        )
        props["column_count_class"] = cn(
            ClassNames.COLUMN_COUNT, props.pop("column_count_class", "")
        )
        props["column_body_class"] = cn(
            ClassNames.COLUMN_BODY, props.pop("column_body_class", "")
        )
        props["card_class"] = cn(ClassNames.CARD, props.pop("card_class", ""))
        props["card_dragging_class"] = cn(
            ClassNames.CARD_DRAGGING, props.pop("card_dragging_class", "")
        )
        props["overlay_card_class"] = cn(
            ClassNames.OVERLAY_CARD, props.pop("overlay_card_class", "")
        )
        return super().create(*children, **props)


kanban = BuridanKanban.create
