import reflex as rx

from app.engine.actions import INITIAL_LOAD_JS
from app.engine.seed import seed_engine
from app.engine.url_sync import url_sync_engine
from app.templates.navbar import navbar
from app.templates.preview import preview
from app.templates.sidebar import sidebar
from app.templates.welcome import welcome_dialog

DIV = "relative flex h-screen flex-col bg-background overflow-hidden scrollbar-none"
MAIN = "flex flex-col gap-x-6 lg:flex-row w-full h-full min-h-0 overflow-hidden p-4 lg:px-6 lg:pb-6 lg:pt-2 gap-y-6 scrollbar-none"


def mainpage() -> rx.Component:
    return rx.el.div(
        seed_engine(),
        url_sync_engine(),
        welcome_dialog(),
        rx.el.div(
            navbar(),
            rx.el.main(sidebar(), preview(), class_name=MAIN),
            class_name=DIV,
            on_mount=rx.call_script(INITIAL_LOAD_JS),
        ),
    )
