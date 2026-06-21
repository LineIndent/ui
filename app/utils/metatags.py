BURIDAN_URL = "https://buridan.reflex.run/"

BURIDAN_KEY_WORDS = (
    "buridan, ui, web apps, framework, open source, frontend, backend, full stack"
)

SOCIAL_CARD_BASE_PATH = (
    "https://raw.githubusercontent.com/LineIndent/ui/refs/heads/main/assets/social/"
)

BURIDAN_KEY_WORDS = (
    "buridan, ui, web apps, framework, open source, frontend, backend, full stack"
)


def generate_site_meta_tags(title: str, url: str, description: str, social_card: str):
    return [
        {"name": "application-name", "content": title},
        {"name": "keywords", "content": BURIDAN_KEY_WORDS},
        {"name": "description", "content": description},
        {"property": "og:url", "content": f"{BURIDAN_URL}{url}"},
        {"property": "og:type", "content": "website"},
        {"property": "og:title", "content": title},
        {"property": "og:description", "content": description},
        {"property": "og:image", "content": f"{SOCIAL_CARD_BASE_PATH}{social_card}"},
        {"property": "og:image:width", "content": "1200"},
        {"property": "og:image:height", "content": "630"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:domain", "content": "buridan.reflex.run"},
        {"property": "twitter:url", "content": f"{BURIDAN_URL}{url}"},
        {"name": "twitter:title", "content": title},
        {"name": "twitter:description", "content": description},
        {"name": "twitter:image", "content": f"{SOCIAL_CARD_BASE_PATH}{social_card}"},
    ]
