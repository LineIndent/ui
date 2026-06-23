"""Custom GitHub-style heatmap component for Reflex — no external dependencies."""

from typing import Any

from reflex.components.component import Component
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from ..utils.twmerge import cn


class ClassNames:
    ROOT = "w-full overflow-x-auto pr-1"
    WRAPPER = "inline-block"


BURIDAN_HEATMAP_JS = """
if (typeof window !== "undefined") { (function () {

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
    if (isNaN(curr.getTime()) || isNaN(endD.getTime())) return days;
    let safety = 0;
    while (curr <= endD && safety++ < 1500) {
      days.push(formatDate(curr));
      curr.setDate(curr.getDate() + 1);
    }
    return days;
  }

  function padToWeekStart(days) {
    const firstDow = days.length > 0 ? parseDate(days[0]).getDay() : 0;
    const safeDow  = Number.isFinite(firstDow) ? firstDow : 0;
    const padding  = safeDow > 0 ? new Array(safeDow).fill(null) : [];
    return padding.concat(days);
  }

  function chunkByWeek(days) {
    const weeks = [];
    for (let i = 0; i < days.length; i += 7) weeks.push(days.slice(i, i + 7));
    return weeks;
  }

  function getMonthLabel(week) {
    const last = week.slice().reverse().find(Boolean);
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
      const maxValue    = data.reduce((max, d) => d.value > max ? d.value : max, 0);
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
})(); }

// SSR-safe wrapper — always defined, renders nothing on server
function BuridanHeatmapSSR(props) {
  const [mounted, setMounted] = React.useState(false);
  React.useEffect(() => { setMounted(true); }, []);
  if (!mounted || typeof BuridanHeatmapRoot === "undefined") return null;
  return React.createElement(BuridanHeatmapRoot, props);
}
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

    tag = "BuridanHeatmapSSR"
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
