import argparse
import ast
import os
import shutil
import sys
from pathlib import Path

# Import registries
from app.registry.colors import COLOR_THEMES
from app.registry.components import COMPONENT_REGISTRY
from app.registry.fonts import FONT_REGISTRY
from app.registry.radii import RADIUS_OPTIONS
from app.registry.styles import STYLE_REGISTRY
from app.registry.themes import BASE_THEMES

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def from_base62(s):
    n = 0
    for i in range(len(s) - 1, -1, -1):
        n = n * 62 + CHARS.find(s[i])
    return n


def flatten_vars(obj):
    out = {}
    for k, v in obj.items():
        key = "--radius" if k == "radius" else f"--{k}"
        out[key] = v
    return out


def rebuild_theme(config):
    base_id = config.get("baseId")
    color_id = config.get("colorId")
    chart_id = config.get("chartId")
    style_id = config.get("styleId")
    font_id = config.get("fontId")
    radius = config.get("radius")
    dark_mode = config.get("darkMode", False)

    base = next((b for b in BASE_THEMES if b["id"] == base_id), None)
    if not base:
        return {}

    base_vars = flatten_vars(base["dark"] if dark_mode else base["light"])
    theme = {**base_vars}

    if color_id:
        color = next((c for c in COLOR_THEMES if c["id"] == color_id), None)
        if color:
            cvars = flatten_vars(color["dark"] if dark_mode else color["light"])
            for k, v in cvars.items():
                if not k.startswith("--chart-"):
                    theme[k] = v

    if chart_id:
        chart = next((c for c in COLOR_THEMES if c["id"] == chart_id), None)
        if chart:
            cvars = flatten_vars(chart["dark"] if dark_mode else chart["light"])
            for k, v in cvars.items():
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


def decode_seed(seed):
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


def generate_from_seed(seed, dark_mode):
    config = decode_seed(seed)
    if not config:
        # For simplicity in CLI, we only support valid encoded seeds
        print(f"Error: Invalid preset ID '{seed}'")
        sys.exit(1)

    config["darkMode"] = dark_mode
    return rebuild_theme(config)


def format_css(config):
    return "\n".join(
        [f"    {k}: {v};" for k, v in config.items() if k.startswith("--")]
    )


def generate_full_css(seed):
    light_config = generate_from_seed(seed, False)
    dark_config = generate_from_seed(seed, True)
    return f":root {{\n{format_css(light_config)}\n}}\n\n.dark {{\n{format_css(dark_config)}\n}}"


TAILWIND_CONFIG_SNIPPET = """        rx.plugins.TailwindV4Plugin(
            TailwindConfig(
                darkMode="class",
                plugins=["@tailwindcss/typography", "tailwind-scrollbar"],
                theme={
                    "extend": {
                        "colors": {
                            "background": "var(--background)",
                            "foreground": "var(--foreground)",
                            "card": "var(--card)",
                            "card-foreground": "var(--card-foreground)",
                            "popover": "var(--popover)",
                            "popover-foreground": "var(--popover-foreground)",
                            "primary": "var(--primary)",
                            "primary-foreground": "var(--primary-foreground)",
                            "secondary": "var(--secondary)",
                            "secondary-foreground": "var(--secondary-foreground)",
                            "muted": "var(--muted)",
                            "muted-foreground": "var(--muted-foreground)",
                            "accent": "var(--accent)",
                            "accent-foreground": "var(--accent-foreground)",
                            "destructive": "var(--destructive)",
                            "border": "var(--border)",
                            "input": "var(--input)",
                            "ring": "var(--ring)",
                            "chart-1": "var(--chart-1)",
                            "chart-2": "var(--chart-2)",
                            "chart-3": "var(--chart-3)",
                            "chart-4": "var(--chart-4)",
                            "chart-5": "var(--chart-5)",
                            "sidebar": "var(--sidebar)",
                            "sidebar-foreground": "var(--sidebar-foreground)",
                            "sidebar-primary": "var(--sidebar-primary)",
                            "sidebar-primary-foreground": "var(--sidebar-primary-foreground)",
                            "sidebar-accent": "var(--sidebar-accent)",
                            "sidebar-accent-foreground": "var(--sidebar-accent-foreground)",
                            "sidebar-border": "var(--sidebar-border)",
                            "sidebar-ring": "var(--sidebar-ring)",
                        },
                        "fontFamily": {
                            "theme": "var(--font-family)",
                        },
                        "borderRadius": {
                            "radius": "var(--radius)",
                        },
                        "padding": {
                            "card": "var(--card-padding)",
                        },
                        "gap": {
                            "card": "var(--card-gap)",
                        },
                        "boxShadow": {
                            "default": "var(--shadow)",
                        },
                    }
                },
            )
        ),"""


