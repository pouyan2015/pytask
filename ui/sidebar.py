from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame, QSizePolicy
from PySide6.QtCore import Signal, Qt, QPropertyAnimation, QEasingCurve

NAV_ITEMS = [
    ("dashboard", "Dashboard", ""),
    ("inbox",     "Inbox",     ""),
    ("my_day",    "My Day",    ""),
    ("upcoming",  "Upcoming",  ""),
    ("all_tasks", "All Tasks", ""),
    ("projects",  "Projects",  ""),
    ("tags",      "Categories & Tags", ""),
    ("calendar",  "Calendar",  ""),
    ("kanban",    "Kanban Board", ""),
    ("completed", "Completed", ""),
    ("archived",  "Archived",  ""),
    ("analytics", "Analytics", ""),
    ("settings",  "Settings",  ""),
]

class Sidebar(QFrame):
    navigate = Signal(str)
    request_close = Signal()

    EXPANDED_W = 240
    COLLAPSED_W = 68

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Sidebar")
        # Use fixed width for smoother animation
        self.setFixedWidth(self.EXPANDED_W)
        self._expanded = True
        self._current = "dashboard"
        self._buttons = {}

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.hamburger = QPushButton("P Y T A S K S")
        self.hamburger.setObjectName("Hamburger")
        self.hamburger.setCursor(Qt.PointingHandCursor)
        self.hamburger.clicked.connect(self.toggle)
        layout.addWidget(self.hamburger)

        for key, label, icon in NAV_ITEMS:
            btn = QPushButton(f"  {label}")
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setProperty("nav_key", key)
            btn.clicked.connect(lambda _, k=key: self._on_nav(k))
            layout.addWidget(btn)
            self._buttons[key] = (btn, label)

        layout.addStretch()

        self.close_btn = QPushButton("  Terminate")
        self.close_btn.setObjectName("CloseBtn")
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.close_btn.clicked.connect(self.request_close.emit)
        layout.addWidget(self.close_btn)

        self._buttons[self._current][0].setChecked(True)

    def _on_nav(self, key):
        for k, (btn, _) in self._buttons.items():
            btn.setChecked(k == key)
        self._current = key
        self.navigate.emit(key)

    def toggle(self):
        self._expanded = not self._expanded
        target = self.EXPANDED_W if self._expanded else self.COLLAPSED_W

        # Animate minimumWidth and maximumWidth together for smoothness
        self.anim_min = QPropertyAnimation(self, b"minimumWidth", self)
        self.anim_min.setDuration(220)
        self.anim_min.setStartValue(self.width())
        self.anim_min.setEndValue(target)
        self.anim_min.setEasingCurve(QEasingCurve.OutCubic)
        
        self.anim_max = QPropertyAnimation(self, b"maximumWidth", self)
        self.anim_max.setDuration(220)
        self.anim_max.setStartValue(self.width())
        self.anim_max.setEndValue(target)
        self.anim_max.setEasingCurve(QEasingCurve.OutCubic)
        
        self.anim_min.start()
        self.anim_max.start()

        if self._expanded:
            self.hamburger.setText("P Y T A S K S")
            self.close_btn.setText("  Terminate")
            for key, (btn, label) in self._buttons.items():
                btn.setText(f"  {label}")
                btn.setToolTip("")
        else:
            self.hamburger.setText("P")
            self.close_btn.setText("X")
            self.close_btn.setToolTip("Terminate")
            for key, (btn, label) in self._buttons.items():
                btn.setText(f" {label[0]}")
                btn.setToolTip(label)
