from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QLineEdit, QMessageBox
from database.connection import get_connection
from ui.widgets.elevated_button import ElevatedButton

class ProjectsView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(14)

        head = QHBoxLayout()
        t = QLabel("PROJECTS"); t.setObjectName("PageTitle")
        head.addWidget(t); head.addStretch()
        self.layout.addLayout(head)

        add_row = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("New project name...")
        self.name_input.returnPressed.connect(self.add_project)
        self.add_btn = ElevatedButton("CREATE", primary=True)
        self.add_btn.clicked.connect(self.add_project)
        add_row.addWidget(self.name_input)
        add_row.addWidget(self.add_btn)
        self.layout.addLayout(add_row)

        self.list = QListWidget()
        self.layout.addWidget(self.list, 1)
        self.refresh()

    def refresh(self):
        self.list.clear()
        conn = get_connection()
        for row in conn.execute("SELECT id, name, created_at FROM projects WHERE archived=0"):
            item = QListWidgetItem(f"{row['name']}  (Created: {row['created_at'][:10]})")
            self.list.addItem(item)

    def add_project(self):
        name = self.name_input.text().strip()
        if not name: return
        conn = get_connection()
        try:
            conn.execute("INSERT INTO projects(name) VALUES(?)", (name,))
            conn.commit()
            self.name_input.clear()
            self.refresh()
        except Exception:
            QMessageBox.warning(self, "Error", "Project already exists.")
