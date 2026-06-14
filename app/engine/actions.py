import json

from app.registry.colors import COLOR_THEMES
from app.registry.fonts import FONT_REGISTRY
from app.registry.radii import RADIUS_OPTIONS
from app.registry.styles import STYLE_REGISTRY
from app.registry.themes import BASE_THEMES


def _engine_js() -> str:
    """
    Inline the full theme engine (registries + rebuildTheme + helpers).
    Used in every action so nothing depends on window.__ globals surviving re-renders.
    """
    style_registry_js = json.dumps(STYLE_REGISTRY)
    base_themes_js = json.dumps(BASE_THEMES)
    color_themes_js = json.dumps(COLOR_THEMES)
    font_registry_js = json.dumps(FONT_REGISTRY)
    radius_options_js = json.dumps(RADIUS_OPTIONS)

    return f"""
        const _STYLE_REGISTRY = {style_registry_js};
        const _BASE_THEMES    = {base_themes_js};
        const _COLOR_THEMES   = {color_themes_js};
        const _FONT_REGISTRY  = {font_registry_js};
        const _RADIUS_OPTIONS = {radius_options_js};
        const _CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

        function _flattenVars(obj) {{
            const out = {{}};
            for (const [k, v] of Object.entries(obj)) {{
                out[k === 'radius' ? '--radius' : '--' + k] = v;
            }}
            return out;
        }}

        function _toBase62(n, len) {{
            let res = "";
            for (let i = 0; i < len; i++) {{
                res += _CHARS[n % 62];
                n = Math.floor(n / 62);
            }}
            return res;
        }}

        function _fromBase62(s) {{
            let n = 0;
            for (let i = s.length - 1; i >= 0; i--) {{
                n = n * 62 + _CHARS.indexOf(s[i]);
            }}
            return n;
        }}

        function _rebuildTheme(config) {{
            const {{ baseId, colorId, chartId, styleId, fontId, radius, darkMode }} = config;
            const base = _BASE_THEMES.find(b => b.id === baseId);
            if (!base) return {{}};

            const baseVars = _flattenVars(darkMode ? base.dark : base.light);
            let theme = {{ ...baseVars, '__base_id': baseId, '__base_label': base.label }};

            if (colorId) {{
                const color = _COLOR_THEMES.find(c => c.id === colorId);
                if (color) {{
                    const cvars = _flattenVars(darkMode ? color.dark : color.light);
                    for (const [k, v] of Object.entries(cvars)) {{
                        if (!k.startsWith('--chart-')) theme[k] = v;
                    }}
                    theme['__color_id']    = colorId;
                    theme['__color_label'] = color.label;
                }}
            }} else {{
                theme['__color_id']    = null;
                theme['__color_label'] = null;
            }}

            if (chartId) {{
                const chart = _COLOR_THEMES.find(c => c.id === chartId);
                if (chart) {{
                    const cvars = _flattenVars(darkMode ? chart.dark : chart.light);
                    for (const [k, v] of Object.entries(cvars)) {{
                        if (k.startsWith('--chart-')) theme[k] = v;
                    }}
                    theme['__chart_id']    = chartId;
                    theme['__chart_label'] = chart.label;
                }}
            }} else {{
                theme['__chart_id']    = null;
                theme['__chart_label'] = null;
            }}

            if (styleId) {{
                const style = _STYLE_REGISTRY.find(s => s.id === styleId);
                if (style) {{
                    Object.assign(theme, style.vars);
                    theme['__style_id']    = styleId;
                    theme['__style_label'] = style.label;
                }}
            }}

            if (fontId) {{
                const font = _FONT_REGISTRY.find(f => f.id === fontId);
                if (font) {{
                    Object.assign(theme, font.vars);
                    theme['__font_id']    = fontId;
                    theme['__font_label'] = font.label;
                }}
            }}

            if (radius) {{
                theme['--radius'] = radius;
            }}

            return theme;
        }}

        function _encodeConfig(theme) {{
            const bIdx  = _BASE_THEMES.findIndex(b => b.id === theme['__base_id']);
            const cIdx  = theme['__color_id'] ? _COLOR_THEMES.findIndex(c => c.id === theme['__color_id']) + 1 : 0;
            const chIdx = theme['__chart_id'] ? _COLOR_THEMES.findIndex(c => c.id === theme['__chart_id']) + 1 : 0;
            const sIdx  = _STYLE_REGISTRY.findIndex(s => s.id === theme['__style_id']);
            const fIdx  = _FONT_REGISTRY.findIndex(f => f.id === theme['__font_id']);
            const rIdx  = _RADIUS_OPTIONS.findIndex(r => r[1] === theme['--radius']);

            if (bIdx === -1 || sIdx === -1 || fIdx === -1 || rIdx === -1) return null;

            // Default state special case
            if (bIdx === 0 && cIdx === 0 && chIdx === 0 && sIdx === 0 && fIdx === 0 && rIdx === 2) return "b0";

            // State space: 6 * 11 * 11 * 5 * 5 * 4 = 72600
            let n = (((((bIdx * 11 + cIdx) * 11 + chIdx) * 5 + sIdx) * 5 + fIdx) * 4 + rIdx);

            // Encode as 9 chars: [Base62(N, 4)] + [Base62(Checksum(N), 5)]
            const checksum = (n * 12345) % 916132832; // 62^5
            return _toBase62(n, 4) + _toBase62(checksum, 5);
        }}

        function _decodeSeed(seed) {{
            if (!seed) return null;
            if (seed === "b0") {{
                return {{ baseId: _BASE_THEMES[0].id, colorId: null, chartId: null, styleId: _STYLE_REGISTRY[0].id, fontId: _FONT_REGISTRY[0].id, radius: _RADIUS_OPTIONS[2][1] }};
            }}
            if (seed.length !== 9) return null;

            const n = _fromBase62(seed.substring(0, 4));
            const checksum = _fromBase62(seed.substring(4));

            if (checksum === (n * 12345) % 916132832 && n < 72600) {{
                let temp = n;
                const rIdx = temp % 4; temp = Math.floor(temp / 4);
                const fIdx = temp % 5; temp = Math.floor(temp / 5);
                const sIdx = temp % 5; temp = Math.floor(temp / 5);
                const chIdx = temp % 11; temp = Math.floor(temp / 11);
                const cIdx = temp % 11; temp = Math.floor(temp / 11);
                const bIdx = temp % 6;

                return {{
                    baseId:  _BASE_THEMES[bIdx].id,
                    colorId: cIdx > 0 ? _COLOR_THEMES[cIdx - 1].id : null,
                    chartId: chIdx > 0 ? _COLOR_THEMES[chIdx - 1].id : null,
                    styleId: _STYLE_REGISTRY[sIdx].id,
                    fontId:  _FONT_REGISTRY[fIdx].id,
                    radius:  _RADIUS_OPTIONS[rIdx][1]
                }};
            }}
            return null;
        }}

        function _hashStringToInt(str) {{
            let hash = 0;
            for (let i = 0; i < str.length; i++) {{
                hash = (hash << 5) - hash + str.charCodeAt(i);
                hash |= 0;
            }}
            return hash >>> 0;
        }}

        function _mulberry32(seed) {{
            return function() {{
                let t = (seed += 0x6D2B79F5);
                t = Math.imul(t ^ (t >>> 15), t | 1);
                t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
                return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
            }};
        }}

        function _generateFromSeed(seedString, darkMode) {{
            let config = _decodeSeed(seedString);
            if (!config) {{
                // Legacy support for non-encoded random strings
                const rand = _mulberry32(_hashStringToInt(seedString));
                config = {{
                    baseId:  _BASE_THEMES[Math.floor(rand() * _BASE_THEMES.length)].id,
                    colorId: (function(r){{ let i = Math.floor(r * 11); return i === 0 ? null : _COLOR_THEMES[i-1].id; }})(rand()),
                    chartId: (function(r){{ let i = Math.floor(r * 11); return i === 0 ? null : _COLOR_THEMES[i-1].id; }})(rand()),
                    styleId: _STYLE_REGISTRY[Math.floor(rand() * _STYLE_REGISTRY.length)].id,
                    fontId:  _FONT_REGISTRY[Math.floor(rand() * _FONT_REGISTRY.length)].id,
                    radius:  _RADIUS_OPTIONS[Math.floor(rand() * _RADIUS_OPTIONS.length)][1]
                }};
            }}

            const theme = _rebuildTheme({{ ...config, darkMode }});
            return {{ ...theme, '__seed': seedString, '__dark': darkMode }};
        }}

        function _randomSeed() {{
            const n = Math.floor(Math.random() * 72600);
            const checksum = (n * 12345) % 916132832;
            return _toBase62(n, 4) + _toBase62(checksum, 5);
        }}
    """


