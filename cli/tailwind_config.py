TAILWIND_CONFIG_SNIPPET = """        rx.plugins.TailwindV4Plugin(
            TailwindConfig(
                darkMode="class",
                plugins=["@tailwindcss/typography", "tailwind-scrollbar", "tailwindcss-animate"],
                theme={
                    "extend": {
                        "colors": {
                            "background": "var(--background)",
                            "foreground": "var(--foreground)",
                            "card": "var(--card)",
                            "card-foreground": "var(--card-foreground)",
                            "popover": "var(--popover)",
                            "popover-foreground": "var(--popover-foreground)",
                            "primary": "var(--primary)",
                            "primary-foreground": "var(--primary-foreground)",
                            "secondary": "var(--secondary)",
                            "secondary-foreground": "var(--secondary-foreground)",
                            "muted": "var(--muted)",
                            "muted-foreground": "var(--muted-foreground)",
                            "accent": "var(--accent)",
                            "accent-foreground": "var(--accent-foreground)",
                            "destructive": "var(--destructive)",
                            "border": "var(--border)",
                            "input": "var(--input)",
                            "ring": "var(--ring)",
                            "chart-1": "var(--chart-1)",
                            "chart-2": "var(--chart-2)",
                            "chart-3": "var(--chart-3)",
                            "chart-4": "var(--chart-4)",
                            "chart-5": "var(--chart-5)",
                            "sidebar": "var(--sidebar)",
                            "sidebar-foreground": "var(--sidebar-foreground)",
                            "sidebar-primary": "var(--sidebar-primary)",
                            "sidebar-primary-foreground": "var(--sidebar-primary-foreground)",
                            "sidebar-accent": "var(--sidebar-accent)",
                            "sidebar-accent-foreground": "var(--sidebar-accent-foreground)",
                            "sidebar-border": "var(--sidebar-border)",
                            "sidebar-ring": "var(--sidebar-ring)",
                        },
                        "fontFamily": {
                            "theme": "var(--font-family)",
                        },
                        "borderRadius": {
                            "radius": "var(--radius)",
                        },
                        "padding": {
                            "card": "var(--card-padding)",
                        },
                        "gap": {
                            "card": "var(--card-gap)",
                        },
                        "boxShadow": {
                            "default": "var(--shadow)",
                        },
                    }
                },
            )
        ),"""
