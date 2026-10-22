from dataclasses import dataclass, field
from typing import Optional, List

PRIORITY_LABELS = {0: "Low", 1: "Normal", 2: "High", 3: "Critical"}

@dataclass
class Task:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    notes: str = ""
    completed: bool = False
    status: int = 0
    priority: int = 1
    start_at: Optional[str] = None
    due_at: Optional[str] = None
    estimated_minutes: Optional[int] = None
    project_id: Optional[int] = None
    archived: bool = False
    deleted: bool = False
    my_day: bool = False
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    completed_at: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    @property
    def priority_label(self) -> str:
        return PRIORITY_LABELS.get(self.priority, "Normal")
