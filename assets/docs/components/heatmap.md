

# Heatmap

A heatmap component to visualize data density over time.

> **Note:** The Heatmap component is a fully custom implementation with no external dependencies. It's a JavaScript component with a Python API used in Reflex.

# Installation

Copy the following code into your app directory.

### CLI

```bash
buridan add component heatmap
```

### Manual Installation

```python
"""Custom GitHub-style heatmap component for Reflex — no external dependencies."""

from typing import Any

from reflex.components.component import Component
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..utils.twmerge import cn


class ClassNames:
    ROOT = "w-full overflow-x-auto pr-2"
    WRAPPER = "inline-block"


BURIDAN_HEATMAP_JS = """
(function () {

  // ── date helpers ───────────────────────────────────────────────────────────
  function formatDate(date) {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, "0");
    const d = String(date.getDate()).padStart(2, "0");
    return `${y}-${m}-${d}`;
  }

  function parseDate(str) {
    return new Date(str + "T00:00:00");
  }

  function getAllDays(start, end) {
    const days = [];
    const curr = parseDate(start);
    const endD = parseDate(end);
    while (curr <= endD) {
      days.push(formatDate(curr));
      curr.setDate(curr.getDate() + 1);
    }
    return days;
  }

  function padToWeekStart(days) {
    const firstDow = parseDate(days[0]).getDay(); // 0=Sun
    const padding  = new Array(firstDow).fill(null);
    return [...padding, ...days];
  }

  function chunkByWeek(days) {
    const weeks = [];
    for (let i = 0; i < days.length; i += 7) weeks.push(days.slice(i, i + 7));
    return weeks;
  }

  function getMonthLabel(week) {
    const last = [...week].reverse().find(Boolean);
    return last
      ? parseDate(last).toLocaleString("default", { month: "short" })
      : null;
  }

  // ── color helpers ──────────────────────────────────────────────────────────
  function defaultColorMap(value, max, colorCount) {
    if (colorCount <= 0 || max <= 0 || value <= 0) return 0;
    const idx = Math.ceil((value / max) * (colorCount - 1));
    return Math.min(Math.max(idx, 0), colorCount - 1);
  }

  function interpolateRgb(value, max, minColor, maxColor, mode) {
    if (value <= 0 || max <= 0) return "var(--secondary)";
    let t = value / max;
    if (mode === "sqrt") t = Math.sqrt(t);
    else if (mode === "log") t = Math.log10(value + 1) / Math.log10(max + 1);
    t = Math.min(Math.max(t, 0), 1);

    function hex(c) { return parseInt(c, 16); }
    const s = { r: hex(minColor.slice(1,3)), g: hex(minColor.slice(3,5)), b: hex(minColor.slice(5,7)) };
    const e = { r: hex(maxColor.slice(1,3)), g: hex(maxColor.slice(3,5)), b: hex(maxColor.slice(5,7)) };
    const r = Math.round(s.r + (e.r - s.r) * t);
    const g = Math.round(s.g + (e.g - s.g) * t);
    const b = Math.round(s.b + (e.b - s.b) * t);
    return `rgb(${r},${g},${b})`;
  }

  const DEFAULT_COLOR_SCALE = [
    "var(--secondary)", // empty
    "#9be9a8",          // green-200
    "#40c463",          // green-400
    "#30a14e",          // green-600
    "#216e39",          // green-800
  ];

  const DOW_LABELS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

  // ── Tooltip (Base UI) ──────────────────────────────────────────────────────
  // We use a plain JS tooltip built on top of Floating UI / manual positioning
  // since we can't easily reference the Reflex tooltip component from inline JS.
  // Rendered as a styled div that follows the hovered cell.
  function HeatmapTooltip({ text, visible, x, y }) {
    if (!visible) return null;
    return (
      <div
        className="bg-secondary dark:bg-card border border-border text-foreground"
        style={{
          position:      "fixed",
          left:          x + "px",
          top:           (y - 8) + "px",
          transform:     "translate(-50%, -100%)",
          borderRadius:  "6px",
          padding:       "4px 8px",
          fontSize:      "11px",
          lineHeight:    1.5,
          pointerEvents: "none",
          zIndex:        9999,
          whiteSpace:    "nowrap",
          boxShadow:     "0 2px 8px rgb(0 0 0 / 0.12)",
        }}
      >
        {text}
      </div>
    );
  }

  // ── Main component ─────────────────────────────────────────────────────────
  function BuridanHeatmapRoot({
    data: rawData,
    startDate,
    endDate,
    cellSize,
    gap,
    colorMode,
    colorScale: rawColorScale,
    minColor,
    maxColor,
    interpolation,
    showDow,
    showMonths,
    valueLabel,
    rootClass,
    wrapperClass,
  }) {
    // ── parse props ──────────────────────────────────────────────────────────
    const data = React.useMemo(() => {
      if (!rawData) return [];
      if (typeof rawData === "string") {
        try { return JSON.parse(rawData); } catch { return []; }
      }
      return rawData;
    }, [rawData]);

    const colorScale = React.useMemo(() => {
      if (!rawColorScale) return DEFAULT_COLOR_SCALE;
      if (typeof rawColorScale === "string") {
        try { return JSON.parse(rawColorScale); } catch { return DEFAULT_COLOR_SCALE; }
      }
      return rawColorScale;
    }, [rawColorScale]);

    const size    = cellSize  || 14;
    const gapPx   = gap       || 3;
    const mode    = colorMode || "discrete";
    const vLabel  = valueLabel || "contributions";
    const showDowF    = showDow    === false || showDow    === "false" ? false : true;
    const showMonthsF = showMonths === false || showMonths === "false" ? false : true;

    // ── build grid ───────────────────────────────────────────────────────────
    const { weeks, monthLabels, maxValue, valueByDate } = React.useMemo(() => {
      const valueByDate = new Map(data.map(({ date, value }) => [date, value]));
      const maxValue    = Math.max(...data.map(d => d.value), 0);
      const days        = getAllDays(startDate, endDate);
      const padded      = padToWeekStart(days);
      const weeks       = chunkByWeek(padded);

      const monthLabels = weeks.map((week, i) => {
        const label     = getMonthLabel(week);
        const prevLabel = i > 0 ? getMonthLabel(weeks[i - 1]) : null;
        return label !== prevLabel ? label : null;
      });

      return { weeks, monthLabels, maxValue, valueByDate };
    }, [data, startDate, endDate]);

    // ── color ────────────────────────────────────────────────────────────────
    function getCellColor(value) {
      if (mode === "interpolate") {
        return interpolateRgb(
          value, maxValue,
          minColor  || "#9be9a8",
          maxColor  || "#216e39",
          interpolation || "linear",
        );
      }
      // discrete
      const scale = colorScale.length > 0 ? colorScale : DEFAULT_COLOR_SCALE;
      return scale[defaultColorMap(value, maxValue, scale.length)];
    }

    // ── tooltip state ────────────────────────────────────────────────────────
    const [tooltip, setTooltip] = React.useState({ visible: false, text: "", x: 0, y: 0 });

    function showTooltip(e, day, value) {
      const rect = e.currentTarget.getBoundingClientRect();
      const date = parseDate(day);
      const dateStr = date.toLocaleDateString("default", {
        weekday: "short", month: "short", day: "numeric", year: "numeric"
      });
      setTooltip({
        visible: true,
        text:    `${value} ${vLabel} · ${dateStr}`,
        x:       rect.left + rect.width  / 2,
        y:       rect.top,
      });
    }

    function hideTooltip() {
      setTooltip(t => ({ ...t, visible: false }));
    }

    // ── layout math ──────────────────────────────────────────────────────────
    const dowColWidth  = showDowF    ? Math.min(12, size) * 2.8 : 0;
    const headerHeight = showMonthsF ? size                     : 0;
    const fontSize     = Math.min(11, size);

    const totalWidth  = dowColWidth + weeks.length * (size + gapPx) - gapPx;
    const totalHeight = headerHeight + 7 * (size + gapPx) - gapPx;

    // ── render ───────────────────────────────────────────────────────────────
    return (
      <div className={rootClass}>
        <div className={wrapperClass}>
          <svg
            width={totalWidth}
            height={totalHeight + (showMonths ? gapPx : 0)}
            style={{ display: "block", overflow: "visible", paddingLeft: "4px" }}
          >
            {/* month labels */}
            {showMonthsF && weeks.map((_, wi) =>
              monthLabels[wi] ? (
                <text
                  key={"m-" + wi}
                  x={dowColWidth + wi * (size + gapPx) + size / 2}
                  y={fontSize}
                  fontSize={fontSize}
                  fill="var(--foreground)"
                  textAnchor="middle"
                >
                  {monthLabels[wi]}
                </text>
              ) : null
            )}

            {/* day-of-week labels */}
            {showDowF && DOW_LABELS.map((label, di) =>
              [1, 3, 5].includes(di) ? (
                <text
                  key={"d-" + di}
                  x={dowColWidth - gapPx * 2}
                  y={headerHeight + di * (size + gapPx) + size * 0.75}
                  fontSize={fontSize}
                  fill="var(--foreground)"
                  textAnchor="end"
                >
                  {label}
                </text>
              ) : null
            )}

            {/* cells */}
            {weeks.map((week, wi) =>
              week.map((day, di) => {
                const cx = dowColWidth + wi * (size + gapPx);
                const cy = headerHeight + di * (size + gapPx);

                const radius = Math.max(2, size * 0.28);

                if (!day) {
                  return (
                    <rect
                      key={`e-${wi}-${di}`}
                      x={cx} y={cy}
                      width={size} height={size}
                      rx={radius} ry={radius}
                      fill={getCellColor(0)}
                    />
                  );
                }

                const value = Math.max(0, valueByDate.get(day) ?? 0);
                const color = getCellColor(value);

                return (
                  <rect
                    key={`c-${wi}-${di}`}
                    x={cx} y={cy}
                    width={size} height={size}
                    rx={radius} ry={radius}
                    fill={color}
                    style={{ cursor: "pointer", transition: "opacity 100ms" }}
                    onMouseEnter={e => showTooltip(e, day, value)}
                    onMouseLeave={hideTooltip}
                  />
                );
              })
            )}
          </svg>
        </div>

        <HeatmapTooltip
          visible={tooltip.visible}
          text={tooltip.text}
          x={tooltip.x}
          y={tooltip.y}
        />
      </div>
    );
  }

  window.BuridanHeatmapRoot = BuridanHeatmapRoot;
})();
"""


class BuridanHeatmap(Component):
    """
    A GitHub-style activity heatmap component.

    Data structure:
        data = [
            {"date": "2025-01-01", "value": 3},
            {"date": "2025-01-15", "value": 7},
        ]

    Props:
        data        — list of {"date": "YYYY-MM-DD", "value": int}
        start_date  — "YYYY-MM-DD" string, start of the range
        end_date    — "YYYY-MM-DD" string, end of the range
        cell_size   — int, size of each cell in px (default 14)
        gap         — int, gap between cells in px (default 3)
        color_mode  — "discrete" | "interpolate" (default "discrete")
        color_scale — list of hex color strings for discrete mode
                      (default: GitHub green scale, 5 levels)
        min_color   — hex string for interpolate mode low end (default "#9be9a8")
        max_color   — hex string for interpolate mode high end (default "#216e39")
        interpolation — "linear" | "sqrt" | "log" (default "linear")
        show_dow    — bool, show day-of-week labels (default True)
        show_months — bool, show month labels (default True)
        value_label — string appended to tooltip count (default "contributions")
    """

    tag = "BuridanHeatmapRoot"
    is_default = False

    data: Var[Any]
    start_date: Var[str]
    end_date: Var[str]
    cell_size: Var[int]
    gap: Var[int]
    color_mode: Var[str]
    color_scale: Var[Any]
    min_color: Var[str]
    max_color: Var[str]
    interpolation: Var[str]
    show_dow: Var[bool]
    show_months: Var[bool]
    value_label: Var[str]
    root_class: Var[str]
    wrapper_class: Var[str]

    def add_custom_code(self) -> list[str]:
        return [BURIDAN_HEATMAP_JS]

    def add_imports(self) -> dict:
        return {"react": ImportVar(tag="React", is_default=True)}

    @classmethod
    def create(cls, *children, **props):
        props.setdefault("show_dow", True)
        props.setdefault("show_months", True)
        props.setdefault("color_mode", "discrete")
        props.setdefault("cell_size", 14)
        props.setdefault("gap", 3)
        props["root_class"] = cn(ClassNames.ROOT, props.pop("root_class", ""))
        props["wrapper_class"] = cn(ClassNames.WRAPPER, props.pop("wrapper_class", ""))
        return super().create(*children, **props)


heatmap = BuridanHeatmap.create
```


