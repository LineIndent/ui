

# Introduction
This walkthrough helps you scaffold the foundational layout for a dashboard-style Reflex app. While dashboards vary in content and complexity, their layout structure is almost always the same:

- A **sidebar** for navigation (often fixed)
- A **sticky sidebar header** for branding or profile info
- A **main content area**
- A **sticky content header** for search, filters, or page titles

This guide walks through building that exact foundation — a reusable layout skeleton you can plug your own pages and components into. It’s meant to save you time, enforce consistency, and give you a solid base to build from.

# Project Setup

To begin, create a new Reflex project using the CLI:

```bash
reflex init --name app
```

When prompted, select: **Blank Reflex App**
This will generate the following project structure:

```text
./
├── assets/
├── app/
│   ├── __init__.py
│   └── app.py
├── .gitignore
├── requirements.txt
└── rxconfig.py
```

To run the development server and see the app in your browser, use:
```bash
reflex run
```

This will start a local server, usually at http://localhost:3000, where you can preview your dashboard as you build it.

# Creating the Main Layout Component

To keep your dashboard clean and maintainable, it’s best to separate each layout section into its own component file.
Here’s a recommended structure for your `app/` directory:

```text
app/
├── __init__.py
├── app.py
├── layout/
│   ├── __init__.py
│   ├── layout.py
│   ├── sidebar.py
│   ├── sidebar_header.py
│   ├── content_header.py

```

We’ll start by building the top-level layout component that wraps all other parts.


```python
def dashboard_layout_example():
    # Assuming app.layout.sidebar and app.layout.content_header are defined elsewhere
    # For demonstration, we'll use placeholders
    def sidebar():
        return rx.box("Sidebar")

    def content_header():
        return rx.box("Content Header")

    return rx.box(
        sidebar(),
        rx.scroll_area(
            content_header(),
            class_name=(
                "flex flex-col w-full gap-y-2 align-start z-[10] pt-12 "
                "[&_.rt-ScrollAreaScrollbar]:mt-[4rem] "
                "[&_.rt-ScrollAreaScrollbar]:mb-[1rem]"
            ),
            height=["100%" if i == 0 else "100vh" for i in range(6)],
        ),
        class_name="w-[100%] h-[100vh] gap-x-0 flex flex-row",
    )
```


Then in your `app.py`, use it as the root of your page:


```python
def app_py_example():
    return rx.markdown(
        r"""```
# app/app.py

import reflex as rx
from app.layout.layout import dashboard_layout

def index() -> rx.Component:
    return dashboard_layout()

app = rx.App()
app.add_page(index)
```"""
    )
```


# Building the Sidebar

The sidebar is a key part of the dashboard layout. It typically contains navigation, branding, or user context and stays fixed on the left side of the screen. We'll start by creating a reusable `sidebar()` component inside `app/layout/sidebar.py`.


```python
def sidebar_example():
    # Assuming sidebar_header is defined elsewhere
    def sidebar_header():
        return rx.box("Sidebar Header")

    return rx.scroll_area(
        sidebar_header(),
        rx.box(
            # Sidebar content (e.g., nav links) goes here
            class_name="flex flex-col w-full h-full pt-12 px-2",
        ),
        class_name=(
            "flex flex-col max-w-[300px] w-full h-[100vh] gap-y-2 align-start "
            "sticky top-0 left-0 z-[10] "
            "[&_.rt-ScrollAreaScrollbar]:mr-[0.1875rem] "
            "[&_.rt-ScrollAreaScrollbar]:mt-[4rem] "
            "[&_.rt-ScrollAreaScrollbar]:mb-[1rem]"
        ),
    )
```


- `rx.scroll_area(...)` lets the sidebar scroll independently if its content exceeds the viewport height.
- `sidebar_header()` is a separate component that we'll define next — it's used for a logo, app title, or profile section.
- The `rx.box(...)` inside is a vertical flex container for sidebar content like links, sections, or collapsible items.
- The `class_name` styling includes:
  - `sticky top-0`: Keeps the sidebar fixed on scroll.
  - `max-w-[300px]`: Limits the sidebar width.
  - Tailwind tweaks like `[&_.rt-ScrollAreaScrollbar]:...` adjust scrollbar margins and spacing inside Reflex's default scroll areas.

Next, we’ll build the **sticky sidebar header** — a small top section inside the sidebar that stays fixed even when you scroll the rest of the sidebar contents.

# Adding the Sticky Sidebar Header

The sidebar header sits at the top of the sidebar and remains fixed while the rest of the sidebar content scrolls. It's ideal for branding, a dashboard title, or user profile info.

Here's the component definition:


```python
def sidebar_header_example():
    return rx.box(
        # You can add a logo, app title, or user info here
        class_name="w-full h-12 p-2 absolute top-0 left-0 z-[99]",
    )
```


Once this header is in place, your sidebar becomes more polished and ready for interactive content. Next, we’ll focus on the main content area, including its own sticky header and scrollable body.


# Defining the Main Content Header

Just like the sidebar has a sticky top section, the main content area also benefits from a persistent header. This can hold breadcrumbs, context info, or action buttons relevant to the current page or dashboard section.

Here’s the header component:


```python
def content_header_example():
    return rx.box(
        # You can add breadcrumbs, titles, or action buttons here
        class_name="w-full h-12 p-2 absolute top-0 left-0 z-[99]",
    )
```


This header is used inside the scroll area of your `dashboard_layout()`. This ensures the content header stays in view as users scroll down the main area of the dashboard. Next, we’ll create the actual main content section — where all your page content, cards, tables, and graphs will appear.

# Main Content Section: Where Everything Goes

With the layout now complete, this is where you’ll add the actual content of your dashboard — charts, tables, cards, forms, and any interactive components. This content should go **inside the scrollable main area**, *beneath* the `content_header()`. In your `dashboard_layout()`, that means placing components after `content_header()` and before the end of the scroll area.

For example, if you have a chart or a card component, you would import it and place it like this:


```python
def main_content_section_example():
    # Assuming content_header, my_chart_component, my_table_component are defined elsewhere
    def content_header():
        return rx.box("Content Header")

    def my_chart_component():
        return rx.box("My Chart Component")

    def my_table_component():
        return rx.box("My Table Component")

    return rx.scroll_area(
        content_header(),
        my_chart_component(),
        my_table_component(),
        # ...
    )
```


# Final Words

You now have a clean, modular dashboard layout built with Reflex — complete with a sticky sidebar, a sticky main header, and a scrollable content area. This layout is designed to be reused across different pages or apps. Whether you're building a data dashboard, admin panel, or internal tool, the structure remains the same — giving you a rock-solid foundation to build on.

From here, you can:

- Start plugging in your actual dashboard content (charts, tables, forms).
- Add routing and navigation logic to move between pages.
- Customize styles, colors, and themes as needed.
- Extract reusable UI patterns to grow your component system.

This foundation keeps your layout logic clean and separate from your business logic — which means faster development and easier maintenance.

Happy building! 🚀
