# # import os
# # import subprocess
# # from pathlib import Path

# # import questionary

# # DOCS_DIR = Path("docs")


# # def build_index():
# #     """
# #     Builds:
# #     {
# #         "getting-started": ["introduction", "installation"],
# #         "components": ["button", "input"]
# #     }
# #     """
# #     sections = {}

# #     for file in DOCS_DIR.glob("**/*.md"):
# #         rel = file.relative_to(DOCS_DIR)
# #         parts = rel.with_suffix("").parts

# #         if len(parts) < 2:
# #             continue

# #         section = parts[0].replace("_", "-")
# #         page = parts[1].replace("_", "-")

# #         sections.setdefault(section, []).append(page)

# #     for k in sections:
# #         sections[k].sort()

# #     return sections


# # def expand_sections(selected_sections, sections):
# #     pages = []
# #     for section in selected_sections:
# #         for page in sections.get(section, []):
# #             pages.append(f"{section}/{page}")
# #     return pages


# # def select_env():
# #     env = questionary.select(
# #         "Run mode:",
# #         choices=["dev", "prod"],
# #     ).ask()

# #     if env is None:
# #         return None

# #     return env


# # def select_mode():
# #     mode = questionary.select(
# #         "What do you want to select?",
# #         choices=["pages", "sections"],
# #     ).ask()

# #     if mode is None:
# #         return None

# #     return mode


# # def select_pages(sections):
# #     choices = []

# #     for section, pages in sections.items():
# #         choices.append(questionary.Separator(f"[{section}]"))
# #         for page in pages:
# #             choices.append(f"{section}/{page}")

# #     result = questionary.checkbox(
# #         "Select pages:",
# #         choices=choices,
# #     ).ask()

# #     if not result:
# #         return None

# #     return result


# # def select_sections(sections):
# #     result = questionary.checkbox(
# #         "Select sections:",
# #         choices=list(sections.keys()),
# #     ).ask()

# #     if not result:
# #         return None

# #     return result


# # def run_reflex(env, pages):
# #     if env == "dev":
# #         os.environ["BURIDAN_DEV_MODE"] = "true"

# #         if pages:
# #             os.environ["BURIDAN_DEV_PAGES"] = ",".join(pages)
# #         else:
# #             os.environ.pop("BURIDAN_DEV_PAGES", None)
# #     else:
# #         os.environ.pop("BURIDAN_DEV_MODE", None)
# #         os.environ.pop("BURIDAN_DEV_PAGES", None)

# #     cmd = ["uv", "run", "reflex", "run", "--env", env]
# #     subprocess.run(cmd)


# # def main():
# #     sections = build_index()

# #     env = select_env()
# #     if env is None:
# #         print("Exiting")
# #         return

# #     mode = select_mode()
# #     if mode is None:
# #         print("Exiting")
# #         return

# #     selected_pages = []

# #     if mode == "pages":
# #         selected_pages = select_pages(sections)
# #         if selected_pages is None:
# #             print("Exiting")
# #             return

# #     elif mode == "sections":
# #         selected_sections = select_sections(sections)
# #         if selected_sections is None:
# #             print("Exiting")
# #             return

# #         selected_pages = expand_sections(selected_sections, sections)

# #     confirm = questionary.confirm(
# #         f"Run reflex in {env} with {len(selected_pages)} pages?"
# #     ).ask()

# #     if not confirm:
# #         print("Cancelled")
# #         return

# #     run_reflex(env, selected_pages)


# # if __name__ == "__main__":
# #     try:
# #         main()
# #     except KeyboardInterrupt:
# #         print("\nExiting")

# import os
# import subprocess
# from pathlib import Path

# import questionary

# DOCS_DIR = Path("docs")


# def build_index():
#     """
#     Builds:
#     {
#         "getting-started": ["introduction", "installation"],
#         "components": ["button", "input"]
#     }
#     """
#     sections = {}

#     for file in DOCS_DIR.glob("**/*.md"):
#         rel = file.relative_to(DOCS_DIR)
#         parts = rel.with_suffix("").parts

