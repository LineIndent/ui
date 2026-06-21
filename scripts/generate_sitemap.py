import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils.routes import (
    BASE_UI_COMPONENTS,
    CHARTS_URLS,
    GET_STARTED_URLS,
    RESOURCES_URLS,
)

BASE_URL = "https://buridan.reflex.run"

TOP_LEVEL = ["/", "/components", "/charts", "/create"]


def generate_sitemap() -> str:
    all_routes = GET_STARTED_URLS + RESOURCES_URLS + BASE_UI_COMPONENTS + CHARTS_URLS

    top = "\n".join(f"  <url><loc>{BASE_URL}{path}</loc></url>" for path in TOP_LEVEL)

    pages = "\n".join(
        f"  <url><loc>{BASE_URL}/{route['url']}</loc></url>"
        for route in all_routes
        if route.get("url") and route["url"] != "llms.txt"
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{top}
{pages}
</urlset>"""


if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(__file__), "..", "assets", "sitemap.xml")
    sitemap = generate_sitemap()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"sitemap.xml written to {output_path}")
