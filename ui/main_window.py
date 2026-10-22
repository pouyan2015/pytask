from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QStackedWidget, QGraphicsDropShadowEffect, QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QColor, QPainter
from ui.sidebar import Sidebar
from views.dashboard import DashboardView
from views.task_list_view import TaskListView
from views.projects import ProjectsView
from views.tags import TagsView
from views.kanban import KanbanView
from views.calendar import CalendarView
from views.analytics import AnalyticsView
from views.settings import SettingsView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyTasks Premium")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(1200, 800)
        self._drag_pos = None

        outer = QVBoxLayout(self)
        outer.setContentsMargins(20, 20, 20, 20)

        self.container = QFrame()
        self.container.setObjectName("MainContainer")
        outer.addWidget(self.container)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setColor(QColor(0, 0, 0, 200))
        self.shadow.setOffset(0, 10)
        self.container.setGraphicsEffect(self.shadow)

        root = QHBoxLayout(self.container)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.sidebar = Sidebar()
        self.sidebar.navigate.connect(self.switch_view)
        self.sidebar.request_close.connect(self.close)
        root.addWidget(self.sidebar)

        self.content_area = QFrame()
        self.content_area.setStyleSheet("background: transparent;")
        content_layout = QVBoxLayout(self.content_area)
        content_layout.setContentsMargins(32, 24, 32, 32)

        self.stack = QStackedWidget()
        content_layout.addWidget(self.stack)
        root.addWidget(self.content_area, 1)

        self.pages = {}
        self.pages["dashboard"] = DashboardView()
        self.pages["inbox"] = TaskListView("inbox", "Inbox")
        self.pages["my_day"] = TaskListView("my_day", "My Day")
        self.pages["upcoming"] = TaskListView("upcoming", "Upcoming")
        self.pages["all_tasks"] = TaskListView("all_tasks", "All Tasks")
        self.pages["completed"] = TaskListView("completed", "Completed Tasks")
        self.pages["archived"] = TaskListView("archived", "Archived Tasks")
        self.pages["projects"] = ProjectsView()
        self.pages["tags"] = TagsView()
        self.pages["kanban"] = KanbanView()
        self.pages["calendar"] = CalendarView()
        self.pages["analytics"] = AnalyticsView()
        self.pages["settings"] = SettingsView()

        self.pages["settings"].theme_changed.connect(self.apply_theme)

        for page in self.pages.values():
            self.stack.addWidget(page)

        self.switch_view("dashboard")
        self._fade_in()

    def _fade_in(self):
        eff = QGraphicsOpacityEffect(self.container)
        self.container.setGraphicsEffect(eff)
        anim = QPropertyAnimation(eff, b"opacity", self)
        anim.setDuration(500)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start()
        self._anim = anim
        # Restore shadow after fade-in completes
        from PySide6.QtCore import QTimer
        QTimer.singleShot(510, self._restore_shadow)

    def _restore_shadow(self):
        # Re-create shadow to avoid C++ deletion error
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setColor(QColor(0, 0, 0, 200))
        self.shadow.setOffset(0, 10)
        self.container.setGraphicsEffect(self.shadow)

    def apply_theme(self, theme_name):
        from PySide6.QtWidgets import QApplication
        from themes.theme_manager import load_theme
        app = QApplication.instance()
        if app:
            app.setStyleSheet(load_theme(theme_name))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), Qt.transparent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self._drag_pos:
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None

    def switch_view(self, key):
        if key in self.pages:
            self.stack.setCurrentWidget(self.pages[key])
            if hasattr(self.pages[key], "refresh"):
                self.pages[key].refresh()
