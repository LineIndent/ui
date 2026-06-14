import ast
import importlib
import inspect
import pathlib
import re
from pathlib import Path
from typing import Callable, Dict, List

import reflex as rx

from app.www.style import markdown_component_map, render_parse_error
from app.www.wrapper import (
    chart_util_wrapper,
    cli_and_manual_installation_wrapper,
    demo_wrapper,
    usage_wrapper,
)


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
                        or isinstance(o, rx.ComponentNamespace)
                    ) and o.__module__ == mod.__name__:
                        self.registry[n.lower()] = o

    def _render(self, cmd: str, arg: str) -> rx.Component:
        try:
            val = (
                ast.literal_eval(arg)
                if arg and any(arg.startswith(c) for c in "[{'\"")
                else arg
            )
            name = val[0] if isinstance(val, list) else val
            obj = self.registry.get(str(name).lower())
            if not obj:
                return render_parse_error(f"'{name}' not found")

            # Use the class for inspection if obj is an instance (like ComponentNamespace)
            inspect_obj = obj
            if not (
                inspect.isclass(obj) or inspect.isfunction(obj) or inspect.ismodule(obj)
            ):
                inspect_obj = getattr(obj, "__class__", obj)

            # Check if it's a chart-related component
            try:
                file_path = inspect.getfile(inspect_obj)
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
                mod = inspect.getmodule(inspect_obj)
                if not mod:
                    return render_parse_error(f"Module not found for {name}")
                src = inspect.getsource(mod).strip()
                return cli_and_manual_installation_wrapper(val[1], src, val[0])

            if cmd == "usage":
                import_name = getattr(obj, "__name__", str(name))
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
                    class_name="w-full mt-4 mb-8 rounded-[0.625rem] outline outline-input flex-1 min-h-0 flex flex-col bg-secondary dark:bg-card",
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
