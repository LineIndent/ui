# Buridan UI Component Registry

Use this list to understand component dependencies. The `buridan add` command handles these automatically.

| Component | Files | Dependencies |
| :--- | :--- | :--- |
| **accordion** | `components/ui/accordion.py` | `button`, `hugeicon`, `base_ui` |
| **avatar** | `components/ui/avatar.py` | `base_ui` |
| **badge** | `components/ui/badge.py` | `component` |
| **button** | `components/ui/button.py` | `others_icons`, `component` |
| **checkbox** | `components/ui/checkbox.py` | `hugeicon`, `twmerge`, `base_ui` |
| **context_menu** | `components/ui/context_menu.py` | `twmerge`, `base_ui`, `button` |
| **dialog** | `components/ui/dialog.py` | `hugeicon`, `base_ui`, `button` |
| **menu** | `components/ui/menu.py` | `hugeicon`, `others_icons`, `twmerge`, `base_ui`, `button` |
| **select** | `components/ui/select.py` | `hugeicon`, `others_icons`, `twmerge`, `base_ui`, `button` |
| **tooltip** | `components/ui/tooltip.py` | `others_icons`, `base_ui` |

## Core Dependencies
Most components depend on these:
- `twmerge`: `components/utils/twmerge.py`
- `component`: `components/ui/component.py` (Base class)
- `base_ui`: `components/ui/base_ui.py` (Package wrapper)
- `hugeicon`: `components/icons/hugeicon.py`
- `others_icons`: `components/icons/others.py` (Spinner, etc.)