def get_source_root():
    """Locate the Buridan UI source components."""
    # 1. Check relative to this file (development mode)
    # cli/main.py -> ROOT
    source_root = Path(__file__).parent.parent
    if (source_root / "components").exists():
        return source_root

    # 2. Try to find the 'components' package
    try:
        import components
        return Path(components.__file__).parent.parent
    except (ImportError, AttributeError):
        return None


def resolve_dependencies(component_names, registry):
    """Recursively resolve dependencies for a list of components."""
    required_files = set()
    visited_components = set()

    def add_component(name):
        name_lower = name.lower()
        if name_lower in visited_components:
            return
        visited_components.add(name_lower)

        entry = registry.get(name_lower)
        if not entry:
            print(f"Warning: Component '{name}' not found in registry.")
            return

        for file_path in entry["files"]:
            required_files.add(file_path)

        for dep in entry.get("dependencies", []):
            add_component(dep)

    for name in component_names:
        add_component(name)

    return sorted(list(required_files))


def add_components_to_project(component_names, target_root=None):
    """Add components and their dependencies to the target project."""
    if target_root is None:
        target_root = Path.cwd()

    if not (target_root / "rxconfig.py").exists():
        print("Error: rxconfig.py not found. Please run this command in a Reflex project root.")
        return False

    source_root = get_source_root()
    if not source_root:
        print("Error: Could not locate Buridan source components. Are you in the repo or is it installed?")
        return False

    files_to_copy = resolve_dependencies(component_names, COMPONENT_REGISTRY)
    if not files_to_copy:
        print("No files to copy.")
        return False

    for rel_path_str in files_to_copy:
        src_path = source_root / rel_path_str
        dest_path = target_root / rel_path_str

        if not src_path.exists():
            print(f"Warning: Source file {src_path} does not exist.")
            continue

        # Create target directory
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        # Ensure __init__.py files exist up to the components root
        current_dir = dest_path.parent
        while current_dir != target_root and current_dir.name != "":
            init_file = current_dir / "__init__.py"
            if not init_file.exists():
                init_file.touch()
            if current_dir.name == "components":
                break
            current_dir = current_dir.parent

        # Copy the file
        shutil.copy2(src_path, dest_path)
        print(f"✓ Added {rel_path_str}")

    return True


