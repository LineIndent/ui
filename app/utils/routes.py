import glob
import os

import app.www.constants as constants
from app.www.frontmatter import parse_frontmatter


# --- Method: Generate doc routes/urls ---
def generate_doc_routes(section_folder, base_path) -> list[dict]:
    """
    Generates routes for a documentation section by recursively reading
    frontmatter from markdown files.

    Args:
        section_folder: The folder name inside 'docs/' (e.g., 'getting_started').
        base_path: The base URL path for the routes (e.g., 'docs/getting-started/').

    Returns:
        A list of route dictionaries, sorted by the 'order' in metadata.
    """
    routes = []
    docs_path = f"{constants.DOCS_BASE_DIR}/{section_folder}"
    search_path = os.path.join(docs_path, "**/*.md")

    md_files = glob.glob(search_path, recursive=True)

    if not md_files:
        print(f"Warning: No markdown files found in '{docs_path}'")
        return []

    for file_path in md_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            continue

        metadata, _ = parse_frontmatter(content)

        if not metadata or "title" not in metadata:
            continue

        # Create a URL slug from the file path relative to the section folder.
        relative_path = os.path.relpath(file_path, docs_path)
        path_slug = relative_path.replace(".md", "").replace("_", "-")

        route_info = {
            "title": metadata["title"],
            "url": f"{base_path}{path_slug}",  # Will include docs/ prefix
            "order": metadata.get("order", 0),
        }

        routes.append(route_info)

    routes.sort(key=lambda x: x["order"])

    return routes


# --- Static: Each generation corresponds to a file in the docs/ folder ---
GET_STARTED_URLS = generate_doc_routes("getting_started", "docs/getting-started/")
BASE_UI_COMPONENTS = sorted(
    generate_doc_routes("components", "docs/components/"), key=lambda x: x["title"]
)
CHARTS_URLS = sorted(
    generate_doc_routes("charts", "docs/charts/"), key=lambda x: x["title"]
)
# WRAPPED_COMPONENTS_URLS = generate_doc_routes(
#     "wrapped_components", "docs/wrapped-components/"
# )
# JS_INTEGRATIONS_URLS = generate_doc_routes(
#     "javascript_integrations", "docs/javascript-integrations/"
# )