def _sync_sidebar_js() -> str:
    """
    After applying a theme config, sync the sidebar ClientStateVars
    so the dropdowns reflect the current state.
    """
    return """
        if (window.__syncSidebar) window.__syncSidebar(config);
    """


SHUFFLE_JS = f"""
(function() {{
    {_engine_js()}

    const dark = refs['_client_state_darkmode'] || false;
    const s    = _randomSeed();

    // update seed input if present
    const el = document.getElementById('seed-input-el');
    if (el) el.value = s;

    const config = _generateFromSeed(s, dark);
    refs['_client_state_setTheme'](config);
    refs['_client_state_setSeed'](s);

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

    const config = _generateFromSeed(s, dark);
    refs['_client_state_setTheme'](config);
    refs['_client_state_setSeed'](s);

    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(s);
}})();
"""

INITIAL_LOAD_JS = f"""
(function() {{
    {_engine_js()}
    window.refs = refs;

    // 1. Helper: Robust URL Parsing
    const getPresetFromURL = () => {{
        try {{
            const params = new URLSearchParams(window.location.search);
            return params.get('preset');
        }} catch (e) {{
            return null;
        }}
    }};

    // 2. Determine Dark Mode
    const savedTheme = localStorage.getItem('theme');
    let isDark = false;
    if (savedTheme === 'dark') {{
        isDark = true;
    }} else if (savedTheme === 'light') {{
        isDark = false;
    }} else {{
        isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    }}

    if (isDark) {{
        document.documentElement.classList.add('dark');
    }} else {{
        document.documentElement.classList.remove('dark');
    }}

    if (refs['_client_state_setDarkmode']) refs['_client_state_setDarkmode'](isDark);

    // 2. Check for Welcome Dialog
    const hasSeenWelcome = localStorage.getItem('has_seen_welcome');
    if (!hasSeenWelcome) {{
            if (refs['_client_state_setWelcome_open']) refs['_client_state_setWelcome_open'](true);
         }}

    // 3. Determine Seed (Prioritize URL > current state > default)
    const urlSeed = getPresetFromURL();
    const currentSeed = refs['_client_state_seed'];
    const s = urlSeed || currentSeed || "b0";

    // 4. Generate and Apply Theme
    const config = _generateFromSeed(s, isDark);

    const applyConfig = () => {{
        if (refs['_client_state_setTheme']) refs['_client_state_setTheme'](config);
        if (refs['_client_state_setSeed']) refs['_client_state_setSeed'](s);

        // Sync sidebar if the helper exists, otherwise retry soon
        if (window.__syncSidebar) {{
            window.__syncSidebar(config);
        }}

        // Ensure URL stays in sync
        if (window.__updatePresetURL) {{
            window.__updatePresetURL(s, false);
        }}

        const el = document.getElementById('seed-input-el');
        if (el) el.value = s;
    }};

    // Execute sequence
    applyConfig();

    // Retries to catch late-binding sidebar/url scripts
    setTimeout(applyConfig, 50);
    setTimeout(applyConfig, 200);
}})();
"""

