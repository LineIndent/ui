from components.ui.heatmap import heatmap


def heatmap_large_cells():
    data = [
        {"date": "2025-10-01", "value": 1},
        {"date": "2025-10-02", "value": 500},
        {"date": "2025-10-03", "value": 10},
        {"date": "2025-10-06", "value": 1000},
        {"date": "2025-10-07", "value": 5},
        {"date": "2025-10-08", "value": 250},
        {"date": "2025-10-09", "value": 3},
        {"date": "2025-10-10", "value": 750},
        {"date": "2025-10-13", "value": 50},
        {"date": "2025-10-14", "value": 900},
        {"date": "2025-10-15", "value": 20},
        {"date": "2025-10-16", "value": 600},
        {"date": "2025-10-17", "value": 8},
        {"date": "2025-10-20", "value": 400},
        {"date": "2025-10-21", "value": 2},
        {"date": "2025-10-22", "value": 800},
        {"date": "2025-10-23", "value": 15},
        {"date": "2025-10-24", "value": 350},
        {"date": "2025-10-27", "value": 100},
        {"date": "2025-10-28", "value": 700},
        {"date": "2025-10-29", "value": 30},
        {"date": "2025-10-30", "value": 950},
        {"date": "2025-10-31", "value": 12},
    ]

    return heatmap(
        data=data,
        start_date="2025-10-01",
        end_date="2025-10-31",
        color_mode="interpolate",
        min_color="#f0fdf4",
        max_color="#14532d",
        interpolation="log",
        value_label="requests",
        cell_size=20,
        gap=4,
        root_class="scrollbar-none",
    )
