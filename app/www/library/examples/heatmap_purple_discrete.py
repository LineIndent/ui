from components.ui.heatmap import heatmap


def heatmap_purple_discrete():
    data = [
        {"date": "2025-01-07", "value": 1},
        {"date": "2025-01-14", "value": 2},
        {"date": "2025-01-21", "value": 3},
        {"date": "2025-01-28", "value": 4},
        {"date": "2025-02-04", "value": 5},
        {"date": "2025-02-11", "value": 3},
        {"date": "2025-03-01", "value": 1},
        {"date": "2025-03-15", "value": 4},
        {"date": "2025-04-10", "value": 2},
        {"date": "2025-05-20", "value": 5},
        {"date": "2025-06-30", "value": 3},
        {"date": "2025-09-01", "value": 4},
        {"date": "2025-10-15", "value": 2},
        {"date": "2025-11-20", "value": 5},
        {"date": "2025-12-10", "value": 1},
    ]

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-12-31",
        color_mode="discrete",
        color_scale=["#f3e8ff", "#d8b4fe", "#a855f7", "#7e22ce", "#3b0764"],
        value_label="deploys",
        cell_size=14,
        root_class="scrollbar-none",
    )
