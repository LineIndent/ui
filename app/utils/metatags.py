from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1200
HEIGHT = 630

TITLE_FONT = ImageFont.truetype(
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    72,
)
DESC_FONT = ImageFont.truetype(
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    40,
)

MAX_TEXT_WIDTH = 850
LEFT_PADDING = 120


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_width: int,
) -> str:
    words = text.split()

    lines = []
    current_line = ""

    for word in words:
        candidate = word if not current_line else f"{current_line} {word}"

        bbox = draw.textbbox(
            (0, 0),
            candidate,
            font=font,
        )

        width = bbox[2] - bbox[0]

        if width <= max_width:
            current_line = candidate
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return "\n".join(lines)


def extract_frontmatter(path: Path) -> tuple[str, str]:
    text = path.read_text()

    if not text.startswith("---"):
        return "", ""

    _, frontmatter, _ = text.split("---", 2)

    data = yaml.safe_load(frontmatter)

    return (
        data.get("title", ""),
        data.get("description", ""),
    )


def draw_border(draw, width, height):
    color = (200, 200, 200)  # Light gray
    stroke = 2
    margin = 80  # Distance from the edge for your "safe area"

    # Top horizontal line (Full width)
    draw.line([(0, margin), (width, margin)], fill=color, width=stroke)

    # Bottom horizontal line (Full width)
    draw.line(
        [(0, height - margin), (width, height - margin)], fill=color, width=stroke
    )

    # Left vertical line (Full height)
    draw.line([(margin, 0), (margin, height)], fill=color, width=stroke)

    # Right vertical line (Full height)
    draw.line([(width - margin, 0), (width - margin, height)], fill=color, width=stroke)


def create_social_card(
    title: str,
    description: str,
    output_path: Path,
):
    img = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "white",
    )

    draw = ImageDraw.Draw(img)

    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    draw_border(draw, WIDTH, HEIGHT)

    wrapped_title = wrap_text(
        draw,
        title,
        TITLE_FONT,
        max_width=900,
    )

    wrapped_description = wrap_text(
        draw,
        description,
        DESC_FONT,
        max_width=900,
    )

    title_bbox = draw.multiline_textbbox(
        (0, 0),
        wrapped_title,
        font=TITLE_FONT,
        spacing=10,
    )

    desc_bbox = draw.multiline_textbbox(
        (0, 0),
        wrapped_description,
        font=DESC_FONT,
        spacing=8,
    )

    title_height = title_bbox[3] - title_bbox[1]
    desc_height = desc_bbox[3] - desc_bbox[1]

    spacing = 50

    block_height = title_height + spacing + desc_height

    start_y = (HEIGHT - block_height) // 2

    draw.multiline_text(
        (100, start_y),
        wrapped_title,
        fill="black",
        font=TITLE_FONT,
        spacing=10,
    )

    draw.multiline_text(
        (
            100,
            start_y + title_height + spacing,
        ),
        wrapped_description,
        fill="#666666",
        font=DESC_FONT,
        spacing=8,
    )

    # 1. Open the logo
    logo = Image.open("assets/logo.webp").convert("RGBA")

    # 2. Optional: Resize (e.g., set width to 100px and maintain aspect ratio)
    logo_width = 200
    logo.thumbnail((logo_width, logo_width))

    # The box is defined as (left, top, right, bottom)
    # Example: crops 10 pixels off every side
    crop_area = (60, 60, logo.width - 60, logo.height - 60)
    logo = logo.crop(crop_area)

    # 3. Calculate position
    # X = Total Width - Right Margin - Logo Width
    # Y = Total Height - Bottom Margin - Logo Height
    # (We add/subtract a little bit for breathing room)
    logo_x = WIDTH - 90 - logo.width
    logo_y = HEIGHT - 90 - logo.height
    # 4. Paste it onto the image
    # If your logo has transparency, use it as the mask
    img.paste(logo, (logo_x, logo_y), mask=logo)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    img.save(
        output_path,
        format="WEBP",
        quality=95,
    )


def generate_social_cards():
    docs_root = Path("docs")

    for md_file in docs_root.rglob("*.md"):
        title, description = extract_frontmatter(md_file)

        filename = md_file.stem.replace("_", "-") + ".webp"

        output_path = Path("assets") / "social" / filename

        create_social_card(
            title=title,
            description=description,
            output_path=output_path,
        )

        print(f"Generated {output_path}")


if __name__ == "__main__":
    generate_social_cards()


BURIDAN_URL = "https://buridan.reflex.run/"
BURIDAN_SLOGAN = (
    "Beautifully designed Reflex components to build your web apps faster. Open source."
)
BURIDAN_KEY_WORDS = (
    "buridan, ui, web apps, framework, open source, frontend, backend, full stack"
)
SITE_LOGO_URL = (
    "https://raw.githubusercontent.com/LineIndent/ui/refs/heads/main/assets/logo.webp"
)


def generate_site_meta_tags(title: str, url: str, description: str, social_card: str):
    BURIDAN_KEY_WORDS = (
        "buridan, ui, web apps, framework, open source, frontend, backend, full stack"
    )
    return [
        {"name": "application-name", "content": title},
        {"name": "keywords", "content": BURIDAN_KEY_WORDS},
        {"name": "description", "content": description},
        {"property": "og:url", "content": url},
        {"property": "og:type", "content": "website"},
        {"property": "og:title", "content": title},
        {"property": "og:description", "content": description},
        {"property": "og:image", "content": social_card},
        {"property": "og:image:width", "content": "1200"},
        {"property": "og:image:height", "content": "630"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"property": "twitter:domain", "content": url},
        {"property": "twitter:url", "content": url},
        {"name": "twitter:title", "content": title},
        {"name": "twitter:description", "content": description},
        {"name": "twitter:image", "content": social_card},
    ]


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