TOGGLE_DARK_JS = f"""
(function() {{
    {_engine_js()}

    const current = refs['_client_state_theme'] || {{}};
    const nowDark = !(current['__dark'] || false);
    refs['_client_state_setDarkmode'](nowDark);

    // Toggle root class for Tailwind
    if (nowDark) {{
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    }} else {{
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    }}

    let config;
    const s = current['__seed'] || refs['_client_state_seed'] || '';
    if (s) {{
        config = _generateFromSeed(s, nowDark);
    }} else {{
        config = _rebuildTheme({{
            baseId:  current['__base_id']  || 'neutral',
            colorId: current['__color_id'] || null,
            chartId: current['__chart_id'] || null,
            styleId: current['__style_id'] || null,
            fontId:  current['__font_id']  || null,
            radius:  current['--radius']   || null,
            darkMode: nowDark,
        }});
        config = {{ ...current, ...config, '__dark': nowDark }};
    }}

    refs['_client_state_setTheme'](config);
    {_sync_sidebar_js()}
}})();
"""


RESET_JS = f"""
(function() {{
    {_engine_js()}

    const dark = refs['_client_state_darkmode'] || false;
    const s    = "b0";

    const config = _generateFromSeed(s, dark);
    refs['_client_state_setTheme'](config);
    refs['_client_state_setSeed'](s);

    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(s);
}})();
"""


