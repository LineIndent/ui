import json

from app.registry.colors import COLOR_THEMES
from app.registry.fonts import FONT_REGISTRY
from app.registry.radii import RADIUS_OPTIONS
from app.registry.styles import STYLE_REGISTRY
from app.registry.themes import BASE_THEMES

# ── shared engine (inlined once per action via _engine_js()) ──────────────────
# NOTE: We intentionally inline the engine into each action rather than
# relying on window.__ globals surviving re-renders. Each action is
# self-contained and safe to call at any time.


def _engine_js() -> str:
    return f"""
        const _SR = {json.dumps(STYLE_REGISTRY)};
        const _BT = {json.dumps(BASE_THEMES)};
        const _CT = {json.dumps(COLOR_THEMES)};
        const _FR = {json.dumps(FONT_REGISTRY)};
        const _RO = {json.dumps(RADIUS_OPTIONS)};
        const _CH = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

        function _flat(obj) {{
            const out = {{}};
            for (const [k, v] of Object.entries(obj))
                out[k === 'radius' ? '--radius' : '--' + k] = v;
            return out;
        }}

        function _b62e(n, len) {{
            let r = '';
            for (let i = 0; i < len; i++) {{ r += _CH[n % 62]; n = Math.floor(n / 62); }}
            return r;
        }}

        function _b62d(s) {{
            let n = 0;
            for (let i = s.length - 1; i >= 0; i--) n = n * 62 + _CH.indexOf(s[i]);
            return n;
        }}

        function _decode(seed) {{
            if (!seed) return null;
            if (seed === 'b0') return {{
                baseId: _BT[0].id, colorId: null, chartId: null,
                styleId: _SR[0].id, fontId: _FR[0].id, radius: _RO[2][1]
            }};
            if (seed.length !== 9) return null;
            const n = _b62d(seed.substring(0, 4));
            const cs = _b62d(seed.substring(4));
            if (cs !== (n * 12345) % 916132832 || n >= 72600) return null;
            let t = n;
            const rI = t % 4; t = Math.floor(t / 4);
            const fI = t % 5; t = Math.floor(t / 5);
            const sI = t % 5; t = Math.floor(t / 5);
            const chI = t % 11; t = Math.floor(t / 11);
            const cI = t % 11; t = Math.floor(t / 11);
            const bI = t % 6;
            return {{
                baseId:  _BT[bI].id,
                colorId: cI  > 0 ? _CT[cI  - 1].id : null,
                chartId: chI > 0 ? _CT[chI - 1].id : null,
                styleId: _SR[sI].id,
                fontId:  _FR[fI].id,
                radius:  _RO[rI][1],
            }};
        }}

        function _encode(cfg) {{
            const bI  = _BT.findIndex(b => b.id === cfg['__base_id']);
            const cI  = cfg['__color_id'] ? _CT.findIndex(c => c.id === cfg['__color_id']) + 1 : 0;
            const chI = cfg['__chart_id'] ? _CT.findIndex(c => c.id === cfg['__chart_id']) + 1 : 0;
            const sI  = _SR.findIndex(s => s.id === cfg['__style_id']);
            const fI  = _FR.findIndex(f => f.id === cfg['__font_id']);
            const rI  = _RO.findIndex(r => r[1] === cfg['--radius']);
            if (bI < 0 || sI < 0 || fI < 0 || rI < 0) return null;
            if (bI === 0 && cI === 0 && chI === 0 && sI === 0 && fI === 0 && rI === 2) return 'b0';
            const n = (((((bI * 11 + cI) * 11 + chI) * 5 + sI) * 5 + fI) * 4 + rI);
            return _b62e(n, 4) + _b62e((n * 12345) % 916132832, 5);
        }}

        function _rebuild(cfg) {{
            const {{ baseId, colorId, chartId, styleId, fontId, radius, darkMode }} = cfg;
            const base = _BT.find(b => b.id === baseId);
            if (!base) return {{}};
            let th = {{ ..._flat(darkMode ? base.dark : base.light), '__base_id': baseId, '__base_label': base.label }};
            if (colorId) {{
                const col = _CT.find(c => c.id === colorId);
                if (col) {{
                    for (const [k, v] of Object.entries(_flat(darkMode ? col.dark : col.light)))
                        if (!k.startsWith('--chart-')) th[k] = v;
                    th['__color_id'] = colorId; th['__color_label'] = col.label;
                }}
            }} else {{ th['__color_id'] = null; th['__color_label'] = null; }}
            if (chartId) {{
                const ch = _CT.find(c => c.id === chartId);
                if (ch) {{
                    for (const [k, v] of Object.entries(_flat(darkMode ? ch.dark : ch.light)))
                        if (k.startsWith('--chart-')) th[k] = v;
                    th['__chart_id'] = chartId; th['__chart_label'] = ch.label;
                }}
            }} else {{ th['__chart_id'] = null; th['__chart_label'] = null; }}
            if (styleId) {{
                const st = _SR.find(s => s.id === styleId);
                if (st) {{ Object.assign(th, st.vars); th['__style_id'] = styleId; th['__style_label'] = st.label; }}
            }}
            if (fontId) {{
                const fn = _FR.find(f => f.id === fontId);
                if (fn) {{ Object.assign(th, fn.vars); th['__font_id'] = fontId; th['__font_label'] = fn.label; }}
            }}
            if (radius) th['--radius'] = radius;
            return th;
        }}

        function _fromSeed(s, dark) {{
            let cfg = _decode(s);
            if (!cfg) {{
                // legacy random seed fallback
                function _hash(str) {{
                    let h = 0;
                    for (let i = 0; i < str.length; i++) {{ h = (h << 5) - h + str.charCodeAt(i); h |= 0; }}
                    return h >>> 0;
                }}
                function _mb32(seed) {{
                    return function() {{
                        let t = (seed += 0x6D2B79F5);
                        t = Math.imul(t ^ (t >>> 15), t | 1);
                        t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
                        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
                    }};
                }}
                const rand = _mb32(_hash(s));
                cfg = {{
                    baseId:  _BT[Math.floor(rand() * _BT.length)].id,
                    colorId: (function(r) {{ const i = Math.floor(r * 11); return i === 0 ? null : _CT[i-1].id; }})(rand()),
                    chartId: (function(r) {{ const i = Math.floor(r * 11); return i === 0 ? null : _CT[i-1].id; }})(rand()),
                    styleId: _SR[Math.floor(rand() * _SR.length)].id,
                    fontId:  _FR[Math.floor(rand() * _FR.length)].id,
                    radius:  _RO[Math.floor(rand() * _RO.length)][1],
                }};
            }}
            const th = _rebuild({{ ...cfg, darkMode: dark }});
            return {{ ...th, '__seed': s, '__dark': dark }};
        }}

        function _randomSeed() {{
            const n = Math.floor(Math.random() * 72600);
            return _b62e(n, 4) + _b62e((n * 12345) % 916132832, 5);
        }}

        // ── KEY FUNCTION: apply CSS vars to preview container only ──────────
        // Targets #theme-preview-container so site styles are unaffected.
        // Falls back to :root if container not found (e.g. other pages).
        function _applyToRoot(config) {{
            const preview = document.getElementById('theme-preview-container');
            const target  = preview || document.documentElement;
            for (const [k, v] of Object.entries(config))
                if (k.startsWith('--')) target.style.setProperty(k, v);
        }}
    """


