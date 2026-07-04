import reflex as rx

from components.icons.hugeicon import hi
from components.ui.button import button
from components.ui.collapsible import collapsible


def collapsible_interactive() -> rx.Component:
    return rx.el.div(
        collapsible.root(
            collapsible.trigger(
                render_=button(
                    rx.el.div(
                        rx.el.div(
                            "JD",
                            class_name="flex size-8 items-center justify-center rounded-full bg-primary/10 text-xs font-bold text-primary",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "John Doe",
                                class_name="text-sm font-semibold text-foreground text-left leading-none",
                            ),
                            rx.el.p(
                                "pro_plan_member",
                                class_name="text-[10px] font-mono text-muted-foreground mt-0.5 text-left",
                            ),
                            class_name="flex flex-col",
                        ),
                        class_name="flex items-center gap-3",
                    ),
                    hi(
                        "ArrowDown01Icon",
                        class_name="size-4 ml-auto text-muted-foreground transition-transform duration-200 group-data-panel-open/button:rotate-180",
                    ),
                    variant="ghost",
                    class_name="w-full h-14 px-3 hover:bg-muted/50 rounded-xl",
                ),
                class_name="w-full",
            ),
            collapsible.panel(
                rx.el.div(
                    rx.el.a(
                        hi("UserIcon", class_name="size-4 text-muted-foreground"),
                        rx.el.span("Edit Profile", class_name="text-xs font-medium"),
                        href="#",
                        class_name="flex items-center gap-2.5 px-3 py-2 rounded-lg hover:bg-muted/70 text-foreground/80 transition-colors",
                    ),
                    rx.el.a(
                        hi("Settings01Icon", class_name="size-4 text-muted-foreground"),
                        rx.el.span(
                            "Security & API Keys", class_name="text-xs font-medium"
                        ),
                        href="#",
                        class_name="flex items-center gap-2.5 px-3 py-2 rounded-lg hover:bg-muted/70 text-foreground/80 transition-colors",
                    ),
                    rx.el.a(
                        hi("Logout01Icon", class_name="size-4 text-destructive/70"),
                        rx.el.span(
                            "Log Out", class_name="text-xs font-medium text-destructive"
                        ),
                        href="#",
                        class_name="flex items-center gap-2.5 px-3 py-2 rounded-lg hover:bg-destructive/10 text-destructive transition-colors",
                    ),
                    class_name="pt-2 px-1 flex flex-col gap-1 border-t border-border/40 mt-1",
                )
            ),
        ),
        class_name="w-full max-w-xs p-2 bg-background border border-input rounded-2xl shadow-xs",
    )