# Usage


```python
from components.ui.heatmap import heatmap
```


# Anatomy 
Use the following composition to build a `Heatmap` component.


```python
heatmap()
```


# Examples

## GitHub-Style HeatMap 

Classic GitHub contribution graph — discrete mode, default green scale.


```python
def heatmap_github():
    data = []
    from datetime import date, timedelta

    d = date(2025, 1, 1)
    while d <= date(2025, 12, 31):
        if random.random() > 0.3:
            data.append({"date": str(d), "value": random.randint(1, 20)})
        d += timedelta(days=1)

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-11-31",
        color_mode="discrete",
        value_label="contributions",
        cell_size=14,
        root_class="scrollbar-none",
    )
```


## Interpolated HeatMap 

Set the `interpolation` prop to `linear` and pass in custom colors for continuous data visualization.


```python
def heatmap_blue_linear():
    data = [
        {"date": "2025-01-05", "value": 2},
        {"date": "2025-01-12", "value": 9},
        {"date": "2025-02-01", "value": 4},
        {"date": "2025-02-20", "value": 15},
        {"date": "2025-03-10", "value": 6},
        {"date": "2025-04-04", "value": 18},
        {"date": "2025-05-15", "value": 3},
        {"date": "2025-06-01", "value": 11},
        {"date": "2025-07-22", "value": 20},
        {"date": "2025-08-08", "value": 7},
        {"date": "2025-09-30", "value": 14},
        {"date": "2025-10-10", "value": 5},
        {"date": "2025-11-11", "value": 19},
        {"date": "2025-12-25", "value": 1},
    ]

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-12-31",
        color_mode="interpolate",
        min_color="#dbeafe",
        max_color="#1d4ed8",
        interpolation="linear",
        value_label="events",
        cell_size=14,
        root_class="scrollbar-none",
    )
```


