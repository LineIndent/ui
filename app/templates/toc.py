from typing import Dict, List

import reflex as rx

from app.www.wrapper import generate_component_id
from components.icons.hugeicon import hi
from components.ui.tooltip import tooltip


def create_copy_button(url: str) -> rx.Component:
    uid = generate_component_id()
    btn_id = f"btn-{uid}"
    icon_id = f"icon-{uid}"
    copy_icon_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="currentColor" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 15C9 12.1716 9 10.7574 9.87868 9.87868C10.7574 9 12.1716 9 15 9L16 9C18.8284 9 20.2426 9 21.1213 9.87868C22 10.7574 22 12.1716 22 15V16C22 18.8284 22 20.2426 21.1213 21.1213C20.2426 22 18.8284 22 16 22H15C12.1716 22 10.7574 22 9.87868 21.1213C9 20.2426 9 18.8284 9 16L9 15Z"/><path d="M16.9999 9C16.9975 6.04291 16.9528 4.51121 16.092 3.46243C15.9258 3.25989 15.7401 3.07418 15.5376 2.90796C14.4312 2 12.7875 2 9.5 2C6.21252 2 4.56878 2 3.46243 2.90796C3.25989 3.07417 3.07418 3.25989 2.90796 3.46243C2 4.56878 2 6.21252 2 9.5C2 12.7875 2 14.4312 2.90796 15.5376C3.07417 15.7401 3.25989 15.9258 3.46243 16.092C4.51121 16.9528 6.04291 16.9975 9 16.9999"/></svg>'
    tick_icon_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="currentColor" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 14.5C5 14.5 6.5 14.5 8.5 18C8.5 18 14.0588 8.83333 19 7"/></svg>'

    return tooltip.provider(
        tooltip.root(
            tooltip.trigger(
                render_=hi(
                    "Copy01Icon", id=icon_id, class_name="size-4 cursor-pointer"
                ),
                id=btn_id,
                on_click=rx.call_script(
                    f"""
                        (async () => {{
                            const res = await fetch("/{url}.md");
                            const text = await res.text();
                            await navigator.clipboard.writeText(text);
                        }})();

                        const icon = document.getElementById('{icon_id}');

                        // Swap to tick
                        icon.innerHTML = `{tick_icon_svg}`;

                        // Revert after 1.5s
                        setTimeout(() => {{
                            icon.innerHTML = `{copy_icon_svg}`;
                        }}, 1500);
                    """
                ),
            ),
            tooltip.portal(
                tooltip.positioner(
                    tooltip.popup(
                        rx.el.p("Copy Page", class_name="!text-xs"),
                        class_name="rounded-radius p-2",
                    ),
                    side="bottom",
                    side_offset=8,
                ),
            ),
        ),
        delay=0,
    )


def _create_markdown_toc_links(toc_data: List[Dict]) -> rx.Component:
    """Create markdown TOC links."""
    if not toc_data:
        return rx.el.div()

    return rx.el.div(
        *[
            rx.el.a(
                entry["text"],
                href=f"#{entry['id']}",
                id=f"toc-{entry['id']}",
                class_name=f"cursor-pointer transition-colors duration-250 text-[0.8rem] text-muted-foreground hover:text-foreground no-underline{' pl-4' if entry['level'] > 1 else ''}",
            )
            for entry in toc_data
        ],
        class_name="flex flex-col w-full gap-y-2",
    )


