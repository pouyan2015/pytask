from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QListWidget, QListWidgetItem, QLineEdit
from PySide6.QtCore import Qt
from database.repositories import task_repo
from models.task import Task
from ui.widgets.elevated_button import ElevatedButton

class StatCard(QFrame):
    def __init__(self, label, value, accent_color):
        super().__init__()
        self.setObjectName("StatCard")
        self.setStyleSheet(f"#StatCard {{ border-top: 4px solid {accent_color}; }}")
        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 16, 20, 16)
        v = QLabel(str(value)); v.setObjectName("StatValue")
        l = QLabel(label.upper()); l.setObjectName("StatLabel")
        lay.addWidget(v); lay.addWidget(l)

class DashboardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(16)
        
        head = QHBoxLayout()
        title = QLabel("DASHBOARD"); title.setObjectName("PageTitle")
        head.addWidget(title)
        head.addStretch()
        self.refresh_btn = ElevatedButton("REFRESH", primary=False)
        self.refresh_btn.clicked.connect(self.refresh)
        head.addWidget(self.refresh_btn)
        self.layout.addLayout(head)

        # Quick Add
        add_row = QHBoxLayout()
        self.quick_input = QLineEdit()
        self.quick_input.setPlaceholderText("Quick add a task...")
        self.quick_input.returnPressed.connect(self.quick_add)
        self.add_btn = ElevatedButton("ADD", primary=True)
        self.add_btn.clicked.connect(self.quick_add)
        add_row.addWidget(self.quick_input)
        add_row.addWidget(self.add_btn)
        self.layout.addLayout(add_row)

        # Stats
        self.cards_row = QHBoxLayout()
        self.cards_row.setSpacing(16)
        self.layout.addLayout(self.cards_row)

        # Lists
        lists_row = QHBoxLayout()
        
        col1 = QVBoxLayout()
        col1.addWidget(QLabel("RECENT TASKS"))
        self.recent_list = QListWidget()
        col1.addWidget(self.recent_list)
        
        col2 = QVBoxLayout()
        col2.addWidget(QLabel("OVERDUE TASKS"))
        self.overdue_list = QListWidget()
        col2.addWidget(self.overdue_list)
        
        lists_row.addLayout(col1)
        lists_row.addLayout(col2)
        self.layout.addLayout(lists_row, 1)

    def quick_add(self):
        text = self.quick_input.text().strip()
        if not text: return
        task_repo.create_task(Task(title=text))
        self.quick_input.clear()
        self.refresh()

    def refresh(self):
        while self.cards_row.count():
            item = self.cards_row.takeAt(0)
            if item.widget(): item.widget().deleteLater()

        c = task_repo.counts()
        self.cards_row.addWidget(StatCard("Active", c["active"], "#89b4fa"))
        self.cards_row.addWidget(StatCard("Completed", c["completed"], "#a6e3a1"))
        self.cards_row.addWidget(StatCard("Overdue", c["overdue"], "#f38ba8"))
        self.cards_row.addWidget(StatCard("Archived", c["archived"], "#6c7086"))

        self.recent_list.clear()
        for t in task_repo.list_tasks()[:10]:
            mark = "[DONE]" if t.completed else "[ ]"
            QListWidgetItem(f"{mark} {t.title}", self.recent_list)

        self.overdue_list.clear()
        from database.connection import get_connection
        conn = get_connection()
        rows = conn.execute("SELECT title FROM tasks WHERE completed=0 AND archived=0 AND due_at IS NOT NULL AND date(due_at) < date('now')").fetchall()
        for r in rows:
            QListWidgetItem(f"[!] {r['title']}", self.overdue_list)
