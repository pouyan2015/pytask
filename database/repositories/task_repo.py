from typing import List
from database.connection import get_connection, transaction
from models.task import Task

def _row_to_task(r) -> Task:
    return Task(id=r["id"], title=r["title"], description=r["description"], notes=r["notes"], completed=bool(r["completed"]), status=r["status"], priority=r["priority"], start_at=r["start_at"], due_at=r["due_at"], estimated_minutes=r["estimated_minutes"], project_id=r["project_id"], archived=bool(r["archived"]), deleted=bool(r["deleted"]), my_day=bool(r["my_day"]), created_at=r["created_at"], updated_at=r["updated_at"], completed_at=r["completed_at"])

def list_tasks(include_archived=False) -> List[Task]:
    conn = get_connection(); q = "SELECT * FROM tasks WHERE deleted=0"
    if not include_archived: q += " AND archived=0"
    return [_row_to_task(r) for r in conn.execute(q + " ORDER BY created_at DESC").fetchall()]

def list_tasks_for_view(view: str) -> List[Task]:
    conn = get_connection(); base = "SELECT * FROM tasks WHERE deleted=0"
    if view == "inbox": sql = base + " AND archived=0 ORDER BY created_at DESC"
    elif view == "my_day": sql = base + " AND archived=0 AND my_day=1 AND completed=0 ORDER BY priority DESC"
    elif view == "upcoming": sql = base + " AND archived=0 AND completed=0 AND due_at IS NOT NULL ORDER BY due_at ASC"
    elif view == "completed": sql = base + " AND completed=1 AND archived=0 ORDER BY completed_at DESC"
    elif view == "archived": sql = "SELECT * FROM tasks WHERE deleted=0 AND archived=1 ORDER BY updated_at DESC"
    else: sql = base + " AND archived=0 ORDER BY created_at DESC"
    return [_row_to_task(r) for r in conn.execute(sql).fetchall()]

def create_task(task: Task) -> int:
    conn = get_connection()
    with transaction():
        cur = conn.execute("INSERT INTO tasks(title, description, notes, completed, status, priority, start_at, due_at, estimated_minutes, project_id, archived, deleted, my_day) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", (task.title, task.description, task.notes, int(task.completed), task.status, task.priority, task.start_at, task.due_at, task.estimated_minutes, task.project_id, int(task.archived), int(task.deleted), int(task.my_day)))
        return cur.lastrowid

def update_status(task_id: int, status: int):
    conn = get_connection()
    with transaction():
        completed = 1 if status == 2 else 0
        conn.execute("UPDATE tasks SET status=?, completed=?, updated_at=datetime('now'), completed_at=CASE WHEN ?=1 THEN datetime('now') ELSE NULL END WHERE id=?", (status, completed, completed, task_id))

def set_completed(task_id: int, completed: bool):
    conn = get_connection()
    with transaction():
        status = 2 if completed else 0
        conn.execute("UPDATE tasks SET completed=?, status=?, updated_at=datetime('now'), completed_at=CASE WHEN ?=1 THEN datetime('now') ELSE NULL END WHERE id=?", (int(completed), status, int(completed), task_id))

def delete_task(task_id: int):
    conn = get_connection()
    with transaction(): conn.execute("UPDATE tasks SET deleted=1 WHERE id=?", (task_id,))

def counts() -> dict:
    conn = get_connection(); row = conn.execute("SELECT SUM(CASE WHEN completed=0 AND archived=0 THEN 1 ELSE 0 END) AS active, SUM(CASE WHEN completed=1 AND archived=0 THEN 1 ELSE 0 END) AS completed, SUM(CASE WHEN archived=1 THEN 1 ELSE 0 END) AS archived, SUM(CASE WHEN archived=0 AND completed=0 AND due_at IS NOT NULL AND date(due_at) < date('now','localtime') THEN 1 ELSE 0 END) AS overdue FROM tasks WHERE deleted=0").fetchone()
    return {k: (row[k] or 0) for k in row.keys()}
