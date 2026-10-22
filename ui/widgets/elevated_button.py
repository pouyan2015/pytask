from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

class ElevatedButton(QPushButton):
    def __init__(self, text="", primary=True, parent=None):
        super().__init__(text, parent)
        self.setObjectName("PrimaryBtn" if primary else "GhostBtn")
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(38)