def _sync_sidebar_js() -> str:
    return "if (window.__syncSidebar) window.__syncSidebar(config);"


# ── helpers used by multiple actions ─────────────────────────────────────────


def _set_refs(seed_val: str = "newSeed") -> str:
    """Sync ClientStateVars that are still needed for reactive UI."""
    return f"""
        // Still needed: seed display, copy button, css_output rendering
        if (refs['_client_state_setSeed'])  refs['_client_state_setSeed']({seed_val});
    """


# ── actions ───────────────────────────────────────────────────────────────────

SHUFFLE_JS = f"""
(function() {{
    {_engine_js()}

    const dark = refs['_client_state_darkmode'] || false;
    const s    = _randomSeed();

    const el = document.getElementById('seed-input-el');
    if (el) el.value = s;

    const config = _fromSeed(s, dark);

    // Apply CSS vars directly — no WebSocket needed
    _applyToRoot(config);

    // Sync remaining refs
    if (refs['_client_state_setSeed'])  refs['_client_state_setSeed'](s);

    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(s);
}})();
"""

APPLY_SEED_JS = f"""
(function() {{
    {_engine_js()}

    const dark = refs['_client_state_darkmode'] || false;
    const el   = document.getElementById('seed-input-el');
    const s    = el ? el.value.trim() : '';
    if (!s) return;

    const config = _fromSeed(s, dark);

    _applyToRoot(config);

    if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](s);

    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(s);
}})();
"""

