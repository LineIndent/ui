"""
Tests to verify that all source markdown files in docs/ have been correctly
processed into their expected outputs:
  - assets/docs/   → markdown files (underscores → hyphens)
  - assets/social/ → .webp social cards
"""

import pathlib
import re

import pytest

# ---------------------------------------------------------------------------
# Paths — adjust ROOT_DIR if you place this file somewhere other than tests/
# ---------------------------------------------------------------------------
ROOT_DIR = pathlib.Path(__file__).parent.parent
DOCS_DIR = ROOT_DIR / "docs"
MARKDOWN_OUTPUT_DIR = ROOT_DIR / "assets" / "docs"
SOCIAL_OUTPUT_DIR = ROOT_DIR / "assets" / "social"

# Hardcoded pages from social_cards generator's PAGES_CONFIG
PAGES_CONFIG_ROUTES = ["create", "charts", "components", "index"]

# Pattern that should NOT appear in any generated markdown file
UNRESOLVED_DELIMITER_PATTERN = re.compile(r"--([\w_]+)(?:\(.*?\))?--")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def all_source_md_files():
    """Return all .md source files under docs/."""
    return list(DOCS_DIR.rglob("*.md"))


def expected_markdown_output_path(md_file: pathlib.Path) -> pathlib.Path:
    """
    Mirror a docs/ source path into assets/docs/, converting underscores to
    hyphens in every path component (matching generator.py behaviour).
    """
    relative = md_file.relative_to(DOCS_DIR)
    hyphenated_parts = [part.replace("_", "-") for part in relative.parts]
    return MARKDOWN_OUTPUT_DIR / pathlib.Path(*hyphenated_parts)


def expected_social_card_path(md_file: pathlib.Path) -> pathlib.Path:
    """
    Derive the expected .webp path for a docs/ source file, matching
    social_cards generator behaviour (stem with underscores → hyphens).
    """
    filename = md_file.stem.replace("_", "-") + ".webp"
    return SOCIAL_OUTPUT_DIR / filename


def has_frontmatter(md_file: pathlib.Path) -> bool:
    """Return True if the markdown file starts with a YAML frontmatter block."""
    try:
        return md_file.read_text(encoding="utf-8").startswith("---")
    except OSError:
        return False


# ---------------------------------------------------------------------------
# Parametrize helpers — collected once at module level so pytest IDs are stable
# ---------------------------------------------------------------------------

_all_md = all_source_md_files()
_md_with_frontmatter = [f for f in _all_md if has_frontmatter(f)]


# ---------------------------------------------------------------------------
# Markdown generator tests
# ---------------------------------------------------------------------------


class TestMarkdownGeneration:
    @pytest.mark.parametrize(
        "md_file", _all_md, ids=lambda f: str(f.relative_to(DOCS_DIR))
    )
    def test_output_file_exists(self, md_file):
        """Every source .md file must have a corresponding generated output file."""
        output = expected_markdown_output_path(md_file)
        assert output.exists(), (
            f"Missing generated markdown for {md_file.relative_to(ROOT_DIR)}\n"
            f"Expected output: {output.relative_to(ROOT_DIR)}"
        )

    @pytest.mark.parametrize(
        "md_file", _all_md, ids=lambda f: str(f.relative_to(DOCS_DIR))
    )
    def test_output_file_is_not_empty(self, md_file):
        """Generated markdown files must not be empty."""
        output = expected_markdown_output_path(md_file)
        if not output.exists():
            pytest.skip("Output file missing — covered by test_output_file_exists")
        assert output.stat().st_size > 0, (
            f"Generated file is empty: {output.relative_to(ROOT_DIR)}"
        )

    @pytest.mark.parametrize(
        "md_file", _all_md, ids=lambda f: str(f.relative_to(DOCS_DIR))
    )
    def test_no_unresolved_delimiters(self, md_file):
        """
        Generated markdown must contain no unresolved --component-- delimiters,
        which would indicate a registry lookup failure during generation.
        """
        output = expected_markdown_output_path(md_file)
        if not output.exists():
            pytest.skip("Output file missing — covered by test_output_file_exists")

        content = output.read_text(encoding="utf-8")
        matches = UNRESOLVED_DELIMITER_PATTERN.findall(content)
        assert not matches, (
            f"Unresolved delimiters found in {output.relative_to(ROOT_DIR)}: "
            + ", ".join(f"--{m}--" for m in matches)
        )

    @pytest.mark.parametrize(
        "md_file", _all_md, ids=lambda f: str(f.relative_to(DOCS_DIR))
    )
    def test_frontmatter_stripped(self, md_file):
        """
        If the source file has YAML frontmatter, the generated output must not
        start with '---' (the generator strips it).
        """
        if not has_frontmatter(md_file):
            pytest.skip("Source file has no frontmatter")

        output = expected_markdown_output_path(md_file)
        if not output.exists():
            pytest.skip("Output file missing — covered by test_output_file_exists")

        content = output.read_text(encoding="utf-8").lstrip()
        assert not content.startswith("---"), (
            f"Frontmatter was NOT stripped in: {output.relative_to(ROOT_DIR)}"
        )

    def test_output_directory_exists(self):
        """The assets/docs/ output directory itself must exist."""
        assert MARKDOWN_OUTPUT_DIR.exists() and MARKDOWN_OUTPUT_DIR.is_dir(), (
            f"Output directory missing: {MARKDOWN_OUTPUT_DIR.relative_to(ROOT_DIR)}"
        )

    def test_no_extra_output_files(self):
        """
        Every file in assets/docs/ should trace back to a source file in docs/.
        Catches stale outputs from deleted source files.
        """
        expected_outputs = {expected_markdown_output_path(f) for f in _all_md}
        actual_outputs = set(MARKDOWN_OUTPUT_DIR.rglob("*.md"))
        stale = actual_outputs - expected_outputs
        assert not stale, "Stale output files with no matching source:\n" + "\n".join(
            f"  {p.relative_to(ROOT_DIR)}" for p in sorted(stale)
        )


