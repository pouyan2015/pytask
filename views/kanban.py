from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QAbstractItemView, QFrame
from PySide6.QtCore import Qt
from database.repositories import task_repo
from models.task import Task

PRIORITY_COLORS = {0: "#a6e3a1", 1: "#89b4fa", 2: "#f9e2af", 3: "#f38ba8"}

class KanbanCard(QFrame):
    def __init__(self, task: Task):
        super().__init__()
        self.setObjectName("KanbanCard")
        self.setStyleSheet("#KanbanCard { background-color: #1e1e2e; border-radius: 8px; border: 1px solid #313244; } #KanbanCard:hover { background-color: #313244; border: 1px solid #45475a; }")
        layout = QVBoxLayout(self); layout.setContentsMargins(12, 12, 12, 12); layout.setSpacing(8)
        top_row = QHBoxLayout()
        stripe = QFrame(); stripe.setFixedSize(4, 16); stripe.setStyleSheet(f"background-color: {PRIORITY_COLORS.get(task.priority, '#89b4fa')}; border-radius: 2px;")
        title = QLabel(task.title); title.setStyleSheet("color: #cdd6f4; font-weight: 600; font-size: 14px; background: transparent;"); title.setWordWrap(True)
        top_row.addWidget(stripe); top_row.addWidget(title, 1); layout.addLayout(top_row)
        if task.due_at:
            due = QLabel(f"Due: {task.due_at[:10]}"); due.setStyleSheet("color: #a6adc8; font-size: 12px; background: transparent;"); layout.addWidget(due)

class KanbanColumn(QListWidget):
    def __init__(self, title, status_code):
        super().__init__()
        self.title = title; self.status_code = status_code
        self.setDragDropMode(QAbstractItemView.DragDrop); self.setDefaultDropAction(Qt.MoveAction)
        self.setStyleSheet("QListWidget { background: transparent; border: none; }")
        self.layout_container = QVBoxLayout()
        header = QLabel(title.upper()); header.setStyleSheet("color: #a6adc8; font-weight: 800; font-size: 12px; letter-spacing: 1px; padding-bottom: 8px; background: transparent;")
        self.layout_container.addWidget(header)

    def refresh(self):
        self.clear()
        for t in task_repo.list_tasks():
            if t.status != self.status_code: continue
            item = QListWidgetItem(); item.setData(Qt.UserRole, t.id)
            widget = KanbanCard(t); item.setSizeHint(widget.sizeHint()); self.addItem(item); self.setItemWidget(item, widget)

    def dropEvent(self, event):
        super().dropEvent(event)
        for i in range(self.count()):
            item = self.item(i); task_id = item.data(Qt.UserRole)
            task_repo.update_status(task_id, self.status_code)

class KanbanView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(14)
        title = QLabel("KANBAN BOARD"); title.setObjectName("PageTitle"); layout.addWidget(title)
        cols = QHBoxLayout(); cols.setSpacing(16)
        self.col_todo = KanbanColumn("To Do", 0); self.col_doing = KanbanColumn("In Progress", 1); self.col_done = KanbanColumn("Done", 2)
        for col in [self.col_todo, self.col_doing, self.col_done]:
            wrapper = QWidget(); w_layout = QVBoxLayout(wrapper); w_layout.setContentsMargins(0, 0, 0, 0)
            header = QLabel(col.title.upper()); header.setStyleSheet("color: #cdd6f4; font-weight: 900; font-size: 14px; letter-spacing: 1px; padding-bottom: 8px; background: transparent;")
            w_layout.addWidget(header); w_layout.addWidget(col); cols.addWidget(wrapper)
        layout.addLayout(cols)

    def refresh(self):
        self.col_todo.refresh(); self.col_doing.refresh(); self.col_done.refresh()
