import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils.routes import (
    BASE_UI_COMPONENTS,
    CHARTS_URLS,
    GET_STARTED_URLS,
    RESOURCES_URLS,
    UTILITIES,
)

BASE_URL = "https://buridan.reflex.run"


def generate_llms_txt() -> str:
    def make_links(routes):
        return "\n".join(
            f"- [{route['title']}]({BASE_URL}/{route['url']}): The {route['title']} component."
            for route in routes
            if route.get("url") and route["url"] != "llms.txt"
        )

    getting_started = "\n".join(
        f"- [{r['title']}]({BASE_URL}/{r['url']}): {r['title']} page."
        for r in GET_STARTED_URLS
        if r.get("url") and r["url"] != "llms.txt"
    )

    resources = "\n".join(
        f"- [{r['title']}]({BASE_URL}/{r['url']}): {r['title']} page."
        for r in RESOURCES_URLS
        if r.get("url")
    )

    components = make_links(BASE_UI_COMPONENTS)
    charts = make_links(CHARTS_URLS)
    utilities = make_links(UTILITIES)

    return f"""# buridan/ui

> Composable, themeable components designed for Reflex. Extend, override, and ship without fighting the framework. Open source. It is built for Reflex using Python. Open Code. AI-ready. It also comes with a command-line tool to install and manage components.

## Overview
{getting_started}

## Resources
{resources}

## Components
{components}

## Charts
{charts}

## Utilities
{utilities}
"""


if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(__file__), "..", "assets", "llms.txt")
    content = generate_llms_txt()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"llms.txt written to {output_path}")