def init(preset, include):
    root = Path.cwd()
    config_path = root / "rxconfig.py"

    if not config_path.exists():
        print(
            "Error: rxconfig.py not found. Please run this command in a Reflex project root."
        )
        return

    # 1. Generate globals.css
    assets_dir = root / "assets"
    assets_dir.mkdir(exist_ok=True)
    css_path = assets_dir / "globals.css"
    css_content = generate_full_css(preset)
    css_path.write_text(css_content)
    print(f"✓ Created {css_path.relative_to(root)}")

    # 2. Update rxconfig.py Safely
    config_content = config_path.read_text()

    if "var(--background)" in config_content:
        print(f"• rxconfig.py already contains Buridan UI theme tokens.")
    else:
        try:
            tree = ast.parse(config_content)
            modified = False
            clean_snippet = TAILWIND_CONFIG_SNIPPET.strip().rstrip(",")

            # Look for ANY assignment that looks like a Reflex config
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    # Check if the right side is rx.Config(...) or rx.config(...)
                    call_node = node.value
                    if (
                        isinstance(call_node, ast.Call)
                        and isinstance(call_node.func, ast.Attribute)
                        and call_node.func.attr.lower() == "config"
                        and getattr(call_node.func.value, "id", "") == "rx"
                    ):
                        # Found it!
                        lines = config_content.splitlines()
                        plugins_kw = next(
                            (kw for kw in call_node.keywords if kw.arg == "plugins"),
                            None,
                        )

                        if plugins_kw:
                            # Scenario 1: plugins=[] exists
                            target_line_idx = -1
                            # Search only within the call node's range
                            for i in range(call_node.lineno - 1, call_node.end_lineno):
                                if "plugins=" in lines[i]:
                                    target_line_idx = i
                                    break
                            
                            if target_line_idx != -1:
                                lines[target_line_idx] = lines[target_line_idx].replace(
                                    "plugins=[", f"plugins=[\n{clean_snippet},"
                                )
                                config_content = "\n".join(lines)
                                modified = True
                        else:
                            # Scenario 2: plugins keyword is missing
                            target_line_idx = -1
                            for i in range(call_node.lineno - 1, call_node.end_lineno):
                                if "Config(" in lines[i] or "config(" in lines[i]:
                                    target_line_idx = i
                                    break
                            
                            if target_line_idx != -1:
                                indent = " " * (len(lines[target_line_idx]) - len(lines[target_line_idx].lstrip()))
                                lines[target_line_idx] = lines[target_line_idx].replace(
                                    "(", f"(\n{indent}    plugins=[\n{clean_snippet}\n{indent}    ],"
                                )
                                config_content = "\n".join(lines)
                                modified = True
                        
                        if modified:
                            # Clean up potential duplicates or empty calls
                            config_content = config_content.replace("rx.plugins.TailwindV4Plugin(),", "")
                            config_content = config_content.replace("rx.plugins.TailwindV4Plugin()", "")
                            config_content = config_content.replace(",,", ",")
                            print(f"✓ Updated rxconfig.py with Buridan UI tokens.")
                            break
            
            if not modified:
                # Last resort fallback: Simple string replacement if AST failed to identify nodes correctly
                if "rx.Config(" in config_content or "rx.config(" in config_content:
                    print("• Using string replacement fallback for rxconfig.py...")
                    config_content = config_content.replace(
                        "rx.Config(", f"rx.Config(\n    plugins=[\n{clean_snippet}\n    ],"
                    ).replace(
                        "rx.config(", f"rx.config(\n    plugins=[\n{clean_snippet}\n    ],"
                    )
                    modified = True

            if modified:
                import_stmt = "from reflex.plugins.shared_tailwind import TailwindConfig"
                if import_stmt not in config_content:
                    config_content = f"{import_stmt}\n{config_content}"
                config_path.write_text(config_content)
            else:
                print("Warning: Could not automatically update rxconfig.py. Please add the Buridan UI Tailwind snippet manually.")

        except Exception as e:
            print(f"Warning: Could not parse rxconfig.py ({e}). Please configure manually.")

    # 3. Include components if full
    if include == "full":
        # For 'full', we'll add ALL components from the registry
        all_components = [
            name
            for name in COMPONENT_REGISTRY.keys()
            if name
            not in ["twmerge", "component", "base_ui", "hugeicon", "others_icons"]
        ]
        print(f"Adding all {len(all_components)} components to project...")
        add_components_to_project(all_components, target_root=root)

    print("\nSuccess! Buridan UI has been initialized.")
    print("Next steps:")
    print("1. Update your rx.App initialization in your main file:")
    print('   app = rx.App(stylesheets=["globals.css"])')
    print("2. You can now add more components using 'buridan add <name>'")


def main():
    parser = argparse.ArgumentParser(description="Buridan UI CLI")
    subparsers = parser.add_subparsers(dest="command")

    # init command
    init_parser = subparsers.add_parser(
        "init", help="Initialize Buridan UI in a project"
    )
    init_parser.add_argument(
        "--preset", required=True, help="Theme preset ID (e.g. b0, b2D0wqNxT)"
    )
    init_parser.add_argument(
        "--include",
        choices=["full", "theme-only"],
        default="full",
        help="What to include (default: full)",
    )

    # add command
    add_parser = subparsers.add_parser(
        "add", help="Add components to your project"
    )
    add_parser.add_argument(
        "components", nargs="+", help="Names of components to add"
    )

    # list command
    subparsers.add_parser(
        "list", help="List all available components"
    )

    args = parser.parse_args()

    if args.command == "init":
        init(args.preset, args.include)
    elif args.command == "add":
        add_components_to_project(args.components)
    elif args.command == "list":
        print("Available components:")
        # Filter out utilities and icons for a cleaner list, or show all?
        # Let's show all that aren't purely internal utilities
        for name in sorted(COMPONENT_REGISTRY.keys()):
            if name not in ["twmerge", "component", "base_ui", "hugeicon", "others_icons"]:
                print(f"  - {name}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
