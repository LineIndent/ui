import reflex as rx


# Used in --show_code(project_setup_init_example)--
def project_setup_init_example():
    return rx.markdown("```bash\nreflex init --name app\n```")


# Used in --show_code(project_setup_run_example)--
def project_setup_run_example():
    return rx.markdown("```bash\nreflex run\n```")


# Used in --show_code(dashboard_layout_example)--
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


# Used in --show_code(app_py_example)--
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


# Used in --show_code(sidebar_example)--
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


# Used in --show_code(sidebar_header_example)--
def sidebar_header_example():
    return rx.box(
        # You can add a logo, app title, or user info here
        class_name="w-full h-12 p-2 absolute top-0 left-0 z-[99]",
    )


# Used in --show_code(content_header_example)--
def content_header_example():
    return rx.box(
        # You can add breadcrumbs, titles, or action buttons here
        class_name="w-full h-12 p-2 absolute top-0 left-0 z-[99]",
    )


# Used in --show_code(main_content_section_example)--
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
