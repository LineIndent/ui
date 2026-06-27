import argparse
import ast
import shutil
import sys
from pathlib import Path

# ── registries ────────────────────────────────────────────────────────────────
from app.registry.colors import COLOR_THEMES
from app.registry.components import COMPONENT_REGISTRY
from app.registry.fonts import FONT_REGISTRY
from app.registry.radii import RADIUS_OPTIONS
from app.registry.styles import STYLE_REGISTRY
from app.registry.themes import BASE_THEMES
from cli.scrollbar_css import SCROLLBAR_CSS
from cli.shimmer_css import SHIMMER_CSS

# ── string constants ──────────────────────────────────────────────────────────
from cli.tailwind_config import TAILWIND_CONFIG_SNIPPET

# ── utilities bundle injected by `buridan init` ───────────────────────────────
# Order matters — each block is appended in sequence.
UTILITIES_BUNDLE = [
    ("shimmer", SHIMMER_CSS),
    ("scrollbar", SCROLLBAR_CSS),
]

# Sentinel comments used to detect whether a utility is already present.
UTILITY_SENTINELS = {
    "shimmer": "/* ── Shimmer utility",
    "scrollbar": "/* ── Scrollbar utilities",
}


# ── helpers ───────────────────────────────────────────────────────────────────

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def from_base62(s: str) -> int:
    n = 0
    for i in range(len(s) - 1, -1, -1):
        n = n * 62 + CHARS.find(s[i])
    return n


def flatten_vars(obj: dict) -> dict:
    out = {}
    for k, v in obj.items():
        key = "--radius" if k == "radius" else f"--{k}"
        out[key] = v
    return out


def rebuild_theme(config: dict) -> dict:
    base_id = config.get("baseId")
    color_id = config.get("colorId")
    chart_id = config.get("chartId")
    style_id = config.get("styleId")
    font_id = config.get("fontId")
    radius = config.get("radius")
    dark = config.get("darkMode", False)

    base = next((b for b in BASE_THEMES if b["id"] == base_id), None)
    if not base:
        return {}

    theme = {**flatten_vars(base["dark"] if dark else base["light"])}

    if color_id:
        color = next((c for c in COLOR_THEMES if c["id"] == color_id), None)
        if color:
            for k, v in flatten_vars(color["dark"] if dark else color["light"]).items():
                if not k.startswith("--chart-"):
                    theme[k] = v

    if chart_id:
        chart = next((c for c in COLOR_THEMES if c["id"] == chart_id), None)
        if chart:
            for k, v in flatten_vars(chart["dark"] if dark else chart["light"]).items():
                if k.startswith("--chart-"):
                    theme[k] = v

    if style_id:
        style = next((s for s in STYLE_REGISTRY if s["id"] == style_id), None)
        if style:
            theme.update(style["vars"])

    if font_id:
        font = next((f for f in FONT_REGISTRY if f["id"] == font_id), None)
        if font:
            theme.update(font["vars"])

    if radius:
        theme["--radius"] = radius

    return theme


def decode_seed(seed: str) -> dict | None:
    if not seed:
        return None
    if seed == "b0":
        return {
            "baseId": BASE_THEMES[0]["id"],
            "colorId": None,
            "chartId": None,
            "styleId": STYLE_REGISTRY[0]["id"],
            "fontId": FONT_REGISTRY[0]["id"],
            "radius": RADIUS_OPTIONS[2][1],
        }
    if len(seed) != 9:
        return None

    n = from_base62(seed[:4])
    checksum = from_base62(seed[4:])

    if checksum == (n * 12345) % 916132832 and n < 72600:
        temp = n
        r_idx = temp % 4
        temp //= 4
        f_idx = temp % 5
        temp //= 5
        s_idx = temp % 5
        temp //= 5
        ch_idx = temp % 11
        temp //= 11
        c_idx = temp % 11
        temp //= 11
        b_idx = temp % 6

        return {
            "baseId": BASE_THEMES[b_idx]["id"],
            "colorId": COLOR_THEMES[c_idx - 1]["id"] if c_idx > 0 else None,
            "chartId": COLOR_THEMES[ch_idx - 1]["id"] if ch_idx > 0 else None,
            "styleId": STYLE_REGISTRY[s_idx]["id"],
            "fontId": FONT_REGISTRY[f_idx]["id"],
            "radius": RADIUS_OPTIONS[r_idx][1],
        }
    return None


