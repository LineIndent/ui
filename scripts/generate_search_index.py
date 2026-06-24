# import json
# from pathlib import Path

# from app.utils.routes import ALL_ROUTES


# def generate_search_index(routes: dict[str, list[dict]]) -> None:
#     data = []

#     for section, pages in routes.items():
#         for page in pages:
#             data.append(
#                 {
#                     "section": section.replace("_", " ").title(),
#                     "title": page["title"],
#                     "description": page.get("description", ""),
#                     "url": page["url"],
#                 }
#             )

#     output_dir = Path("assets/fuse")
#     output_dir.mkdir(parents=True, exist_ok=True)

#     output_file = output_dir / "searchList.json"

#     with output_file.open("w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)

#     print(f"Generated {output_file}")


# if __name__ == "__main__":
#     generate_search_index(ALL_ROUTES)


"""
Generate assets/fuse/searchList.json combining:
  - buridan/ui routes (from ALL_ROUTES)
  - Reflex docs pages (fetched from GitHub)

Usage:
    python generate_search_index.py
    python generate_search_index.py --github-token YOUR_TOKEN   # avoids rate limits
"""

import argparse
import json
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from app.utils.routes import ALL_ROUTES

REFLEX_REPO = "reflex-dev/reflex"
REFLEX_FOLDER = "docs"
REFLEX_BASE_URL = "https://reflex.dev"

# Folders inside /docs to skip (non-doc content)
SKIP_DIRS = {"__pycache__"}
SKIP_FILES = {"__init__.py"}


# ─── GitHub API ───────────────────────────────────────────────────────────────


def gh_get(path: str, token: str | None) -> list[dict] | None:
    url = f"https://api.github.com/repos/{REFLEX_REPO}/contents/{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "buridan-search-indexer",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    try:
        with urlopen(req) as resp:
            return json.loads(resp.read())
    except HTTPError as e:
        if e.code == 403:
            print(f"  [rate limited] {path} — add --github-token to avoid this")
        else:
            print(f"  [HTTP {e.code}] {path}")
        return None


def crawl_folder(folder_path: str, token: str | None, depth: int = 0) -> list[dict]:
    """Recursively walk a GitHub folder, returning .md/.mdx files."""
    if depth > 4:
        return []

    items = gh_get(folder_path, token)
    if not items or not isinstance(items, list):
        return []

    # Be polite to the API
    if depth > 0:
        time.sleep(0.15)

    results = []
    for item in items:
        name = item.get("name", "")
        itype = item.get("type", "")
        ipath = item.get("path", "")

        if itype == "dir":
            if name not in SKIP_DIRS:
                results.extend(crawl_folder(ipath, token, depth + 1))

        elif itype == "file":
            if name in SKIP_FILES:
                continue
            if not (name.endswith(".md") or name.endswith(".mdx")):
                continue
            results.append(item)

    return results


# ─── URL + title helpers ──────────────────────────────────────────────────────


def file_to_url(github_path: str) -> str:
    """
    Convert a GitHub file path like docs/getting_started/introduction.md
    to a reflex.dev URL like https://reflex.dev/docs/getting_started/introduction/
    """
    # Strip leading docs/ and file extension
    rel = github_path
    if rel.startswith(f"{REFLEX_FOLDER}/"):
        rel = rel[len(REFLEX_FOLDER) + 1 :]
    rel = rel.rsplit(".", 1)[0]  # remove .md / .mdx
    rel = rel.replace("_", "-")  # underscores -> hyphens in URLs
    return f"{REFLEX_BASE_URL}/docs/{rel}/"


def file_to_section(github_path: str) -> str:
    """
    docs/getting_started/introduction.md  ->  Getting Started
    docs/components/forms/input.md        ->  Components / Forms
    """
    parts = github_path.split("/")
    # parts[0] = "docs", parts[1] = section, parts[2+] = subsection/file
    if len(parts) >= 3:
        section = parts[1].replace("_", " ").title()
        if len(parts) >= 4:
            subsection = parts[2].replace("_", " ").title()
            return f"Reflex / {section} / {subsection}"
        return f"Reflex / {section}"
    return "Reflex"


def file_to_title(filename: str) -> str:
    """introduction.md -> Introduction"""
    stem = filename.rsplit(".", 1)[0]
    return stem.replace("_", " ").replace("-", " ").title()


# ─── Buridan routes ───────────────────────────────────────────────────────────


def buridan_entries(routes: dict) -> list[dict]:
    entries = []
    for section, pages in routes.items():
        for page in pages:
            entries.append(
                {
                    "section": section.replace("_", " ").title(),
                    "title": page["title"],
                    "url": page["url"],
                }
            )
    return entries


# ─── Reflex docs entries ──────────────────────────────────────────────────────


def reflex_entries(token: str | None) -> list[dict]:
    print(f"Fetching Reflex docs from github.com/{REFLEX_REPO}/{REFLEX_FOLDER} ...")
    files = crawl_folder(REFLEX_FOLDER, token)
    print(f"  Found {len(files)} doc files")

    entries = []
    for f in files:
        path = f["path"]
        name = f["name"]
        entries.append(
            {
                "section": file_to_section(path),
                "title": file_to_title(name),
                "url": file_to_url(path),
            }
        )
    return entries


# ─── Main ─────────────────────────────────────────────────────────────────────


def generate_search_index(
    routes: dict,
    include_reflex: bool = True,
    github_token: str | None = None,
) -> None:
    data = buridan_entries(routes)
    print(f"Buridan entries: {len(data)}")

    if include_reflex:
        reflex = reflex_entries(github_token)
        data.extend(reflex)
        print(f"Reflex entries:  {len(reflex)}")

    print(f"Total entries:   {len(data)}")

    output_dir = Path("assets/fuse")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "searchList.json"

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Written to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--github-token", default=None, help="GitHub personal access token"
    )
    parser.add_argument(
        "--no-reflex", action="store_true", help="Skip Reflex docs fetch"
    )
    args = parser.parse_args()

    generate_search_index(
        ALL_ROUTES,
        include_reflex=not args.no_reflex,
        github_token=args.github_token,
    )
