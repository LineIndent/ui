import reflex as rx

from app.pages.blocks import blocks_page
from app.pages.charts import chart_page
from app.pages.components import components_page
from app.pages.landing import landing_page
from app.templates.docpage import docpage
from app.templates.mainpage import mainpage
from app.templates.toc import table_of_content
from app.utils.metatags import generate_site_meta_tags
from app.www.generator import generate_docs_library


def export_site(app: rx.App):
    app.add_page(
        component=mainpage(),
        route="/create",
        title="New Project - buridan/ui",
        meta=generate_site_meta_tags(
            title="New Project",
            url="/create",
            description="Build your theme system for Reflex. Customize everything from the ground up. Pick your font, color scheme, and more.",
            social_card="create.webp",
        ),
    )

    app.add_page(
        component=chart_page(),
        route="/charts",
        title="Charts - buridan/ui",
        meta=generate_site_meta_tags(
            title="Charts",
            url="/charts",
            description="A collection of ready-to-use chart components built with Recharts. From basic charts to rich data displays, copy and paste into your apps.",
            social_card="charts.webp",
        ),
    )

    app.add_page(
        component=blocks_page(),
        route="/blocks",
        title="Building Blocks for Dashboards - buridan/ui",
        meta=generate_site_meta_tags(
            title="Blocks",
            url="/blocks",
            description="Clean, modern building blocks for Reflex dashboards. Copy and paste into your apps. Open Source. Extensible.",
            social_card="blocks.webp",
        ),
    )

    app.add_page(
        component=components_page(),
        route="/components",
        title="Components - buridan/ui",
        meta=generate_site_meta_tags(
            title="Components",
            url="/components",
            description="A collection of ready-to-use UI components for building modern applications. From simple controls to complex interface patterns, copy and paste into your apps.",
            social_card="components.webp",
        ),
    )

    app.add_page(
        component=landing_page(),
        route="/",
        title="The UI Library for Reflex Developers - buridan/ui",
        meta=generate_site_meta_tags(
            title="Buridan UI",
            url="/",
            description="Composable, themeable components designed for Reflex. Extend, override, and ship without fighting the framework. Open source.",
            social_card="index.webp",
        ),
    )

    for doc in generate_docs_library():
        main_content = rx.el.div(*doc.component, class_name="w-full")
        toc_content = table_of_content(doc.url, doc.table_of_content)

        title_s = doc.url.split("/")[-1].replace("-", " ").title()
        title = f"{title_s} – buridan/ui"
        card_path = f"{doc.url.split('/')[-1]}.webp"

        app.add_page(
            docpage(main_content, toc_content),
            route=f"/{doc.url}",
            title=title,
            meta=generate_site_meta_tags(
                title=title_s,
                url=f"{doc.url}",
                description=doc.description,
                social_card=card_path,
            ),
        )