def format_css(config: dict) -> str:
    return "\n".join(f"    {k}: {v};" for k, v in config.items() if k.startswith("--"))


def generate_theme_css(seed: str) -> str:
    def build(dark):
        return format_css(rebuild_theme({**decode_seed(seed), "darkMode": dark}))

    return f":root {{\n{build(False)}\n}}\n\n.dark {{\n{build(True)}\n}}"


def get_source_root() -> Path | None:
    source_root = Path(__file__).parent.parent
    if (source_root / "components").exists():
        return source_root
    try:
        import components

        return Path(components.__file__).parent.parent
    except (ImportError, AttributeError):
        return None


def resolve_dependencies(component_names: list[str], registry: dict) -> list[str]:
    required_files: set[str] = set()
    visited: set[str] = set()

    def add(name: str):
        key = name.lower()
        if key in visited:
            return
        visited.add(key)
        entry = registry.get(key)
        if not entry:
            print(f"Warning: Component '{name}' not found in registry.")
            return
        for f in entry["files"]:
            required_files.add(f)
        for dep in entry.get("dependencies", []):
            add(dep)

    for name in component_names:
        add(name)

    return sorted(required_files)


BLOCK_SOURCE_PREFIX = "app/www/library/blocks/"


def remap_dest(rel: str) -> str:
    """Remap block source paths to blocks/ in the user's project root."""
    if rel.startswith(BLOCK_SOURCE_PREFIX):
        return "blocks/" + Path(rel).name
    return rel


def add_components_to_project(
    component_names: list[str], target_root: Path = None
) -> bool:
    if target_root is None:
        target_root = Path.cwd()

    if not (target_root / "rxconfig.py").exists():
        print(
            "Error: rxconfig.py not found. Please run this command in a Reflex project root."
        )
        return False

    source_root = get_source_root()
    if not source_root:
        print("Error: Could not locate Buridan source components.")
        return False

    files = resolve_dependencies(component_names, COMPONENT_REGISTRY)
    if not files:
        print("No files to copy.")
        return False

    for rel in files:
        src = source_root / rel
        dest = target_root / remap_dest(rel)

        if not src.exists():
            print(f"Warning: Source file {src} does not exist.")
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)

        # ensure __init__.py chain exists up to components/ or blocks/
        current = dest.parent
        while current != target_root:
            init = current / "__init__.py"
            if not init.exists():
                init.touch()
            if current.name in ("components", "blocks"):
                break
            current = current.parent

        shutil.copy2(src, dest)
        print(f"✓ Added {remap_dest(rel)}")

    return True


def patch_rxconfig(config_path: Path) -> None:
    """Inject TailwindV4 plugin into rxconfig.py if not already present."""
    content = config_path.read_text()

    if "var(--background)" in content:
        print("• rxconfig.py already contains Buridan UI theme tokens.")
        return

    try:
        tree = ast.parse(content)
        snippet = TAILWIND_CONFIG_SNIPPET.strip().rstrip(",")
        lines = content.splitlines()
        modified = False

        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign):
                continue
            call = node.value
            if not (
                isinstance(call, ast.Call)
                and isinstance(call.func, ast.Attribute)
                and call.func.attr.lower() == "config"
                and getattr(call.func.value, "id", "") == "rx"
            ):
                continue

            plugins_kw = next((kw for kw in call.keywords if kw.arg == "plugins"), None)

            if plugins_kw:
                for i in range(call.lineno - 1, call.end_lineno):
                    if "plugins=" in lines[i]:
                        lines[i] = lines[i].replace(
                            "plugins=[", f"plugins=[\n{snippet},"
                        )
                        modified = True
                        break
            else:
                for i in range(call.lineno - 1, call.end_lineno):
                    if "Config(" in lines[i] or "config(" in lines[i]:
                        indent = " " * (len(lines[i]) - len(lines[i].lstrip()))
                        lines[i] = lines[i].replace(
                            "(", f"(\n{indent}    plugins=[\n{snippet}\n{indent}    ],"
                        )
                        modified = True
                        break

            if modified:
                content = "\n".join(lines)
                content = content.replace("rx.plugins.TailwindV4Plugin(),", "")
                content = content.replace("rx.plugins.TailwindV4Plugin()", "")
                content = content.replace(",,", ",")
                break

        if not modified:
            if "rx.Config(" in content:
                content = content.replace(
                    "rx.Config(", f"rx.Config(\n    plugins=[\n{snippet}\n    ],"
                )
                modified = True
            elif "rx.config(" in content:
                content = content.replace(
                    "rx.config(", f"rx.config(\n    plugins=[\n{snippet}\n    ],"
                )
                modified = True

        if modified:
            import_stmt = "from reflex.plugins.shared_tailwind import TailwindConfig"
            if import_stmt not in content:
                content = f"{import_stmt}\n{content}"
            config_path.write_text(content)
            print("✓ Updated rxconfig.py with Buridan UI Tailwind config.")
        else:
            print(
                "Warning: Could not automatically update rxconfig.py. Please configure manually."
            )

    except Exception as e:
        print(f"Warning: Could not parse rxconfig.py ({e}). Please configure manually.")


