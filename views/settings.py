from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QHBoxLayout
from PySide6.QtCore import Signal
from app.config import DB_PATH, BACKUP_DIR, get_setting, set_setting

class SettingsView(QWidget):
    theme_changed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        
        title = QLabel("SETTINGS"); title.setObjectName("PageTitle")
        layout.addWidget(title)
        
        theme_row = QHBoxLayout()
        theme_row.addWidget(QLabel("Theme:"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Premium Dark", "Light"])
        self.theme_combo.setStyleSheet("padding: 8px; border-radius: 6px;")
        
        # Load saved theme
        current = get_setting("theme", "dark")
        self.theme_combo.setCurrentIndex(0 if current == "dark" else 1)
        
        self.theme_combo.currentIndexChanged.connect(self._on_theme_change)
        theme_row.addWidget(self.theme_combo)
        theme_row.addStretch()
        layout.addLayout(theme_row)
        
        layout.addWidget(QLabel("Database Location:"))
        db_lbl = QLabel(str(DB_PATH))
        db_lbl.setStyleSheet("color: #a6adc8; background: #1e1e2e; padding: 10px; border-radius: 6px;")
        layout.addWidget(db_lbl)
        
        layout.addWidget(QLabel("Backups Location:"))
        bk_lbl = QLabel(str(BACKUP_DIR))
        bk_lbl.setStyleSheet("color: #a6adc8; background: #1e1e2e; padding: 10px; border-radius: 6px;")
        layout.addWidget(bk_lbl)
        
        layout.addStretch()

    def _on_theme_change(self, index):
        theme = "dark" if index == 0 else "light"
        set_setting("theme", theme)
        self.theme_changed.emit(theme)
