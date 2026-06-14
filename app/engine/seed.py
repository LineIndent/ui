import json

import reflex as rx

from app.registry.colors import COLOR_THEMES
from app.registry.fonts import FONT_REGISTRY
from app.registry.radii import RADIUS_OPTIONS
from app.registry.styles import STYLE_REGISTRY
from app.registry.themes import BASE_THEMES


def seed_engine() -> rx.Script:
    style_registry_js = json.dumps(STYLE_REGISTRY)
    base_themes_js = json.dumps(BASE_THEMES)
    color_themes_js = json.dumps(COLOR_THEMES)
    font_registry_js = json.dumps(FONT_REGISTRY)
    radius_options_js = json.dumps(RADIUS_OPTIONS)

    return rx.script(f"""
    function hashStringToInt(str) {{
        let hash = 0;
        for (let i = 0; i < str.length; i++) {{
            hash = (hash << 5) - hash + str.charCodeAt(i);
            hash |= 0;
        }}
        return hash >>> 0;
    }}

    function mulberry32(seed) {{
        return function() {{
            let t = (seed += 0x6D2B79F5);
            t = Math.imul(t ^ (t >>> 15), t | 1);
            t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
            return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
        }};
    }}

    const STYLE_REGISTRY = {style_registry_js};
    const BASE_THEMES    = {base_themes_js};
    const COLOR_THEMES   = {color_themes_js};
    const FONT_REGISTRY  = {font_registry_js};
    const RADIUS_OPTIONS = {radius_options_js};
    const CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

    // Flatten a shadcn cssVars object → prefixed CSS var dict
    // e.g. {{ primary: "oklch(...)" }} → {{ "--primary": "oklch(...)" }}
    function flattenVars(obj) {{
        const out = {{}};
        for (const [k, v] of Object.entries(obj)) {{
            out[k === 'radius' ? '--radius' : '--' + k] = v;
        }}
        return out;
    }}

    function toBase62(n, len) {{
        let res = "";
        for (let i = 0; i < len; i++) {{
            res += CHARS[n % 62];
            n = Math.floor(n / 62);
        }}
        return res;
    }}

    function fromBase62(s) {{
        let n = 0;
        for (let i = s.length - 1; i >= 0; i--) {{
            n = n * 62 + CHARS.indexOf(s[i]);
        }}
        return n;
    }}

    function encodeConfig(theme) {{
        const bIdx  = BASE_THEMES.findIndex(b => b.id === theme['__base_id']);
        const cIdx  = theme['__color_id'] ? COLOR_THEMES.findIndex(c => c.id === theme['__color_id']) + 1 : 0;
        const chIdx = theme['__chart_id'] ? COLOR_THEMES.findIndex(c => c.id === theme['__chart_id']) + 1 : 0;
        const sIdx  = STYLE_REGISTRY.findIndex(s => s.id === theme['__style_id']);
        const fIdx  = FONT_REGISTRY.findIndex(f => f.id === theme['__font_id']);
        const rIdx  = RADIUS_OPTIONS.findIndex(r => r[1] === theme['--radius']);

        if (bIdx === -1 || sIdx === -1 || fIdx === -1 || rIdx === -1) return null;

        // Default state special case
        if (bIdx === 0 && cIdx === 0 && chIdx === 0 && sIdx === 0 && fIdx === 0 && rIdx === 2) return "b0";

        // State space: 6 * 11 * 11 * 5 * 5 * 4 = 72600
        let n = (((((bIdx * 11 + cIdx) * 11 + chIdx) * 5 + sIdx) * 5 + fIdx) * 4 + rIdx);

        // Encode as 9 chars: [Base62(N, 4)] + [Base62(Checksum(N), 5)]
        const checksum = (n * 12345) % 916132832; // 62^5
        return toBase62(n, 4) + toBase62(checksum, 5);
    }}

    function decodeSeed(seed) {{
        if (!seed) return null;
        if (seed === "b0") {{
            return {{ baseId: BASE_THEMES[0].id, colorId: null, chartId: null, styleId: STYLE_REGISTRY[0].id, fontId: FONT_REGISTRY[0].id, radius: RADIUS_OPTIONS[2][1] }};
        }}
        if (seed.length !== 9) return null;

        const n = fromBase62(seed.substring(0, 4));
        const checksum = fromBase62(seed.substring(4));

        if (checksum === (n * 12345) % 916132832 && n < 72600) {{
            let temp = n;
            const rIdx = temp % 4; temp = Math.floor(temp / 4);
            const fIdx = temp % 5; temp = Math.floor(temp / 5);
            const sIdx = temp % 5; temp = Math.floor(temp / 5);
            const chIdx = temp % 11; temp = Math.floor(temp / 11);
            const cIdx = temp % 11; temp = Math.floor(temp / 11);
            const bIdx = temp % 6;

            return {{
                baseId:  BASE_THEMES[bIdx].id,
                colorId: cIdx > 0 ? COLOR_THEMES[cIdx - 1].id : null,
                chartId: chIdx > 0 ? COLOR_THEMES[chIdx - 1].id : null,
                styleId: STYLE_REGISTRY[sIdx].id,
                fontId:  FONT_REGISTRY[fIdx].id,
                radius:  RADIUS_OPTIONS[rIdx][1]
            }};
        }}
        return null;
    }}

    function generateFromSeed(seedString, darkMode) {{
        let config = decodeSeed(seedString);
        if (!config) {{
            const rand = mulberry32(hashStringToInt(seedString));
            config = {{
                baseId:  BASE_THEMES[Math.floor(rand() * BASE_THEMES.length)].id,
                colorId: (function(r){{ let i = Math.floor(r * 11); return i === 0 ? null : COLOR_THEMES[i-1].id; }})(rand()),
                chartId: (function(r){{ let i = Math.floor(r * 11); return i === 0 ? null : COLOR_THEMES[i-1].id; }})(rand()),
                styleId: STYLE_REGISTRY[Math.floor(rand() * STYLE_REGISTRY.length)].id,
                fontId:  FONT_REGISTRY[Math.floor(rand() * FONT_REGISTRY.length)].id,
                radius:  RADIUS_OPTIONS[Math.floor(rand() * RADIUS_OPTIONS.length)][1]
            }};
        }}

        const theme = rebuildTheme({{
            ...config,
            darkMode: darkMode
        }});

        return {{
            ...theme,
            "__seed": seedString,
            "__dark": darkMode,
        }};
    }}

    function rebuildTheme(config) {{
        const {{ baseId, colorId, chartId, styleId, fontId, radius, darkMode }} = config;
        const base = BASE_THEMES.find(b => b.id === baseId);
        if (!base) return {{}};

        const baseVars = flattenVars(darkMode ? base.dark : base.light);
        let theme = {{ ...baseVars, "__base_id": baseId, "__base_label": base.label }};

        if (colorId) {{
            const color = COLOR_THEMES.find(c => c.id === colorId);
            if (color) {{
                const cvars = flattenVars(darkMode ? color.dark : color.light);
                for (const [k, v] of Object.entries(cvars)) {{
                    if (!k.startsWith('--chart-')) theme[k] = v;
                }}
                theme["__color_id"] = colorId;
                theme["__color_label"] = color.label;
            }}
        }} else {{
            theme["__color_id"] = null;
            theme["__color_label"] = null;
        }}

        if (chartId) {{
            const chart = COLOR_THEMES.find(c => c.id === chartId);
            if (chart) {{
                const cvars = flattenVars(darkMode ? chart.dark : chart.light);
                for (const [k, v] of Object.entries(cvars)) {{
                    if (k.startsWith('--chart-')) theme[k] = v;
                }}
                theme["__chart_id"] = chartId;
                theme["__chart_label"] = chart.label;
            }}
        }} else {{
            theme["__chart_id"] = null;
            theme["__chart_label"] = null;
        }}

        if (styleId) {{
            const style = STYLE_REGISTRY.find(s => s.id === styleId);
            if (style) {{
                Object.assign(theme, style.vars);
                theme["__style_id"] = styleId;
                theme["__style_label"] = style.label;
            }}
        }}

        if (fontId) {{
            const font = FONT_REGISTRY.find(f => f.id === fontId);
            if (font) {{
                Object.assign(theme, font.vars);
                theme["__font_id"] = fontId;
                theme["__font_label"] = font.label;
            }}
        }}

        if (radius) {{
            theme["--radius"] = radius;
        }}

        return theme;
    }}

    function randomSeed() {{
        const n = Math.floor(Math.random() * 72600);
        const checksum = (n * 12345) % 916132832;
        return toBase62(n, 4) + toBase62(checksum, 5);
    }}

    window.__STYLE_REGISTRY = STYLE_REGISTRY;
    window.__BASE_THEMES    = BASE_THEMES;
    window.__COLOR_THEMES   = COLOR_THEMES;
    window.__FONT_REGISTRY  = FONT_REGISTRY;
    window.__RADIUS_OPTIONS = RADIUS_OPTIONS;
    window.__generateFromSeed = generateFromSeed;
    window.__rebuildTheme     = rebuildTheme;
    window.__randomSeed       = randomSeed;
    window.__flattenVars      = flattenVars;
    window.__encodeConfig     = encodeConfig;
    window.__decodeSeed       = decodeSeed;
    """)
