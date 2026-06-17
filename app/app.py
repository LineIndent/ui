import reflex as rx

app = rx.App(
    head_components=[
        rx.el.script(src="/prism/prism.js"),
    ],
    stylesheets=[
        # --- Site CSS ---
        "globals.css",
        # --- Prism CSS ---
        "prism/prism.css",
        # --- Sans Fonts ---
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap",
        "https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;500;600;700&display=swap",
        "https://cdn.jsdelivr.net/npm/geist@1.3.0/dist/font/sans.css",
        # --- Serif Fonts ---
        "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap",
        "https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400..700;1,400..700&display=swap",
        "https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap",
        # --- Monospace Fonts ---
        "https://fonts.googleapis.com/css2?family=Fira+Code:wght@300..700&display=swap",
        "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&display=swap",
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600&display=swap",
        "https://cdn.jsdelivr.net/npm/geist@1.3.0/dist/font/mono.css",
    ],
)


export_site(app=app)
