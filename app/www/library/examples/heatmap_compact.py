import random

from components.ui.heatmap import heatmap


def heatmap_compact():
    data = [
        {
            "date": f"2025-{str(m).zfill(2)}-{str(d).zfill(2)}",
            "value": random.randint(0, 10),
        }
        for m in range(1, 13)
        for d in range(1, 28)
    ]

    return heatmap(
        data=data,
        start_date="2025-01-01",
        end_date="2025-12-31",
        color_mode="discrete",
        show_dow=False,
        show_months=False,
        cell_size=10,
        gap=2,
        value_label="sales",
        root_class="scrollbar-none",
    )
