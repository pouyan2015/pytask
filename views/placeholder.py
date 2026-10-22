from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class PlaceholderView(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        t = QLabel(title.upper()); t.setObjectName("PageTitle")
        note = QLabel("This view is coming in a future phase.")
        note.setStyleSheet("color: #8a8a90; margin-top: 20px;")
        layout.addWidget(t)
        layout.addWidget(note)
        layout.addStretch()