#         if len(parts) < 2:
#             continue

#         section = parts[0].replace("_", "-")
#         page = parts[1].replace("_", "-")

#         sections.setdefault(section, []).append(page)

#     for k in sections:
#         sections[k].sort()

#     return sections


# def expand_sections(selected_sections, sections):
#     pages = []
#     for section in selected_sections:
#         for page in sections.get(section, []):
#             pages.append(f"{section}/{page}")
#     return pages


# def select_env():
#     env = questionary.select(
#         "Run mode:",
#         choices=["dev", "prod"],
#     ).ask()

#     if env is None:
#         return None

#     return env


# def select_mode():
#     mode = questionary.select(
#         "What do you want to select?",
#         choices=[
#             "pages",
#             "sections",
#             "section-pages",
#         ],
#     ).ask()

#     if mode is None:
#         return None

#     return mode


# def select_pages(sections):
#     choices = []

#     for section, pages in sections.items():
#         choices.append(questionary.Separator(f"[{section}]"))
#         for page in pages:
#             choices.append(f"{section}/{page}")

#     result = questionary.checkbox(
#         "Select pages:",
#         choices=choices,
#     ).ask()

#     if not result:
#         return None

#     return result


# def select_sections(sections):
#     result = questionary.checkbox(
#         "Select sections:",
#         choices=list(sections.keys()),
#     ).ask()

#     if not result:
#         return None

#     return result


# def select_pages_from_sections(selected_sections, sections):
#     choices = []

#     for section in selected_sections:
#         pages = sections.get(section, [])

#         choices.append(questionary.Separator(f"[{section}]"))

#         for page in pages:
#             choices.append(f"{section}/{page}")

#     result = questionary.checkbox(
#         "Select pages:",
#         choices=choices,
#     ).ask()

#     if not result:
#         return None

#     return result


# def run_reflex(env, pages):
#     if env == "dev":
#         os.environ["BURIDAN_DEV_MODE"] = "true"

#         if pages:
#             os.environ["BURIDAN_DEV_PAGES"] = ",".join(pages)
#         else:
#             os.environ.pop("BURIDAN_DEV_PAGES", None)
#     else:
#         os.environ.pop("BURIDAN_DEV_MODE", None)
#         os.environ.pop("BURIDAN_DEV_PAGES", None)

#     subprocess.run(["uv", "run", "reflex", "run", "--env", env])


# def main():
#     sections = build_index()

#     env = select_env()
#     if env is None:
#         print("Exiting")
#         return

#     mode = select_mode()
#     if mode is None:
#         print("Exiting")
#         return

#     selected_pages = []

#     if mode == "pages":
#         selected_pages = select_pages(sections)
#         if selected_pages is None:
#             print("Exiting")
#             return

#     elif mode == "sections":
#         selected_sections = select_sections(sections)
#         if selected_sections is None:
#             print("Exiting")
#             return

#         selected_pages = expand_sections(selected_sections, sections)

#     elif mode == "section-pages":
#         selected_sections = select_sections(sections)
#         if selected_sections is None:
#             print("Exiting")
#             return

#         selected_pages = select_pages_from_sections(selected_sections, sections)
#         if selected_pages is None:
#             print("Exiting")
#             return

#     confirm = questionary.confirm(
#         f"Run reflex in {env} with {len(selected_pages)} pages?"
#     ).ask()

#     if not confirm:
#         print("Cancelled")
#         return

#     run_reflex(env, selected_pages)


# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\nExiting")

# import os
# import subprocess
# from pathlib import Path

# import questionary

# DOCS_DIR = Path("docs")


# def build_index():
#     """
#     Builds:
#     {
#         "getting-started": ["introduction", "installation"],
#         "components": ["button", "input"]
#     }
#     """
#     sections = {}

#     for file in DOCS_DIR.glob("**/*.md"):
#         rel = file.relative_to(DOCS_DIR)
#         parts = rel.with_suffix("").parts

#         if len(parts) < 2:
#             continue