def _create_external_tool_links(url: str):
    """Create links for viewing documentation in external tools."""

    fmt_url = "https://buridan-ui.reflex.run/" + url
    prompt = f"""I'm looking at this buridan/ui documentation: {fmt_url}.
    Help me understand how to use it. Be ready to explain concepts, give examples, or help debug based on it.
    """

    def external_tool_item(
        icon_light,
        icon_dark,
        tooltip_content: str,
        href: str,
        icon_size: str = "size-4",
    ):
        return tooltip.provider(
            tooltip.root(
                tooltip.trigger(
                    render_=rx.el.a(
                        rx.el.image(
                            rx.color_mode_cond(icon_light, icon_dark),
                            class_name=icon_size,
                        ),
                        href=href,
                        target="_blank",
                        rel="noopener noreferrer",
                    )
                ),
                tooltip.portal(
                    tooltip.positioner(
                        tooltip.popup(
                            rx.el.p(tooltip_content, class_name="!text-xs"),
                            class_name="rounded-radius p-2",
                        ),
                        side="bottom",
                        side_offset=8,
                    ),
                ),
            ),
            delay=0,
        )

    return rx.el.div(
        external_tool_item(
            icon_light="/svg/markdown/md_light.svg",
            icon_dark="/svg/markdown/md_dark.svg",
            tooltip_content="View Markdown",
            href=f"/{url}.md",
            icon_size="size-5",
        ),
        external_tool_item(
            icon_light="/svg/openai/ai_light.svg",
            icon_dark="/svg/openai/ai_dark.svg",
            tooltip_content="Open in ChatGPT",
            href=f"https://chatgpt.com/?q={prompt}",
        ),
        external_tool_item(
            icon_light="/svg/claude/claude_light.svg",
            icon_dark="/svg/claude/claude_dark.svg",
            tooltip_content="Open in Claude",
            href=f"https://claude.ai/new?q={prompt}",
        ),
        external_tool_item(
            icon_light="/svg/reflex/reflex_light.svg",
            icon_dark="/svg/reflex/reflex_dark.svg",
            tooltip_content="Open in Reflex",
            href=f"https://build.reflex.dev/?prompt={prompt}",
        ),
        rx.el.p("︲", class_name="text-muted-foreground/50 font-thin hidden lg:flex"),
        create_copy_button(url),
        class_name="flex flex-row items-center w-full gap-x-2.5",
    )


def table_of_content(url: str, toc_data: List[Dict]):
    """
    Render table of contents.

    Args:
        toc_data: List of dicts with 'text', 'id', 'level' keys
    """
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                #
                rx.el.div(
                    rx.el.p(
                        "External Tools",
                        class_name="text-xs text-muted-foreground font-medium pb-2",
                    ),
                    _create_external_tool_links(url),
                    class_name="w-full flex flex-col",
                ),
                #
                rx.el.div(
                    rx.el.p(
                        "Agent Resources",
                        class_name="text-xs text-muted-foreground font-medium pb-2",
                    ),
                    rx.el.a(
                        rx.el.p(
                            "llms.txt",
                            class_name="text-[0.8rem] text-muted-foreground hover:text-foreground",
                        ),
                        href="/llms.txt",
                        target="_blank",
                        rel="noopener noreferrer",
                    ),
                    class_name="w-full flex flex-col",
                ),
                #
                rx.el.div(
                    rx.el.p(
                        "On This Page",
                        class_name="text-xs text-muted-foreground font-medium pb-2",
                    ),
                    _create_markdown_toc_links(toc_data),
                    class_name="w-full flex flex-col",
                ),
                class_name="flex flex-col w-full h-full p-4 gap-y-6",
            ),
            class_name="flex flex-col gap-y-4 overflow-scroll scrollbar-none",
        ),
        class_name="hidden xl:block max-w-[18rem] w-full sticky top-18 h-[calc(100vh-3rem)] shrink-0",
        on_mount=rx.call_script("""
        console.log("TOC mounted");

        const headings = document.querySelectorAll('header[id]');
        console.log("headings:", headings);

        let currentId = null;

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        currentId = entry.target.id;
                        console.log("active:", currentId);
                    }
                });

                if (!currentId) return;

                // reset all TOC links
                document.querySelectorAll('[id^="toc-"]').forEach((el) => {
                    el.classList.remove('text-foreground', 'font-semibold');
                    el.classList.add('text-muted-foreground');
                });

                // activate current one
                document
                    .getElementById(`toc-${currentId}`)
                    ?.classList.remove('text-muted-foreground');

                document
                    .getElementById(`toc-${currentId}`)
                    ?.classList.add('text-foreground', 'font-semibold');
            },
            {
                rootMargin: '-20% 0px -70% 0px',
                threshold: 0.1,
            }
        );

        headings.forEach((h) => observer.observe(h));
        """),
    )
