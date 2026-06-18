import ast
import importlib
import inspect
import pathlib
import re
from pathlib import Path
from typing import Callable, Dict, List

import reflex as rx

from app.registry.components import COMPONENT_REGISTRY
from app.www.style import markdown_component_map, render_parse_error
from app.www.wrapper import (
    chart_util_wrapper,
    cli_and_manual_installation_wrapper,
    demo_wrapper,
    usage_wrapper,
)


def get_all_dependencies(name: str, registry: Dict) -> List[str]:
    """Recursively get all dependencies for a component in correct order."""
    deps = []

    def resolve(comp_name: str):
        comp = registry.get(comp_name.lower())
        if not comp:
            return
        for dep in comp.get("dependencies", []):
            if dep not in deps:
                resolve(dep)
        if comp_name not in deps:
            deps.append(comp_name)

    resolve(name)
    return deps


class DocParser:
    """Minimal markdown parser for Reflex documentation."""

    def __init__(
        self, registry: Dict[str, Callable] = None, dynamic_load_dirs: List[str] = None
    ):
        self.registry = registry or {}
        root = pathlib.Path(__file__).parent.parent.parent
        for d in dynamic_load_dirs or []:
            for py in (root / d).rglob("*.py"):
                if py.name.startswith("__"):
                    continue
                mod = importlib.import_module(
                    ".".join(py.relative_to(root).with_suffix("").parts)
                )
                for n, o in inspect.getmembers(mod):
                    if (
                        inspect.isfunction(o)
                        or inspect.isclass(o)
                        or inspect.ismethod(o)
                        or isinstance(o, rx.ComponentNamespace)
                    ) and getattr(o, "__module__", None) == mod.__name__:
                        self.registry[n.lower()] = (o, n)

    def _render(self, cmd: str, arg: str) -> rx.Component:

        try:
            val = (
                ast.literal_eval(arg)
                if arg and any(arg.startswith(c) for c in "[{'\"")
                else arg
            )
            name = val[0] if isinstance(val, list) else val
            
            registry_entry = self.registry.get(str(name).lower())
            if not registry_entry and cmd != "install":
                return render_parse_error(f"'{name}' not found")
            
            obj, preferred_name = (
                registry_entry if registry_entry else (None, str(name))
            )

            # Use the class for inspection if obj is an instance (like ComponentNamespace)
            inspect_obj = obj
            if obj and not (
                inspect.isclass(obj) or inspect.isfunction(obj) or inspect.ismodule(obj)
            ):
                inspect_obj = getattr(obj, "__class__", obj)

            # Check if it's a chart-related component
            try:
                file_path = inspect.getfile(inspect_obj) if inspect_obj else ""
                is_chart = "charts" in file_path
            except (TypeError, ValueError):
                is_chart = False
                file_path = ""

            if "demo" in cmd:
                # src = inspect.getsource(obj).strip()
                src = Path(inspect.getsourcefile(obj)).read_text().strip()
                return demo_wrapper(obj(), src)

            if "code" in cmd:
                src = (
                    inspect.getsource(inspect.getmodule(inspect_obj))
                    if "_file" in cmd
                    else inspect.getsource(obj)
                ).strip()

                return chart_util_wrapper(source=src)

            if cmd == "install":
                comp_name = str(name).lower()
                all_deps = get_all_dependencies(comp_name, COMPONENT_REGISTRY)
                if not all_deps:
                    return render_parse_error(
                        f"Component '{name}' not found in registry"
                    )

                files_data = []
                for dep in all_deps:
                    comp_info = COMPONENT_REGISTRY.get(dep)
                    for f_path in comp_info.get("files", []):
                        try:
                            content = Path(f_path).read_text().strip()
                            files_data.append((f_path, content))
                        except Exception as e:
                            return render_parse_error(f"Error reading {f_path}: {e}")

                cli_cmd = f"uv run buridan add component {comp_name}"
                return cli_and_manual_installation_wrapper(cli_cmd, files_data)

            if cmd == "usage":
                import_name = preferred_name
                module_stem = pathlib.Path(file_path).stem if file_path else "component"
                return usage_wrapper(
                    f"from components.ui.{module_stem} import {import_name}"
                )

            if cmd == "anatomy":
                from app.www.anatomy import ANATOMY

                src = ANATOMY.get(str(name).lower())
                if not src:
                    return render_parse_error(f"No anatomy found for '{name}'")
                return rx.el.div(
                    rx.el.code(
                        src,
                        style={
                            "white-space": "pre",
                            "color": "var(--foreground)",
                            "font-size": "13px",
                            "padding": "1rem 0.75rem",
                            "display": "block",
                        },
                    ),
                    class_name="overflow-x-auto overflow-y-auto scrollbar-none w-full mt-4 mb-8 rounded-[1rem] outline outline-input flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card",
                )

            return render_parse_error(f"Unknown command: {cmd}")
        except Exception as e:
            return render_parse_error(f"Error in {cmd}: {e}")

    def parse_and_render(self, content: str) -> List[rx.Component]:
        res = []
        for s in re.split(r"(--[\w_]+(?:\([^)]+\))?--)", content):
            if m := re.match(r"--([\w_]+)(?:\(([^)]+)\))?--", s):
                res.append(self._render(m.group(1).lower(), m.group(2)))
            elif t := s.strip():
                res.append(rx.markdown(t, component_map=markdown_component_map))

        return res