#         section = parts[0].replace("_", "-")
#         page = parts[1].replace("_", "-")

#         sections.setdefault(section, []).append(page)

#     for k in sections:
#         sections[k].sort()

#     return sections


# def expand_sections(selected_sections, sections):
#     pages = []
#     for section in selected_sections:
#         for page in sections.get(section, []):
#             pages.append(f"{section}/{page}")
#     return pages


# def select_env():
#     env = questionary.select(
#         "Run mode:",
#         choices=["dev", "prod"],
#     ).ask()

#     if env is None:
#         return None

#     return env


# def select_mode():
#     mode = questionary.select(
#         "What do you want to select?",
#         choices=[
#             "pages",
#             "sections",
#             "section-pages",
#         ],
#     ).ask()

#     if mode is None:
#         return None

#     return mode


# def select_pages(sections):
#     choices = []

#     for section, pages in sections.items():
#         choices.append(questionary.Separator(f"[{section}]"))
#         for page in pages:
#             choices.append(f"{section}/{page}")

#     result = questionary.checkbox(
#         "Select pages:",
#         choices=choices,
#     ).ask()

#     if not result:
#         return None

#     return result


# def select_sections(sections):
#     result = questionary.checkbox(
#         "Select sections:",
#         choices=list(sections.keys()),
#     ).ask()

#     if not result:
#         return None

#     return result


# def select_pages_from_sections(selected_sections, sections):
#     choices = []

#     for section in selected_sections:
#         pages = sections.get(section, [])

#         choices.append(questionary.Separator(f"[{section}]"))

#         for page in pages:
#             choices.append(f"{section}/{page}")

#     result = questionary.checkbox(
#         "Select pages:",
#         choices=choices,
#     ).ask()

#     if not result:
#         return None

#     return result


# def run_reflex(env, pages):
#     if env == "dev":
#         os.environ["BURIDAN_DEV_MODE"] = "true"

#         if pages:
#             os.environ["BURIDAN_DEV_PAGES"] = ",".join(pages)
#         else:
#             os.environ.pop("BURIDAN_DEV_PAGES", None)
#     else:
#         os.environ.pop("BURIDAN_DEV_MODE", None)
#         os.environ.pop("BURIDAN_DEV_PAGES", None)

#     cmd = ["uv", "run", "reflex", "run", "--env", env]
#     subprocess.run(cmd)


# def main():
#     sections = build_index()

#     env = select_env()
#     if env is None:
#         print("Exiting")
#         return

#     # ---------------- FAST PATH: PROD ----------------
#     if env == "prod":
#         print("Launching full site (prod mode)...")
#         run_reflex(env, pages=None)
#         return

#     # ---------------- DEV FLOW ----------------
#     mode = select_mode()
#     if mode is None:
#         print("Exiting")
#         return

#     selected_pages = []

#     if mode == "pages":
#         selected_pages = select_pages(sections)
#         if selected_pages is None:
#             print("Exiting")
#             return

#     elif mode == "sections":
#         selected_sections = select_sections(sections)
#         if selected_sections is None:
#             print("Exiting")
#             return

#         selected_pages = expand_sections(selected_sections, sections)

#     elif mode == "section-pages":
#         selected_sections = select_sections(sections)
#         if selected_sections is None:
#             print("Exiting")
#             return

#         selected_pages = select_pages_from_sections(selected_sections, sections)
#         if selected_pages is None:
#             print("Exiting")
#             return

#     confirm = questionary.confirm(
#         f"Run reflex in {env} with {len(selected_pages)} pages?"
#     ).ask()

#     if not confirm:
#         print("Cancelled")
#         return

#     run_reflex(env, selected_pages)


# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\nExiting")


import os
import subprocess
from pathlib import Path

import questionary

DOCS_DIR = Path("docs")