# ---------------------------------------------------------------------------
# Social card generator tests
# ---------------------------------------------------------------------------


class TestSocialCardGeneration:
    def test_output_directory_exists(self):
        """The assets/social/ output directory must exist."""
        assert SOCIAL_OUTPUT_DIR.exists() and SOCIAL_OUTPUT_DIR.is_dir(), (
            f"Social card output directory missing: {SOCIAL_OUTPUT_DIR.relative_to(ROOT_DIR)}"
        )

    @pytest.mark.parametrize("route", PAGES_CONFIG_ROUTES)
    def test_pages_config_card_exists(self, route):
        """Each hardcoded PAGES_CONFIG entry must have a .webp social card."""
        filename = route.replace("/", "-") + ".webp"
        card_path = SOCIAL_OUTPUT_DIR / filename
        assert card_path.exists(), (
            f"Missing social card for PAGES_CONFIG route '{route}': "
            f"{card_path.relative_to(ROOT_DIR)}"
        )

    @pytest.mark.parametrize("route", PAGES_CONFIG_ROUTES)
    def test_pages_config_card_is_not_empty(self, route):
        """PAGES_CONFIG social cards must not be zero-byte files."""
        filename = route.replace("/", "-") + ".webp"
        card_path = SOCIAL_OUTPUT_DIR / filename
        if not card_path.exists():
            pytest.skip("Card missing — covered by test_pages_config_card_exists")
        assert card_path.stat().st_size > 0, (
            f"Social card is empty: {card_path.relative_to(ROOT_DIR)}"
        )

    @pytest.mark.parametrize(
        "md_file", _md_with_frontmatter, ids=lambda f: str(f.relative_to(DOCS_DIR))
    )
    def test_doc_social_card_exists(self, md_file):
        """Every docs/ markdown file with frontmatter must have a .webp social card."""
        card_path = expected_social_card_path(md_file)
        assert card_path.exists(), (
            f"Missing social card for {md_file.relative_to(ROOT_DIR)}\n"
            f"Expected: {card_path.relative_to(ROOT_DIR)}"
        )

    @pytest.mark.parametrize(
        "md_file", _md_with_frontmatter, ids=lambda f: str(f.relative_to(DOCS_DIR))
    )
    def test_doc_social_card_is_not_empty(self, md_file):
        """Social cards for docs pages must not be zero-byte files."""
        card_path = expected_social_card_path(md_file)
        if not card_path.exists():
            pytest.skip("Card missing — covered by test_doc_social_card_exists")
        assert card_path.stat().st_size > 0, (
            f"Social card is empty: {card_path.relative_to(ROOT_DIR)}"
        )

    @pytest.mark.parametrize(
        "md_file", _md_with_frontmatter, ids=lambda f: str(f.relative_to(DOCS_DIR))
    )
    def test_doc_social_card_is_webp(self, md_file):
        """
        Social card files should be valid WEBP images — checked by magic bytes
        (no Pillow dependency needed at test time).
        WEBP files start with b'RIFF' at offset 0 and b'WEBP' at offset 8.
        """
        card_path = expected_social_card_path(md_file)
        if not card_path.exists():
            pytest.skip("Card missing — covered by test_doc_social_card_exists")

        with card_path.open("rb") as fh:
            header = fh.read(12)

        assert header[:4] == b"RIFF" and header[8:12] == b"WEBP", (
            f"File does not appear to be a valid WEBP: {card_path.relative_to(ROOT_DIR)}"
        )