## Square Root HeatMap 

Set the `interpolation` prop to `sqrt` and pass in custom colors. `sqrt` scaling makes low values more visible — good when most activity is sparse.


```python
def heatmap_red_sqrt():
    data = [
        {"date": "2025-01-03", "value": 1},
        {"date": "2025-01-10", "value": 50},
        {"date": "2025-02-14", "value": 3},
        {"date": "2025-03-01", "value": 100},
        {"date": "2025-04-20", "value": 2},
        {"date": "2025-05-05", "value": 75},
        {"date": "2025-06-15", "value": 10},
        {"date": "2025-07-04", "value": 90},
        {"date": "2025-08-12", "value": 5},
        {"date": "2025-09-09", "value": 40},
        {"date": "2025-10-31", "value": 8},
        {"date": "2025-11-25", "value": 60},
        {"date": "2025-12-01", "value": 20},
    ]

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-12-31",
        color_mode="interpolate",
        min_color="#fee2e2",
        max_color="#991b1b",
        interpolation="sqrt",
        value_label="errors",
        cell_size=14,
        root_class="scrollbar-none",
    )
```


## Discrete Color Mode 

Set the `color_mode` prop to `discrete` with a custom 5-level purple color scale. Pass any list of hex colors to color_scale — more levels = finer granularity.