def build_index():
    """
    Builds:
    {
        "getting-started": ["introduction", "installation"],
        "components": ["button", "input"]
    }
    """
    sections = {}

    for file in DOCS_DIR.glob("**/*.md"):
        rel = file.relative_to(DOCS_DIR)
        parts = rel.with_suffix("").parts

        if len(parts) < 2:
            continue

        section = parts[0].replace("_", "-")
        page = parts[1].replace("_", "-")

        sections.setdefault(section, []).append(page)

    for k in sections:
        sections[k].sort()

    return sections


def expand_sections(selected_sections, sections):
    pages = []
    for section in selected_sections:
        for page in sections.get(section, []):
            pages.append(f"{section}/{page}")
    return pages


def select_env():
    env = questionary.select(
        "Run mode:",
        choices=["dev", "prod"],
    ).ask()

    if env is None:
        return None

    return env


def select_mode():
    mode = questionary.select(
        "What do you want to select?",
        choices=[
            "pages",
            "sections",
            "section-pages",
        ],
    ).ask()

    if mode is None:
        return None

    return mode


def select_pages(sections):
    choices = []

    for section, pages in sections.items():
        choices.append(questionary.Separator(f"[{section}]"))
        for page in pages:
            choices.append(f"{section}/{page}")

    result = questionary.checkbox(
        "Select pages:",
        choices=choices,
    ).ask()

    if not result:
        return None

    return result


def select_sections(sections):
    result = questionary.checkbox(
        "Select sections:",
        choices=list(sections.keys()),
    ).ask()

    if not result:
        return None

    return result


def select_pages_from_sections(selected_sections, sections):
    choices = []

    for section in selected_sections:
        pages = sections.get(section, [])

        choices.append(questionary.Separator(f"[{section}]"))

        for page in pages:
            choices.append(f"{section}/{page}")

    result = questionary.checkbox(
        "Select pages:",
        choices=choices,
    ).ask()

    if not result:
        return None

    return result


def run_reflex(env, pages):
    """
    Runs Reflex and prints correct URLs ONLY after the actual port is known.
    """
    if env == "dev":
        os.environ["BURIDAN_DEV_MODE"] = "true"

        if pages:
            os.environ["BURIDAN_DEV_PAGES"] = ",".join(pages)
        else:
            os.environ.pop("BURIDAN_DEV_PAGES", None)
    else:
        os.environ.pop("BURIDAN_DEV_MODE", None)
        os.environ.pop("BURIDAN_DEV_PAGES", None)

    cmd = ["uv", "run", "reflex", "run", "--env", env]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    port = None

    for line in process.stdout:
        print(line, end="")

        # Detect actual runtime port from Reflex output
        if "App running at:" in line:
            try:
                port = line.split("http://localhost:")[1].split("/")[0]

                # Print correct clickable URLs ONLY when server is ready
                if pages:
                    base_url = f"http://localhost:{port}/docs"

                    print("\nLoading specified URLs:")
                    for page in pages:
                        print(f"{base_url}/{page}")

            except Exception:
                pass

    return port


def main():
    sections = build_index()

    env = select_env()
    if env is None:
        print("Exiting")
        return

    # ---------------- FAST PATH: PROD ----------------
    if env == "prod":
        print("Launching full site (prod mode)...")
        run_reflex(env, pages=None)
        return

    # ---------------- DEV FLOW ----------------
    mode = select_mode()
    if mode is None:
        print("Exiting")
        return

    selected_pages = []

    if mode == "pages":
        selected_pages = select_pages(sections)
        if selected_pages is None:
            print("Exiting")
            return

    elif mode == "sections":
        selected_sections = select_sections(sections)
        if selected_sections is None:
            print("Exiting")
            return

        selected_pages = expand_sections(selected_sections, sections)

    elif mode == "section-pages":
        selected_sections = select_sections(sections)
        if selected_sections is None:
            print("Exiting")
            return

        selected_pages = select_pages_from_sections(selected_sections, sections)
        if selected_pages is None:
            print("Exiting")
            return

    confirm = questionary.confirm(
        f"Run reflex in {env} with {len(selected_pages)} pages?"
    ).ask()

    if not confirm:
        print("Cancelled")
        return

    run_reflex(env, selected_pages)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting")
