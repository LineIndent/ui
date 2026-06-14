# --- Simple frontmatter parser. ---
def parse_frontmatter(content: str) -> tuple[dict, str]:
    """A simple frontmatter parser."""
    metadata = {}
    if not content.startswith("---"):
        return metadata, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return metadata, content

    frontmatter = parts[1]
    rest_of_content = parts[2]

    for line in frontmatter.strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if (value.startswith('"') and value.endswith('"')) or (
                value.startswith("'") and value.endswith("'")
            ):
                value = value[1:-1]

            if key == "order" and value.isdigit():
                value = int(value)

            metadata[key] = value

    return metadata, rest_of_content.lstrip()
