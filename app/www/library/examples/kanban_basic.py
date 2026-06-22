from components.ui.kanban import kanban


def kanban_basic():
    return kanban(
        columns={
            "To Do": [
                {
                    "id": "t1",
                    "title": "Fix login bug",
                    "priority": "high",
                    "description": "OAuth flow broken on Safari",
                    "assignee": "Ahmad Salim",
                    "due_date": "Jan 10, 2025",
                },
                {
                    "id": "t2",
                    "title": "Fix login bug",
                    "priority": "medium",
                    "description": "OAuth flow broken on Safari",
                    "assignee": "Ahmad Salim",
                    "due_date": "Jan 10, 2025",
                },
                {
                    "id": "t3",
                    "title": "Fix login bug",
                    "priority": "low",
                    "description": "OAuth flow broken on Safari",
                    "assignee": "Ahmad Salim",
                    "due_date": "Jan 10, 2025",
                },
            ],
            "In Progress": [],
        },
        board_class="w-full max-w-xs",
        column_class="w-[300px]",
    )