INITIAL_LOAD_JS = f"""
(function() {{
    {_engine_js()}
    window.refs = refs;

    // 1. Determine dark mode
    const saved = localStorage.getItem('theme');
    let isDark = saved === 'dark' ? true
               : saved === 'light' ? false
               : window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (isDark) document.documentElement.classList.add('dark');
    else        document.documentElement.classList.remove('dark');

    if (refs['_client_state_setDarkmode']) refs['_client_state_setDarkmode'](isDark);

    // 2. Welcome dialog
    if (!localStorage.getItem('has_seen_welcome'))
        if (refs['_client_state_setWelcome_open']) refs['_client_state_setWelcome_open'](true);

    // 3. Determine seed
    let urlSeed = null;
    try {{ urlSeed = new URLSearchParams(window.location.search).get('preset'); }} catch(e) {{}}
    const s = urlSeed || refs['_client_state_seed'] || 'b0';

    // 4. Build config and apply CSS vars immediately — before WebSocket matters
    const config = _fromSeed(s, isDark);

    function apply() {{
        // Apply CSS vars to :root — instant, no WebSocket needed
        _applyToRoot(config);

        // Sync remaining reactive refs
        if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](s);

        if (window.__syncSidebar) window.__syncSidebar(config);
        if (window.__updatePresetURL) window.__updatePresetURL(s, false);

        const el = document.getElementById('seed-input-el');
        if (el) el.value = s;
    }}

    apply();
    setTimeout(apply, 50);
    setTimeout(apply, 200);
}})();
"""

TOGGLE_DARK_JS = f"""
(function() {{
    {_engine_js()}

    const nowDark = !document.documentElement.classList.contains('dark');

    if (nowDark) {{
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    }} else {{
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    }}

    if (refs['_client_state_setDarkmode']) refs['_client_state_setDarkmode'](nowDark);

    const s = refs['_client_state_seed'] || 'b0';
    const config = _fromSeed(s, nowDark);

    _applyToRoot(config);

    if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](s);
    {_sync_sidebar_js()}
}})();
"""

RESET_JS = f"""
(function() {{
    {_engine_js()}

    const dark = document.documentElement.classList.contains('dark');
    const s    = 'b0';
    const config = _fromSeed(s, dark);

    _applyToRoot(config);

    if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](s);
    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(s);
}})();
"""


