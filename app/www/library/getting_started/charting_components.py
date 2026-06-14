import reflex as rx


# Used in --show_code(charting_state_example)--
class charting_state_example(rx.State):
    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]


# Used in --show_code(area_chart_example)--
def area_chart_example():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="desktop",
            fill=rx.color("accent"),
            stroke=rx.color("accent", 8),
        ),
        data=charting_state_example.data,
        width="100%",
        height=250,
    )


# Used in --show_code(cartesian_grid_example)--
def cartesian_grid_example():
    return rx.recharts.cartesian_grid(
        horizontal=True, vertical=False, class_name="opacity-25"
    )


# Used in --show_code(xaxis_example)--
def xaxis_example():
    return rx.recharts.x_axis(
        data_key="month",
        axis_line=False,
        tick_size=10,
        tick_line=False,
        custom_attrs={"fontSize": "12px"},
        interval="preserveStartEnd",
    )


# Used in --show_code(tooltip_example)--
def tooltip_example():
    tooltip_styles = {
        "is_animation_active": False,
        "separator": "",
        "cursor": False,
        "item_style": {
            "color": "currentColor",
            "display": "flex",
            "paddingBottom": "0px",
            "justifyContent": "space-between",
            "textTransform": "capitalize",
        },
        "label_style": {
            "color": rx.color("slate", 9),
            "fontWeight": "500",
        },
        "content_style": {
            "background": rx.color("slate", 1),
            "borderColor": rx.color("slate", 5),
            "borderRadius": "5px",
            "fontFamily": "var(--font-instrument-sans)",
            "fontSize": "0.875rem",
            "lineHeight": "1.25rem",
            "fontWeight": "500",
            "letterSpacing": "-0.01rem",
            "minWidth": "8rem",
            "width": "175px",
            "padding": "0.375rem 0.625rem",
            "position": "relative",
        },
    }
    return rx.recharts.tooltip(**tooltip_styles)
