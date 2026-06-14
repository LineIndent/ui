from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import reflex as rx


@dataclass
class DocDataStruct:
    """The data structure for the generated doc page"""

    url: str
    component: List[rx.Component]
    table_of_content: List[Dict]


# --- Docs Path Constants ---
DOCS_BASE_DIR = Path("docs")
DOCS_LIBRARY_ROOT = "app/www/library"
COMPONENTS_ROOT = "components/ui"