```python
def heatmap_purple_discrete():
    data = [
        {"date": "2025-01-07", "value": 1},
        {"date": "2025-01-14", "value": 2},
        {"date": "2025-01-21", "value": 3},
        {"date": "2025-01-28", "value": 4},
        {"date": "2025-02-04", "value": 5},
        {"date": "2025-02-11", "value": 3},
        {"date": "2025-03-01", "value": 1},
        {"date": "2025-03-15", "value": 4},
        {"date": "2025-04-10", "value": 2},
        {"date": "2025-05-20", "value": 5},
        {"date": "2025-06-30", "value": 3},
        {"date": "2025-09-01", "value": 4},
        {"date": "2025-10-15", "value": 2},
        {"date": "2025-11-20", "value": 5},
        {"date": "2025-12-10", "value": 1},
    ]

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-12-31",
        color_mode="discrete",
        color_scale=["#f3e8ff", "#d8b4fe", "#a855f7", "#7e22ce", "#3b0764"],
        value_label="deploys",
        cell_size=14,
        root_class="scrollbar-none",
    )
```


## Cell Size

Set the `cell_size` prop to a number to change cell size. Setting the `interpolation` to `log` is ideal when a few extreme values dominate — compresses the high end.


```python
def heatmap_large_cells():
    data = [
        {"date": "2025-10-01", "value": 1},
        {"date": "2025-10-02", "value": 500},
        {"date": "2025-10-03", "value": 10},
        {"date": "2025-10-06", "value": 1000},
        {"date": "2025-10-07", "value": 5},
        {"date": "2025-10-08", "value": 250},
        {"date": "2025-10-09", "value": 3},
        {"date": "2025-10-10", "value": 750},
        {"date": "2025-10-13", "value": 50},
        {"date": "2025-10-14", "value": 900},
        {"date": "2025-10-15", "value": 20},
        {"date": "2025-10-16", "value": 600},
        {"date": "2025-10-17", "value": 8},
        {"date": "2025-10-20", "value": 400},
        {"date": "2025-10-21", "value": 2},
        {"date": "2025-10-22", "value": 800},
        {"date": "2025-10-23", "value": 15},
        {"date": "2025-10-24", "value": 350},
        {"date": "2025-10-27", "value": 100},
        {"date": "2025-10-28", "value": 700},
        {"date": "2025-10-29", "value": 30},
        {"date": "2025-10-30", "value": 950},
        {"date": "2025-10-31", "value": 12},
    ]

    return heatmap(
        data=data,
        start_date="2025-10-01",
        end_date="2025-10-31",
        color_mode="interpolate",
        min_color="#f0fdf4",
        max_color="#14532d",
        interpolation="log",
        value_label="requests",
        cell_size=20,
        gap=4,
        root_class="scrollbar-none",
    )
```


