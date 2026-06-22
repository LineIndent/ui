from components.ui.kanban import kanban


def kanban_basic():
    return kanban(
        columns={
            "To Do": ["Fix bug", "Write tests"],
            "In Progress": ["Deploy"],
        }
    )
