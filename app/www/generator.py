import os
import re
from typing import List

import app.www.constants as constants
from app.www.frontmatter import parse_frontmatter
from app.www.parser import DocParser

parser = DocParser(dynamic_load_dirs=[constants.DOCS_LIBRARY_ROOT, constants.COMPONENTS_ROOT])


def generate_docs_library() -> List[constants.DocDataStruct]:
    docs = []
    dev_mode = os.environ.get("BURIDAN_DEV_MODE") == "true"

    if not constants.DOCS_BASE_DIR.exists():
        print(f"Warning: Docs base directory not found: {constants.DOCS_BASE_DIR}")
        return []

    # Create a mapping from URL slug to file path for all markdown files
    all_md_files = list(constants.DOCS_BASE_DIR.glob("**/*.md"))
    slug_to_path_map = {}
    for md_file in all_md_files:
        relative_path = md_file.relative_to(constants.DOCS_BASE_DIR)
        slug = "/".join(
            [part.replace("_", "-") for part in relative_path.with_suffix("").parts]
        )
        slug_to_path_map[slug] = md_file

    md_files_to_process = []
    if dev_mode:
        print("--- Development Mode Enabled ---")
        pages_str = os.environ.get("BURIDAN_DEV_PAGES", "")
        if not pages_str:
            print("Warning: BURIDAN_DEV_PAGES is not set. Loading no pages.")
            return []

        page_slugs = [slug.strip() for slug in pages_str.split(",")]
        print(f"Loading specified pages: {page_slugs}")
        print("Loading specified URLs:")
        for slug in page_slugs:
            print(f"http://localhost:3000/docs/{slug}")
            if slug in slug_to_path_map:
                md_files_to_process.append(slug_to_path_map[slug])
            else:
                print(f"Warning: Markdown file not found for slug: {slug}")
    else:
        md_files_to_process = all_md_files

    for md_file_path in md_files_to_process:
        relative_path = md_file_path.relative_to(constants.DOCS_BASE_DIR)
        url_path_parts = [part.replace("_", "-") for part in relative_path.parts]
        url_path = "docs/" + "/".join(url_path_parts).replace(".md", "")

        # Read the markdown content
        with open(md_file_path, "r") as f:
            md_content = f.read()

        __, md_content = parse_frontmatter(md_content)

        # Extract headings for TOC from THIS file's content
        toc_data = []
        for match in re.finditer(r"^(#{1,2})\s+(.+)$", md_content, re.MULTILINE):
            level = len(match.group(1))  # Count the # characters (1-2)
            heading_text = match.group(2).strip()  # Get the heading text

            toc_data.append(
                {
                    "text": heading_text,
                    "id": heading_text,
                    "level": level,
                }
            )

        # Create the doc component (no need for inner function)
        doc = constants.DocDataStruct(
            url=url_path,
            component=parser.parse_and_render(md_content),
            table_of_content=toc_data,
        )

        docs.append(doc)

    return docs