# ── commands ──────────────────────────────────────────────────────────────────


def cmd_init():
    """
    Initialize Buridan UI utilities in an existing Reflex project.

    - Locates or creates assets/globals.css
    - Appends CSS utilities (shimmer, scrollbar) if not already present
    - Updates rxconfig.py with TailwindV4 plugin config
    """
    root = Path.cwd()

    if not (root / "rxconfig.py").exists():
        print(
            "Error: rxconfig.py not found. Please run this command in a Reflex project root."
        )
        sys.exit(1)

    # ── ensure assets/globals.css exists ─────────────────────────────────────
    assets_dir = root / "assets"
    assets_dir.mkdir(exist_ok=True)
    css_path = assets_dir / "globals.css"

    if not css_path.exists():
        css_path.write_text("")
        print(f"✓ Created {css_path.relative_to(root)}")
    else:
        print(f"• Found {css_path.relative_to(root)}")

    # ── append utilities that aren't already present ──────────────────────────
    current_css = css_path.read_text()
    added = []

    for name, css in UTILITIES_BUNDLE:
        sentinel = UTILITY_SENTINELS[name]
        if sentinel in current_css:
            print(f"• {name} utility already present in globals.css — skipping.")
        else:
            current_css += f"\n{css}"
            added.append(name)

    if added:
        css_path.write_text(current_css)
        for name in added:
            print(f"✓ Added {name} utility to globals.css")

    # ── patch rxconfig.py ─────────────────────────────────────────────────────
    patch_rxconfig(root / "rxconfig.py")

    # ── next steps ────────────────────────────────────────────────────────────
    print("\n✓ Buridan UI initialized successfully.")
    print("\nNext steps:")
    print("  1. Add globals.css to your app stylesheets:")
    print('     app = rx.App(stylesheets=["globals.css"])')
    print("  2. Apply a theme:")
    print("     buridan apply --preset b0")
    print("  3. Add components:")
    print("     buridan add button")


