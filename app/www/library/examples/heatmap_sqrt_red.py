from components.ui.heatmap import heatmap


def heatmap_red_sqrt():
    data = [
        {"date": "2025-01-03", "value": 1},
        {"date": "2025-01-10", "value": 50},
        {"date": "2025-02-14", "value": 3},
        {"date": "2025-03-01", "value": 100},
        {"date": "2025-04-20", "value": 2},
        {"date": "2025-05-05", "value": 75},
        {"date": "2025-06-15", "value": 10},
        {"date": "2025-07-04", "value": 90},
        {"date": "2025-08-12", "value": 5},
        {"date": "2025-09-09", "value": 40},
        {"date": "2025-10-31", "value": 8},
        {"date": "2025-11-25", "value": 60},
        {"date": "2025-12-01", "value": 20},
    ]

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-12-31",
        color_mode="interpolate",
        min_color="#fee2e2",
        max_color="#991b1b",
        interpolation="sqrt",
        value_label="errors",
        cell_size=14,
        root_class="scrollbar-none",
    )
