import ast
import importlib
import inspect
import pathlib
import re
import shutil
import sys

# Add the project root to the Python path to allow imports
ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

# --- PATHS ---
DOCS_SOURCE_DIR = ROOT_DIR / "docs"
MARKDOWN_OUTPUT_DIR = ROOT_DIR / "assets" / "docs"
DYNAMIC_LOAD_DIRS = ["app/www/library", "components/ui"]


def dynamic_load_components(dirs: list[str]) -> dict:
    """
    Dynamically loads component functions and classes from given directories.
    """
    registry = {}
    for d in dirs:
        dir_path = ROOT_DIR / d
        if not dir_path.exists():
            print(f"Warning: Directory not found: {dir_path}")
            continue

        for py_file in dir_path.rglob("*.py"):
            if py_file.name.startswith("__"):
                continue

            relative_py_file = py_file.relative_to(ROOT_DIR)
            module_path = ".".join(relative_py_file.with_suffix("").parts)

            try:
                module = importlib.import_module(module_path)
                # First, identify objects defined in this module
                for name, obj in inspect.getmembers(module):
                    if (
                        hasattr(obj, "__module__") and obj.__module__ == module.__name__
                    ) or (
                        # Handle cases where __module__ might be different but it's defined here
                        # or it's a ComponentNamespace
                        getattr(obj, "__module__", None) == module.__name__
                    ):
                        # Check if it's a function, class, method, or callable assigned to a name
                        if (
                            inspect.isfunction(obj)
                            or inspect.isclass(obj)
                            or inspect.ismethod(obj)
                            or callable(obj)
                        ):
                            registry[name.lower()] = (obj, name)
            except Exception as e:
                print(
                    f"Warning: Could not import from module {module_path}. Error: {e}",
                    file=sys.stderr,
                )
    return registry


def convert_to_pure_markdown(content: str, registry: dict) -> str:
    """
    Replaces custom component delimiters in markdown content with formatted code blocks.
    """
    delimiter_pattern = r"--([\w_]+)(?:\((.*)\))?--"

    def replacer(match):
        cmd = match.group(1).lower()
        arg = match.group(2)

        try:
            # Parse argument (handle strings or lists)
            val = (
                ast.literal_eval(arg)
                if arg and any(arg.startswith(c) for c in "[{'\"")
                else arg
            )
            name = val[0] if isinstance(val, list) else val
            registry_entry = registry.get(str(name).lower())

            if not registry_entry and cmd != "anatomy":
                return f"\n> **Error: '{name}' not found in registry**\n"

            obj, preferred_name = (
                registry_entry if registry_entry else (None, str(name))
            )

            # Use the class for inspection if obj is an instance (like ComponentNamespace)
            inspect_obj = obj
            if obj and not (
                inspect.isclass(obj)
                or inspect.isfunction(obj)
                or inspect.ismodule(obj)
                or inspect.ismethod(obj)
            ):
                inspect_obj = getattr(obj, "__class__", obj)

            # 1. Anatomy logic
            if cmd == "anatomy":
                from app.www.anatomy import ANATOMY

                src = ANATOMY.get(str(name).lower())
                if not src:
                    return f"\n> **Error: No anatomy found for '{name}'**\n"
                return f"\n```python\n{src.strip()}\n```\n"

            # 2. Demo logic (source code of the specific function)
            if "demo" in cmd:
                try:
                    src = inspect.getsource(obj).strip()
                    return f"\n```python\n{src}\n```\n"
                except Exception as e:
                    return f"\n> **Error getting source for {name}: {e}**\n"

            # 3. Code / Code File logic
            if "code" in cmd:
                try:
                    language = "python"
                    if isinstance(val, list) and len(val) > 1:
                        language = val[1] or "python"

                    if "_file" in cmd:
                        # Full module source
                        module = inspect.getmodule(inspect_obj)
                        src = inspect.getsource(module).strip()
                    else:
                        # Specific object source
                        src = (
                            inspect.getsource(obj)
                            if not inspect.ismethod(obj)
                            else inspect.getsource(inspect_obj)
                        )
                        src = src.strip()

                    return f"\n```{language}\n{src}\n```\n"
                except Exception as e:
                    return f"\n> **Error getting code for {name}: {e}**\n"

            # 4. Install logic
            if cmd == "install":
                try:
                    # val is ["Name", "cli_command"] or "Name"
                    cli_cmd = (
                        val[1]
                        if isinstance(val, list) and len(val) > 1
                        else f"buridan add component {str(name).lower()}"
                    )
                    module = inspect.getmodule(inspect_obj)
                    module_src = inspect.getsource(module).strip()

                    return (
                        f"### CLI\n\n```bash\n{cli_cmd}\n```\n\n"
                        f"### Manual Installation\n\n```python\n{module_src}\n```\n"
                    )
                except Exception as e:
                    return f"\n> **Error processing install for {name}: {e}**\n"

            # 5. Usage logic
            if cmd == "usage":
                try:
                    file_path = inspect.getfile(inspect_obj)
                    module_stem = pathlib.Path(file_path).stem
                    return f"\n```python\nfrom components.ui.{module_stem} import {preferred_name}\n```\n"
                except Exception as e:
                    return f"\n> **Error processing usage for {name}: {e}**\n"

            return f"\n> **Warning: Unknown command '{cmd}'**\n"

        except Exception as e:
            return f"\n> **Error in {cmd}: {e}**\n"

    # Remove frontmatter if present (consistent with generator.py)
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) > 2:
            content = parts[2]

    return re.sub(delimiter_pattern, replacer, content)


def main():
    """Main function to generate pure markdown files from the docs directory."""
    print("Starting markdown generation process...")

    # Clean up old output directory
    if MARKDOWN_OUTPUT_DIR.exists():
        shutil.rmtree(MARKDOWN_OUTPUT_DIR)
        print(f"Cleaned up old output: {MARKDOWN_OUTPUT_DIR}")

    # Load components from all target directories
    print(f"Loading components from: {DYNAMIC_LOAD_DIRS}")
    component_registry = dynamic_load_components(DYNAMIC_LOAD_DIRS)
    print(f"Successfully loaded {len(component_registry)} objects into registry.")

    # Ensure output directory exists
    MARKDOWN_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Process markdown files
    print(f"Processing markdown files from: {DOCS_SOURCE_DIR}")
    file_count = 0
    for md_file in DOCS_SOURCE_DIR.rglob("*.md"):
        file_count += 1
        original_content = md_file.read_text()
        pure_md_content = convert_to_pure_markdown(original_content, component_registry)

        # Create new path with hyphens (e.g., getting_started -> getting-started)
        relative_path = md_file.relative_to(DOCS_SOURCE_DIR)
        hyphenated_parts = [part.replace("_", "-") for part in relative_path.parts]
        output_path = MARKDOWN_OUTPUT_DIR / pathlib.Path(*hyphenated_parts)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(pure_md_content)

        print(
            f"Processed: {md_file.relative_to(ROOT_DIR)} -> {output_path.relative_to(ROOT_DIR)}"
        )

    print(f"\nMarkdown generation complete. Processed {file_count} files.")


if __name__ == "__main__":
    main()
