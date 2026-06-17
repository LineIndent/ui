import reflex as rx

from app.pages.charts import chart_page
from app.pages.components import components_page
from app.pages.landing import landing_page
from app.templates.docpage import docpage
from app.templates.mainpage import mainpage
from app.templates.toc import table_of_content
from app.utils.metatags import generate_site_meta_tags
from app.www.generator import generate_docs_library

BURIDAN_URL = "https://buridan.reflex.run/"
BURIDAN_SLOGAN = (
    "Beautifully designed Reflex components to build your web apps faster. Open source."
)
BURIDAN_KEY_WORDS = (
    "buridan, ui, web apps, framework, open source, frontend, backend, full stack"
)
SITE_LOGO_URL = "https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/site/site_preview.webp"

SITE_META_TAGS = [
    {"name": "application-name", "content": "Buridan UI"},
    {"name": "keywords", "content": BURIDAN_KEY_WORDS},
    {"name": "description", "content": BURIDAN_SLOGAN},
    {"property": "og:url", "content": BURIDAN_URL},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Buridan UI"},
    {"property": "og:description", "content": BURIDAN_SLOGAN},
    {"property": "og:image", "content": SITE_LOGO_URL},
    {"property": "og:image:width", "content": "1200"},
    {"property": "og:image:height", "content": "630"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": BURIDAN_URL},
    {"property": "twitter:url", "content": BURIDAN_URL},
    {"name": "twitter:title", "content": "Buridan UI"},
    {"name": "twitter:description", "content": BURIDAN_SLOGAN},
    {"name": "twitter:image", "content": SITE_LOGO_URL},
]


app = rx.App(
    head_components=[
        rx.el.script(src="/prism/prism.js"),
    ],
    stylesheets=[
        "globals.css",
        # --- Prism CSS ---
        "prism/prism.css",
        # --- Sans Fonts ---
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;500;600;700&display=swap",
        "https://cdn.jsdelivr.net/npm/geist@1.3.0/dist/font/sans.css",  # Geist Sans
        # --- Serif Fonts ---
        "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap",
        "https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&display=swap",
        "https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap",
        # --- Monospace Fonts ---
        "https://fonts.googleapis.com/css2?family=Fira+Code:wght@300..700&display=swap",
        "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&display=swap",
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600&display=swap",
        "https://cdn.jsdelivr.net/npm/geist@1.3.0/dist/font/mono.css",  # Geist Mono
    ],
)

app.add_page(
    component=mainpage(),
    route="/create",
    title="New Project - buridan/ui",
    meta=SITE_META_TAGS,
)

app.add_page(
    component=chart_page(),
    route="/charts",
    title="Charts - buridan/ui",
    meta=SITE_META_TAGS,
)

app.add_page(
    component=components_page(),
    route="/components",
    title="Components - buridan/ui",
    meta=SITE_META_TAGS,
)

app.add_page(
    component=landing_page(),
    route="/",
    title="The UI Library for Reflex Developers - buridan/ui",
    meta=SITE_META_TAGS,
)

# Add all the documentation pages
for doc in generate_docs_library():
    main_content = rx.el.div(*doc.component, class_name="w-full")
    toc_content = table_of_content(doc.url, doc.table_of_content)

    title_s = doc.url.split("/")[-1].replace("-", " ").title()
    title = f"{title_s} – buridan/ui"
    card_path = f"https://raw.githubusercontent.com/LineIndent/ui/refs/heads/main/assets/social/{doc.url.split('/')[-1]}.webp"
    print(card_path)
    app.add_page(
        docpage(main_content, toc_content),
        route=f"/{doc.url}",
        title=title,
        meta=generate_site_meta_tags(
            title=title_s,
            url=f"https://buridan.reflex.run/{doc.url}",
            description=doc.description,
            social_card=card_path,
        ),
    )
