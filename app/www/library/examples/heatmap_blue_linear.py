from components.ui.heatmap import heatmap


def heatmap_blue_linear():
    data = [
        {"date": "2025-01-05", "value": 2},
        {"date": "2025-01-12", "value": 9},
        {"date": "2025-02-01", "value": 4},
        {"date": "2025-02-20", "value": 15},
        {"date": "2025-03-10", "value": 6},
        {"date": "2025-04-04", "value": 18},
        {"date": "2025-05-15", "value": 3},
        {"date": "2025-06-01", "value": 11},
        {"date": "2025-07-22", "value": 20},
        {"date": "2025-08-08", "value": 7},
        {"date": "2025-09-30", "value": 14},
        {"date": "2025-10-10", "value": 5},
        {"date": "2025-11-11", "value": 19},
        {"date": "2025-12-25", "value": 1},
    ]

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-12-31",
        color_mode="interpolate",
        min_color="#dbeafe",
        max_color="#1d4ed8",
        interpolation="linear",
        value_label="events",
        cell_size=14,
        root_class="scrollbar-none",
    )