## Minimal HeatMap

Set the `show_dow` and `show_months` props to `False` and lower the `cell_size` to get a compact, minimal heatmap. Useful as a sparkline-style indicator embedded in a dashboard card.


```python
def heatmap_compact():
    data = [
        {
            "date": f"2025-{str(m).zfill(2)}-{str(d).zfill(2)}",
            "value": random.randint(0, 10),
        }
        for m in range(1, 13)
        for d in range(1, 28)
    ]

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-12-31",
        color_mode="discrete",
        show_dow=False,
        show_months=False,
        cell_size=10,
        gap=2,
        value_label="sales",
        root_class="scrollbar-none",
    )
```


# API Reference

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `data` | `list[dict]` | — | **Required.** List of `{"date": "YYYY-MM-DD", "value": int}` entries. Dates not in the list render as empty cells. |
| `start_date` | `str` | — | **Required.** Start of the date range in `YYYY-MM-DD` format. |
| `end_date` | `str` | — | **Required.** End of the date range in `YYYY-MM-DD` format. |
| `color_mode` | `str` | `"discrete"` | Color strategy. `"discrete"` maps values to a fixed color scale. `"interpolate"` blends smoothly between `min_color` and `max_color`. |
| `color_scale` | `list[str]` | GitHub green scale | Discrete mode only. List of hex color strings ordered from empty → max intensity. The first entry is always used for zero-value cells. |
| `min_color` | `str` | `"#9be9a8"` | Interpolate mode only. Hex color for the lowest non-zero value. |
| `max_color` | `str` | `"#216e39"` | Interpolate mode only. Hex color for the highest value. |
| `interpolation` | `str` | `"linear"` | Interpolate mode only. Scaling function applied before color blending. `"linear"` is uniform. `"sqrt"` makes low values more visible. `"log"` compresses high-end outliers. |
| `cell_size` | `int` | `14` | Width and height of each cell in pixels. Also scales the border radius and font size proportionally. |
| `gap` | `int` | `3` | Gap between cells in pixels. |
| `show_dow` | `bool` | `True` | Whether to show Mon / Wed / Fri labels on the left axis. |
| `show_months` | `bool` | `True` | Whether to show month labels along the top axis. |
| `value_label` | `str` | `"contributions"` | Word appended to the count in the tooltip, e.g. `"commits"` → `"3 commits · Mon Jan 1 2025"`. |
| `root_class` | `str` | `"w-full overflow-x-auto"` | Tailwind classes applied to the outermost div. Controls scroll and outer layout. |
| `wrapper_class` | `str` | `"inline-block"` | Tailwind classes applied to the inner SVG wrapper div. |

## Data format

```python
data = [
    {"date": "2025-01-01", "value": 3},
    {"date": "2025-06-15", "value": 12},
]
```

Dates must be strings in `YYYY-MM-DD` format. Values must be non-negative integers.
Dates outside the `start_date`/`end_date` range are ignored. Dates within the range
that are missing from `data` render as empty cells using `var(--secondary)`.

## Color Modes

## Discrete

Values are bucketed into `len(color_scale)` levels using a linear scale from `0` to `max(value)`.
The default scale is a 5-level GitHub-style green:

```python
color_scale = [
    "var(--secondary)",  # 0  — empty
    "#9be9a8",           # 1  — low
    "#40c463",           # 2
    "#30a14e",           # 3
    "#216e39",           # 4  — high
]
```

Pass any number of hex strings to customize. More levels give finer granularity.

## Interpolate

Colors are blended smoothly between `min_color` and `max_color` using the chosen `interpolation` function.
Zero-value cells always use `var(--secondary)` regardless of `min_color`.

| Interpolation | Best for |
|---------------|----------|
| `"linear"` | Evenly distributed values |
| `"sqrt"` | Sparse data where low values need visibility |
| `"log"` | Data with extreme outliers that would wash out lower values |
