from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QLineEdit, QCheckBox, QMessageBox
from PySide6.QtCore import Qt
from database.repositories import task_repo
from models.task import Task
from ui.widgets.elevated_button import ElevatedButton

class TaskListView(QWidget):
    def __init__(self, view_key: str, title: str, parent=None):
        super().__init__(parent)
        self.view_key = view_key
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(14)

        head = QHBoxLayout()
        t = QLabel(title.upper()); t.setObjectName("PageTitle")
        head.addWidget(t); head.addStretch()
        
        if self.view_key not in ["completed", "archived"]:
            self.refresh_btn = ElevatedButton("REFRESH", primary=False)
            self.refresh_btn.clicked.connect(self.refresh)
            head.addWidget(self.refresh_btn)
        self.layout.addLayout(head)

        if self.view_key in ["inbox", "all_tasks", "my_day", "upcoming"]:
            add_row = QHBoxLayout()
            self.new_task_input = QLineEdit()
            self.new_task_input.setPlaceholderText("Add a new task...")
            self.new_task_input.returnPressed.connect(self.add_task)
            self.add_btn = ElevatedButton("ADD", primary=True)
            self.add_btn.clicked.connect(self.add_task)
            add_row.addWidget(self.new_task_input)
            add_row.addWidget(self.add_btn)
            self.layout.addLayout(add_row)

        self.list = QListWidget()
        self.layout.addWidget(self.list, 1)
        self.refresh()

    def refresh(self):
        self.list.clear()
        tasks = task_repo.list_tasks_for_view(self.view_key)
        
        if not tasks:
            item = QListWidgetItem("No tasks found.")
            item.setFlags(Qt.NoItemFlags)
            item.setForeground(Qt.gray)
            self.list.addItem(item)
            return

        for task in tasks:
            item = QListWidgetItem()
            item.setData(Qt.UserRole, task.id)
            
            widget = QWidget()
            widget.setStyleSheet("background: transparent;")
            layout = QHBoxLayout(widget)
            layout.setContentsMargins(10, 8, 10, 8)
            
            cb = QCheckBox()
            cb.setChecked(task.completed)
            cb.stateChanged.connect(lambda state, t_id=task.id: self.toggle_completion(t_id, state))
            
            title = QLabel(task.title)
            title.setStyleSheet(f"color: {'#6c7086' if task.completed else '#cdd6f4'}; font-size: 15px; font-weight: 600; text-decoration: {'line-through' if task.completed else 'none'};")
            
            del_btn = ElevatedButton("X", primary=False)
            del_btn.setFixedSize(30, 30)
            del_btn.setStyleSheet("background: #ff4b4b; color: white; border-radius: 8px; font-weight: bold; border-bottom: 2px solid #cc3b3b;")
            del_btn.clicked.connect(lambda _, t_id=task.id: self.delete_task(t_id))
            
            layout.addWidget(cb)
            layout.addWidget(title)
            layout.addStretch()
            layout.addWidget(del_btn)
            
            item.setSizeHint(widget.sizeHint())
            self.list.addItem(item)
            self.list.setItemWidget(item, widget)

    def add_task(self):
        text = self.new_task_input.text().strip()
        if not text: return
        t = Task(title=text)
        if self.view_key == "my_day": t.my_day = True
        task_repo.create_task(t)
        self.new_task_input.clear()
        self.refresh()

    def toggle_completion(self, task_id, state):
        task_repo.set_completed(task_id, state == Qt.Checked.value)
        self.refresh()

    def delete_task(self, task_id):
        reply = QMessageBox.question(self, "Delete", "Delete this task?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            task_repo.delete_task(task_id)
            self.refresh()