def cmd_apply(preset: str):
    """
    Apply a theme preset to the project.

    Decodes the preset seed and writes :root / .dark CSS variables
    to assets/globals.css, preserving any existing utility blocks.
    """
    root = Path.cwd()

    if not (root / "rxconfig.py").exists():
        print("Error: rxconfig.py not found. Please run this in a Reflex project root.")
        sys.exit(1)

    config = decode_seed(preset)
    if not config:
        print(
            f"Error: Invalid preset ID '{preset}'. Get a valid preset from https://buridan-ui.com/create"
        )
        sys.exit(1)

    assets_dir = root / "assets"
    assets_dir.mkdir(exist_ok=True)
    css_path = assets_dir / "globals.css"

    theme_css = generate_theme_css(preset)
    theme_marker = ":root {"

    if css_path.exists():
        current = css_path.read_text()
        if theme_marker in current:
            # replace existing :root / .dark block, preserve everything after
            # find where :root starts and .dark block ends
            lines = current.splitlines()
            start_line = next(
                (i for i, l in enumerate(lines) if l.strip().startswith(":root {")),
                None,
            )
            if start_line is not None:
                # find end of .dark block
                brace_depth = 0
                end_line = start_line
                in_block = False
                for i, line in enumerate(lines[start_line:], start_line):
                    brace_depth += line.count("{") - line.count("}")
                    if brace_depth > 0:
                        in_block = True
                    if in_block and brace_depth == 0:
                        end_line = i
                        # keep going to also consume .dark {}
                        # find next block
                        rest = lines[end_line + 1 :]
                        for j, l in enumerate(rest):
                            if l.strip().startswith(".dark {"):
                                bd = 0
                                for k, dl in enumerate(
                                    lines[end_line + 1 + j :], end_line + 1 + j
                                ):
                                    bd += dl.count("{") - dl.count("}")
                                    if bd > 0:
                                        pass
                                    if bd == 0 and k > end_line + 1 + j:
                                        end_line = k
                                        break
                                break
                        break

                after = "\n".join(lines[end_line + 1 :]).lstrip("\n")
                new_css = theme_css + ("\n\n" + after if after else "")
                css_path.write_text(new_css)
            else:
                css_path.write_text(theme_css + "\n\n" + current)
        else:
            # no existing theme — prepend
            css_path.write_text(theme_css + "\n\n" + current)
    else:
        css_path.write_text(theme_css)

    print(f"✓ Applied preset '{preset}' to globals.css")
    print("\nNext steps:")
    print("  Add globals.css to your app stylesheets if you haven't already:")
    print('  app = rx.App(stylesheets=["globals.css"])')


def cmd_create():
    """Open the Buridan UI theme builder in the browser."""
    import webbrowser

    url = "https://buridan.reflex.run/create"
    print(f"Opening theme builder: {url}")
    webbrowser.open(url)


def cmd_add(component_names: list[str]):
    """Add one or more components and their dependencies to the project."""
    css_path = Path.cwd() / "assets" / "globals.css"
    if not css_path.exists() or ":root {" not in css_path.read_text():
        print("⚠  Warning: No theme detected in assets/globals.css.")
        print(
            "   Components use CSS variables that require a theme to render correctly."
        )
        print("   Run 'buridan apply --preset b0' to apply a default theme.\n")

    if not add_components_to_project(component_names):
        sys.exit(1)
    """Add one or more components and their dependencies to the project."""
    css_path = Path.cwd() / "assets" / "globals.css"
    if not css_path.exists() or ":root {" not in css_path.read_text():
        print("⚠  Warning: No theme detected in assets/globals.css.")
        print(
            "   Components use CSS variables that require a theme to render correctly."
        )
        print("   Run 'buridan apply --preset b0' to apply a default theme.\n")

    if not add_components_to_project(component_names):
        sys.exit(1)


def cmd_list():
    """List all available components."""
    skip = {"twmerge", "component", "base_ui", "hugeicon", "others_icons"}
    names = sorted(n for n in COMPONENT_REGISTRY if n not in skip)
    print(f"Available components ({len(names)}):\n")
    for name in names:
        print(f"  {name}")


# ── entry point ───────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        prog="buridan",
        description="Buridan UI — CLI for Reflex component library",
    )
    sub = parser.add_subparsers(dest="command")

    # create
    sub.add_parser("create", help="Open the Buridan UI theme builder in your browser")

    # apply
    apply_p = sub.add_parser(
        "apply", help="Apply a theme preset (from buridan-ui.com/create)"
    )
    apply_p.add_argument(
        "--preset", required=True, help="Preset ID e.g. b0 or b2D0wqNxT"
    )

    # add
    add_p = sub.add_parser("add", help="Add components to your project")
    add_p.add_argument("components", nargs="+", help="Component name(s) to add")

    # list
    sub.add_parser("list", help="List all available components")

    args = parser.parse_args()

    if args.command == "create":
        cmd_create()
    elif args.command == "init":
        cmd_init()
    elif args.command == "apply":
        cmd_apply(args.preset)
    elif args.command == "add":
        cmd_add(args.components)
    elif args.command == "list":
        cmd_list()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