def _apply_base_theme_js(base_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const dark = document.documentElement.classList.contains('dark');
        const cur  = refs['_client_state_seed'] || 'b0';
        const prev = _fromSeed(cur, dark);
        const config = _rebuild({{
            baseId:  '{base_id}',
            colorId: prev['__color_id'] || null,
            chartId: prev['__chart_id'] || null,
            styleId: prev['__style_id'] || null,
            fontId:  prev['__font_id']  || null,
            radius:  prev['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encode(config) || cur;
        config['__seed'] = newSeed; config['__dark'] = dark;
        _applyToRoot(config);
        if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _apply_color_theme_js(color_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const dark = document.documentElement.classList.contains('dark');
        const cur  = refs['_client_state_seed'] || 'b0';
        const prev = _fromSeed(cur, dark);
        const config = _rebuild({{
            baseId:  prev['__base_id']  || 'neutral',
            colorId: '{color_id}',
            chartId: prev['__chart_id'] || null,
            styleId: prev['__style_id'] || null,
            fontId:  prev['__font_id']  || null,
            radius:  prev['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encode(config) || cur;
        config['__seed'] = newSeed; config['__dark'] = dark;
        _applyToRoot(config);
        if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _apply_chart_color_js(color_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const dark = document.documentElement.classList.contains('dark');
        const cur  = refs['_client_state_seed'] || 'b0';
        const prev = _fromSeed(cur, dark);
        const config = _rebuild({{
            baseId:  prev['__base_id']  || 'neutral',
            colorId: prev['__color_id'] || null,
            chartId: '{color_id}',
            styleId: prev['__style_id'] || null,
            fontId:  prev['__font_id']  || null,
            radius:  prev['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encode(config) || cur;
        config['__seed'] = newSeed; config['__dark'] = dark;
        _applyToRoot(config);
        if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _apply_style_js(style_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const dark = document.documentElement.classList.contains('dark');
        const cur  = refs['_client_state_seed'] || 'b0';
        const prev = _fromSeed(cur, dark);
        const config = _rebuild({{
            baseId:  prev['__base_id']  || 'neutral',
            colorId: prev['__color_id'] || null,
            chartId: prev['__chart_id'] || null,
            styleId: '{style_id}',
            fontId:  prev['__font_id']  || null,
            radius:  prev['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encode(config) || cur;
        config['__seed'] = newSeed; config['__dark'] = dark;
        _applyToRoot(config);
        if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _apply_font_js(font_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const dark = document.documentElement.classList.contains('dark');
        const cur  = refs['_client_state_seed'] || 'b0';
        const prev = _fromSeed(cur, dark);
        const config = _rebuild({{
            baseId:  prev['__base_id']  || 'neutral',
            colorId: prev['__color_id'] || null,
            chartId: prev['__chart_id'] || null,
            styleId: prev['__style_id'] || null,
            fontId:  '{font_id}',
            radius:  prev['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encode(config) || cur;
        config['__seed'] = newSeed; config['__dark'] = dark;
        _applyToRoot(config);
        if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _patch_radius_js(value: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const dark = document.documentElement.classList.contains('dark');
        const cur  = refs['_client_state_seed'] || 'b0';
        const prev = _fromSeed(cur, dark);
        const config = _rebuild({{
            baseId:  prev['__base_id']  || 'neutral',
            colorId: prev['__color_id'] || null,
            chartId: prev['__chart_id'] || null,
            styleId: prev['__style_id'] || null,
            fontId:  prev['__font_id']  || null,
            radius:  '{value}',
            darkMode: dark,
        }});
        const newSeed = _encode(config) || cur;
        config['__seed'] = newSeed; config['__dark'] = dark;
        _applyToRoot(config);
        if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


APPLY_BASE_PRIMARY_JS = f"""
(function() {{
    {_engine_js()}
    const dark = document.documentElement.classList.contains('dark');
    const cur  = refs['_client_state_seed'] || 'b0';
    const prev = _fromSeed(cur, dark);
    const config = _rebuild({{
        baseId:  prev['__base_id']  || 'neutral',
        colorId: null,
        chartId: prev['__chart_id'] || null,
        styleId: prev['__style_id'] || null,
        fontId:  prev['__font_id']  || null,
        radius:  prev['--radius']   || null,
        darkMode: dark,
    }});
    const newSeed = _encode(config) || cur;
    config['__seed'] = newSeed; config['__dark'] = dark;
    _applyToRoot(config);
    if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](newSeed);
    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
}})();
"""

APPLY_BASE_CHARTS_JS = f"""
(function() {{
    {_engine_js()}
    const dark = document.documentElement.classList.contains('dark');
    const cur  = refs['_client_state_seed'] || 'b0';
    const prev = _fromSeed(cur, dark);
    const config = _rebuild({{
        baseId:  prev['__base_id']  || 'neutral',
        colorId: prev['__color_id'] || null,
        chartId: null,
        styleId: prev['__style_id'] || null,
        fontId:  prev['__font_id']  || null,
        radius:  prev['--radius']   || null,
        darkMode: dark,
    }});
    const newSeed = _encode(config) || cur;
    config['__seed'] = newSeed; config['__dark'] = dark;
    _applyToRoot(config);
    if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](newSeed);
    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
}})();
"""

ADD_SWATCHES_JS = """
(function() {
    function injectSwatches() {
        const block = document.getElementById("css-export-block");
        if (!block) return;
        const code = block.querySelector("code") || block;
        if (code.dataset.swatchesDone === "true") return;
        code.innerHTML = code.textContent.replace(/oklch\([^)]+\)/g, (m) =>
            `<span style="background-color:${m};width:.85em;height:.85em;display:inline-block;margin-right:.4em;border-radius:3px;border:1px solid rgba(255,255,255,.15);vertical-align:middle;flex-shrink:0;"></span>` + m
        );
        code.dataset.swatchesDone = "true";
    }
    setTimeout(injectSwatches, 40);
    setTimeout(injectSwatches, 120);
    setTimeout(injectSwatches, 300);
})();
"""

FORMAT_CSS_JS = f"""
(function() {{
    {_engine_js()}

    const s = refs['_client_state_seed'] || 'b0';
    const light = _fromSeed(s, false);
    const dark  = _fromSeed(s, true);

    const fmt = (cfg) => Object.entries(cfg)
        .filter(([k]) => k.startsWith('--'))
        .map(([k, v]) => `    ${{k}}: ${{v}};`)
        .join('\\n');

    const css = `:root {{\\n${{fmt(light)}}\\n}}\\n\\n.dark {{\\n${{fmt(dark)}}\\n}}`;

    if (refs['_client_state_setCssoutput']) refs['_client_state_setCssoutput'](css);

    setTimeout(() => {{
        const block = document.getElementById("css-export-block");
        if (!block) return;
        const code = block.querySelector("code") || block;
        code.innerHTML = code.textContent.replace(/oklch\([^)]+\)/g, (m) =>
            `<span style="background-color:${{m}};width:.85em;height:.85em;display:inline-block;margin-right:.4em;border-radius:3px;border:1px solid rgba(255,255,255,.15);vertical-align:middle;flex-shrink:0;"></span>` + m
        );
        code.dataset.swatchesDone = "true";
    }}, 60);
}})();
"""