def _apply_base_theme_js(base_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const current = refs['_client_state_theme'] || {{}};
        const dark    = refs['_client_state_darkmode'] || false;
        let config  = _rebuildTheme({{
            baseId:  '{base_id}',
            colorId: current['__color_id'] || null,
            chartId: current['__chart_id'] || null,
            styleId: current['__style_id'] || null,
            fontId:  current['__font_id']  || null,
            radius:  current['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encodeConfig(config);
        config['__seed'] = newSeed;
        config['__dark'] = dark;
        refs['_client_state_setTheme'](config);
        refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _apply_color_theme_js(color_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const current = refs['_client_state_theme'] || {{}};
        const dark    = refs['_client_state_darkmode'] || false;
        let config  = _rebuildTheme({{
            baseId:  current['__base_id']  || 'neutral',
            colorId: '{color_id}',
            chartId: current['__chart_id'] || null,
            styleId: current['__style_id'] || null,
            fontId:  current['__font_id']  || null,
            radius:  current['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encodeConfig(config);
        config['__seed'] = newSeed;
        config['__dark'] = dark;
        refs['_client_state_setTheme'](config);
        refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _apply_chart_color_js(color_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const current = refs['_client_state_theme'] || {{}};
        const dark    = refs['_client_state_darkmode'] || false;
        let config  = _rebuildTheme({{
            baseId:  current['__base_id']  || 'neutral',
            colorId: current['__color_id'] || null,
            chartId: '{color_id}',
            styleId: current['__style_id'] || null,
            fontId:  current['__font_id']  || null,
            radius:  current['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encodeConfig(config);
        config['__seed'] = newSeed;
        config['__dark'] = dark;
        refs['_client_state_setTheme'](config);
        refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _apply_style_js(style_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const current = refs['_client_state_theme'] || {{}};
        const dark    = refs['_client_state_darkmode'] || false;
        let config  = _rebuildTheme({{
            baseId:  current['__base_id']  || 'neutral',
            colorId: current['__color_id'] || null,
            chartId: current['__chart_id'] || null,
            styleId: '{style_id}',
            fontId:  current['__font_id']  || null,
            darkMode: dark,
        }});
        const newSeed = _encodeConfig(config);
        config['__seed'] = newSeed;
        config['__dark'] = dark;
        refs['_client_state_setTheme'](config);
        refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _apply_font_js(font_id: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const current = refs['_client_state_theme'] || {{}};
        const dark    = refs['_client_state_darkmode'] || false;
        let config  = _rebuildTheme({{
            baseId:  current['__base_id']  || 'neutral',
            colorId: current['__color_id'] || null,
            chartId: current['__chart_id'] || null,
            styleId: current['__style_id'] || null,
            fontId:  '{font_id}',
            radius:  current['--radius']   || null,
            darkMode: dark,
        }});
        const newSeed = _encodeConfig(config);
        config['__seed'] = newSeed;
        config['__dark'] = dark;
        refs['_client_state_setTheme'](config);
        refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


APPLY_BASE_PRIMARY_JS = f"""
(function() {{
    {_engine_js()}
    const current = refs['_client_state_theme'] || {{}};
    const dark    = refs['_client_state_darkmode'] || false;
    let config  = _rebuildTheme({{
        baseId:  current['__base_id']  || 'neutral',
        colorId: null,
        chartId: current['__chart_id'] || null,
        styleId: current['__style_id'] || null,
        fontId:  current['__font_id']  || null,
        darkMode: dark,
    }});
    const newSeed = _encodeConfig(config);
    config['__seed'] = newSeed;
    config['__dark'] = dark;
    refs['_client_state_setTheme'](config);
    refs['_client_state_setSeed'](newSeed);
    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
}})();
"""

APPLY_BASE_CHARTS_JS = f"""
(function() {{
    {_engine_js()}
    const current = refs['_client_state_theme'] || {{}};
    const dark    = refs['_client_state_darkmode'] || false;
    let config  = _rebuildTheme({{
        baseId:  current['__base_id']  || 'neutral',
        colorId: current['__color_id'] || null,
        chartId: null,
        styleId: current['__style_id'] || null,
        fontId:  current['__font_id']  || null,
        darkMode: dark,
    }});
    const newSeed = _encodeConfig(config);
    config['__seed'] = newSeed;
    config['__dark'] = dark;
    refs['_client_state_setTheme'](config);
    refs['_client_state_setSeed'](newSeed);
    {_sync_sidebar_js()}
    if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
}})();
"""

ADD_SWATCHES_JS = """
(function() {
    function injectSwatches() {
        const block = document.getElementById("css-export-block");
        if (!block) return;

        // Ensure we are targeting the inner block text wrapper
        const codeElement = block.querySelector("code") || block;

        // Prevent infinite loops if already formatted
        if (codeElement.dataset.swatchesDone === "true") return;

        let rawText = codeElement.textContent;

        // Match all variations of oklch(...) globally
        const oklchRegex = /oklch\([^)]+\)/g;

        // Map every text match to an HTML template containing the swatch + the string itself
        const highLightedHtml = rawText.replace(oklchRegex, (match) => {
            const swatchHtml = `<span data-color-swatch="true" style="background-color:${match}; width:0.85em; height:0.85em; display:inline-block; margin-right:0.4em; border-radius:3px; border:1px solid rgba(255,255,255,0.15); vertical-align:middle; flex-shrink:0;"></span>`;
            return swatchHtml + match;
        });

        codeElement.innerHTML = highLightedHtml;
        codeElement.dataset.swatchesDone = "true";
    }

    // Run quickly across standard rendering cycles
    setTimeout(injectSwatches, 40);
    setTimeout(injectSwatches, 120);
    setTimeout(injectSwatches, 300);
})();
"""


FORMAT_CSS_JS = f"""
(function() {{
    {_engine_js()}

    const theme = refs['_client_state_theme'] || {{}};
    const seed  = theme['__seed'] || 'b0';

    const lightConfig = _generateFromSeed(seed, false);
    const darkConfig  = _generateFromSeed(seed, true);

    const format = (config) =>
        Object.entries(config)
            .filter(([k]) => k.startsWith('--'))
            .map(([k, v]) => `    ${{k}}: ${{v}};`)
            .join('\\n');

    const css = `:root {{\\n${{format(lightConfig)}}\\n}}\\n\\n.dark {{\\n${{format(darkConfig)}}\\n}}`;

    // 1. Send the clean raw string text back to state
    refs['_client_state_setCssoutput'](css);

    // 2. Wait for React render state update, then cleanly map HTML templates
    setTimeout(() => {{
        const block = document.getElementById("css-export-block");
        if (!block) return;

        const codeElement = block.querySelector("code") || block;
        let rawText = codeElement.textContent;

        const oklchRegex = /oklch\\([^)]+\\)/g;
        const highLightedHtml = rawText.replace(oklchRegex, (match) => {{
            return `<span data-color-swatch="true" style="background-color:${{match}}; width:0.85em; height:0.85em; display:inline-block; margin-right:0.4em; border-radius:3px; border:1px solid rgba(255,255,255,0.15); vertical-align:middle; flex-shrink:0;"></span>` + match;
        }}); // <-- FIXED: Doubled the function body closing brace '}}'

        codeElement.innerHTML = highLightedHtml;
        codeElement.dataset.swatchesDone = "true";
    }}, 60);
}})();
"""


def _patch_js(updates: dict) -> str:
    updates_js = json.dumps(updates)
    return f"""
    (function() {{
        {_engine_js()}
        const current = refs['_client_state_theme'] || {{}};
        const dark    = refs['_client_state_darkmode'] || false;
        let config    = {{...current, ...{updates_js}}};

        // Ensure rebuild to get IDs for encoding
        config = _rebuildTheme({{
            baseId:   config['__base_id']  || 'neutral',
            colorId:  config['__color_id'] || null,
            chartId:  config['__chart_id'] || null,
            styleId:  config['__style_id'] || null,
            fontId:   config['__font_id']  || null,
            radius:   config['--radius']   || null,
            darkMode: dark
        }});

        const newSeed = _encodeConfig(config);
        config['__seed'] = newSeed;
        config['__dark'] = dark;

        refs['_client_state_setTheme'](config);
        refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """


def _patch_radius_js(value: str) -> str:
    return f"""
    (function() {{
        {_engine_js()}
        const current = refs['_client_state_theme'] || {{}};
        const dark    = refs['_client_state_darkmode'] || false;

        let config = _rebuildTheme({{
            baseId:  current['__base_id']  || 'neutral',
            colorId: current['__color_id'] || null,
            chartId: current['__chart_id'] || null,
            styleId: current['__style_id'] || 'vega',
            fontId:  current['__font_id']  || 'inter',
            radius:  '{value}',
            darkMode: dark,
        }});

        const newSeed = _encodeConfig(config);
        config['__seed'] = newSeed;
        config['__dark'] = dark;

        refs['_client_state_setTheme'](config);
        refs['_client_state_setSeed'](newSeed);
        {_sync_sidebar_js()}
        if (window.__updatePresetURL) window.__updatePresetURL(newSeed);
    }})();
    """
